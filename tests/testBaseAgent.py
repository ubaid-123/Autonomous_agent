import unittest
from baseAgent import BaseAgent

class TestBaseAgent(unittest.TestCase):
    def test_initialization(self):
        # Test the initialization of the BaseAgent class.
        agent_name = "Test Agent"
        role = "Test Role"
        base_agent = BaseAgent(agent_name, role)

        self.assertEqual(base_agent.agent.name, f"{agent_name} ({role})")
        self.assertEqual(base_agent.host, 'localhost')
        self.assertEqual(base_agent.port, 9999)
        self.assertIsInstance(base_agent.socket, object)
        self.assertTrue(hasattr(base_agent, 'handle_incoming_messages'))
        self.assertTrue(hasattr(base_agent, 'run_agent_threads'))
        self.assertTrue(hasattr(base_agent, 'send_outbox_messages'))
        self.assertTrue(hasattr(base_agent, 'close_connection'))

if __name__ == '__main__':
    unittest.main()
