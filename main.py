import requests
import pprint
import time
import os
ip = input("Enter victim ip address : ")
# ip = "8.8.8.8"
print("  _____  ______ _   _______            _____  ")
print(" |  __ \|  ____| | |__   __|/\        |  __ \ ")
print(" | |  | | |__  | |    | |  /  \ ______| |  | |")
print(" | |  | |  __| | |    | | / /\ \______| |  | |")
print(" | |__| | |____| |____| |/ ____ \     | |__| |")
print(" |_____/|______|______|_/_/    \_\    |_____/ ")
print("                                               ")
print("join us on telegram --> https://t.me/delta_D_squad")
time.sleep(2.4)
#time.sleep(2.4)
print("collceting your data....")
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

text = 'information gathering source'
colored_text = colored(255, 0, 0, text)
r = requests.get(url)
pprint.pprint(r.json())
