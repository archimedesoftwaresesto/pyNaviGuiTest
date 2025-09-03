import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_BORN, KEY_WEIGHT, KEY_AGE, KEY_EMAIL, KEY_BTN_ADD,
KEY_FIELD1, KEY_FIELD2, KEY_FIELD3,
 *_ ) = window.set_keys()

# general settings of the window and other use, ful variables
window.win_title('Titolo della finestra').win_size('800x600')

# first column
ref_y = 30
ref_x = 80

(window.move_to(ref_x,ref_y).set_row_height(20).set_input_size(30,1).
 text('Name').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br().
 text('Date of born').br().
 input('', k=KEY_BORN)
 )

# second column
(window.move_to(ref_x + 220 ,ref_y).set_row_height(20).set_input_size(30,1).
 text('Weight').br().
 input('', k=KEY_WEIGHT).br().
 text('Age').br().
 input('', k=KEY_AGE).br().
 text('Email').br().
 input('', k=KEY_EMAIL)
 )

# last line with commands
(window.move_to(80,230).set_row_height(30).set_input_size(30,1).
 button('Add elements',k=KEY_BTN_ADD)
 )

window.finalize_layout()

while True:
    event, values = window.read()

    if event == KEY_BTN_ADD:

        # deleting the elements
        window.delete(k=KEY_FIELD1).delete(k=KEY_FIELD2).delete(k=KEY_FIELD3)

        # adding the elements
        (window.move_below(k=KEY_EMAIL).set_row_height(20).set_input_size(30, 1).
         text('Field 1').
         input('', k=KEY_FIELD1).br().
         text('Filed 2').br().
         input('', k=KEY_FIELD2).br().
         text('Field 3').br().
         input('', k=KEY_FIELD3)
         )

    if event == None:
        print('Window closed')
        break

window.close()