import flet as ft
import numpy as np
import random
winAdd = 0
lossAdd = 0
def main(page: ft.Page):
    page.title = "Krakashima Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = True

    def clearRes(e):
        result.value = ""
        page.update()

    def resulter(rec,resultText):
        if resultLenght.value == True:
            result.value = str(result.value) + resultText + str(np.unique(rec)) + "\n"
        else:
            result.value = str(result.value) + resultText + str(rec) + "\n"

    def textbox_changed(e):
        thumbCountFlip.value = "Number of Coins to Flip : " + str(pow(2,int(e.control.value)))
        page.update()

    thumbs = ft.TextField(max_length=1,value="0", text_align=ft.TextAlign.RIGHT, width=100,input_filter=ft.NumbersOnlyInputFilter(),adaptive=True,on_change=textbox_changed)
    krakTrigger = ft.TextField(max_length=3,value="0", text_align=ft.TextAlign.RIGHT, width=100,input_filter=ft.NumbersOnlyInputFilter(),adaptive=True)
    outcome = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100,input_filter=ft.NumbersOnlyInputFilter(),adaptive=True)
    result = ft.Text("")
    thumbCountFlip = ft.Text("")
    resultLenght = ft.Checkbox(label="Log level (true = short, false = long. Relevant for thumb results)", value=True)
    
    def addToTriggers(e):
        global winAdd
        if int(krakTrigger.value) + winAdd < 999:
            krakTrigger.value = int(krakTrigger.value) + winAdd
        else:
            #clearRes(e)
            result.value =  "To many Krak triggers, max is 999. Game is already won right?"  + "\n" + str(result.value)
        winAdd = 0
        lossAdd = 0
        page.update()


    
    def flip(e):
        clearRes(e)
        records = []
        global winAdd
        global lossAdd
        win = 0
        loss = 0
        
        thumbsCount = pow(2,int(thumbs.value))
        for i in range(0,int(krakTrigger.value)):
            if int(thumbsCount) > 1:
                for b in range(0,int(thumbsCount)):
                    records.append(random.randint(0, 1))
                if int(outcome.value) in records:
                    resulter(records,"win  : ")
                    page.update()
                    win+=1
                else:
                    resulter(records,"loss : ")
                    page.update()
                    loss+=1
            else:
                flip = random.randint(0, 1)
                if flip == int(outcome.value):
                    result.value = str(result.value) + "win"  + "\n"
                    page.update()
                    win += 1
                else:
                    result.value = str(result.value) + "loss"  + "\n"
                    page.update()
                    loss += 1
            records = []
        result.value =   "\n" + "Total win  : " + str(win) + "\n\n" + str(result.value)
        result.value =   "\n" + "Total loss : " + str(loss) + str(result.value)
        if int(thumbsCount) >= 1:
            thum = int(krakTrigger.value) * thumbsCount
            calc = (1 - (2 / 2**int(thum))) * 100
        else:
            calc = (1 - (2 / 2**int(krakTrigger.value))) * 100
        result.value = "Probability to get copy and bounce: " + str(calc) + "%" + "\n\n" + result.value
        winAdd = win
        lossAdd = loss
        page.update()

    page.add(
        ft.Row(
            [   
                ft.Text("How it works",size=30)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text("For Flips with the Thumb out results will look like:  'win [0 1]' 'loss [1]' 'loss [0]' 'win [0]' 'loss [0]'")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text("If no Thumb is present the results are a simple 'win' or 'loss'")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text("For presence of thumb the array result is important since you choose if you want to win or loose the flip")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                resultLenght
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [   
                ft.Text("Number of Thumbs"),
                thumbs,
                thumbCountFlip
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [   
                thumbCountFlip
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [   
                ft.Text("Number of Krak Triggers"),
                krakTrigger
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [   
                ft.Text("Heads/Tails (0/1)"),
                outcome
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.TextButton(text="Flip The Coins", on_click=flip),
                ft.TextButton(text="Clear Results", on_click=clearRes),
                ft.TextButton(text="Add result to Krak Trigger Count?", on_click=addToTriggers)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                result
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main, view=ft.AppView.WEB_BROWSER)
