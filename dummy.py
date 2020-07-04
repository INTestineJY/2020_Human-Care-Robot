# #!/usr/bin/env python
#
# import rospy
# import yaml
# import rospkg
# from geometry_msgs.msg import PoseStamped
# from actionlib_msgs.msg import GoalID #cancel goal. 1안
# from move_base_msgs.msg import MoveBaseActionResult
# from human.msg import order
# from human.msg import stop
# import sys, select, termios, tty
#
#
# class ServiceCore:
#     def __init__(self):  # 변수, publisher, subscriber 등 선언
#
#         # 방문 장소의 좌표를 저장. [0]: 대기 장소, [1]~[n]: 방문 가능 장소
#         self.poseStampedTable = [0] * (n + 1)
#         # 프로세스를 나타내는 변수
#         self.is_robot_reached_target = True
#         self.robot_service_sequence = 0
#         self.goal = -1
#
#         self.InitParam()
#
#         # publisher, subscriber 선언
#         self.pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
#         self.pub2 = rospy.Publisher('move_base/cancel', GoalID, queue_size=10)  # 1안
#
#
#         rospy.Subscriber('order', order, self.ReceiveOrder)
#         rospy.Subscriber('stop', stop, self.ChangeOrder)
#         rospy.Subscriber('move_base/result', MoveBaseActionResult, self.cbCheckArrivalStatus)
#
#         rate = rospy.Rate(10)
#         while not rospy.is_shutdown():
#             self.PubPose()
#         rate.sleep()
#
#
#     def InitParam(self):  # 선택 가능한 목적지의 좌표값을 리스트에 저장
#
#
#         # yaml 파일의 목적지 좌표 읽어오기.
#         rospack = rospkg.RosPack()
#         path_loc = rospack.get_path("human") + "/param/target_pose.yaml"
#         with open(path_loc, 'r') as doc:
#             loc = yaml.load(doc)
#
#         # 장소 별로 코드 반복..
#         for i in range(0, n + 1):
#             now = rospy.Time.now()
#
#             self.poseStampedTable[i] = PoseStamped()
#
#             self.poseStampedTable[i].header.frame_id = "map"
#             self.poseStampedTable[i].header.stamp = now
#
#             self.poseStampedTable[i].pose.position.x = float(loc["place_" + str(i)]["position"][0])
#             self.poseStampedTable[i].pose.position.y = float(loc["place_" + str(i)]["position"][1])
#             self.poseStampedTable[i].pose.position.z = float(loc["place_" + str(i)]["position"][2])
#
#             self.poseStampedTable[i].pose.orientation.x = float(loc["place_" + str(i)]["orientation"][0])
#             self.poseStampedTable[i].pose.orientation.y = float(loc["place_" + str(i)]["orientation"][1])
#             self.poseStampedTable[i].pose.orientation.z = float(loc["place_" + str(i)]["orientation"][2])
#             self.poseStampedTable[i].pose.orientation.w = float(loc["place_" + str(i)]["orientation"][3])
#
#
#     def PubPose(self):  # 적당한 타이밍에 move_base 노드에 목적지 전송
#
#
#         if self.is_robot_reached_target:
#
#         if self.robot_service_sequence == 1:
#             self.pub.publish(self.poseStampedTable[self.goal])  # 수신한 목적지로
#             self.is_robot_reached_target = False  # 주행 중
#             self.robot_service_sequence = 2  # 도착 후에 수행할 단계
#             self.goal = -1
#
#         elif self.robot_service_sequence == 2:
#             self.goal = 0
#             self.pub.publish(self.poseStampedTable[self.goal])  # 대기 장소로
#             self.is_robot_reached_target = False  # 주행 중
#             self.robot_service_sequence = 0  # 도착 후에 수행할 단계
#             self.goal = -1
#
#
#     def ReceiveOrder(self, Data):  # 목적지 정보 수신
#
#
#         # 주행 중이거나, 대기 상태가 아니거나, 목적지가 이미 정해져 있으면
#         if self.is_robot_reached_target is False:
#             return
#         if self.robot_service_sequence != 0:
#             return
#         if self.goal != -1:
#             return
#
#         self.goal = Data.index
#         self.robot_service_sequence = 1
#
#
#     def ChangeOrder(self, Data):  #
#
#
#         if Data.stop == 1:
#             self.ResetGoal()
#         elif Data.stop == 2:
#             self.Restart()
#
#
#     def Restart(self, Data):  # 다시 출발
#
#
#         # 다시 주행하라는 명령을 받고 움직임.
#         self.is_robot_reached_target = True
#         self.robot_service_sequence = 1
#
#
#     def ResetGoal(self, Data):  # 정지
#
#
#         self.stop = GoalID()
#         now = rospy.Time.now()
#         self.stop.stamp = now
#         self.stop.id = "ui"  # id unique 해야한다길래 일단 마음대로 정함.. 안될 수 있음.
#         self.pub2.publish(self.stop)
#
#
#     def CheckArrivalStatus(self, Data):  # 도착 여부 수신
#
#
#         # 목적지에 도착했다는 메시지가 수신되면 주행 중 상태를 해제
#         # 목적지 새로 설정 가능
#         if Data.data == 1:
#             self.is_robot_reached_target = True
#
# if __name__ =="__main__":
#     rospy.init_node("service_core", anonymous = True)
#     ServiceCore()
#     rospy.spin()

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('move_base_simple/goal', String, queue_size=10)
pub.publish(poseStampedTable[goal])
