from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from colorama import Fore, init
from prettytable import PrettyTable
from data.tasks_selector import selector
from data.updater import git_update
import requests, random, math, time, os, json, yaml
init()

# PREFERENCES
with open("config/preferences.yml", "r") as f:
    preferences = yaml.load(f, Loader=yaml.FullLoader)["PREFERENCES"]

    SCORE_GOAL = int(preferences["SCORE_GOAL"])
    DO_TASKS = preferences["DO_TASKS"]
    DO_SEARCHES = preferences["DO_SEARCHES"]
    AUTO_UPDATE = preferences["AUTO_UPDATE"]
    ALLOW_VPN = preferences["ALLOW_VPN"]
    IPVANISH = preferences["IPVANISH"]
    MULTIACCOUNT = preferences["MULTIACCOUNT"]
    lvl_1 = False

# GLOBAL VARIABLES
WINDOWS_USER = os.getlogin() # System Username
COUNTRIES = json.loads(open('config/countries.json', 'r').read())

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

# Get keywords
word_site = "https://www.myhelpfulguides.com/keywords.txt"
try:
    response = requests.get(word_site, timeout=3)
    words = response.text.splitlines()
except:
    print(f"{YELLOW}[{WHITE}·{YELLOW}] Using emergency words{RESET}")
    with open("data/emergency_words.txt", "r") as f:
        words = f.read().splitlines()

def new_search():
    global words

    def Diff(li1, li2):
        return (list(set(li1) - set(li2)))

    with open('data/usedKeywords.txt', 'r') as f:
        used = f.read().splitlines()

    new = Diff(words, used)
    if len(new) == 0:
        with open('data/usedKeywords.txt', 'w+') as f: f.write("")
        return new_search()

    search = random.choice(new)
    with open('data/usedKeywords.txt', 'a') as x:
            x.write(search + "\n")

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

def loginAccount(driver, account):
    driver.get("https://login.live.com/login.srf")
    driver.find_element(By.ID, "i0116").send_keys(account["email"])
    driver.find_element(By.XPATH, "//*[contains(@id,'idSIButton')]").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "i0118").send_keys(account["password"])
    driver.find_element(By.XPATH, "//*[contains(@id,'idSIButton')]").click()
    time.sleep(2)

def pcDriver(s, driver, second=False, account=False):
    try: driver.quit()
    except: pass

    options = webdriver.EdgeOptions()
    if account: options.add_argument("inprivate")
    else: options.add_argument(f"user-data-dir=C:\\Users\\{WINDOWS_USER}\\AppData\\Local\\Microsoft\\Edge\\User Data") # Data1 for other profile
    options.add_argument("--log-level=3")

    try: driver = webdriver.Edge(service=s, options=options)
    except Exception as error:
        if not second:
            os.system("taskkill /f /im msedge.exe")
            time.sleep(3)
            driver = pcDriver(driver, True)
        else:
            return f"\n{RED}[{WHITE}error{RED}] Close Edge before using this program :3{RESET}{error}"
    
    if account: loginAccount(driver, account) 
    return driver

def mobileDriver(s, driver, second=False, account=False):
    try: driver.quit()
    except: pass

    mobile_emulation = {"userAgent": "Mozilla/5.0 (Linux; Android 5.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    options = webdriver.EdgeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    if account: options.add_argument("inprivate")
    else: options.add_argument(f"user-data-dir=C:\\Users\\{WINDOWS_USER}\\AppData\\Local\\Microsoft\\Edge\\User Data") # Data1 for other profile
    options.add_argument("--log-level=3")

    try: driver = webdriver.Chrome(service=s, options=options)
    except Exception as error:
        if not second:
            os.system("taskkill /f /im msedge.exe")
            time.sleep(3)
            driver = mobileDriver(driver, True)
        else:
            return f"\n{RED}[{WHITE}error{RED}] Close Edge before using this program :3{RESET}{error}"
    
    if account: loginAccount(driver, account) 
    return driver

def search(driver, total, task=False):
    i = 0

    while i != total:
        i += 1
        try: 
            word = new_search()
            if not task: 
                print(f"{CYAN}[{WHITE}{i}{CYAN}] Search: {BLUE}{word}{RESET}", end="")

            driver.get(f"https://www.bing.com/search?q={word}&qs=n&form=QBRE&sp=-1&pq=aaaa&sc=8-4&sk=&cvid=68BA88FDD17C49629D9563F0C2E1FEF1")
            time.sleep(2)
            print("")
        except:
            print(RED + " - Error. Retrying..." + RESET)
            i -= 1

def tasks(driver):
    search(driver, 1, True)
    print(f"\n{CYAN}[{WHITE}·{CYAN}] Doing Tasks... {RESET}")

    # Do daily tasks
    check = False
    i = 1
    while not check:
        time.sleep(3)
        try : driver.find_element(By.XPATH, '//*[@id="id_rh"]').click()
        except:
            try: driver.execute_script('document.getElementsByClassName("b_hide langdisp")[0].firstChild.click()')
            except: pass
            
            driver.refresh()
            continue
        time.sleep(2)

        try:
            check = driver.execute_script('let j = 2; let section = document.querySelector("#bepfm").contentDocument.body.getElementsByClassName("rw-accd-i")[0].children[1].firstChild.children; while(true) {if(j < 0 || section.length < 3) {return true; break} try{if(section[j].getElementsByClassName("point_cont complete").length == 0) {section[j].firstChild.click(); return false; break} else throw Error} catch {j--}}')
            
            if not check:
                time.sleep(4)

                selector(driver)
                driver.refresh()
                print(f"\t{GREEN}[{WHITE}·{GREEN}] Daily Task {WHITE}{i}{RESET}")
                i += 1
        except:
            driver.refresh()
            continue

        if i > 10: 
            print(f"\t{RED}[{WHITE}!{RED}] Daily Task Limit Reached {RESET}")
            break
    
    # Select the second box and do their tasks
    contador = 1
    query = True
    firts = True
    while query:
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="id_rh"]').click()
        time.sleep(2)

        try:
            driver.execute_script('try{document.querySelector("#bepfm").contentDocument.body.getElementsByClassName("rw-accd-i")[1].children[1].click()}catch{}')
            time.sleep(1)
            query = driver.execute_script('let resp = false; try {let section = document.querySelector("#bepfm").contentDocument.body.getElementsByClassName("rw-accd-i")[1].children[2].firstChild.children; section[0].firstChild.click(); if(section[0].firstChild.firstChild.tagName == "svg") throw Error; return true}catch{return false}')
            time.sleep(4)
        except:
            driver.refresh()
            continue

        if query:
            if firts: print(WHITE + "\t--------------------" + RESET)
            firts = False

            time.sleep(2)
            selector(driver)
            time.sleep(2)
            driver.refresh()
            print(f"\t{GREEN}[{WHITE}·{GREEN}] Secondary Task {WHITE}{contador}{RESET}")
            contador += 1

        if contador > 15:
            print(f"\t{RED}[{WHITE}!{RED}] Secondary Task Limit Reached {RESET}")
            break

def getStatus(driver, count_max):
    global lvl_1
    driver.get("https://rewards.bing.com/status/pointsbreakdown")

    table = PrettyTable([f'{WHITE}Task type{RESET}', f'{WHITE}Remaining points{RESET}', f'{WHITE}Searches{RESET}'])
    while True:
        try:
            pc = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(' / ')
            
            total_pc = int(pc[1]) - int(pc[0])
            table.add_row([f'{GREEN if total_pc == 0 else RED}PC{RESET}', f'{GREEN if total_pc == 0 else RED}{total_pc}{RESET}', f'{GREEN if total_pc == 0 else RED}{math.ceil(total_pc/count_max)}{RESET}'])

            mobile = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(' / ')
            total_mobile = int(mobile[1]) - int(mobile[0])
            table.add_row([f'{GREEN if total_mobile == 0 else RED}Mobile{RESET}', f'{GREEN if total_mobile == 0 else RED}{total_mobile}{RESET}', f'{GREEN if total_mobile == 0 else RED}{math.ceil(total_mobile/count_max)}{RESET}'])

            try:
                edge = driver.find_element(By.XPATH, '//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(' / ')
                total_edge = int(edge[1]) - int(edge[0])
                table.add_row([f'{GREEN if total_edge == 0 else RED}Edge{RESET}', f'{GREEN if total_edge == 0 else RED}{total_edge}{RESET}',f'{GREEN if total_edge == 0 else RED}{math.ceil(total_edge/count_max)}{RESET}'])
            except:
                lvl_1 = True
                total_edge = 0
            break
        except: 
            print(RED + f"[{WHITE}·{RED}] Retrying..." + RESET)
            
            try: driver.execute_script('try {document.getElementsByClassName("glyph-cancel")[0].click()} catch {}')
            except: pass
            
            driver.refresh()
            time.sleep(2)

    print(table)
    return math.ceil(total_pc/count_max), math.ceil(total_mobile/count_max), math.ceil(total_edge/count_max)

def main(s, account=None):
    global lvl_1, COUNTRIES
    check = True
    driver = None
    try: os.system("taskkill /f /im msedge.exe")
    except: pass

    if not ALLOW_VPN: COUNTRIES["countries"] = [COUNTRIES["default_country"]]

    for i in range(len(COUNTRIES["countries"])):
        print(f"\n{CYAN}[{WHITE}·{CYAN}] Connecting to {COUNTRIES['countries'][i][0]}... {RESET}")
        count_max = COUNTRIES["countries"][i][1]
        
        while check and DO_SEARCHES:
            check = False

            # Get information of the remaining tasks
            if account: driver = pcDriver(s, driver, account=account)
            else: driver = pcDriver(s, driver)

            data = getStatus(driver, count_max)

            # Complete the PC searches
            if data[0] + data[2] > 0:
                art_pc()
                search(driver, data[0] + data[2])
                check = True

            # Complete the Mobile searches
            if data[1] > 0 and not lvl_1:
                art_mobile()

                if account: driver = mobileDriver(s, driver, account=account)
                else: driver = mobileDriver(s, driver)

                if "error" in str(driver):
                    print(driver)
                    input(f"\nPress enter to close")
                    return
                search(driver, data[1])
                check = True
        
        if not DO_SEARCHES:
            if account: driver = pcDriver(s, driver, account=account)
            else: driver = pcDriver(s, driver)

        if DO_TASKS: tasks(driver)

        if i < len(COUNTRIES["countries"]) - 1:
            vpn_res = input(f"\n{BLUE}[{WHITE}·{BLUE}] Change manually to Spain with VPN and press enter to continue... {MAGENTA}(N to exit) {RESET}")
            if vpn_res.lower() == 'n': break
            check = True
    
    driver.get("https://rewards.bing.com/status/pointsbreakdown")
    time.sleep(3)
    
    try:
        available_points = int(driver.find_elements(By.CLASS_NAME, 'margin-top-1')[0].text.replace(",",""))
        print(f"\n{BLUE}[{WHITE}·{BLUE}] Available points: {WHITE}{available_points}")
        if available_points >= SCORE_GOAL: print(f"{GREEN}[{WHITE}·{GREEN}] You have reached the goal of {WHITE}{SCORE_GOAL}{GREEN}!{RESET}")
    except: pass

    return driver

if __name__ == "__main__":
    if AUTO_UPDATE: 
        git_update()
        time.sleep(2)

    if MULTIACCOUNT:
        accounts = json.load(open("config/accounts.json", "r"))

        for account in accounts:
            s = Service(EdgeChromiumDriverManager().install())
            print(f"\n{BLUE}[{WHITE}·{BLUE}] Starting account {WHITE}{account['name']}{WHITE}...{RESET}")
            driver = main(s, account)
    else:
        s = Service(EdgeChromiumDriverManager().install())
        driver = main(s)

    input(f"\n{GREEN}[{WHITE}·{GREEN}] Done! {RESET}Press enter to close")
    try: driver.quit()
    except: pass
