import os, time, logging
write = open("test.log", "a")
host = "google.com"

while True:
    write.write(str(os.system("ping -c 1 " + host)))
    time.sleep(10)

