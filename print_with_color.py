from termcolor import cprint

link="www.pentest.com"
outside_link="www.example.com"

cprint("[*] Initiating Crawling", "blue",attrs=["bold"])

cprint(f"[+] Find link:{link}", "green",attrs=["bold"])

cprint(f"[-] Skip cross-domain link {outside_link}", "red",attrs=["bold"])

cprint("[*] Crawler finished", "blue",attrs=["bold"],)
