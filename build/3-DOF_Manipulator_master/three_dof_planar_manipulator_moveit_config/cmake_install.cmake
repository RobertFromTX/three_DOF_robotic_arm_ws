# Install script for directory: C:/Users/robc/ROS/three_DOF_robotic_arm_ws/src/3-DOF_Manipulator_master/three_dof_planar_manipulator_moveit_config

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator_moveit_config/catkin_generated/installspace/three_dof_planar_manipulator_moveit_config.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator_moveit_config/cmake" TYPE FILE FILES
    "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator_moveit_config/catkin_generated/installspace/three_dof_planar_manipulator_moveit_configConfig.cmake"
    "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/build/3-DOF_Manipulator_master/three_dof_planar_manipulator_moveit_config/catkin_generated/installspace/three_dof_planar_manipulator_moveit_configConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator_moveit_config" TYPE FILE FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/src/3-DOF_Manipulator_master/three_dof_planar_manipulator_moveit_config/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator_moveit_config" TYPE DIRECTORY FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/src/3-DOF_Manipulator_master/three_dof_planar_manipulator_moveit_config/launch" REGEX "/setup\\_assistant\\.launch$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/three_dof_planar_manipulator_moveit_config" TYPE DIRECTORY FILES "C:/Users/robc/ROS/three_DOF_robotic_arm_ws/src/3-DOF_Manipulator_master/three_dof_planar_manipulator_moveit_config/config")
endif()

