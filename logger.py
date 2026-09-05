from datetime import datetime




def save_log(message):
    with open("logs/server.log", "a") as file:
       timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       file.write(f"[{timestamp}] {message}\n")
