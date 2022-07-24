from colorama import Fore, init
import subprocess, yaml
init()

def pref_restore(preferences):
    temp = ""

    with open("preferences.yml", "r") as f:
        new = yaml.load(f, Loader=yaml.FullLoader)["PREFERENCES"]
        n_values = new.values()
        p_values = preferences.values()
    
    with open("preferences.yml", "r") as f:
        for x in f.readlines():
            i = 0
            
            for y in new:
                try:
                    if y in x:
                        x = x.replace(str(list(n_values)[i]), str(list(p_values)[i]))
                        break
                    i += 1
                except: pass

            temp = temp + x
        
        with open("preferences.yml", "w+") as f:
            if temp != "": f.write(temp)

def run(cmd):
    txt = f"powershell {cmd}"
    return subprocess.run(txt, capture_output=True)

def git_update(preferences):
    process = run("git reset --hard HEAD; git clean -d -f; git pull")
    # print(str(process))

    if 'changed' in str(process): 
        print(Fore.LIGHTGREEN_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTGREEN_EX}] Updated" + Fore.RESET)
        pref_restore(preferences)
    else: print(Fore.LIGHTRED_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTRED_EX}] Not a git repository" + Fore.RESET)

def git_check(preferences):
    process = run("git pull")

    if "Already up to date" in str(process.stdout): 
        print(Fore.LIGHTGREEN_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTGREEN_EX}] Already up to date" + Fore.RESET)
    elif 'changed' in str(process): 
        print(Fore.LIGHTGREEN_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTGREEN_EX}] Updated" + Fore.RESET)
        pref_restore(preferences)
    else: git_update(preferences)