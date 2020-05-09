import json
import sys

import psutil


def fecth_memoryinfo():
    procs = {}
    # process_name = "System"
    for proc in psutil.process_iter():
        process = psutil.Process(proc.pid)  # Get the process info using PID
        pname = process.name().lower().replace('.exe', '')  # Here is the process name
        if pname in procs:
            procs[pname] += process.memory_info().private
        else:
            procs[pname] = process.memory_info().private

    with open("out.json", 'w+') as out:
        json.dump(procs, out)
