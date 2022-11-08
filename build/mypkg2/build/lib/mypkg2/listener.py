import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):

    def __init__(self):
        super().__init__("Listener")
        self.create_subscription(Init16, "countup", self.cb, 10)

    def cd(self, msg):
        self.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
rclpy.spin( ListenerNode() )
