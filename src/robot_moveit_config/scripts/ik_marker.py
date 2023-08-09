#!/usr/bin/env python

import rospy
import tf
import copy

import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Pose

from interactive_markers.interactive_marker_server import *
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *
from geometry_msgs.msg import Pose

#added
import math
#Added to convert rpy to quaternions
from tf.transformations import quaternion_from_euler
steps=[]

#steps_marker=MarkerArray()
steps_marker = MarkerArray()
count =0

 
def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians

def processFeedback(feedback):
	print('+++++++++++',feedback.menu_entry_id,'+++++++++++++++++++++')
	#This is for setting orientation, feedback event type is not menu_select
	if feedback.menu_entry_id == 0:
		magnitude = math.sqrt((int_marker.pose.position.x)**2 + (int_marker.pose.position.y)**2 + (int_marker.pose.position.z-5.23)**2)
		#print(int_marker.pose)
		try:
			base_joint_angle_degrees = math.atan(int_marker.pose.position.y/int_marker.pose.position.x) * (180/math.pi)
			if base_joint_angle_degrees < 0:
				base_joint_angle_degrees = 180 + base_joint_angle_degrees
			within_horz_plane_length = math.sqrt((int_marker.pose.position.x)**2 + (int_marker.pose.position.y)**2)
			base_to_eff_length = math.sqrt(within_horz_plane_length**2 + (int_marker.pose.position.z-5.23)**2) #base to end effector, in vertical plane. The 5.234334 is from the ground to top of arm segment 1
			segment_length = 2.49  #in
			#print("base to eff:", base_to_eff_length)
			phi_degrees = math.acos((base_to_eff_length/2)/segment_length) * (180/math.pi) #angle from base_to_eff_length to arm segment 2
			aggregate_angle = math.atan((int_marker.pose.position.z-5.23)/within_horz_plane_length) * (180/math.pi)

			arm_seg_2_joint_angle_degrees = 90 - phi_degrees - aggregate_angle
			arm_seg_3_joint_angle_degrees = 180-(90-phi_degrees)*2

			#print("joint angles")
			#print(base_joint_angle_degrees,arm_seg_2_joint_angle_degrees,arm_seg_3_joint_angle_degrees, phi_degrees, aggregate_angle)

			#print(feedback.pose.orientation.x + feedback.pose.orientation.y + feedback.pose.orientation.z)
			#print(feedback.pose.orientation.z)
			
			r = 0
			p = arm_seg_2_joint_angle_degrees + arm_seg_3_joint_angle_degrees
			y = base_joint_angle_degrees #yaw based off soley base joint
			r_rad = math.radians(r)
			p_rad = math.radians(p)
			y_rad = math.radians(y)
			#print("'incorrect' rpy:", r, p, y)
			q = quaternion_from_euler(r_rad,p_rad,y_rad) #quaternion
			#print("q", q)
			feedback.pose.orientation.x=q[0]
			feedback.pose.orientation.y=q[1]
			feedback.pose.orientation.z=q[2]
			feedback.pose.orientation.w=q[3]
			server.setPose(feedback.marker_name, feedback.pose)
		except:
			pass

	if feedback.event_type == InteractiveMarkerFeedback.MENU_SELECT:
		if feedback.menu_entry_id==1:
			
			group.set_joint_value_target(feedback.pose, True)
			#group.set_position_target([feedback.pose.position.x,feedback.pose.position.y,feedback.pose.position.z], end_effector_link = "end_of_arm_tool_link") #For when you have ik that doesn't need to be approximated to work
			#group.set_pose_target(feedback.pose) #give for 6 or more dof arms
			plan = group.go(wait=True)
			group.stop()
			group.clear_pose_targets()
			#pub.publish(feedback.pose)
            	
            
		elif feedback.menu_entry_id==2:
			listener.waitForTransform('/end_of_arm_tool_link','/bottom_base_link',rospy.Time(), rospy.Duration(1.0))
			(trans,rot)=listener.lookupTransform('bottom_base_link','end_of_arm_tool_link',rospy.Time())
			print(trans,rot)

			feedback.pose.position.x=trans[0]
			feedback.pose.position.y=trans[1]
			feedback.pose.position.z=trans[2]
			feedback.pose.orientation.x=rot[0]
			feedback.pose.orientation.y=rot[1]
			feedback.pose.orientation.z=rot[2]
			feedback.pose.orientation.w=rot[3]
			print('correct rpy: ', euler_from_quaternion(rot[0], rot[1], rot[2], rot[3]))
			server.setPose( feedback.marker_name, feedback.pose )
            
		elif feedback.menu_entry_id==4:
			steps.append(feedback.pose)
			print('Count: ',len(steps))
			marker = Marker()
			marker.header.frame_id = "bottom_base_link"
			marker.type=Marker.SPHERE
			marker.action=marker.ADD
			marker.scale.x=.5
			marker.scale.y=.5
			marker.scale.z=.5
			marker.color.r=.5
			marker.color.g=1
			marker.color.b=1
			marker.color.a=1.0

			marker.pose = feedback.pose
            
			steps_marker.markers.append(marker)
			
			id=0
			for m in steps_marker.markers:
				m.id=id
				id+=1
            
            
			marker_pub.publish(steps_marker)
        
		elif feedback.menu_entry_id==5:
			if len(steps)>0:
				for step in steps:
					group.set_joint_value_target(step, True)
					plan = group.go(wait=True)
					group.stop()
					group.clear_pose_targets()
            
		elif feedback.menu_entry_id==6:
			if len(steps_marker.markers)>0:
				steps[:]=[]
				for m in steps_marker.markers:
					m.action=Marker().DELETE
				marker_pub.publish(steps_marker)
				print('Cleared all steps')
			else:
				print('No stepss set')
		elif feedback.menu_entry_id==7:
			feedback.pose.position.x = float(input("Enter X coordinate: "))
			feedback.pose.position.y = float(input("Enter Y coordinate: "))
			feedback.pose.position.z = float(input("Enter Z coordinate: "))
			server.setPose(feedback.marker_name, feedback.pose)
			#group.set_joint_value_target(feedback.pose, True)
			#plan = group.go(wait=True)
			#group.stop()
			#group.clear_pose_targets()
            
		elif feedback.menu_entry_id==8:
			pass

	server.applyChanges()

if __name__=="__main__":

	rospy.init_node("simple_marker")
	int_marker = InteractiveMarker()
	menu_handler = MenuHandler()
	listener=tf.TransformListener()
	display_traj_pub=rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
	marker_pub= rospy.Publisher('/via_points',MarkerArray,queue_size=20)

	# moveit start

	moveit_commander.roscpp_initialize(sys.argv)
	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	group_name = "robot_arm"
	group = moveit_commander.MoveGroupCommander(group_name)
	group.clear_pose_targets()
	print(group.get_goal_tolerance())
	group.set_goal_joint_tolerance(.0001)
	group.set_goal_position_tolerance(.0001)
	group.set_goal_orientation_tolerance(100000)
	print(group.get_goal_tolerance())
	# create an interactive marker server on the topic namespace simple_marker
	server = InteractiveMarkerServer("simple_marker")

	# create an interactive marker for our server

	int_marker.header.frame_id = "bottom_base_link"
	int_marker.name = "my_marker"
	int_marker.description = "Simple 1-DOF Control"
	int_marker.scale=2


	listener.waitForTransform('/end_of_arm_tool_link','/bottom_base_link',rospy.Time(), rospy.Duration(1.0))
	print(listener.frameExists('bottom_base_link'))
	print(listener.frameExists('end_of_arm_tool_link'))
	(trans,rot)=listener.lookupTransform('bottom_base_link','end_of_arm_tool_link',rospy.Time())
	print(trans,rot)

	int_marker.pose.position.x=trans[0]
	int_marker.pose.position.y=trans[1]
	int_marker.pose.position.z=trans[2]
	int_marker.pose.orientation.x=rot[0]
	int_marker.pose.orientation.y=rot[1]
	int_marker.pose.orientation.z=rot[2]
	int_marker.pose.orientation.w=rot[3]
	
	marker= Marker()
	marker.type=Marker.SPHERE
	marker.scale.x=1
	marker.scale.y=1
	marker.scale.z=1
	marker.color.r=1
	marker.color.g=0
	marker.color.b=0
	marker.color.a=1.0
	
	#added  "C:\opt\ros\melodic\x64\include\rviz\default_plugin\interactive_markers\interactive_marker_control.h" might show how orientation changes with arm
	sphere_control = InteractiveMarkerControl()
	sphere_control.always_visible = True
	sphere_control.markers.append(marker)
	int_marker.controls.append(sphere_control)
	
	#C:\opt\ros\melodic\x64\lib\site-packages\visualization_msgs\msg\_InteractiveMarkerControl.py on settings like move_axis
	trans_x_control = InteractiveMarkerControl()
	trans_x_control.always_visible = True
	trans_x_control.name = "trans_x"
	trans_x_control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
	trans_x_control.always_visible = True
	int_marker.controls.append(trans_x_control)

	trans_y_control = InteractiveMarkerControl()
	trans_y_control.always_visible = True
	trans_y_control.orientation.w=1
	trans_y_control.orientation.x=0
	trans_y_control.orientation.y=0
	trans_y_control.orientation.z=1
	trans_y_control.name = "trans_y"
	trans_y_control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
	trans_y_control.always_visible = True
	int_marker.controls.append(trans_y_control)
	
	trans_z_control = InteractiveMarkerControl()
	trans_z_control.always_visible = True
	trans_z_control.orientation.w=1
	trans_z_control.orientation.x=0
	trans_z_control.orientation.y=1
	trans_z_control.orientation.z=0
	trans_z_control.name = "trans_z"
	trans_z_control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
	trans_z_control.always_visible = True
	int_marker.controls.append(trans_z_control)

	rotate_x_control = InteractiveMarkerControl()
	rotate_x_control.always_visible = True
	rotate_x_control.name = "rotate_x"
	rotate_x_control.interaction_mode = InteractiveMarkerControl.ROTATE_AXIS
	rotate_x_control.always_visible = True
	int_marker.controls.append(rotate_x_control)

	rotate_y_control = InteractiveMarkerControl()
	rotate_y_control.always_visible = True	
	rotate_y_control.orientation.w=1
	rotate_y_control.orientation.x=0
	rotate_y_control.orientation.y=0
	rotate_y_control.orientation.z=1
	rotate_y_control.name = "rotate_y"
	rotate_y_control.interaction_mode = InteractiveMarkerControl.ROTATE_AXIS
	rotate_y_control.always_visible = True
	int_marker.controls.append(rotate_y_control)

	rotate_z_control = InteractiveMarkerControl()
	rotate_z_control.always_visible = True	
	rotate_z_control.orientation.w=1
	rotate_z_control.orientation.x=0
	rotate_z_control.orientation.y=1
	rotate_z_control.orientation.z=0
	rotate_z_control.name = "rotate_z"
	rotate_z_control.interaction_mode = InteractiveMarkerControl.ROTATE_AXIS
	rotate_z_control.always_visible = True
	int_marker.controls.append(rotate_z_control)
	
	'''rotate_control = InteractiveMarkerControl()
	rotate_control.orientation.w=1
	rotate_control.orientation.x=0
	rotate_control.orientation.y=1
	rotate_control.orientation.z=0
	rotate_control.name = "moving"
	rotate_control.interaction_mode = InteractiveMarkerControl.MOVE_PLANE
	rotate_control.always_visible = True
	rotate_control.markers.append(marker)
	
	int_marker.controls.append(rotate_control)'''


	# add the interactive marker to our collection &
	# tell the server to call processFeedback() when feedback arrives for it
	server.insert(int_marker, processFeedback)
	menu_handler.insert( "Execute Motion",callback=processFeedback )
	menu_handler.insert( "Move to endeff", callback=processFeedback )
	ViaPoints=menu_handler.insert( "Multi-Step Movement")
	menu_handler.insert( "Add step-point", parent=ViaPoints ,callback=processFeedback )
	menu_handler.insert( "Execute Trajectory", parent=ViaPoints ,callback=processFeedback )
	menu_handler.insert( "Reset step-points", parent=ViaPoints, callback=processFeedback )
	menu_handler.insert("set xyz", callback=processFeedback)
	menu_handler.insert("set orientation", callback=processFeedback)
	menu_handler.apply( server, int_marker.name )

	# 'commit' changes and send to all clients
	server.applyChanges()

	rospy.spin()
