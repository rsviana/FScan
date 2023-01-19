import paramiko, os
def ssh_command(ip, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.invoke_shell()
    while True:
        command = input("Enter command (exit to close connection): ")
        if command.strip() == "exit":
            break
        ssh_session.send(command + "\n")
        while not ssh_session.recv_ready():
            pass
        print(ssh_session.recv(1024).decode())
    client.close()
    os.system('python main.py') 
