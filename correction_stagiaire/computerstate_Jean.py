import os
import psutil
import sys

file = sys.argv[1]

# Save a reference to the original standard output :
original_stdout = sys.stdout

with open(file, 'w') as f:
    sys.stdout = f
# Type de système d’exploitation
    print("OS: " + os.uname().sysname)
# nom de la machine
    print("Hostname: " + os.uname().nodename)
# nombre de cpu
    print("cpu_count: " + str(psutil.cpu_count()))
# % d'utilisation en cpu
    print("cpu_percent: " + str(psutil.cpu_percent()) + "%")
# utilisation du disque en pourcentage
    percent_disk_usage = str(psutil.disk_usage('/'))
    print("disk_usage: " + percent_disk_usage[-5:-1] + "%")
# la mémoire virtuelle totale
    print("virtual_memory total: " + str(round(psutil.virtual_memory().total, 2)))
# la mémoire virtuelle totale en Gb
    print("virtual_memory total in Gb: " + str(round(psutil.virtual_memory().total / 1024**3, 2)))
# la mémoire virtuelle utilisée
    print("virtual_memory used: " + str(round(psutil.virtual_memory().used, 2)))
# la mémoire virtuelle utilisée en Gb
    print("virtual_memory used in Gb: " + str(round(psutil.virtual_memory().used / 1024**3, 2)))
# le taux d'occupation de la mémoire
    print("virtual_memory percent: " + str(psutil.virtual_memory().percent) + "%")

sys.stdout = original_stdout