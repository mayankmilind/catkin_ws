"""autogenerated by genpy from fovis_ros/FovisInfo.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class FovisInfo(genpy.Message):
  _md5sum = "2e964f4d41f3876e14c50795334bf34c"
  _type = "fovis_ros/FovisInfo"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Internal information on the
# fovis algorithm parameters
# and results

Header header

# True if in the next run the reference 
# frame will be changed. This is the case
# when the number of inliers drops below
# a threshold or the previous motion estimate
# failed in last motion estimation.
bool change_reference_frame

# The threshold that is currently 
# used for the FAST feature detector.
int32 fast_threshold

# total number of detected keypoints in raw image
int32 num_total_detected_keypoints

# same as above per pyramid level, starting at 0
int32[] num_detected_keypoints

# total number of keypoints after bucketing and
# edge and depth filter
int32 num_total_keypoints

# same as above per pyramid level, starting at 0
int32[] num_keypoints

# info from motion estimator
int32 motion_estimate_status_code
string motion_estimate_status
bool motion_estimate_valid
int32 num_matches
int32 num_inliers
int32 num_reprojection_failures

# runtime of last iteration in seconds
float64 runtime


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','change_reference_frame','fast_threshold','num_total_detected_keypoints','num_detected_keypoints','num_total_keypoints','num_keypoints','motion_estimate_status_code','motion_estimate_status','motion_estimate_valid','num_matches','num_inliers','num_reprojection_failures','runtime']
  _slot_types = ['std_msgs/Header','bool','int32','int32','int32[]','int32','int32[]','int32','string','bool','int32','int32','int32','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,change_reference_frame,fast_threshold,num_total_detected_keypoints,num_detected_keypoints,num_total_keypoints,num_keypoints,motion_estimate_status_code,motion_estimate_status,motion_estimate_valid,num_matches,num_inliers,num_reprojection_failures,runtime

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FovisInfo, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.change_reference_frame is None:
        self.change_reference_frame = False
      if self.fast_threshold is None:
        self.fast_threshold = 0
      if self.num_total_detected_keypoints is None:
        self.num_total_detected_keypoints = 0
      if self.num_detected_keypoints is None:
        self.num_detected_keypoints = []
      if self.num_total_keypoints is None:
        self.num_total_keypoints = 0
      if self.num_keypoints is None:
        self.num_keypoints = []
      if self.motion_estimate_status_code is None:
        self.motion_estimate_status_code = 0
      if self.motion_estimate_status is None:
        self.motion_estimate_status = ''
      if self.motion_estimate_valid is None:
        self.motion_estimate_valid = False
      if self.num_matches is None:
        self.num_matches = 0
      if self.num_inliers is None:
        self.num_inliers = 0
      if self.num_reprojection_failures is None:
        self.num_reprojection_failures = 0
      if self.runtime is None:
        self.runtime = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.change_reference_frame = False
      self.fast_threshold = 0
      self.num_total_detected_keypoints = 0
      self.num_detected_keypoints = []
      self.num_total_keypoints = 0
      self.num_keypoints = []
      self.motion_estimate_status_code = 0
      self.motion_estimate_status = ''
      self.motion_estimate_valid = False
      self.num_matches = 0
      self.num_inliers = 0
      self.num_reprojection_failures = 0
      self.runtime = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B2i.pack(_x.change_reference_frame, _x.fast_threshold, _x.num_total_detected_keypoints))
      length = len(self.num_detected_keypoints)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.num_detected_keypoints))
      buff.write(_struct_i.pack(self.num_total_keypoints))
      length = len(self.num_keypoints)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.num_keypoints))
      buff.write(_struct_i.pack(self.motion_estimate_status_code))
      _x = self.motion_estimate_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3id.pack(_x.motion_estimate_valid, _x.num_matches, _x.num_inliers, _x.num_reprojection_failures, _x.runtime))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.change_reference_frame, _x.fast_threshold, _x.num_total_detected_keypoints,) = _struct_B2i.unpack(str[start:end])
      self.change_reference_frame = bool(self.change_reference_frame)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.num_detected_keypoints = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (self.num_total_keypoints,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.num_keypoints = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (self.motion_estimate_status_code,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motion_estimate_status = str[start:end].decode('utf-8')
      else:
        self.motion_estimate_status = str[start:end]
      _x = self
      start = end
      end += 21
      (_x.motion_estimate_valid, _x.num_matches, _x.num_inliers, _x.num_reprojection_failures, _x.runtime,) = _struct_B3id.unpack(str[start:end])
      self.motion_estimate_valid = bool(self.motion_estimate_valid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B2i.pack(_x.change_reference_frame, _x.fast_threshold, _x.num_total_detected_keypoints))
      length = len(self.num_detected_keypoints)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.num_detected_keypoints.tostring())
      buff.write(_struct_i.pack(self.num_total_keypoints))
      length = len(self.num_keypoints)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.num_keypoints.tostring())
      buff.write(_struct_i.pack(self.motion_estimate_status_code))
      _x = self.motion_estimate_status
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3id.pack(_x.motion_estimate_valid, _x.num_matches, _x.num_inliers, _x.num_reprojection_failures, _x.runtime))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.change_reference_frame, _x.fast_threshold, _x.num_total_detected_keypoints,) = _struct_B2i.unpack(str[start:end])
      self.change_reference_frame = bool(self.change_reference_frame)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.num_detected_keypoints = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (self.num_total_keypoints,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.num_keypoints = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (self.motion_estimate_status_code,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.motion_estimate_status = str[start:end].decode('utf-8')
      else:
        self.motion_estimate_status = str[start:end]
      _x = self
      start = end
      end += 21
      (_x.motion_estimate_valid, _x.num_matches, _x.num_inliers, _x.num_reprojection_failures, _x.runtime,) = _struct_B3id.unpack(str[start:end])
      self.motion_estimate_valid = bool(self.motion_estimate_valid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
_struct_3I = struct.Struct("<3I")
_struct_B3id = struct.Struct("<B3id")
_struct_B2i = struct.Struct("<B2i")
