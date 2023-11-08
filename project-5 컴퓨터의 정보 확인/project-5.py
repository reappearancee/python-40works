import psutil

### 5-1번
# cpu = psutil.cpu_freq()
# print(cpu)

# cpu_core = psutil.cpu_count(logical=False)
# print(cpu_core)

# memory = psutil.virtual_memory()
# print(memory)

# disk = psutil.disk_partitions()
# print(disk)

# net = psutil.net_io_counters()
# print(net)

### 5-2번
# cpu = psutil.cpu_freq()
# cpu_current_ghz = round(cpu.current / 1000, 2)
# print(f"cpu속도 : {cpu_current_ghz}GHz")

# cpu_core = psutil.cpu_count(logical=False)
# print(f"코어 : {cpu_core}개")

# memory = psutil.virtual_memory()
# memory_total = round(memory.total / 1024 **3)
# print(f'메모리: {memory_total}GB')

# disk = psutil.disk_partitions()
# for p in disk:
#     print(p.mountpoint, p.fstype, end=' ')
#     du = psutil.disk_usage(p.mountpoint)
#     disk_total = round(du.total / 1024 **3)
#     print(f'디스크크기:{disk_total}GB')

# net = psutil.net_io_counters()
# sent = round(net.bytes_sent/1024**2, 1)
# recv = round(net.bytes_recv/1024**2, 1)
# print(f'보내기: {sent}MB받기: {recv}MB')

### 5-3번
curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0 

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    print(f'CPU사용량 : {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3, 1)
    
    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent, 1)
    recv = round(curr_recv-prev_recv, 1)

    print(f'보내기 : {sent}MB받기 : {recv}MB')

    prev_recv = curr_recv
    prev_sent = curr_sent