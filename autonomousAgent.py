import queue
import random
import time

class AutonomousAgent:
    
    def __init__(self, name):
        self.name = name      
        self.inbox = queue.Queue()
        self.outbox = queue.Queue()
        self.behaviors = []

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def handle_messages(self):
        while True:
            if not self.inbox.empty():
                message_content = self.inbox.get()
                if "hello" in message_content.lower():
                    print(f"FILTERED MESSAGE: {self.name} handling message: {message_content}")
                else:
                    print(f"{self.name} received message: {message_content}")

    def run_behaviors(self):
        while True:
            for behavior in self.behaviors:
                behavior()
            time.sleep(1)


class ConcreteAgent(AutonomousAgent):
    def __init__(self, name):
        super().__init__(name)
        self.add_behavior(self.random_message_generator)

    def random_message_generator(self):
        words = ["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"]
        message = " ".join(random.sample(words, 2))
        print(f"{self.name} generated message: {message}")
        self.outbox.put(message)
        time.sleep(2)
