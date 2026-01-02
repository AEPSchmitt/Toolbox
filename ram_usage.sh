free -h | awk '/Mem:/ {print "Memory Used: "$3 " / "$2 " (" $3/$2*100 "%)"}'
