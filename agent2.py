from baseAgent import BaseAgent
import threading

def run_agent2():
    client_agent = BaseAgent("Agent 2", "Patient Care Coordinator")
    client_agent.socket.connect((client_agent.host, client_agent.port))
    print(f"Agent 2 connected to Agent 1 server on port {client_agent.port}")

    client_agent.run_agent_threads()

    threading.Thread(target=client_agent.handle_incoming_messages, daemon=True, args=(client_agent.socket,)).start()

    client_agent.send_outbox_messages(client_agent.socket)
    client_agent.close_connection(client_agent.socket)

if __name__ == "__main__":
    run_agent2()
