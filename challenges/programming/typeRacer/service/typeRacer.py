#! /usr/bin/env python3
import socket, threading
from random import *
from threading import Timer
GREEN = '\033[94m'
END = '\033[0m'
PORT= 30152
start='''Welcome to the Fastest Hand in the West. Type 300 words in 1 minute to get the flag\nPress any button to start\n'''
def timeout():
    con.sendall("\n\n\nTimes up, Press Enter to see your score\n".encode())


wordlist=[]
with open("wordlist.txt","r") as f:
	for line in f:
		wordlist.append(line.strip())


def question(con,addr):
	
	
	try:
		correct=0
		wrong=0
		t = Timer(60, timeout)
		t.start()
		con.sendall(start.encode())
		#con.settimeout(20)
		startTest=con.recv(100)
		#con.settimeout(5)
		if  startTest:
				for i in range(len(wordlist)):
					if not t.is_alive():
						break
					x=randint(0,len(wordlist)-1)
					buf=GREEN+wordlist[x]+END+'\n'
					con.sendall(buf.encode())
					ans=str(wordlist[x]).lower().strip()
					userAns=con.recv(100).decode().lower().strip()
					con.sendall("\n\n".encode())
					if userAns==ans:
						correct+=1
					else:
						wrong+=1
		buf="\nYou have typed "+str(correct)+" correct words per minute and "+str(wrong)+" wrong words\n"
		con.sendall(buf.encode())
		if correct>=300:
			con.sendall("Here is your flag: GCTF{F457_F1N93R}\n".encode())
		con.close()
	except socket.timeout:
		con.sendall("\nYou are too slow\n".encode())
		con.close()



serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0',PORT))
serversocket.listen(5)
print("Server started")
while(1):
	con,addr=serversocket.accept()
	#con.settimeout(5)
	print("A new connection to ",addr)
	threading.Thread(target = question,args = (con,addr)).start()
	


question(con)
