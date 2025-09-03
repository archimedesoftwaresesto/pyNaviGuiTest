import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS,KEY_BTN_LEGGI,KEY_SEX,KEY_MACHINE,KEY_TABELLA,
 *_ ) = window.set_keys()

# general settings of the window and other use, ful variables
(window.win_title('Titolo della finestra').win_size('800x600'))



(window.move_to(30,80).set_row_height(20).set_input_size(30,1).
 text('Name').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br().
 checkboxes( ('Male','Female','Other'), k=KEY_SEX ).
 checkboxes(('Maserati|MAS', 'Ferrari|FERR', 'Lamborghini|LAMB','Fiat|FIAT'),k=KEY_MACHINE).br()
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
    ['Marco', 'Bianchi', 39],
    ['Laura', 'Rossi', 44],
    ['Andrea', 'Romano', 31],
    ['Dario', 'Ferrari', 52],
    ['Giulia', 'Fontana', 29],
    ['Roberto', 'Greco', 37],
    ['Simona', 'Martini', 36],
    ['Alessandro', 'Giordano', 43],
    ['Elena', 'Costa', 25],
    ['Stefano', 'Moretti', 47],
    ['Paola', 'Mancini', 34],
    ['Giuseppe', 'Lombardi', 51],
    ['Marco', 'Giacomelli', 40],
    ['Laura', 'Ferrari', 38],
    ['Andrea', 'Bianchi', 33],
    ['Giulia', 'Rossi', 31],
    ['Federica', 'Romano', 36],
    ['Roberto', 'Fontana', 45],
    ['Dario', 'Greco', 48],
    ['Alessandro', 'Martini', 32],
    ['Elena', 'Mancini', 29],
    ['Stefano', 'Costa', 44],
    ['Paola', 'Giordano', 37],
    ['Giuseppe', 'Ferrari', 50],
    ['Marco', 'Romano', 34],
    ['Laura', 'Fontana', 41],
    ['Andrea', 'Martini', 30],
    ['Giulia', 'Greco', 35],
    ['Federica', 'Bianchi', 38],
    ['Roberto', 'Rossi', 42],
    ['Simona', 'Giacomelli', 33],
    ['Alessandro', 'Lombardi', 47],
    ['Elena', 'Moretti', 26],
    ['Dario', 'Mancini', 49],
    ['Paola', 'Costa', 35],
    ['Giuseppe', 'Giordano', 46],
    ['Marco', 'Fontana', 37]
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
    window.table('Tabella anagrafica', conf=tableconf, data= tabledata, nr_rows=7, rowcolors=colors, k=KEY_TABELLA).br().
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