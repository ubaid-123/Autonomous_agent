import unittest
import threading
import socket
import time
from agent1 import run_agent1
from agent2 import run_agent2

class TestIntegrationAgents(unittest.TestCase):
    def test_agent_communication(self):
        #Test communication between agent1 and agent2.
        # Start server in a separate thread
        server_thread = threading.Thread(target=run_agent1, daemon=True)
        server_thread.start()
        
        # Allow the server some time to start up
        time.sleep(1)
        
        # Start client in a separate thread
        client_thread = threading.Thread(target=run_agent2, daemon=True)
        client_thread.start()
        
        # Allow some time for communication
        time.sleep(17)
        
        # After 12 seconds (server & client should have shut down)
        # Assert server socket is closed
        with self.assertRaises(OSError):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('localhost', 9999))
        
if __name__ == '__main__':
    unittest.main()
