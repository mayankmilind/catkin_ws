
#include<vector>
#include<math.h>
#include <ros/ros.h>
#include <iomanip>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include "opencv2/core/core.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/video/tracking.hpp>
#include "opencv2/contrib/contrib.hpp"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include "std_msgs/String.h"
#include "std_msgs/Int32.h"
#include "std_msgs/Int32MultiArray.h"
#include "std_msgs/Float32.h"
#include <cv_bridge/cv_bridge.h>
#include <math.h>
#include <message_filters/subscriber.h>
#include <message_filters/synchronizer.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <sensor_msgs/Image.h>
#include <opencv2/nonfree/nonfree.hpp>
#include <opencv2/nonfree/features2d.hpp>
#include <stdio.h>
#include <opencv2/legacy/legacy.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/nonfree/nonfree.hpp>
#include <opencv2/nonfree/features2d.hpp>
float nndrRatio = 0.70f;
namespace enc = sensor_msgs::image_encodings;
using namespace std;
using namespace cv;
using namespace sensor_msgs;
using namespace message_filters;
int der_x=1,der_y=1,kernel=1,value=1500,ratio=0;

void imageCallback(const ImageConstPtr& imagel,const ImageConstPtr& imager)
{

	
	cv_bridge::CvImagePtr origl_img;
	cv_bridge::CvImagePtr origr_img;
	origl_img = cv_bridge::toCvCopy(imagel, enc::BGR8);
	origr_img = cv_bridge::toCvCopy(imager, enc::BGR8);
	
	cv::Mat left_img = origl_img->image;
	cv::Mat right_img = origr_img->image;
	Mat left_gray,right_gray,disp,disp8_sgbm,disp8_sbm;
	cvtColor(left_img, left_gray, CV_BGR2GRAY);
	cvtColor(right_img, right_gray, CV_BGR2GRAY);
	
    
   ORB orb;


// In case of SURF, you apply the below two lines
 //   createTrackbar( "Value","SIFT", &value,10000, NULL );
  //  cv::SurfFeatureDetector detector(1500);
   // cv::SurfDescriptorExtractor extractor;


    //FAST feature detector 
    // cv::FastFeatureDetector detector(1500);
    // cv::FastDescriptorExtractor extractor;
     

    // Feature detection
	Mat descriptor1,descriptor2;   
	vector<KeyPoint> kp1;
	vector<KeyPoint> kp2;
	orb(left_gray,Mat(),kp1,descriptor1);
	orb(right_gray,Mat(),kp2,descriptor2);
    
    // Feature display
    int key1 = kp1.size();
    int key2 = kp2.size();
    printf("Keypoint1=%d \nKeypoint2=%d", key1, key2);
 
    // Feature descriptor computation

    // corresponded points
	vector< vector< DMatch >  > matches;
 
    // L2 distance based matching. Brute Force Matching
    BFMatcher matcher(NORM_L1); 
 
    // Flann-based matching
   // FlannBasedMatcher matcher;
 
    // display of corresponding points
    matcher.knnMatch( descriptor1, descriptor2, matches ,2);
 
	vector< DMatch > good_matches;
	good_matches.reserve(matches.size());  
	   
	for (size_t i = 0; i < matches.size(); ++i)
	{ 
	    if (matches[i].size() < 2)
		        continue;
	   
	    const DMatch &m1 = matches[i][0];
	    const DMatch &m2 = matches[i][1];
		
	    if(m1.distance <= nndrRatio * m2.distance)        
	    good_matches.push_back(m1);     
	}

	std::vector< Point2f >  obj;
    std::vector< Point2f >  scene;
 
    for( unsigned int i = 0; i < good_matches.size(); i++ )
    {
        //-- Get the keypoints from the good matches
        obj.push_back( kp1[ good_matches[i].queryIdx ].pt );
        scene.push_back( kp2[ good_matches[i].trainIdx ].pt );
    }
     
    // matching result
    Mat result;
    drawMatches( left_gray, kp1, right_gray, kp2, matches, result );
 
    // output file
 //   imwrite( "result.bmp", result );
 
    // display the result
    namedWindow("SIFT", CV_WINDOW_AUTOSIZE );
    imshow("SIFT", result);
	
    waitKey(10); //press any key to quit


}	

int main(int argc, char** argv)
{	
	ros::init(argc, argv, "feature_extract");
	ros::NodeHandle nh;
	
	image_transport::ImageTransport *it   = new image_transport::ImageTransport(nh);

// GsCam
	/*message_filters::Subscriber<Image> imagel_sub(nh, "minoru/left/camera/image_raw", 1);
	message_filters::Subscriber<Image> imager_sub(nh, "minoru/right/camera/image_raw", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfol_sub(nh,"minoru/left/camera_info", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfor_sub(nh,"minoru/right/camera_info", 1);*/

// MIT Database
	message_filters::Subscriber<Image> imagel_sub(nh, "/wide_stereo/left/image_rect", 1);
	message_filters::Subscriber<Image> imager_sub(nh, "/wide_stereo/right/image_rect", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfol_sub(nh,"/wide_stereo/left/camera_info", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfor_sub(nh,"/wide_stereo/right/camera_info", 1);

// Vslam
	/*message_filters::Subscriber<Image> imagel_sub(nh, "/narrow_stereo/left/image_rect", 1);
	message_filters::Subscriber<Image> imager_sub(nh, "/narrow_stereo/right/image_rect", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfol_sub(nh,"/narrow_stereo/left/camera_info", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfor_sub(nh,"/narrow_stereo/right/camera_info", 1);*/

// blue bag
	/*message_filters::Subscriber<Image> imagel_sub(nh, "/bumblebee/left/image_rect_resized", 1);
	message_filters::Subscriber<Image> imager_sub(nh, "/bumblebee/right/image_rect_resized", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfol_sub(nh,"bumblebee/left/camera_info", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfor_sub(nh,"bumblebee/right/camera_info", 1);*/
	
// Rotating detergent
	/*message_filters::Subscriber<Image> imagel_sub(nh, "/narrow_stereo_textured/left/image_raw", 1);
	message_filters::Subscriber<Image> imager_sub(nh, "/narrow_stereo_textured/right/image_raw", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfol_sub(nh,"/narrow_stereo_textured/left/camera_info", 1);
	message_filters::Subscriber<sensor_msgs::CameraInfo>  caminfor_sub(nh,"/narrow_stereo_textured/right/camera_info", 1);*/

	typedef sync_policies::ApproximateTime<Image,Image> MySyncPolicy;
	// ApproximateTime takes a queue size as its constructor argument, hence MySyncPolicy(10)
	Synchronizer<MySyncPolicy> sync(MySyncPolicy(10), imagel_sub,imager_sub);
	sync.registerCallback(boost::bind(&imageCallback, _1, _2));
//	image_transport::Subscriber imagemaskSub = it->subscribe   ("/riverdetector/visualization" , 1, maskimageCb);
	while (ros::ok())
	{
	

//	ROS_INFO("I published something!");

	ros::spinOnce();
}
  return 0;
}
