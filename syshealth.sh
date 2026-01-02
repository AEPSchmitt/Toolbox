#!/bin/bash

echo "===== 🖥️ System Health Check ====="
echo
echo "📌 Uptime:"
uptime
echo
echo "📌 CPU Usage:"
mpstat 1 1 | awk '/Average/ && $12 ~ /[0-9.]+/ {print 100 - $12 "% used"}'
echo
echo "📌 Memory Usage:"
free -h | awk '/Mem:/ {print $3 " / " $2 " (" $3/$2*100 "%)"}'
echo
echo "📌 Disk Usage:"
df -h --output=source,pcent,size,used,avail | grep -v 'tmpfs'
echo
echo "📌 Top 5 CPU Processes:"
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6
echo
echo "📌 Top 5 Memory Processes:"
ps -eo pid,comm,%mem,%cpu --sort=-%mem | head -n 6
echo
echo "📌 Active Network Connections:"
ss -tunap | wc -l
