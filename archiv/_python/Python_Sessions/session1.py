import time
import sys

for i in range(100):
    time.sleep(0.25)
    sys.stdout.write(" loaded stand-by")	
    sys.stdout.write("               \r%d%%" % i)
    sys.stdout.flush()

print (" Skynet is loaded please enter your username and password when requested ")


username = input ( " Enter your username :- ")
password = input ( " Enter your pin :- ")

if username == "julian" and password == "9999" :
    print((" Hello " + username + ". The system is now on-line "))
elif username == "kyle" and password == "5555" :
    print((" Hello " + username + ". The system is now on-line "))
elif username == "rhiannon" and password == "6666" :
    print((" Hello " + username + ". The system is now on-line "))
elif username == "dojo" and password == "7777":
    print((" Hello " + username + ". The system is now on-line "))
else:
    print (" Unauthorized access !!!! this has been recorded ")

