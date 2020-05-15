import socket

s = socket.socket()
host = socket.gethostname()
port = 8081
print(host)

s.bind((host,port))
s.listen(1)
print("Waiting for any incoming connections ...")
conn, addr = s.accept()

print(addr, "Has connected successfully")

name = input("Enter your name: ")
while True:
    rD = conn.recv(1024).decode()
    print(rD)
    sD = input(f'{name}: ')
    conn.send(f'{name}: {sD}'.encode())
    if(sD == "Bye" or sD == "bye"):
        break
conn.close()