#!/usr/bin/env python3

import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Float64, Int16

class StanleyController:
    def __init__(self):
        self.midpoints = None
        self.k = 0.3
        self.filtered_yaw = 0.0
        self.gps_speed = 0.0
        self.decelerate_counter = 0
        self.accelerate_counter = 0
        self.curve_flag = False  # Flag to indicate whether curve action was executed
        self.straight_flag = False  # Flag to indicate whether straight action was executed
        self.prev_yaw = 0

        self.vehicle_pos = np.array([0, 0])
        self.rate = rospy.Rate(20)
        self.sub_path = rospy.Subscriber('/path_planning', PointCloud2, self.path_callback)
        self.sub_gps_speed = rospy.Subscriber('/gps_speed', Float64, self.gps_speed_callback)
        self.pub_steering = rospy.Publisher('/steering_angle', Int16, queue_size=1)
        self.pub_speed = rospy.Publisher('/decelerate_speed', Int16, queue_size=1)
        self.pub_regen_brake = rospy.Publisher('/motor', Int16, queue_size=1)


    def path_callback(self, msg):
        self.midpoints = np.array(list(pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))))
        self.control()

    def gps_speed_callback(self, msg):
        self.gps_speed = msg.data

    def calculate_curvature(self, yaw):
        # 곡률은 연속된 두 포인트 간의 각도 차이로 추정합니다.
        curvature = abs(yaw)# -self.prev_yaw

        # 최대 곡률을 np.pi /2로 설정
        #curvature = min(curvature ,np.pi /2)
        self.prev_yaw = yaw
        return curvature
    
    def control(self):
        if self.midpoints is None:
            return

        fifth_point = self.midpoints[7]
        last_point = self.midpoints[-1]
        slope = np.arctan2(last_point[1] - fifth_point[1], last_point[0] - fifth_point[0])
        # print(fifth_point)
        # print(last_point)
        
        if slope >= np.pi/8 and slope <= np.pi*7/8:
            self.decelerate_counter += 1
            self.accelerate_counter = 0
    
            if self.decelerate_counter >= 2 and not self.curve_flag:
                #print("50")
                # print(slope)
                self.pub_regen_brake.publish(Int16(1))
                #rospy.sleep(1)
                self.pub_regen_brake.publish(Int16(0))
                self.pub_speed.publish(Int16(50))
                self.curve_flag = True
                self.straight_flag = False
                self.decelerate_counter = 0
                
        else:
            self.accelerate_counter += 1
            self.decelerate_counter = 0
            if self.accelerate_counter >= 10 and not self.straight_flag:
                #print("150")
                self.pub_speed.publish(Int16(150))
                self.pub_regen_brake.publish(Int16(0))
                self.straight_flag = True
                self.curve_flag = False
                self.accelerate_counter = 0
                
        # print(slope)        

        x_error = self.midpoints[3][1]
        first_point = self.midpoints[0]
        lastest_point = self.midpoints[5]
        yaw = np.arctan2(lastest_point[1] - first_point[1], lastest_point[0] - first_point[0])
        # yaw = yaw * 0.5

        if self.gps_speed > 1 and self.gps_speed < 30:
            speed_for_calculation = self.gps_speed
        else:
            speed_for_calculation = 1

        if yaw >= np.pi/2:
            yaw = yaw - np.pi

        #if slope >= np.pi/2:
        #    slope = slope - np.pi

        # print("yaw :",yaw)
        # print("slope :",slope)
        
        curvature = self.calculate_curvature(yaw)

        # 선형 보간을 사용하여 k 값을 동적으로 조정
        k_straight = 0.1  # 직선 코스용 k 값
        k_curve = 0.5  # 곡선 코스용 k 값

        # 곡률의 기준값
        curvature_straight = 0.0
        curvature_curve = np.pi / 2

        # 선형 보간
        self.k = np.interp(curvature, [curvature_straight, curvature_curve], [k_straight, k_curve])

        steering_angle = yaw + np.arctan2(self.k * x_error, speed_for_calculation)

        max_steering_angle = np.radians(25)
        steering_angle = np.clip(steering_angle, -max_steering_angle, max_steering_angle)

        mapped_steering_angle = np.interp(steering_angle, [-max_steering_angle, max_steering_angle], [6.54, 78])
        self.pub_steering.publish(Int16(data=int(mapped_steering_angle)))
        
        print("steering_angle:",steering_angle)
        print("mapping:",mapped_steering_angle)
        print("yaw :",yaw)
        print("k :",self.k)
        print("뒤:", np.arctan2(self.k * x_error, speed_for_calculation))
        
        
        self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('stanley_controller')
    controller = StanleyController()
    rospy.spin()
