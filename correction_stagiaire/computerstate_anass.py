import psutil
import os
import sys

original_stdout = sys.stdout
file_path = sys.argv[1]
# file_path = 'nouveau_fichExo.txt'
sys.stdout = open(file_path, "w")

nombre_cpu = psutil.cpu_count(logical=False)
cpu_percent = psutil.cpu_percent(1)
vir_memo_tot = psutil.virtual_memory().total
vir_memo_used = psutil.virtual_memory().used
vir_memo_percent = psutil.virtual_memory().percent
name_sys = os.uname().sysname

print(f'\n Os name: {name_sys}')
print("\n cpu_count : ",  + nombre_cpu)
print(f'\n cpu_ percent :  {cpu_percent} % ')
print("\n virtual_memory total : ", vir_memo_tot)
print("\n virtual_memory total in Gb : ", round(vir_memo_tot/1024/1024/1024, 2))
print("\n virtual_memory used : ", vir_memo_used)
print("\n virtual_memory used in Gb : ", round(vir_memo_used/1024/1024/1024, 2))
print("\n virtual_memory percent : ", vir_memo_percent, "%")


sys.stdout = original_stdout
