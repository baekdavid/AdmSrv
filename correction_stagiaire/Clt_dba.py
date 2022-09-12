#Socket client
import socket

host, port_ecoute = ('192.168.1.31', 5555) #SrvVmUb_dba -.31

mon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mon_socket.connect((host, port_ecoute))
print("connexion réussie sur :", host, ":", port_ecoute)
address = mon_socket.accept()
print("connexion entrante réussie", address)