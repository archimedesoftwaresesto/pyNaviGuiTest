import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS,KEY_BTN_LEGGI,KEY_SEX,KEY_MACHINE,
 *_ ) = window.set_keys()

# general settings of the window and other use, ful variables
(window.winTitle('Titolo della finestra').winGeometry('800x600'))



(window.gotoxy(30,80).setRowHeigh(20).setInputSize(30,1).
 text('Name').crlf().
 input('', k=KEY_NAME).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf().
 checkboxes( ('Male','Female','Other'), k=KEY_SEX ).
 checkboxes(('Maserati|MAS', 'Ferrari|FERR', 'Lamborghini|LAMB','Fiat|FIAT'),k=KEY_MACHINE).crlf().
 button('Leggi',k=KEY_BTN_LEGGI)


 )


window.finalize_layout()

while True:
    event, values = window.read()

    if event == KEY_BTN_LEGGI:
        print(values)

    if event == None:
        print('Window closed')
        break

window.close()