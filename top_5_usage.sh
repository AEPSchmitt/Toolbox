ps -eo pid,comm,%mem,%cpu --sort=-%mem | head -n 6

ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6
