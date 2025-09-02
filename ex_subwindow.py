import pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_BORN, KEY_WEIGHT, KEY_AGE, KEY_EMAIL, KEY_BTN_ADD, KEY_SEARCH_NAMES,
 KEY_FIELD1, KEY_FIELD2, KEY_FIELD3, KEY_BTN_SEARCH_NAMES, KEY_CERCA_NOME, KEY_CERCA_PAESE, KEY_BTN_CERCA_NOMINATIVO,
 *_) = window.set_keys()

# General settings of the window
window.winTitle('Window Title').winGeometry('800x600')

# First column
ref_y = 30
ref_x = 80

(window.gotoxy(ref_x, ref_y).setRowHeigh(20).setInputSize(30, 1).
 text('Name').crlf().
 input('', k=KEY_NAME).button('...', k=KEY_BTN_SEARCH_NAMES).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf().
 text('Date of born').crlf().
 input('', k=KEY_BORN)
 )

# Second column
(window.gotoxy(ref_x + 220, ref_y).setRowHeigh(20).setInputSize(30, 1).
 text('Weight').crlf().
 input('', k=KEY_WEIGHT).crlf().
 text('Age').crlf().
 input('', k=KEY_AGE).crlf().
 text('Email').crlf().
 input('', k=KEY_EMAIL)
 )

# Last line with commands
(window.gotoxy(80, 230).setRowHeigh(30).setInputSize(30, 1).
 button('Add elements', k=KEY_BTN_ADD)
 )

window.finalize_layout()

while True:
    event, values = window.read()

    if event == KEY_BTN_SEARCH_NAMES:
        # Clean up any existing search area first
        window.delete(k=KEY_SEARCH_NAMES)
        window.delete(k=KEY_CERCA_NOME)
        window.delete(k=KEY_CERCA_PAESE)
        window.delete(k=KEY_BTN_CERCA_NOMINATIVO)


        (window.gotoBelow(k=KEY_BTN_SEARCH_NAMES).
         area('Search names', geometry='400x400', s='SEARCH_NAMES', k=KEY_SEARCH_NAMES).
        gotoxy(10,10).text('Nome contiene').input('', k=KEY_CERCA_NOME).crlf().
        text('Paese').input('', k=KEY_CERCA_PAESE).crlf().
        button('Cerca', k=KEY_BTN_CERCA_NOMINATIVO).crlf().
        area('')  # Close area
         )

    if event == KEY_BTN_ADD:
        # Delete any existing field elements
        window.delete(k=KEY_FIELD1)
        window.delete(k=KEY_FIELD2)
        window.delete(k=KEY_FIELD3)

        # Add new elements
        (window.gotoBelow(k=KEY_BTN_SEARCH_NAMES).setRowHeigh(20).setInputSize(30, 1).
         text('Field 1').input('', k=KEY_FIELD1).crlf().
         text('Field 2').crlf().
         input('', k=KEY_FIELD2).crlf().
         text('Field 3').crlf().
         input('', k=KEY_FIELD3)
         )

    if event is None:
        print('Window closed')
        break

window.close()