import runner,  pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_BTN_LEGGI, KEY_CHECKBOXES1, KEY_CHECKBOXES2, KEY_COMBOBOX,
 *_) = window.set_keys()

# general settings of the window and other use, ful variables
(window.win_title('Titolo della finestra').win_size('800x600'))

(window.move_to(30, 80).set_row_height(20).set_input_size(30, 1).
 text('Name').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br().
 checkboxes('Gender:', ('Male', 'Female', 'Other'), k=KEY_CHECKBOXES1).
 checkboxes('Cars:', ('Maserati', 'Ferrari', 'Lamborghini', 'Fiat'), k=KEY_CHECKBOXES2).
 combobox('Select these:', ('Aereoplane|AEREO', 'Elicopter|ELIC', 'Machine|MAC', 'Gun|GUN', 'Gun 1|GUN1', 'Gun2|GUN2', 'Gun3|GUN3', 'Bomb|BOMB'),  nr_rows=5, k=KEY_COMBOBOX,
         default='ELIC' , event_change=False ).br().
 button('Leggi', k=KEY_BTN_LEGGI)
 )



while True:
    event, values = window.read()

    if event == KEY_BTN_LEGGI:
        print("\n=== VALORI LETTI ===")
        print(f"Name: '{values.get(KEY_NAME, '')}'")
        print(f"Surname: '{values.get(KEY_SURNAME, '')}'")
        print(f"Gender: {values.get(KEY_CHECKBOXES1, [])}")
        print(f"Cars: {values.get(KEY_CHECKBOXES2, [])}")
        print(f"Selected Vehicle: '{values.get(KEY_LISTBOX, '')}'")
        print("===================\n")

    if event == KEY_COMBOBOX:
        print('You changed the combobox!')
        print(f"Selected Vehicle: '{values.get(KEY_COMBOBOX, '')}'")




    elif event == None:
        print('Window closed')
        break

window.close()


#2025_0908 event_click and event_dbclick , event_change on listbox