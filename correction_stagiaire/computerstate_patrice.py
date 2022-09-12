import psutil
import platform
import math
import sys

# récupération du nom du fichier sur la ligne d'arguments
file_name = sys.argv[1]

# création du dictionnaire
d = dict()

# insertion des paires "clé : valeur"
d["Hostname"] = platform.uname().node
d["OS"] = platform.system()
d["cpu_count"] = psutil.cpu_count(logical=False)
d["cpu_percent"] = "{}%".format(round(psutil.cpu_percent(interval=1), 2))
d["disk_usage"] = "{}%".format(round(psutil.disk_usage('/').percent, 2))
d["virtual_memory total"] = psutil.virtual_memory().total
d["virtual_memory total in Gb"] = "{}".format(round(psutil.virtual_memory().total/math.pow(1024, 3), 2))
d["virtual_memory used"] = psutil.virtual_memory().used
d["virtual_memory used in Gb"] = "{}".format(round(psutil.virtual_memory().used/math.pow(1024, 3), 2))
d["virtual_memory percent"] = "{}%".format(round(psutil.virtual_memory().percent), 2)

# ouverture du fichier en écriture
with open(file_name, "w") as f:
    # parcours des paires "clé : valeur"
    for k, v in d.items():
        # création de la chaîne de caractères à traiter
        line = f"{k}:{v}\n"
        # affichage de la chaîne sur la sortie std => ici l'écran
        print(line, end="")
        # écriture de la ligne dans le fichier
        f.write(line)
