import os
import platform
from setup import colors
from setup.colors import r,g,y,c

logo = f"""


                       ,,.*((####(###(//***, ***                            
                  /./#################(/********** .(                       
               .(#####################(/************** *.                   
            ,%########################(/***************** ,                 
          .##########################(//********************,               
        ,(#############################/*********************.,             
       *##############################//*********************** .           
      /###############################(/************************ ,          
     *###############################(/**************************           
    .###############################(//******  . ..  . ...  ******.         
   .################################(((/***    ***********    .*** *        
   /(################################(//****************************        
   ,##################################(/***********          *******        
   ,#########(#########(/##############//*****   *,  .******** *****        
   ,########(           .##((#########(/**. ,*****.  .*************/        
   ,#################/       .########(/ *********   *************/,        
   /(####################/     .#####(/*******/*,   ..  ,***/*.***,*        
   ((###########(/***/((#############(/***, ,.****,,***,,,.. .****.(       
   ./##########/.         ,##########(/**.             ,,.     ,**..        
    ,################################//****, ..,,*,   , /*********        
     ################################(/************   ************          
    ((###############################(//***********   ************(     
     ,###############################(/***********,   ***********.          
     *(#############################(/******* *************** .*/,          
      .#############################(/******** .    ..,,.    .**.           
       .(##################. ,#######(/**   * .,,,,*,,,,,,, */*.            
        ,/##################### ,(###(. ,,,,,,,,,,,,,,, ,, ***,             
         (//#########################(*,,,,,,,,,,,,,,. ,.,* ,/              
          ,*,#######################(/*,,,,,,,,..   ,,,.**. /               
            .(,####################/.        ..,,, .. ** *.     
             /(*/###################(**,,...   .,.**.* ,./              
               .#,(##################(*,,,,,  **** **./                     
                 *(,(###############/**********, ** * /             
                  //#,##############(/******* *** *,(                       
                    #,#*(###########//********,,*.(                         
                       .(#/#########//****** **.                            
                          .(########//*****,.*                              
                             ,.*(##(//* ./




                             {c + "coded By: hacker_6_2_9_1"+y +" "}             
                                                                                                                   
"""
c = colors
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")

def banner():
    print(c.ran + logo)
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @qadirahmad ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @qadirahmad6291 ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/hacker629 ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @qadirahmad ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram@qadirahmad6291", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github:  https://github.com/hacker6291  ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
