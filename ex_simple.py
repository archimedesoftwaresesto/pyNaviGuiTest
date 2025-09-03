import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS,KEY_BTN_LEGGI,KEY_SEX,KEY_MACHINE,
 *_ ) = window.set_keys()

# general settings of the window and other use, ful variables
(window.win_title('Titolo della finestra').win_size('800x600'))



(window.move_to(30,80).set_row_height(20).set_input_size(30,1).
 text('Name').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br().
 checkboxes( ('Male','Female','Other'), k=KEY_SEX ).
 checkboxes(('Maserati|MAS', 'Ferrari|FERR', 'Lamborghini|LAMB','Fiat|FIAT'),k=KEY_MACHINE).br().
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