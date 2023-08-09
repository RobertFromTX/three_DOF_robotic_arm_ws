# Install script for directory: C:/Users/robc/ROS/three_DOF_robotic_arm_ws/src/3-DOF_Manipulator_master/three_dof_planar_manipulator

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator/srv" TYPE FILE FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/src/3-DOF_Manipulator_master/three_dof_planar_manipulator/srv/Floats_array.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator/cmake" TYPE FILE FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator/catkin_generated/installspace/three_dof_planar_manipulator-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/devel/include/three_dof_planar_manipulator")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/devel/share/roseus/ros/three_dof_planar_manipulator")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/devel/share/common-lisp/ros/three_dof_planar_manipulator")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/devel/share/gennodejs/ros/three_dof_planar_manipulator")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "C:/opt/ros/melodic/x64/python.exe" -m compileall "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/devel/lib/site-packages/three_dof_planar_manipulator")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/site-packages" TYPE DIRECTORY FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/devel/lib/site-packages/three_dof_planar_manipulator")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator/catkin_generated/installspace/three_dof_planar_manipulator.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator/cmake" TYPE FILE FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator/catkin_generated/installspace/three_dof_planar_manipulator-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator/cmake" TYPE FILE FILES
    "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator/catkin_generated/installspace/three_dof_planar_manipulatorConfig.cmake"
    "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator/catkin_generated/installspace/three_dof_planar_manipulatorConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator" TYPE FILE FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/src/3-DOF_Manipulator_master/three_dof_planar_manipulator/package.xml")
endif()

