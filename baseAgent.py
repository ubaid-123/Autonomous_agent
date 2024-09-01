import socket
import time
import threading
from autonomousAgent import ConcreteAgent

class BaseAgent:
    def __init__(self, agent_name, role, host='localhost', port=9999):
        self.agent = ConcreteAgent(f"{agent_name} ({role})")
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_incoming_messages(self, conn):
        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if data:
                    self.agent.inbox.put(data)
                else:
                    break
            except socket.error as e:
                if isinstance(e, ConnectionResetError) or isinstance(e, OSError):
                    break
                print(f"Error receiving data: {e}")
                break

    def run_agent_threads(self):
        threading.Thread(target=self.agent.handle_messages, daemon=True).start()
        threading.Thread(target=self.agent.run_behaviors, daemon=True).start()

    def send_outbox_messages(self, conn, duration=15):
        start_time = time.time()
        while True:
            if not self.agent.outbox.empty():
                message = self.agent.outbox.get()
                conn.sendall(message.encode('utf-8'))
            if time.time() - start_time > duration:
                print(f"{duration} seconds elapsed. Shutting down.")
                break
            time.sleep(1)

    def close_connection(self, conn):
        conn.close()
        self.socket.close()
