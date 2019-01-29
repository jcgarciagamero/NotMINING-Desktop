import os, sys, requests


if os.name == 'nt':
	while True:
		os.system('cls')
		print(" _   _       _   __  __ _____ _   _ _____ _   _  _____ ")      
		print("| \ | |     | | |  \/  |_   _| \ | |_   _| \ | |/ ____|")      
		print("|  \| | ___ | |_| \  / | | | |  \| | | | |  \| | |  __ ") 
		print("| . ` |/ _ \| __| |\/| | | | | . ` | | | | . ` | | |_ |")
		print("| |\  | (_) | |_| |  | |_| |_| |\  |_| |_| |\  | |__| |")
		print("|_| \_|\___/ \__|_|  |_|_____|_| \_|_____|_| \_|\_____(")
		print("                                  https://notmining.org")
		print("Detect: Windows")
		print("")

		print("Select an option: ")
		print("(1): Scan")
		print("(2): Reanalyze")
		print("(3): Blacklist")
		print("")
		print("(0): Exit")
		print("")
		option = input("Option: ")

		if option == "1":
			web = input("Enter URL: ")
			print("Result: ")
			print("")
			scan = "https://notmining.org/url?busqueda="+web
			a = requests.get(scan)
			lines = a.text

			if "NOT Mining!" in lines:
				print("Not Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Mining!" in lines:
				print("Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Enter a valid URL" in lines:
				print("Enter a valid URL")
				print("")
			else:
				print("The requested website is not available, prevents its analysis, or is incorrect URL.")
				print(f"Analysis: {web}")
				print("")
		if option == "2":
			web = input("Enter URL: ")
			scan = "https://notmining.org/analyze?busqueda="+web
			a = requests.get(scan)
			lines = a.text

			if "NOT Mining!" in lines:
				print("Not Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Mining!" in lines:
				print("Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Enter a valid URL" in lines:
				print("Enter a valid URL")
				print("")
			else:
				print("The requested website is not available, prevents its analysis, or is incorrect URL.")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")

		if option == "3":
			os.system('cls')
			web = "https://notmining.org/export.php"
			a = requests.get(web)
			lines = a.text
			print(lines)

		if option == 0:
			os.system('cls')
			print(" _   _       _   __  __ _____ _   _ _____ _   _  _____ ")      
			print("| \ | |     | | |  \/  |_   _| \ | |_   _| \ | |/ ____|")      
			print("|  \| | ___ | |_| \  / | | | |  \| | | | |  \| | |  __ ") 
			print("| . ` |/ _ \| __| |\/| | | | | . ` | | | | . ` | | |_ |")
			print("| |\  | (_) | |_| |  | |_| |_| |\  |_| |_| |\  | |__| |")
			print("|_| \_|\___/ \__|_|  |_|_____|_| \_|_____|_| \_|\_____(")
			print("                                  https://notmining.org")
			print("Detect: UNIX")
			print("")
			print("Credits:")
			print("")
			print("NotMINING Desktop")
			print("Version: 1.0.2")
			print("Website: http://notmining.org")
			print("Twitter: @notminingorg")
			print("E-Mail:  info@notmining.org")
			print("Created by Jose C. García Gamero & Adam K. Martin")
			sys.exit()

		else: 
			print("Select a valid option:")
			input("Press enter to continue...")
else:
	while True:
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
		option = int(input("Option: "))


		if option == "1":
			web = input("Enter URL: ")
			print("Result: ")
			print("")
			scan = "https://notmining.org/url?busqueda="+web
						a = requests.get(scan)
			lines = a.text

			if "NOT Mining!" in lines:
				print("Not Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Mining!" in lines:
				print("Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Enter a valid URL" in lines:
				print("Enter a valid URL")
				print("")
			else:
				print("The requested website is not available, prevents its analysis, or is incorrect URL.")
				print(f"Analysis: {web}")
				print("")
		if option == "2":
			web = input("Enter URL: ")
			scan = "https://notmining.org/analyze?busqueda="+web
						a = requests.get(scan)
			lines = a.text

			if "NOT Mining!" in lines:
				print("Not Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Mining!" in lines:
				print("Mining")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")
			elif "Enter a valid URL" in lines:
				print("Enter a valid URL")
				print("")
			else:
				print("The requested website is not available, prevents its analysis, or is incorrect URL.")
				print(f"Analysis: https://notmining.org/url?busqueda={web}")
				print("")

		if option == "3":
			os.system('clear')
			web = "https://notmining.org/export.php"
			a = requests.get(web)
			lines = a.text
			print(lines)

		if option == 0:
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
			print("Version: 1.0.2")
			print("Website: http://notmining.org")
			print("Twitter: @notminingorg")
			print("E-Mail:  info@notmining.org")
			print("Created by Jose C. García Gamero")
			print("Updated by @Manza_Root")
			sys.exit()

		else: 
			print("Select a valid option:")
			input("Press enter to continue...")
		
