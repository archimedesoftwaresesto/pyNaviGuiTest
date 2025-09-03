import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_BTN_TAB1, KEY_BTN_TAB2, KEY_BTN_TAB3,
KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_BORN, KEY_WEIGHT, KEY_AGE, KEY_EMAIL, KEY_BTN_ADD,
KEY_FIELD1, KEY_FIELD2, KEY_FIELD3, KEY_ADDRESS_1, KEY_ADDRESS_2, KEY_ADDRESS_3,
KEY_NOTE_1, KEY_NOTE_2, KEY_NOTE_3,
 *_ ) = window.set_keys()

# general settings of the window and other use, ful variables
(window.win_title('Titolo della finestra').win_size('800x600'))

# first column
ref_y = 10
ref_x = 80
(window.move_to(ref_x,ref_y).set_row_height(20).set_input_size(30,1).
 button('Tab 1',k=KEY_BTN_TAB1).br().
 button('Tab 2',k=KEY_BTN_TAB2).button('Tab 3',k=KEY_BTN_TAB3)
 )

# first tab

ref_y = 100
(window.move_to(ref_x,ref_y).
 set(s='t1').
 text('Name').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br().
 text('Date of born').br().
 input('', k=KEY_BORN).

 move_to(ref_x + 220 ,ref_y).
 text('Weight').br().
 input('',  k=KEY_WEIGHT).br().
 text('Age').br().
 input('', k=KEY_AGE).br().
 text('Email').br().
 input('',  k=KEY_EMAIL)
 )

# second tab
(window.move_to(ref_x   ,ref_y).
 set(s='t2').
 text('Address 1').input('', k=KEY_ADDRESS_1).br().
 text('Address 2').input('', k=KEY_ADDRESS_2).br().
 text('Address 3').input('', k=KEY_ADDRESS_3).
 set(s='')
 )

# third tab
(window.move_to(90   ,60).
set(s='t3').
 text('Note 1').br().
 input('', k=KEY_NOTE_1).br().
 text('Address 2').input('',k=KEY_NOTE_2).br().
 text('Address 3').input('', k=KEY_NOTE_3)
 )

window.finalize_layout()

#initializatin
window.visible(True,shas='t1').visible(False, shas='t2').visible(False, shas='t3')

while True:
    event, values = window.read()
    if event == KEY_BTN_TAB1:
        window.visible(True,shas='t1').visible(False, shas='t2').visible(False, shas='t3')
    if event == KEY_BTN_TAB2:
        window.visible(False,shas='t1').visible(True, shas='t2').visible(False, shas='t3')
    if event == KEY_BTN_TAB3:
        window.visible(False,shas='t1').visible(False, shas='t2').visible(True, shas='t3')
    if event == None:
        print('Window closed')
        break
window.close()