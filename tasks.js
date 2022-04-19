// Muchas cajas - setInterval('muchasCajas()', 2000);
function muchasCajas() {
    try { document.getElementById("rqStartQuiz")
        document.getElementById("rqStartQuiz").click()

        corrects = document.querySelectorAll('[iscorrectoption="True"]')
        for(i=0;i<corrects.length;i++) {
            corrects[i].click()
        }
    } catch(err) { return false }
}

// Circulitos - LO COMPLETA = WKQuiz_V2.showQuestionPane()
function circulitos() {
    try { document.getElementsByClassName("FooterText0 wk_textCenterAlign b_footnote")[0].innerHTML
    } catch(err) { return false }

    // Collect the correct answer
    try { console.log(document.getElementsByClassName("wk_correctAns")[0].children[1].textContent)
    } catch(error) { console.log(error) }

    // Choice another answer
    try {
        answers = document.getElementsByClassName("wk_choicesInstLink")
        answers[Math.floor(Math.random()*answers.length)].click()
    } catch(error) { document.getElementsByClassName("cbtn")[0].click() }
}

// 2 cajas grandes
function dosCajasGrandes() {
    document.getElementsByClassName("btOptionCard")[0].click()
}

// 2 cajas pequeñas
function dosCajasPequenas() {
    document.getElementsByClassName("btOption b_cards")[0].click()
}

