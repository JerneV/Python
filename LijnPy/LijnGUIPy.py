import PySimpleGUI as sg
from LijnPy import getPassingBy
import os

name = os.getlogin()
stop = 0


## Main function
def getStops():
    while True:
        button, values = window.Read()
        if button == 'Submit':
            if values[0] == 'Kortenberg Kappeleke':
                stop = 302763
                break
            elif values[0] == 'Kortenberg Vaan':
                stop = 302782
                break
            elif values[0] == 'Sterrebeek - Oud Station':
                stop = 305516
                break
            elif values[0] == 'Leuven Station 8':
                stop = 303134
                break
            elif values[0] == 'Leuven - Jan Stas':
                stop = 303059
                break
            elif values[0] == 'Leuven - Sint Jacob':
                stop = 306319
                break

    deLijn = getPassingBy(stop, 10, False, False)
    print('\n\nPasserende bussen bij ' + values[0] + ' om ' + deLijn[0] + "\n")
    for x in range(1, len(deLijn), 2):
        print("Bus " + str(deLijn[x]) + " komt om/in: " + str(deLijn[x+1]))
    getStops() #Just so we can keep calling it, I also could have use a double while loop I guess?


## The actual window

layout = [ [sg.Text('Welcome ' + str(name).title())],
           [sg.Text('Choose stop'), sg.InputCombo(('Kortenberg Kappeleke', 'Kortenberg Vaan', 'Sterrebeek - Oud Station', 'Leuven Station 8', 'Leuven - Jan Stas', 'Leuven - Sint Jacob'), size=(20, 1))], ## This is custom made for my daily travels, maybe later I'll add something where you can acutally choose where you start. 
           [sg.ReadButton('Submit')],
           [sg.Output(size=(88, 20), font='Courier 10')],
        ]

window = sg.Window('LijnPy - GUI').Layout(layout)
window.Read()
getStops()







    
