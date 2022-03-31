from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from colorama import Fore, init
from prettytable import PrettyTable
import requests, random, math
init()

WINDOWS_USER = "Neko" # Change this to your username

####### COLORS #######
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
BLUE = Fore.LIGHTBLUE_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
CYAN = Fore.LIGHTCYAN_EX
WHITE = Fore.LIGHTWHITE_EX
RESET = Fore.RESET
######################

def new_search():
    def Diff(li1, li2):
        return (list(set(li1) - set(li2)))

    word_site = "https://www.myhelpfulguides.com/keywords.txt"

    response = requests.get(word_site)
    words = response.text.splitlines()

    for i in range(30):
        f = open('usedKeywords.txt', 'r')
        used = f.read().splitlines()

    new = Diff(words, used)

    search = random.choice(new)
    f = open('usedKeywords.txt', 'a')
    f.write(search + "\n")
    f.close()

    return search

def art_pc():
        print("""
        
    ██████╗  ██████╗
    ██╔══██╗██╔════╝
    ██████╔╝██║     
    ██╔═══╝ ██║     
    ██║     ╚██████╗
    ╚═╝      ╚═════╝
                    
    """)

def art_mobile():
    print("""

    ███╗   ███╗ ██████╗ ██████╗ ██╗██╗     ███████╗
    ████╗ ████║██╔═══██╗██╔══██╗██║██║     ██╔════╝
    ██╔████╔██║██║   ██║██████╔╝██║██║     █████╗  
    ██║╚██╔╝██║██║   ██║██╔══██╗██║██║     ██╔══╝  
    ██║ ╚═╝ ██║╚██████╔╝██████╔╝██║███████╗███████╗
    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝╚══════╝
                                                
    """)
    
def art_edge():
    print("""
        
    ███████╗██████╗  ██████╗ ███████╗
    ██╔════╝██╔══██╗██╔════╝ ██╔════╝
    █████╗  ██║  ██║██║  ███╗█████╗  
    ██╔══╝  ██║  ██║██║   ██║██╔══╝  
    ███████╗██████╔╝╚██████╔╝███████╗
    ╚══════╝╚═════╝  ╚═════╝ ╚══════╝
                                    
    """)


def pcDriver():
    s = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir=C:/Users/{WINDOWS_USER}/AppData/Local/Google/Chrome/User Data/')
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=s, options=options)

    return driver

def mobileDriver():
    s = Service(ChromeDriverManager().install())
    mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument(f'--user-data-dir=C:/Users/{WINDOWS_USER}/AppData/Local/Google/Chrome/User Data/')
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=s, options=options)
    
    return driver

def search(driver, total):
    for i in range(total):
        word = new_search()
        print(f"{CYAN}[{WHITE}{i+1}{CYAN}] Search: {BLUE}{word}{RESET}")
        driver.get(f"https://www.bing.com/search?q={word}&qs=n&form=QBRE&sp=-1&pq=aaaa&sc=8-4&sk=&cvid=68BA88FDD17C49629D9563F0C2E1FEF1")
    driver.quit()

def getStatus(driver):
    driver.get("https://rewards.bing.com/status/pointsbreakdown")

    t = PrettyTable([f'{WHITE}Task type{RESET}', f'{WHITE}Remaining points{RESET}', f'{WHITE}Searches{RESET}'])
    while True:
        try:
            pc = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
            total_pc = 90 - int(pc)
            t.add_row([f'{GREEN if total_pc == 0 else RED}PC{RESET}', f'{GREEN if total_pc == 0 else RED}{total_pc}{RESET}', f'{GREEN if total_pc == 0 else RED}{math.ceil(total_pc/3)}{RESET}'])

            mobile = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
            total_mobile = 60 - int(mobile)
            t.add_row([f'{GREEN if total_mobile == 0 else RED}PC{RESET}', f'{GREEN if total_mobile == 0 else RED}{total_mobile}{RESET}', f'{GREEN if total_mobile == 0 else RED}{math.ceil(total_mobile/3)}{RESET}'])

            edge = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text
            total_edge = 12 - int(edge)
            t.add_row([f'{GREEN if total_edge == 0 else RED}PC{RESET}', f'{GREEN if total_edge == 0 else RED}{total_edge}{RESET}','-'])
            break
        except: print(RED + f"[{WHITE}·{RED}] Retrying..." + RESET)
    print(t)
    return math.ceil(total_pc/3), math.ceil(total_mobile/3), math.ceil(total_edge/3)

def main():
    # Get information of the remaining tasks
    driver = pcDriver()
    data = getStatus(driver)

    # Complete the PC searches
    if data[0] > 0:
        art_pc()
        search(driver, data[0])

    # Complete the Mobile searches
    if data[1] > 0:
        art_mobile()
        driver = mobileDriver()
        search(driver, data[1])

    # Probably complete the Edge task in future c:

    print(f"\n{GREEN}[{WHITE}·{GREEN}] Done!{RESET}")

if __name__ == "__main__":
    main()