import xmlrpclib, pickle, cv2, Image, os, glob, timeit
import thread  
import threading
from threading import Thread

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
proxy2 = xmlrpclib.ServerProxy("http://localhost:8001/")

i=0
os.chdir("image")
for file in glob.glob("*.*"):
    i=i+1
i = i/2
print str(i)
j=0
k=0
def fungsi():
    start = timeit.default_timer()
    for file in glob.glob("*.*"):
        j = j + 1
        if j > i:
            break
        try:
            with open("../gray/" + file, "wb") as han:
                with open(file, "rb") as hi:
                    han.write(proxy.terima(xmlrpclib.Binary(hi.read())).data)
        except:
            print file
    stop = timeit.default_timer()
    time = stop - start
    print "Waktu total server 1 = " + str(time)

def fungsi2():
    start = timeit.default_timer()
    for file in glob.glob("*.*"):
        k = k + 1
        if k <= i:
            continue
        try:
            with open("../gray/" + file, "wb") as han:
                with open(file, "rb") as hi:
                    han.write(proxy.terima2(xmlrpclib.Binary(hi.read())).data)
        except:
            print file
    stop = timeit.default_timer()
    time = stop - start
    print "Waktu total server 2 = " + str(time)

("Thread-2", 4, )

try:
    thread.start_new_thread(fungsi,("Thread-1", ));
    thread.start_new_thread(fungsi2),("Thread-2", );
except:
    print "error thread"


