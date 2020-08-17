# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:07:57 2020

@author: rakes
"""
import psutil

def cpu_info():
    print("="*20, "Cpu Information", "="*20)
    #Amount of cores
    print("physical cores :", psutil.cpu_count(logical=False))
    print("total cores :", psutil.cpu_count(logical=True))
    #frequency 
    cpufreq = psutil.cpu_freq()
    print(f"Max frequency :{cpufreq.max:.2f}Mhz")
    print(f"Min frequency :{cpufreq.min:.2f}Mhz")
    print(f"current frequency :{cpufreq.current:.2f}Mhz")
    #usage
    print("Cpu usage per core")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval = 1)):
        print(f"core{i}: {percentage}%")
    print(f"Total_cpu_usage: {psutil.cpu_percent()}%")
    
if __name__ == "__main__":
    cpu_info()