import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS,KEY_BTN_LEGGI,KEY_SEX,KEY_MACHINE,KEY_TABELLA,
 *_ ) = window.set_keys()

# general settings of the window and other use, ful variables
(window.winTitle('Titolo della finestra').winGeometry('800x600'))



(window.gotoxy(30,80).setRowHeigh(20).setInputSize(30,1).
 text('Name').crlf().
 input('', k=KEY_NAME).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf().
 checkboxes( ('Male','Female','Other'), k=KEY_SEX ).
 checkboxes(('Maserati|MAS', 'Ferrari|FERR', 'Lamborghini|LAMB','Fiat|FIAT'),k=KEY_MACHINE).crlf()
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
    ['Giuseppe', 'Moretti', 48]
]

colors=[]
for i,r in enumerate(tabledata):
    colsfondo='white'
    colcarattere='black'
    if r[2]>40:
        colsfondo='yellow'
        colcarattere='red'
    colors.append([i, colsfondo, colcarattere])

(
    window.table('Tabella anagrafica', conf=tableconf, data= tabledata, nr_rows=7, rowcolors=colors, k=KEY_TABELLA).crlf().
    button('Leggi',k=KEY_BTN_LEGGI)
)


window.finalize_layout()

while True:
    event, values = window.read()

    if event == KEY_BTN_LEGGI:
        print(values)
        selected = values[KEY_TABELLA]
        print(selected)
        for x in selected:
            print(tabledata[x])

    if event == None:
        print('Window closed')
        break

window.close()