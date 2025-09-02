import runner, pyNaviGui as ng, os

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_BTN_LEGGI, KEY_SEX, KEY_MACHINE, KEY_IMKMAGINE,
 KEY_BTN_AVANTI, KEY_BTN_INDIETRO,KEY_TABELLANAV,
 *_) = window.set_keys()

# Configurazione generale della finestra
window.winTitle('Tabella Navigabile').winGeometry('800x800')

# Input iniziali
(window.gotoxy(30, 80).setRowHeigh(20).setInputSize(30, 1).
 text('Name').crlf().
 input('', k=KEY_NAME).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf()
 )

# Configurazione tabella
tableconf = {'NOME': ['Nome', 10], 'COGNOME': ['Cognome', 20], 'ANNI': ['Anni', 5]}
tabledata = [
    ['Dario', 'Giacomelli', 50, '012 04.jpg'],
    ['Marco', 'Rossi', 35, '034G 06.jpg'],
    ['Laura', 'Bianchi', 42, '034M 10.jpg'],
    ['Andrea', 'Ferrari', 28, '034P 24.jpg'],
    ['Giulia', 'Romano', 33, 'giulia.png'],
    ['Federica', 'Fontana', 34, 'federica.png'],
    ['Roberto', 'Martini', 41, 'roberto.png'],
    ['Simona', 'Greco', 38, 'simona.png'],
    ['Alessandro', 'Costa', 30, 'alessandro.png'],
    ['Elena', 'Giordano', 27, 'elena.png'],
    ['Stefano', 'Mancini', 46, 'stefano.png'],
    ['Paola', 'Lombardi', 32, '038 04.jpg'],
    ['Giuseppe', 'Moretti', 48, 'giuseppe.png'],
    ['Luca', 'Costa', 30, 'luca.png'],
    ['Actarus', 'Giordano', 27, 'actarus.png'],
    ['Goldrake', 'Mancini', 46, '041 10.jpg'],
    ['Luke', 'Lombardi', 32, 'luke.png'],
    ['Geeg', 'Moretti', 48, '038 08.jpg']
]

# Bottoni di navigazione e altre funzioni
window.navtable('Articoli', conf=tableconf, data=tabledata, nr_rows=7, folder_images ='./tableimages/img', k=KEY_TABELLANAV)

window.finalize_layout()



while True:
    event, values = window.read()

    if  event == KEY_BTN_LEGGI:
        print("Valori correnti:", values)


    if event is None:
        print('Finestra chiusa')
        break

window.close()