# Objectif du programme monitoring.py : A chaque exécution le programme récupère les informations suivantes :
# Ces informations seront structuré dans un tableau stocké sous forme d’un fichier csv avec comme
# séparateur de champs le caractère « ; »
# Le fichier se normera monitoring.csv
#
# Les enregistrements devront être ajouté aux précédentes a chaque exécution afin de pouvoir les historiser

# Import
import datetime
import psutil
import pandas as pd

# Date d’exécution au format JJ-MM-AAAA
today = datetime.datetime.now()
jour = today.strftime("%d/%m/%Y")
# Heure d’exécution au format hh:mm:ss
heure = today.strftime("%H:%M:%S")


# Nombre de CPU
cpu_nb = psutil.cpu_count()
# % d’Utilisation du CPU
cpu_percent = psutil.cpu_percent()
# L’utilisation du disque « / » ou « C:\ » (Si c’est une machine Windows) en %
disque_percent = psutil.disk_usage("/").percent
#ajout de IF pour windows ?                                                                                               A Traiter

# La mémoire virtuelle total en Gb arrondi à 2 décimal
mem_total = round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2)

# La mémoire virtuelle utilisé en Gb arrondi à 2 décimal
mem_used = round(psutil.virtual_memory().used / 1024 / 1024 / 1024, 2)

# Le taux d’occupation de mémoire virtuelle en %
mem_percent = psutil.virtual_memory().percent

data = {
        "jour": [jour],
        "heure":[heure],
        "Nombre de CPU": [cpu_nb],
        "Utilisation du CPU": [cpu_percent],
        "Utilisation du disque": [disque_percent],
        "Memoire virtuelle totale": [mem_total],
        "Memoire virtuelle utilisée": [mem_used],
        "Memoire virtuelle utilisée en %":[mem_percent]
        }

df = pd.DataFrame(data)
print(df)

# df.to_csv("monitoring.csv", encoding='utf8', sep=';', index=False) pour créer le fichier la première fois
df.to_csv("monitoring.csv", encoding='utf8', sep=';', index=False, header=False, mode="a")

# crontab pour info : https://crontab-generator.com/fr
# m h  dom mon dow   command
# */2 * * * * /home/user/PycharmProjects/demo-app-2/venv/bin/python /home/user/PycharmProjects/demo-app-2/monitoring.py
