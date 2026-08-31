# ==========================================
# OS-Lab 01: System Profiler
# Student ID: [67113282]
# ==========================================
import os
import platform
import psutil

# TODO: Write your system profiler code here 
# Follow the instructions in the Lab manual.

print(f"OS Name: {platform.system()} {platform.release()}")
print(f"Number of CPU Cores: {psutil.cpu_count(logical=True)}")
print(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")

