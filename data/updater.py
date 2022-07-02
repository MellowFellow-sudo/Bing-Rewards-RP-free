from colorama import Fore, init
import subprocess
init()

def run(cmd):
    return subprocess.run(["powershell", *cmd.split(' ')], capture_output=True)

def git_update():
    process = run("git reset --hard HEAD; git clean -d -f; git pull origin main")
    # print(process)

    if 'changed' in str(process): print(Fore.LIGHTGREEN_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTGREEN_EX}] Updated" + Fore.RESET)
    elif "Already up to date" in str(process): print(Fore.LIGHTYELLOW_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTYELLOW_EX}] Already up to date" + Fore.RESET)
    else: print(Fore.LIGHTRED_EX + f"[{Fore.LIGHTWHITE_EX}·{Fore.LIGHTRED_EX}] Not a git repository" + Fore.RESET)