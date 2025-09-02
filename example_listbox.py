import runner, import pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_BTN_LEGGI, KEY_CHECKBOXES1, KEY_CHECKBOXES2, KEY_LISTBOX,
 *_) = window.set_keys()

# general settings of the window and other use, ful variables
(window.winTitle('Titolo della finestra').winGeometry('800x600'))

(window.gotoxy(30, 80).setRowHeigh(20).setInputSize(30, 1).
 text('Name').crlf().
 input('', k=KEY_NAME).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf().
 checkboxes('Gender:', ('Male', 'Female', 'Other'), k=KEY_CHECKBOXES1).
 checkboxes('Cars:', ('Maserati', 'Ferrari', 'Lamborghini', 'Fiat'), k=KEY_CHECKBOXES2).
 listbox('Select these:', ('Aereoplane|AEREO', 'Elicopter|ELIC', 'Machine|MAC', 'Gun|GUN', 'Gun 1|GUN1', 'Gun2|GUN2', 'Gun3|GUN3', 'Bomb|BOMB'), multi_select=True, nr_rows=5, k=KEY_LISTBOX,
         default='ELIC').crlf().
 button('Leggi', k=KEY_BTN_LEGGI)
 )

window.finalize_layout()

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

    elif event == None:
        print('Window closed')
        break

window.close()