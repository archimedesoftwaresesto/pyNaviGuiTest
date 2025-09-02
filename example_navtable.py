import runner, pyNaviGui as ng, os

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS,KEY_BTN_LEGGI,KEY_SEX,KEY_MACHINE,KEY_IMKMAGINE,
KEY_BTN_AVANTI,KEY_BTN_INDIETRO,
 *_ ) = window.set_keys()

# general settings of the window and other use, ful variables
(window.winTitle('Titolo della finestra').winGeometry('800x800'))



(window.gotoxy(30,80).setRowHeigh(20).setInputSize(30,1).
 text('Name').crlf().
 input('', k=KEY_NAME).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf()
 )

tableconf={'NOME':['Nome',10], 'COGNOME':['Cognome',20], 'ANNI':['Anni',5]}
tabledata = [
    ['Dario', 'Giacomelli', 50],
    ['Marco', 'Rossi', 35],
    ['Laura', 'Bianchi', 42],
    ['Andrea', 'Ferrari', 28],
    ['Giulia', 'Romano', 33],
    ['Federica', 'Fontana', 34],
    ['Roberto', 'Martini', 41],
    ['Simona', 'Greco', 38],
    ['Alessandro', 'Costa', 30],
    ['Elena', 'Giordano', 27],
    ['Stefano', 'Mancini', 46],
    ['Paola', 'Lombardi', 32],
    ['Giuseppe', 'Moretti', 48],
    ['Luca', 'Costa', 30],
    ['Actarus', 'Giordano', 27],
    ['Goldrake', 'Mancini', 46],
    ['Luke', 'Lombardi', 32],
    ['Geeg', 'Moretti', 48]
]
window.setTextSize(20)
for i in range(7):
    window.image('./tableimages/img/desktop-app.png', size='50x50', k=f'IMG_ROW_{i}' )
    keylist = tableconf.keys()
    for j,k in enumerate(keylist):
        text_size = tableconf[k][1]
        window.setTextSize(text_size).text(tabledata[i][j])
    window.crlf()


(window.crlf().button( '  <<  ',k=KEY_BTN_INDIETRO).button('  >>  ',k=KEY_BTN_AVANTI).crlf().
 button('Leggi',k=KEY_BTN_LEGGI).crlf()
 )


window.finalize_layout()

while True:
    event, values = window.read()

    if event == KEY_IMKMAGINE:
        print('Image was clicked!')
    if event == KEY_BTN_LEGGI:
        print(values)

    if event == None:
        print('Window closed')
        break

window.close()