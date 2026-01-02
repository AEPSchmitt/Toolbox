mpstat 1 1 | awk '/Average/ && $12 ~ /[0-9.]+/ {print "CPU Usage: " 100 - $12 "%"}'
