import argparse                   #library that allows us to command the tool from the terminal
import scapy.all as scapy         #library used for networking
from termcolor import colored
#import optparse                  #This too library that allows us to give orders from the terminal
#import args                      #Second library that allows us to command the tool from the terminal
#import sys                       #System Commands
#import os                        #Operation system commands


class ARP():
  
  def __init__(self):
    print("Scan Started ")



  def terminal_inputs(self):
   
    inputs = argparse.ArgumentParser()
    inputs.add_argument("-ip", "--ipadress",type=str,help=" Enter the 4 digit network number and range   " +  colored("EXAMPLE: 10.10.10.10/24 ","red"))
    proccess = inputs.parse_args()
     
    if proccess.ipadress == None:
      print("Broo, where is Arguments!?")
    
    else:
       print(str(proccess.ipadress) + " -->" + colored("OK!","green"))
       return  proccess
       



  def arp_request(self,ip):
    
    arp_ip_range = scapy.ARP(pdst=ip)
    brodcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = brodcast_packet / arp_ip_range
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()
    #To print summary information
    
    #ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst="192.168.1.0/24"), timeout=2)
  
  

if __name__ == "__main__":
  start = ARP()
  user_inputs = start.terminal_inputs()
  start.arp_request(user_inputs.ipadress)
