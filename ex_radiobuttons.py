import runner, pyNaviGui as ng


window = ng.Ng()

(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_CB_COLORS, KEY_NOTE1, KEY_NOTE2, KEY_RB_AUTOMOBILE, KEY_BTN_RIASSUMI,KEY_RB_ELEMENTS,
KEY_EMAIL, KEY_BTN_INVISIBILITA,  *_) = window.set_keys()

(window.win_title('Titolo della finestra').win_size('800x600'))

(window.move_to(30, 20).set_text_size(10).set_input_size(30, 1).
 text('Name',s='ana').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br().br().
 text('Note ').input('', k=KEY_NOTE1).br().
 text('Note altre').input('', k=KEY_NOTE2).br().br().
 set(s='c1').
 checkboxes('Your very preferred colours', ('Red', 'Yellow', 'Brown'), k=KEY_CB_COLORS).
 radio('Automobile used', ('Maserati|MASER', 'Ferrari|FERRARI', 'Lamborghini|LAMB', 'Fiat|FIAT'), default='LAMB', k=KEY_RB_AUTOMOBILE).
 set(s='').
 text('Email').input('', k=KEY_EMAIL).
 radio('Choose', ('First element|FIRST', 'Secon element|SECOND'), k=KEY_RB_ELEMENTS).br().
 button('Riassumi valori', k=KEY_BTN_RIASSUMI).br().
button('Prime due colonne invisibili', k=KEY_BTN_INVISIBILITA)
 )

window.finalize_layout()

flipflopvisible = True

while True:
    event, values = window.read()

    if event == None:
        print('Window closed')
        break
    if event == KEY_BTN_INVISIBILITA:
        flipflopvisible = not flipflopvisible
        window.visible(flipflopvisible, shas='c1')


    if event == KEY_BTN_RIASSUMI:
        print('\n=== RIASSUNTO VALORI ===')
        print(f'Name: {values.get(KEY_NAME, "")}')
        print(f'Surname: {values.get(KEY_SURNAME, "")}')

        # Per i checkbox, i valori sono liste
        colors = values.get(KEY_CB_COLORS, [])
        print(f'{colors}')
        if colors:

            print('Preferred colours', ','.join(colors))

        else:
            print('Preferred colours: Nessuna selezione')

        automobiles = values.get(KEY_RB_AUTOMOBILE, [])
        if automobiles:
            print('Automobile used:',automobiles)

        else:
            print('Automobile used: Nessuna selezione')

        elements = values.get(KEY_RB_ELEMENTS, [])
        if elements:
            print('Elements used:', elements)

        else:
            print('Elements used: Nessuna selezione')


        print('========================\n')

window.close()