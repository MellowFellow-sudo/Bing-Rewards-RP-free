import time, random

def Box_or_Box(driver):
    res = driver.execute_script('try {document.getElementsByClassName("btOptionCard")[1].click(); return true} catch {return false}')

    if res == True:
        time.sleep(2)

        i = 0
        while(res):
            res = driver.execute_script('if (document.getElementsByClassName("headerMessage_Refresh").length != 0 || document.getElementsByClassName("headerMessage").length != 0) {return false} else {return true}')
            driver.execute_script('try {document.getElementsByClassName("btOptionCard")[1].click(); return true} catch {return false}')
            time.sleep(5)
            i += 1

            if i == 10: 
                driver.refresh()
                i = 0
        return False
    return True

def Short_Answer_Box2(driver):
    res = driver.execute_script('try {document.getElementById("btoption0").click(); return true} catch {return false}')
    if res: 
        time.sleep(2)
        return False
    return True

def To_Many_Box(driver):
    check = False
    res = True

    i = 0
    while(res):
        res = driver.execute_script('if (document.getElementsByClassName("headerMessage_Refresh").length != 0 || document.getElementsByClassName("headerMessage").length != 0) {return false} else {return true}')
        res2 = driver.execute_script("""try {if(document.getElementById("rq_standardPromos")) throw Error; corrects = document.querySelectorAll('[iscorrectoption="True"]'); if (corrects.length == 0) throw Error; for(i=0;i<corrects.length;i++) {corrects[i].click()}; return true} catch {return false}""")
        
        if res2:
            time.sleep(4)
            check = True
            i += 1
        else: break
        
        if i == 30: 
            driver.refresh()
            i = 0


    if check: return False
    return True

def Four_Boxes(driver):
    i = 0
    res = True
    check = False

    while res:
        res = driver.execute_script('if (document.getElementsByClassName("headerMessage_Refresh").length != 0 || document.getElementsByClassName("headerMessage").length != 0) {return false} else {return true}')
        
        if res: 
            driver.execute_script(f'document.getElementsByClassName("rq_button")[{i}].firstChild.firstChild.click()')
            time.sleep(3)
            check = True
            i += 1

        if i == 4: i = 0

    if check: return False
    return True

def Short_Answer_Box(driver):
    res = driver.execute_script('try {document.getElementById("rqStartQuiz").click(); return true} catch {return false}')
    comp = driver.execute_script('if (document.getElementsByClassName("rq_button").length == 0) {return false} else {return true}')
    
    if res == True and comp == True: return Four_Boxes(driver)

    elif res == True and comp != True:
        time.sleep(2)
        res = driver.execute_script('try {document.getElementsByClassName("rq_button")[0].firstChild.firstChild.click(); return true} catch {return false}')
        time.sleep(2)
        res = driver.execute_script('try {document.getElementsByClassName("rq_button")[1].firstChild.firstChild.click(); return true} catch {return false}')
        time.sleep(1)

        if not res: return To_Many_Box(driver)
        return False
        
    else: return To_Many_Box(driver)

def Three_Circles(driver):
    check = False
    res = True

    while res:
        time.sleep(2)
        ran = random.randint(0,2)
        res = driver.execute_script('try{document.getElementsByClassName("wk_choicesInstLink")[' + str(ran) + '].click(); return true} catch {try{document.getElementsByClassName("wk_button")[0].click()} catch {}; return false}')
        check = True

    if check: return False
    return True

def extra(driver):
    driver.execute_script('try {document.getElementsByClassName("item col")[1].firstChild.firstChild.click(); return true} catch {return false}')

def selector(driver):
    res = Box_or_Box(driver)
    if res: res = Short_Answer_Box(driver)
    if res: res= Short_Answer_Box2(driver)
    if res: res = Three_Circles(driver)

    if res: extra(driver)

    driver.switch_to.window(driver.window_handles[0])
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
