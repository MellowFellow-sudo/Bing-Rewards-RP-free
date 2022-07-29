# Bing-Rewards-RP-free
This program automates the daily searches and tasks for Bing Rewards. You can earn up to 6500 points every 11-15 days (using VPN).

<div align="center">
<img src="https://user-images.githubusercontent.com/57575090/177008524-6c68a6f3-8bdc-442c-b4e6-df89ba603943.png" width="300" /><br><br>
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/bing-rewards?style=flat-square&label=Python&logo=python&logoColor=yellow">
<a href="https://pypi.org/project/bing-rewards/"> <img alt="PyPi" src="https://img.shields.io/pypi/v/bing-rewards?label=PyPI&style=flat-square&logo=pypi&logoColor=yellow"></a>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/bing-rewards?style=flat-square&label=License&color=blueviolet">
</div><br>

# Installation 📀
First of all, you need to login to your account on Edge. The program uses the browser data to prevent the saving of credentials and avoid logging every time the program executes.

It is recommended to have only one account started in Edge in order to avoid errors (student accounts are not accepted by Rewards itself).

Second, install the required dependencies: 
```
pip install -r requirements.txt
```

If you want the program to update automatically you need to have Git installed. https://git-scm.com/download/win
<br><br>

# Configuration ⚙️
All the configuration is inside `/config` folder:<br>
- `accounts.json` - Currently multi-accounts are not available.
- `countries.json` - If you find more regions where searches can be done you can add it to the list. The combination that currently works is the default
- `preferences.yml` - Activate or deactivate the functionalities you need.
<br><br>

# How to use 📝
Run the program and it automatically starts Edge and makes the searches and tasks on PC mode and Mobile mode.
If you have the VPN option activated you will be asked to manipulate the VPN for each country in the list<br>
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/57575090/177008476-c13c5e41-7d2d-439f-8fe6-3aeccb9aca8a.png)](https://www.youtube.com/watch?v=csWUqLFyooI)
<br>

### **- Youtube Video:** *https://www.youtube.com/watch?v=csWUqLFyooI*
<br>

# Important! ⚠️
This program has been created to work on Windows 10. I have not tried to use it on Linux due to the Selenium package gives problems.

You can't use Edge when the program is running, so you need to close Edge before running the program.
That's why it takes the Edge data.

~ *Now the program kills the Edge process before starting.*
<br><br>

# For double the points (VPN)🔥
If you have the VPN mode activated, the program does the process for each country in the list that is inside the config folder as `countries.json`.

You just have to wait and manipulate the VPN when indicated on the console.
<br><br>

# Rewards 🥵
My first intention with this program was to get RP, the currency within the League of Legends video game.
![image](https://user-images.githubusercontent.com/57575090/161355891-71f72e14-1695-4193-96b8-a83f85956a8e.png)

But there are many other rewards that the page offers: https://rewards.bing.com/redeem/
<br><br>

# Contributors
<table>
  <tr>
    <td align="center"><a href="https://github.com/EricDragon8"><img src="https://avatars.githubusercontent.com/u/98742666?v=4" width="122px;" alt=""/><br /><sub><b>Eric Mas</b></sub></a>
  </tr>
</table>
<br>

# To Do List 💡
- [x] Do daily tasks
- [x] Auto Update
- [ ] Automatic VPN changing (In the next version)
- [ ] Multiple Accounts *(Not sure)*
- [ ] GUI
