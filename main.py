from cgitb import reset
from subprocess import CompletedProcess
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from colorama import Fore, init
from prettytable import PrettyTable
import requests, random, math, time, os
init()

WINDOWS_USER = os.getlogin() # System Username
lvl_1 = False # Check if the user is in lvl 1

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
        print(WHITE + """
        
    ██████╗  ██████╗
    ██╔══██╗██╔════╝
    ██████╔╝██║     
    ██╔═══╝ ██║     
    ██║     ╚██████╗
    ╚═╝      ╚═════╝
                    
    """ + RESET)

def art_mobile():
    print(WHITE + """

    ███╗   ███╗ ██████╗ ██████╗ ██╗██╗     ███████╗
    ████╗ ████║██╔═══██╗██╔══██╗██║██║     ██╔════╝
    ██╔████╔██║██║   ██║██████╔╝██║██║     █████╗  
    ██║╚██╔╝██║██║   ██║██╔══██╗██║██║     ██╔══╝  
    ██║ ╚═╝ ██║╚██████╔╝██████╔╝██║███████╗███████╗
    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝╚══════╝
                                                
    """ + RESET)

def pcDriver(driver, second=False):
    try: driver.quit()
    except: pass

    s = Service(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_argument(f"user-data-dir=C:\\Users\\{WINDOWS_USER}\\AppData\\Local\\Microsoft\\Edge\\User Data") # Data1 for other profile
    options.add_argument("--log-level=3")
    try: driver = webdriver.Edge(service=s, options=options)
    except Exception as error:
        if not second:
            os.system("taskkill /f /im msedge.exe")
            pcDriver(driver, True)
        return f"\n{RED}[{WHITE}error{RED}] Close Edge before using this program :3{RESET}{error}"

    return driver

def mobileDriver(driver, second=False):
    try: driver.quit()
    except: pass

    s = Service(EdgeChromiumDriverManager().install())
    mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 5.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    options = webdriver.EdgeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument(f"user-data-dir=C:\\Users\\{WINDOWS_USER}\\AppData\\Local\\Microsoft\\Edge\\User Data") # Data1 for other profile
    options.add_argument("--log-level=3")
    try: driver = webdriver.Chrome(service=s, options=options)
    except Exception as error:
        if not second:
            os.system("taskkill /f /im msedge.exe")
            mobileDriver(driver, True)
        return f"\n{RED}[{WHITE}error{RED}] Close Edge before using this program :3{RESET}{error}"
    
    return driver

def search(driver, total):
    for i in range(total):
        word = new_search()
        print(f"{CYAN}[{WHITE}{i+1}{CYAN}] Search: {BLUE}{word}{RESET}")
        driver.get(f"https://www.bing.com/search?q={word}&qs=n&form=QBRE&sp=-1&pq=aaaa&sc=8-4&sk=&cvid=68BA88FDD17C49629D9563F0C2E1FEF1")

def tasks(driver):
    driver.get("https://rewards.bing.com")

    time.sleep(2)
    t1 = driver.find_element(By.XPATH, '//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[1]')
    t1.click()

    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="id_rh"]').click()

    t2 = driver.find_element(By.XPATH, '//*[@id="modern-flyout"]/div/div[3]/div[2]/div[1]/div[2]/div/div[2]').click()
    t3 = driver.find_element(By.XPATH, '//*[@id="modern-flyout"]/div/div[3]/div[2]/div[1]/div[2]/div/div[3]').click()
    input()

def getStatus(driver):
    global lvl_1
    driver.get("https://rewards.bing.com/status/pointsbreakdown")

    table = PrettyTable([f'{WHITE}Task type{RESET}', f'{WHITE}Remaining points{RESET}', f'{WHITE}Searches{RESET}'])
    while True:
        try:
            pc = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(' / ')
            total_pc = int(pc[1]) - int(pc[0])
            table.add_row([f'{GREEN if total_pc == 0 else RED}PC{RESET}', f'{GREEN if total_pc == 0 else RED}{total_pc}{RESET}', f'{GREEN if total_pc == 0 else RED}{math.ceil(total_pc/3)}{RESET}'])

            mobile = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(' / ')
            total_mobile = int(mobile[1]) - int(mobile[0])
            table.add_row([f'{GREEN if total_mobile == 0 else RED}Mobile{RESET}', f'{GREEN if total_mobile == 0 else RED}{total_mobile}{RESET}', f'{GREEN if total_mobile == 0 else RED}{math.ceil(total_mobile/3)}{RESET}'])

            try:
                edge = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(' / ')
                total_edge = int(edge[1]) - int(edge[0])
                table.add_row([f'{GREEN if total_edge == 0 else RED}Edge{RESET}', f'{GREEN if total_edge == 0 else RED}{total_edge}{RESET}',f'{GREEN if total_edge == 0 else RED}{math.ceil(total_edge/3)}{RESET}'])
            except:
                lvl_1 = True
                total_edge = 0
            break
        except: print(RED + f"[{WHITE}·{RED}] Retrying..." + RESET)
    print(table)
    return math.ceil(total_pc/3), math.ceil(total_mobile/3), math.ceil(total_edge/3)

def main():
    global lvl_1
    check = True
    driver = None

    while check:
        check = False

        # Get information of the remaining tasks
        driver = pcDriver(driver)
        if "error" in str(driver):
            print(driver)
            input(f"\n[·] Press enter to close")
            return
        data = getStatus(driver)

        # Complete the PC searches
        if data[0] > 0:
            art_pc()
            search(driver, data[0])
            check = True

        if data[2] > 0 and data[0] == 0:
            art_pc()
            search(driver, data[2])
            check = True

        # Complete the Mobile searches
        if data[1] > 0 and not lvl_1:
            art_mobile()
            driver = mobileDriver(driver)
            if "error" in str(driver):
                print(driver)
                input(f"\nPress enter to close")
                return
            search(driver, data[1])
            check = True

    open('usedKeywords.txt', 'w').write("")
    # tasks(driver)
    driver.quit()
    input(f"\n{GREEN}[{WHITE}·{GREEN}] Done! {RESET}Press enter to close") # Add total poinst gotten c:

if __name__ == "__main__":
    main()