from RobotRaconteur.Client import *
import time
import numpy as np
import matplotlib.pyplot as plt

c = RRN.ConnectService('rr+tcp://ros-dist-ui:11111?service=tormach_robot')

cmd_w = c.position_command.Connect()
state_w = c.robot_state.Connect()
state_w.WaitInValueValid()

robot_const = RRN.GetConstants("com.robotraconteur.robotics.robot", c)
halt_mode = robot_const["RobotCommandMode"]["halt"]
trajectory_mode = robot_const["RobotCommandMode"]["trajectory"]
jog_mode = robot_const["RobotCommandMode"]["jog"]

RobotJointCommand = RRN.GetStructureType("com.robotraconteur.robotics.robot.RobotJointCommand",c)

c.command_mode = halt_mode
time.sleep(0.1)
c.command_mode = jog_mode

while np.linalg.norm(state_w.InValue.joint_position)>0.01:
	c.jog_joint(-0.2*state_w.InValue.joint_position,1, True)
print('jog complete')



c.command_mode = halt_mode
time.sleep(0.1)
c.command_mode = trajectory_mode



JointTrajectoryWaypoint = RRN.GetStructureType("com.robotraconteur.robotics.trajectory.JointTrajectoryWaypoint",c)
JointTrajectory = RRN.GetStructureType("com.robotraconteur.robotics.trajectory.JointTrajectory",c)
waypoints = []

for i in range(10000):
	t=float(i/1000.)
	wp = JointTrajectoryWaypoint()
	wp.joint_position = [np.sin(t)/4.,np.sin(t)/4.,np.sin(t)/4.,np.sin(t)/4.,np.sin(t)/4.,np.sin(t)/4.]
	wp.time_from_start = t
	waypoints.append(wp)

traj = JointTrajectory()
# traj.joint_names = [j.joint_identifier.name for j in c.robot_info.joint_info]
traj.joint_names=['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6']
traj.waypoints = waypoints


traj_gen = c.execute_trajectory(traj)

while (True):
	t = time.time()

	try:
		res = traj_gen.Next()
	except RR.StopIterationException:
		print('completed')
		break

# plt.plot(time_stamps,joint_positions_history)
# plt.plot(time_stamps,desired_position)

# plt.title('sin_traj')
# plt.show()