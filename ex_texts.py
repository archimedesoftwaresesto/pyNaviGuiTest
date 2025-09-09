import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS,KEY_BTN_READ_VALUES,KEY_SEX,KEY_MACHINE,
 KEY_BTN_FOCUS_TO_NAME, KEY_BTN_FOCUS_SURNAME,KEY_EMAIL,KEY_NATION,KEY_WEIGHT,
 *_ ) = window.set_keys()

(window.win_title('Test of inputs').win_size('800x600').move_to(30,80).
 text('Nation' ).input('',   k=KEY_NATION, event_enter=True).br().
 text('Name',font='Arial 22', fg='red').input('',   k=KEY_NAME, event_enter=True).br().
 text('Weight', font=('Arial', 33, 'bold italic'), fg='blue').input('',fg='green', bg='blue', font=('Arial', 33, 'bold italic'), set_focus=True,
                                                         event_tab=True, k=KEY_WEIGHT).br().
 text('Surname',font=('Arial',33), fg='red', bg='yellow').input('', font=('Arial',22) , fg='red', bg='silver',set_focus=True, event_tab=True , k=KEY_SURNAME).br().
 text('Email',font='Arial 66').input('', set_focus=True, event_enter=True, event_tab=True, event_change=500, k=KEY_EMAIL).br().

 button('Read values',k=KEY_BTN_READ_VALUES).text('               ').
 button('Set focus on name',k=KEY_BTN_FOCUS_TO_NAME).button('Set focus on surname',k=KEY_BTN_FOCUS_SURNAME)
 )

nr_changes = 0

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

    if event == KEY_EMAIL :
        print('You pressed enter on the email edit!')

    if event == KEY_EMAIL + '_TAB':
        print('You pressed tab on the email edit!')

    if event == KEY_EMAIL + '_CHANGE':
        nr_changes += 1
        print(f'You change {nr_changes} times,  the email field!')


    if event == None:
        print('Window closed')
        break

window.close()

#2025_0909G messo font su .text e .input