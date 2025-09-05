import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS,KEY_BTN_READ_VALUES,KEY_SEX,KEY_MACHINE,
 KEY_BTN_FOCUS_TO_NAME, KEY_BTN_FOCUS_SURNAME,
 *_ ) = window.set_keys()

(window.win_title('Test of inputs').win_size('800x600').move_to(30,80).
 text('Name').input('',   k=KEY_NAME, event_enter=True).br().
 text('Surname').input('', set_focus=True, event_tab=True , k=KEY_SURNAME).br().
 button('Read values',k=KEY_BTN_READ_VALUES).text('               ').
 button('Set focus on name',k=KEY_BTN_FOCUS_TO_NAME).button('Set focus on surname',k=KEY_BTN_FOCUS_SURNAME)
 )

while True:
    event, values = window.read()

    if event == KEY_BTN_READ_VALUES:
        print(values)

    if event == KEY_BTN_FOCUS_TO_NAME:
        window.set_focus(k=KEY_NAME)

    if event == KEY_BTN_FOCUS_SURNAME:
        window.set_focus(k=KEY_SURNAME)

    if event == KEY_NAME:
        print('You pressed anter on the name edit!')

    if event == KEY_SURNAME + '_TAB':
        print('You pressed tab on the surname edit!')

    if event == None:
        print('Window closed')
        break

window.close()