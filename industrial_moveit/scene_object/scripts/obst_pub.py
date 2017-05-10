#!/usr/bin/env python
# license removed for brevity
import rospy
from moveit_msgs.msg import CollisionObject
from geometric_shapes_msgs.msg import Shape
from geometry_msgs.msg import Pose

def obst_pub():
    pub = rospy.Publisher('moveit_msgs/CollisionObject', CollisionObject, queue_size=10)
    rospy.init_node('obstacles_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        cylinder_object=CollisionObject()
        cylinder_object.id = "pole";
        cylinder_object.operation = cylinder_object.ADD;
        cylinder_object.header.frame_id = "base_link";
        cylinder_object.header.stamp = rospy.Time.now()
        object=Shape();
        object.type = Shape.CYLINDER;
        object.dimensions.resize(2);
        object.dimensions[0] = .1;
        object.dimensions[1] = .75;
        pose = Pose()
        pose.position.x = .6;
        pose.position.y = -.6;
        pose.position.z = .375;
        pose.orientation.x = 0;
        pose.orientation.y = 0;
        pose.orientation.z = 0;
        pose.orientation.w = 1;
        cylinder_object.shapes.push_back(object);
        cylinder_object.poses.push_back(pose);   
        rospy.loginfo(cylinder_object)
        pub.publish(cylinder_object)
        rate.sleep()

if __name__ == '__main__':
    try:
        obst_pub()
    except rospy.ROSInterruptException:
        pass