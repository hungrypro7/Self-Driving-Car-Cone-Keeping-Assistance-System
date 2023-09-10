#!/usr/bin/env python3

import numpy as np
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import std_msgs.msg
from sklearn.cluster import DBSCAN
from sklearn.svm import SVC
from visualization_msgs.msg import Marker

def pointcloud_callback(msg):
    global midpoints

    pc_data = pc2.read_points(msg, skip_nans=True, field_names=("x", "y", "z"))
    pc_array = np.array(list(pc_data))

    # All points for clustering
    all_points = np.array([(x, y) for x, y, z in pc_array])

    # DBSCAN Clustering
    clustering = DBSCAN(eps=3, min_samples=2).fit(all_points)
    labels = clustering.labels_

    # Assuming the algorithm finds 2 clusters for the left and right lane
    left_lane_mask = labels == 0
    right_lane_mask = labels == 1

    left_lane = all_points[left_lane_mask]
    right_lane = all_points[right_lane_mask]

    # Combine lanes for SVC
    X = np.vstack((left_lane, right_lane))
    y = np.hstack((np.zeros(len(left_lane)), np.ones(len(right_lane))))

    # Train an SVC model
    model = SVC(kernel='rbf', C=3.0, gamma='scale')
    model.fit(X, y)

    xx, yy = np.meshgrid(np.linspace(min(X[:, 0]), max(X[:, 0]), 100), np.linspace(min(X[:, 1]), max(X[:, 1]), 100))
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Find points near the decision boundary
    contour_mask = np.abs(Z) < 0.05
    xs = xx[contour_mask]
    ys = yy[contour_mask]

    num_points = 20
    idxs = np.linspace(0, len(xs) - 1, num_points).astype(int)
    selected_xs = xs[idxs]
    selected_ys = ys[idxs]

    midpoints = np.column_stack((selected_xs, selected_ys, np.zeros_like(selected_xs)))

    # Find the closest and farthest points to the vehicle
    vehicle_pos = np.array([0, 0])
    distances = np.linalg.norm(midpoints[:, :2] - vehicle_pos, axis=1)
    closest_idx = np.argmin(distances)
    farthest_idx = np.argmax(distances)

    closest_point = midpoints[closest_idx]
    farthest_point = midpoints[farthest_idx]

    # Calculate the slope of the line connecting the closest and farthest points
    delta_y = farthest_point[1] - closest_point[1]
    delta_x = farthest_point[0] - closest_point[0]
    slope = delta_y / delta_x if delta_x != 0 else np.inf

    print(f"Slope of the line connecting the closest and farthest points: {slope}")

    publish_midpoint_marker(closest_point, farthest_point, msg.header.frame_id)

    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    header.frame_id = msg.header.frame_id

    fields = [
        pc2.PointField('x', 0, pc2.PointField.FLOAT32, 1),
        pc2.PointField('y', 4, pc2.PointField.FLOAT32, 1),
        pc2.PointField('z', 8, pc2.PointField.FLOAT32, 1),
    ]

    pc_msg = pc2.create_cloud(header, fields, midpoints)
    pub.publish(pc_msg)

def publish_midpoint_marker(closest_point, farthest_point, frame_id):
    # Marker for the closest point
    marker = Marker()
    marker.header.frame_id = frame_id
    marker.header.stamp = rospy.Time.now()
    marker.id = 0  # Set another unique ID
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.pose.position.x = closest_point[0]
    marker.pose.position.y = closest_point[1]
    marker.pose.position.z = closest_point[2]

    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 0.1
    marker.scale.y = 0.1
    marker.scale.z = 0.1
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0
    marker_pub.publish(marker)

    marker1 = Marker()
    marker1.header.frame_id = frame_id
    marker1.header.stamp = rospy.Time.now()
    marker1.id = 1  # Set another unique ID
    marker1.type = Marker.SPHERE
    marker1.action = Marker.ADD
    marker1.pose.position.x = farthest_point[0]
    marker1.pose.position.y = farthest_point[1]
    marker1.pose.position.z = farthest_point[2]
    marker1.pose.orientation.x = 0.0
    marker1.pose.orientation.y = 0.0
    marker1.pose.orientation.z = 0.0
    marker1.pose.orientation.w = 1.0
    marker1.scale.x = 0.1
    marker1.scale.y = 0.1
    marker1.scale.z = 0.1
    marker1.color.a = 1.0
    marker1.color.r = 1.0
    marker1.color.g = 0.0
    marker1.color.b = 0.0
    marker_pub.publish(marker1)


def listener():
    rospy.init_node('pointcloud_listener', anonymous=True)
    rospy.Subscriber('/object_centroids', PointCloud2, pointcloud_callback)
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/path_planning', PointCloud2, queue_size=10)
    marker_pub = rospy.Publisher('/midpoint_marker', Marker, queue_size=10)
    listener()
