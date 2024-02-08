import os
import json
import traceback
import datetime
import requests
import psutil
import fade
from colorama import Fore, Style
from urllib.request import Request, urlopen

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_directory(category):
    directory = f"./resource/{category}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def save_error_log(error):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_directory = create_directory("logs")
    log_file = os.path.join(log_directory, f"error_{timestamp}.log")
    with open(log_file, "w") as file:
        file.write(str(error))

def handle_error():
    error = traceback.format_exc()
    print(Style.RESET_ALL + "An error occurred. Please check the logs for more details.")
    save_error_log(error)

snusbase_auth = 'sbuncd7b2bfcflweh3dkbeqsuzlzqk'
snusbase_api = 'https://api-experimental.snusbase.com/'

#API-COMBO:
def api_combo():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    class network_discord:
        def __init__(self):
            pass

        def search(self, term):
            f = requests.get(f"https://beta.snusbase.com/v2/combo/{term}")
            if f.status_code == 200:
                out = f.json()["result"]
                l = []
                for item in out:
                    for item2 in out[item]:
                        l.append(item2)
                        
                formatted_results = json.dumps(l, indent=2)  # Pretty print the results
                print("")
                print(formatted_results)
            else:
                print("The request failed.")
    
    if __name__ == '__main__':

        term = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter any value: ")

        if term == "exit":
            exit()

        elif term == "menu":
            default_menu()

        else:
            search = network_discord()
            search.search(term)
            input("\nPress Enter to continue...")
            default_menu()

#-----------------------------------------------------------------

#API-IP WHOIS:
def api_ip_whois():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def api_whois(auth_token, ip):
        url = f"https://beta.snusbase.com/v1/whois/{ip}"
        headers = {
            "authorization": auth_token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print("")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("The request failed.")

    if __name__ == "__main__":
        auth_token = "sb0sl0hf866dmrtc4fkeatw7h8wlfo"
        ip = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter the IP address: ")

        api_whois(auth_token, ip)
        input("\nPress Enter to continue...")
        default_menu()

#-----------------------------------------------------------------

#API-EMAIL:
def api_email():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter an Email address: ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["email"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nPress Enter to continue...")
            default_menu()

#-----------------------------------------------------------------

#API-USERNAME:
def api_username():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter a Username: ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["username"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nPress Enter to continue...")
            default_menu()

#-----------------------------------------------------------------

#API-IP:
def api_ip():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter an IP address: ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["lastip"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nPress Enter to continue...")
            default_menu()

#-----------------------------------------------------------------

#API-HASH:
def api_hash():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter a Hashed Password: ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["hash"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nPress Enter to continue...")
            default_menu()

#-----------------------------------------------------------------

#API-PASSWORD:
def api_password():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter a Password: ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["password"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nPress Enter to continue...")
            default_menu()

#-----------------------------------------------------------------

#API-NAME:
def api_name():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter a First & Last Name separated by space: ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["name"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nPress Enter to continue...")
            default_menu()

#-----------------------------------------------------------------

#DEFAULT TEXT:
text_default ='''
          c,_.--.,y
            7 a.a(
           (   ,_Y)
           :  '---;
       ___.'\.  - (
     .'"""S,._'--'_2..,_
     |    ':::::=:::::  \
     .     f== ;-,---.' T
      Y.   r,-,_/_      |
      |:\___.---' '---./
      |'`             )
       \             ,
       ':;,.________.;L
       /  '---------' |
       |              \
       L---'-,--.-'--,-'
        T    /   \   Y
        |   Y    ,   |
        |   \    (   |
        (   )     \,_L
        7-./      )  `,
IW    /  _(      '._  \
'''

#MENU:
def default_menu():
    try:
        clear_screen()
        text_default_fade = fade.greenblue(text_default)
        print(text_default_fade)

        choose_text = '''(1) - Search with an Email.           /  (5) - Search via a Password.
(2) - Search with a Username.        /  (6) - Search with a Hashed Password.
(3) - Search via an IP Address.      /  (7) - Search with Combo.
(4) - Whois an IP Address.           /  (8) - Search with First & Last Name.
               (exit) for leave the app ! (by discord.gg/toolsfr on discord)'''
        
        text_choose_fade = fade.purpleblue(choose_text)
        print(text_choose_fade)

        print(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Enter your choice (1-8):")
        choice = input("> ")
        
        #API EMAIL:
        if choice == "1":
            api_email()

        #API USERNAME:
        if choice == "2":
            api_username()

        #API IP:
        elif choice == "3":
            api_ip()

        #API IP WHOIS:
        elif choice == "4":
            api_ip_whois()

        #API PASSWORD:
        elif choice == "5":
            api_password()

        #API HASH:
        elif choice == "6":
            api_hash()

        #API COMBO:
        elif choice == "7":
            api_combo()

        #API NAME:
        elif choice == "8":
            api_name()

        #EXIT:
        elif choice == "exit":
            clear_screen()
            exit()

        #ERROR
        else:
            print("Invalid choice. Please try again.")
            input("Press any key to continue...")
            default_menu()
            
    except Exception as e:
        handle_error()

if __name__ == "__main__":
    default_menu()
