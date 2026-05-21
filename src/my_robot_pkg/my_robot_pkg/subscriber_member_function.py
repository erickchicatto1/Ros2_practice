import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import Num

class MinimalSubscriber(Node):
    
    def __init__(self):
        super().__init__('minimal_publisher')
        self.subscription = self.create_subscription(
	    Num,
	    'topic',
	    self.listener_callback,
	    10)
        self.subscription
	
    def listener_callback(self,msg):
        self.get_logger().info('I heard:"%s"' % msg.num)
        
        
def main(args=None):
    try:
        rclpy.init(args=args)
        minimal_subscriber = MinimalSubscriber()
        rclpy.spin(minimal_subscriber)
    except (KeyboardInterrupt,ExternalShutdownException):
        pass
        
if __name__ == '__main__':
    main()
