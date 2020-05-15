import socket
s = socket.socket()

host = input(str("Enter Host Address : "))
port = 8081

s.connect((host,port))

print("connected .....")
name = input("Enter Name ")
while True:
    st = input(f'{name}: ')
    s.send(f'{name}: {st}'.encode())
    if(st == "Bye" or st == "bye"):
        break
    print(s.recv(1024).decode())
s.close()