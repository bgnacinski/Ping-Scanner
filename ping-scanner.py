import threading
import sys
import os

def ping(host):
    os.system("ping -c 1 %s | grep '64 bytes' | cut -d' ' -f4 | sed 's/.$//'" % host)

try:
    for i in range(1, 255):
        ip = "%s.%r" % (sys.argv[1], str(i))

        ping_thread = threading.Thread(target=ping, args=(ip,))
        ping_thread.start()

except Exception as e:
    print("[ERROR] " + str(e).replace("[Errno ","").replace("]",""))