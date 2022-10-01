import psutil

print("{:<6} {:<20.19} {:>10} {:>6}".format('PID', 'NAME', 'MEMORY', 'CPU'))

for process in psutil.process_iter():
    try:
        info = process.as_dict(attrs=['name', 'pid', 'memory_percent', 'cpu_percent'])

        text = '{:<6}'.format(info['pid'])
        text = text + '{:<20.19}'.format(info['name'])
        text = text + '{:>10.2f}'.format(info['memory_percent'])
        text = text + '{:>10.2f}'.format(info['cpu_percent'])
        print(text)

    except psutil.NoSuchProcess:
        pass
