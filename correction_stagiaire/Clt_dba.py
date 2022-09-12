#Socket client
import socket
import time

host, port_ecoute = ('192.168.1.31', 5555) #SrvVmUb_dba -.31

mon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mon_socket.connect((host, port_ecoute))
print("connexion réussie sur :", host, ":", port_ecoute)

# address = mon_socket.accept()
# print("connexion entrante réussie", address)

# msg = "Je suis le client"
# msg =msg.encode("utf8")
mon_socket.send("Je suis DBA Client".encode())
