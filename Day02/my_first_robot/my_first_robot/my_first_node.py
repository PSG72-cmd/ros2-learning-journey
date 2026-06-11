import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyFirstNode(Node):

    def __init__(self):

        super().__init__("first_node")

        self.counter = 0

        self.publisher_ = self.create_publisher(
            String,
            "my_topic",
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

    def timer_callback(self):

        self.counter += 1

        msg = String()

        msg.data = f"Hello {self.counter}"

        self.publisher_.publish(msg)

        self.get_logger().info(
            f"Publishing: {msg.data}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = MyFirstNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
