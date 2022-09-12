import psutil
import sys
import os
import argparse

#Sauvegarde de la sortie standard
original_stdout = sys.stdout

#Paramétrage des arguments de la ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=argparse.FileType('w'))
args = parser.parse_args()


#Ouverture du fichier préciser dans l'argument 1 avec With "as f"
with open(sys.argv[1], 'w') as f:
    # Renvoie de la sortie standard dans f
    sys.stdout = f
    # récupération des commandes avec print
    print(f"Hostname: {os.uname().nodename}")
    print(f"OS: {os.uname().sysname}")
    print(f"cpu_count: {psutil.cpu_count()}")
    print(f"cpu_percent: {psutil.cpu_percent()}%")
    print(f"disk_usage: {psutil.disk_usage('/').percent}%")
    print(f"virtual_memory total: {psutil.virtual_memory().total}")
    print(f"virtual_memory total in Gb: {round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)}")
    print(f"virtual_memory used: {psutil.virtual_memory().used}")
    print(f"virtual_memory total in Gb: {round(psutil.virtual_memory().used / 1024 / 1024 / 1024, 2)}")
    print(f"virtual_memory percent: {psutil.virtual_memory().percent}%")
    #Restauration de la sortie standard
    sys.stdout = original_stdout
