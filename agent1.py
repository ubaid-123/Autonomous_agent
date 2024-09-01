from baseAgent import BaseAgent
import threading

def run_agent1():
    server_agent = BaseAgent("Agent 1", "Generic Health Agent")
    server_agent.socket.bind((server_agent.host, server_agent.port))
    server_agent.socket.listen(1)
    print(f"Agent 1 server listening on port {server_agent.port}")
    
    conn, addr = server_agent.socket.accept()
    print(f"Connected to {addr}")

    server_agent.run_agent_threads()

    threading.Thread(target=server_agent.handle_incoming_messages, args=(conn,), daemon=True).start()

    server_agent.send_outbox_messages(conn)
    server_agent.close_connection(conn)

if __name__ == "__main__":
    run_agent1()