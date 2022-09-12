import psutil
import pandas
from datetime import datetime

df = pandas.read_csv('cpstate.csv', sep=';')

data = [f"{datetime.now().strftime('%Y-%m-%d')}",
        f"{datetime.now().strftime('%H:%M:%S')}",
        f"{psutil.cpu_count()}",
        f"{psutil.cpu_percent()}",
        f"{psutil.disk_usage('/').percent}",
        f"{round(psutil.virtual_memory().total / (1024*1024*1024) , 2)}",
        f"{round(psutil.virtual_memory().used / (1024*1024*1024) , 2)}",
        f"{psutil.virtual_memory().percent}"]

n = pandas.DataFrame([data], columns=['date',
                                    'time',
                                    'cpu_count',
                                    'cpu_percent',
                                    'disk_usage',
                                    'virtual_memory_total',
                                    'virtual_memory_used',
                                    'virtual_memory_percent'])
df = pandas.concat([df,n])
df.to_csv('cpstate.csv', sep=';',index=False)