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

'''display_traj_pub=rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
marker_pub= rospy.Publisher('/via_points',MarkerArray,queue_size=20)
group_name = "robot_arm"
group = moveit_commander.MoveGroupCommander(group_name)
rospy.init_node("robot_program_node")
listener=tf.TransformListener()
listener.waitForTransform('/end_of_arm_tool_link','/bottom_base_link',rospy.Time(), rospy.Duration(1.0))
PoseStamped = group.get_current_pose()
print(PoseStamped)
target_pose1 = PoseStamped.pose

target_pose1.orientation.w = target_pose1.orientation.w
target_pose1.position.x = target_pose1.position.x + 0.01
target_pose1.position.y = target_pose1.position.y
target_pose1.position.z = target_pose1.position.z - 0.01'''

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("robot_program_node") #Creates new node
robot = moveit_commander.RobotCommander() #outer level interface to robot
scene = moveit_commander.PlanningSceneInterface()

group_name = "robot_arm"
group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)  #publish trajectories for rviz to visualize

# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print("============ Reference frame: %s" % planning_frame)

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print("============ End effector: %s" % eef_link)

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print("============ Robot Groups:", robot.get_group_names())

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print("============ Printing robot state")
print(robot.get_current_state())
print()

#We can plan a motion for this group to a desired pose for the end-effector:
pose_goal = geometry_msgs.msg.Pose() #no idea what this does, file of PoseStamped class is C:\opt\ros\melodic\x64\lib\site-packages\geometry_msgs\msg\_PoseStamped.py
pose_goal.orientation.w = 1.0
pose_goal.position.x = 1.0
pose_goal.position.y = 1.0
pose_goal.position.z = 7.0
group.clear_pose_targets()
group.set_joint_value_target(pose_goal, True)
#group.set_pose_target(pose_goal)




plan = group.go(wait=True)
group.stop()
group.clear_pose_targets()



pose_goal.position.x = 2.0
pose_goal.position.y = 2.0
pose_goal.position.z = 6.0
group.clear_pose_targets()
group.set_joint_value_target(pose_goal, True)

plan = group.go(wait=True)
group.stop()
group.clear_pose_targets()
#"C:\opt\ros\melodic\x64\python.exe" C:\Users\robc\ROS\three_DOF_robotic_arm_ws\src\robot_moveit_config\scripts\robot_move.py