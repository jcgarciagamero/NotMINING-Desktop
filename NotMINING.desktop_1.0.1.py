#! /usr/bin/python3
# -*- coding: utf-8 -*-
import urllib
import os
import sys
os.system('clear')


print(" _   _       _   __  __ _____ _   _ _____ _   _  _____ ")      
print("| \ | |     | | |  \/  |_   _| \ | |_   _| \ | |/ ____|")      
print("|  \| | ___ | |_| \  / | | | |  \| | | | |  \| | |  __ ") 
print("| . ` |/ _ \| __| |\/| | | | | . ` | | | | . ` | | |_ |")
print("| |\  | (_) | |_| |  | |_| |_| |\  |_| |_| |\  | |__| |")
print("|_| \_|\___/ \__|_|  |_|_____|_| \_|_____|_| \_|\_____(")
print("                                  https://notmining.org")
print("")
print("")

print("\x1b[1;37m" + "Select an option: ")
print("(1): Scan")
print("(2): Reanalyze")
print("(3): Blacklist")
print("")
print("(0): Exit")
print("")
option = input("Option: ")


if option == 1:
	web = raw_input("Enter URL: ")
	print("Result: ")
	print("")
	scan = "https://notmining.org/api/url?busqueda="+web
	lines = urllib.urlopen(scan).read()

	search = lines.find("NOT Mining!")
	search1 = lines.find("Mining!")
	search2 = lines.find("Enter a valid URL")

	if search != -1:
		print("Not Mining")
		print("Analysis: https://notmining.org/url?busqueda="+web)
		print("")
	elif search1 != -1:
		print("Mining")
		print("Analysis: https://notmining.org/url?busqueda="+web)
		print("")
	elif search2 != -1:
		print("Enter a valid URL")
		print("")
	else:
		print("The requested website is not available, prevents its analysis, or is incorrect URL.")
		print("Analysis: "+web)
		print("")
elif option == 2:
	web = raw_input("Enter URL: ")
	scan = "https://notmining.org/api/scan?busqueda="+web
	lines = urllib.urlopen(scan).read()

	search = lines.find("NOT Mining!")
	search1 = lines.find("Mining!")
	search2 = lines.find("Enter a valid URL")

	if search != -1:
		print("Not Mining")
		print("Analysis: https://notmining.org/url?busqueda="+web)
		print("")
	elif search1 != -1:
		print("Mining")
		print("Analysis: https://notmining.org/url?busqueda="+web)
		print("")
	elif search2 != -1:
		print("Enter a valid URL")
		print("")
	else:
		print("The requested website is not available, prevents its analysis, or is incorrect URL.")
		print("Analysis: https://notmining.org/url?busqueda="+web)
		print("")

elif option == 3:
	os.system('clear')
	web = "https://notmining.org/export.php"
	lines = urllib.urlopen(web).read()
	print(lines)

elif option == 0:
	os.system('clear')
	print(" _   _       _   __  __ _____ _   _ _____ _   _  _____ ")      
	print("| \ | |     | | |  \/  |_   _| \ | |_   _| \ | |/ ____|")      
	print("|  \| | ___ | |_| \  / | | | |  \| | | | |  \| | |  __ ") 
	print("| . ` |/ _ \| __| |\/| | | | | . ` | | | | . ` | | |_ |")
	print("| |\  | (_) | |_| |  | |_| |_| |\  |_| |_| |\  | |__| |")
	print("|_| \_|\___/ \__|_|  |_|_____|_| \_|_____|_| \_|\_____(")
	print("                                  https://notmining.org")
	print("")
	print("")
	print("Credits:")
	print("")
	print("NotMINING Desktop")
	print("Version: 1.0.1")
	print("Website: http://notmining.org")
	print("Twitter: @notminingorg")
	print("E-Mail:  info@notmining.org")
	print("Created by Jose C. García Gamero & Adam K. Martin")
	sys.exit()

else: 
	print("Select a valid option:")

raw_input("Press enter to continue...")
os.system ("/usr/bin/python NotMINING.desktop_1.0.1.py")
	




