import runner, pyNaviGui as ng


# Create window
window = ng.Ng(geometry='500x500')
KEY_CB_SELECTION , KEY_BTN_CB_VISIBLE, KEY_BTN_CB_INVISIBLE , *_ = window.set_keys()

# Sample data for combobox
options = ['Opzione 1|val1', 'Opzione 2|val2', 'Opzione 3|val3', 'Opzione 4|val4']

# Create combobox with change event
(window.move_to(50,50).text('Seleziona un\'opzione:').br().
 combobox('Combo con eventi:', options, s='-a-b-c-d', k=KEY_CB_SELECTION, default='val2', event_change=True).br(10).
    button('Set the combo visible', k=KEY_BTN_CB_VISIBLE).text('   ').button('Set the combo invisible', k=KEY_BTN_CB_INVISIBLE)

 )

# Event loop
while True:
    event, values = window.read()

    if event is None:  # Window closed
        break

    if event == KEY_CB_SELECTION:
        print('You selected on combobox')

    if event == KEY_BTN_CB_VISIBLE:
        print('set visible!')
        window.visible(True, shas='a')

    if event == KEY_BTN_CB_INVISIBLE:
        print('set invisible!')
        window.visible(False, shas='a')

window.close()