# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mayank/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mayank/catkin_ws/build

# Include any dependencies generated for this target.
include stereo/CMakeFiles/stereo.dir/depend.make

# Include the progress variables for this target.
include stereo/CMakeFiles/stereo.dir/progress.make

# Include the compile flags for this target's objects.
include stereo/CMakeFiles/stereo.dir/flags.make

stereo/CMakeFiles/stereo.dir/src/main.cpp.o: stereo/CMakeFiles/stereo.dir/flags.make
stereo/CMakeFiles/stereo.dir/src/main.cpp.o: /home/mayank/catkin_ws/src/stereo/src/main.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/mayank/catkin_ws/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object stereo/CMakeFiles/stereo.dir/src/main.cpp.o"
	cd /home/mayank/catkin_ws/build/stereo && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/stereo.dir/src/main.cpp.o -c /home/mayank/catkin_ws/src/stereo/src/main.cpp

stereo/CMakeFiles/stereo.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/stereo.dir/src/main.cpp.i"
	cd /home/mayank/catkin_ws/build/stereo && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/mayank/catkin_ws/src/stereo/src/main.cpp > CMakeFiles/stereo.dir/src/main.cpp.i

stereo/CMakeFiles/stereo.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/stereo.dir/src/main.cpp.s"
	cd /home/mayank/catkin_ws/build/stereo && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/mayank/catkin_ws/src/stereo/src/main.cpp -o CMakeFiles/stereo.dir/src/main.cpp.s

stereo/CMakeFiles/stereo.dir/src/main.cpp.o.requires:
.PHONY : stereo/CMakeFiles/stereo.dir/src/main.cpp.o.requires

stereo/CMakeFiles/stereo.dir/src/main.cpp.o.provides: stereo/CMakeFiles/stereo.dir/src/main.cpp.o.requires
	$(MAKE) -f stereo/CMakeFiles/stereo.dir/build.make stereo/CMakeFiles/stereo.dir/src/main.cpp.o.provides.build
.PHONY : stereo/CMakeFiles/stereo.dir/src/main.cpp.o.provides

stereo/CMakeFiles/stereo.dir/src/main.cpp.o.provides.build: stereo/CMakeFiles/stereo.dir/src/main.cpp.o

# Object files for target stereo
stereo_OBJECTS = \
"CMakeFiles/stereo.dir/src/main.cpp.o"

# External object files for target stereo
stereo_EXTERNAL_OBJECTS =

/home/mayank/catkin_ws/devel/lib/stereo/stereo: stereo/CMakeFiles/stereo.dir/src/main.cpp.o
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libcv_bridge.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_calib3d.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_contrib.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_core.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_features2d.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_flann.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_gpu.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_highgui.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_imgproc.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_legacy.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_ml.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_nonfree.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_objdetect.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_photo.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_stitching.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_superres.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_video.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libopencv_videostab.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libimage_transport.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libtinyxml.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libclass_loader.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libPocoFoundation.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/x86_64-linux-gnu/libdl.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libroslib.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libmessage_filters.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libroscpp.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libboost_signals-mt.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libboost_filesystem-mt.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libxmlrpcpp.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/librosconsole.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/librosconsole_log4cxx.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/librosconsole_backend_interface.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/liblog4cxx.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libboost_regex-mt.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libroscpp_serialization.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/librostime.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libboost_date_time-mt.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libboost_system-mt.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/libboost_thread-mt.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libcpp_common.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: /opt/ros/hydro/lib/libconsole_bridge.so
/home/mayank/catkin_ws/devel/lib/stereo/stereo: stereo/CMakeFiles/stereo.dir/build.make
/home/mayank/catkin_ws/devel/lib/stereo/stereo: stereo/CMakeFiles/stereo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/mayank/catkin_ws/devel/lib/stereo/stereo"
	cd /home/mayank/catkin_ws/build/stereo && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/stereo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
stereo/CMakeFiles/stereo.dir/build: /home/mayank/catkin_ws/devel/lib/stereo/stereo
.PHONY : stereo/CMakeFiles/stereo.dir/build

stereo/CMakeFiles/stereo.dir/requires: stereo/CMakeFiles/stereo.dir/src/main.cpp.o.requires
.PHONY : stereo/CMakeFiles/stereo.dir/requires

stereo/CMakeFiles/stereo.dir/clean:
	cd /home/mayank/catkin_ws/build/stereo && $(CMAKE_COMMAND) -P CMakeFiles/stereo.dir/cmake_clean.cmake
.PHONY : stereo/CMakeFiles/stereo.dir/clean

stereo/CMakeFiles/stereo.dir/depend:
	cd /home/mayank/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mayank/catkin_ws/src /home/mayank/catkin_ws/src/stereo /home/mayank/catkin_ws/build /home/mayank/catkin_ws/build/stereo /home/mayank/catkin_ws/build/stereo/CMakeFiles/stereo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : stereo/CMakeFiles/stereo.dir/depend
