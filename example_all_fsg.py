import FreeSimpleGUI as sg

# Definizione delle chiavi
KEY_NAME = '-NAME-'
KEY_SURNAME = '-SURNAME-'
KEY_CB_COLORS = '-CB_COLORS-'
KEY_RB_ANIMAL = '-RB_ANIMAL-'
KEY_LB_WEAPON = '-LB_WEAPON-'
KEY_NOTE1 = '-NOTE1-'
KEY_NOTE2 = '-NOTE2-'
KEY_CB_AUTOMOBILE = '-CB_AUTOMOBILE-'
KEY_BTN_RIASSUMI = '-BTN_RIASSUMI-'
KEY_CB_ELEMENTS = '-CB_ELEMENTS-'
KEY_EMAIL = '-EMAIL-'
KEY_BTN_INVISIBILITA = '-BTN_INVISIBILITA-'
KEY_ML_NOTE = '-ML_NOTE-'

# Layout della finestra - cerchiamo di replicare esattamente quello della screenshot
layout = [
    # Prima sezione: inputs singoli in colonna
    [sg.Text('Name', size=(10, 1))],
    [sg.InputText('', key=KEY_NAME, size=(30, 1))],
    [sg.Text('Surname', size=(10, 1))],
    [sg.InputText('', key=KEY_SURNAME, size=(30, 1))],
    [sg.Text('')],  # Spacing
    [sg.Text('Note', size=(10, 1)), sg.InputText('', key=KEY_NOTE1, size=(30, 1))],
    [sg.Text('Note altre', size=(10, 1)), sg.InputText('', key=KEY_NOTE2, size=(30, 1))],
    [sg.Text(''), sg.Text(''), sg.Text('')],  # Spacing maggiore per simulare spacing=100

    # Seconda sezione: elementi affiancati orizzontalmente
    [
        # Colonna 1: Preferred colours
        sg.Column([
            [sg.Text('Preferred colours', font=('Arial', 10, 'bold'))],
            [sg.Checkbox('Red', key=KEY_CB_COLORS + 'Red')],
            [sg.Checkbox('Yellow', key=KEY_CB_COLORS + 'Yellow')],
            [sg.Checkbox('Brown', key=KEY_CB_COLORS + 'Brown')]
        ], vertical_alignment='top'),

        # Colonna 2: Automobile used
        sg.Column([
            [sg.Text('Automobile used', font=('Arial', 10, 'bold'))],
            [sg.Checkbox('Maserati', key=KEY_CB_AUTOMOBILE + 'MASER')],
            [sg.Checkbox('Ferrari', key=KEY_CB_AUTOMOBILE + 'FERRARI')],
            [sg.Checkbox('Lamborghini', key=KEY_CB_AUTOMOBILE + 'LAMB')],
            [sg.Checkbox('Fiat', key=KEY_CB_AUTOMOBILE + 'FIAT')]
        ], vertical_alignment='top'),

        # Colonna 3: Email + Multiline
        sg.Column([
            [sg.Text('Email', size=(10, 1))],
            [sg.InputText('', key=KEY_EMAIL, size=(30, 1))],
            [sg.Text('')],  # Spacing
            [sg.Text('Note ampie', font=('Arial', 10, 'bold'))],
            [sg.Multiline('', key=KEY_ML_NOTE, size=(20, 10))]
        ], vertical_alignment='top'),

        # Colonna 4: Radio buttons
        sg.Column([
            [sg.Text('Select one', font=('Arial', 10, 'bold'))],
            [sg.Radio('tiger', 'RADIO1', key=KEY_RB_ANIMAL + 'TIG', default=True)],
            [sg.Radio('oak', 'RADIO1', key=KEY_RB_ANIMAL + 'OAK')],
            [sg.Radio('a good cat', 'RADIO1', key=KEY_RB_ANIMAL + 'CAT')]
        ], vertical_alignment='top'),

        # Colonna 5: Listbox
        sg.Column([
            [sg.Text('Weapons', font=('Arial', 10, 'bold'))],
            [sg.Listbox(['Bomb', 'Missile', 'Star'], key=KEY_LB_WEAPON, size=(15, 3))]
        ], vertical_alignment='top'),

        # Colonna 6: Choose checkboxes
        sg.Column([
            [sg.Text('Choose', font=('Arial', 10, 'bold'))],
            [sg.Checkbox('First element', key=KEY_CB_ELEMENTS + 'FIRST')],
            [sg.Checkbox('Second element', key=KEY_CB_ELEMENTS + 'SECOND')]
        ], vertical_alignment='top')
    ],

    # Ultima sezione: bottoni
    [sg.Text('')],  # Spacing
    [sg.Button('Riassumi valori', key=KEY_BTN_RIASSUMI)],
    [sg.Button('Prime due colonne invisibili', key=KEY_BTN_INVISIBILITA)]
]

# Creazione della finestra
window = sg.Window('Titolo della finestra', layout, size=(1300, 600), finalize=True)

flipflopvisible = True

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == None:
        print('Window closed')
        break

    if event == KEY_BTN_INVISIBILITA:
        flipflopvisible = not flipflopvisible
        # Nascondi/mostra i primi due gruppi di checkbox (equivalente a shas='c1')
        elements_to_toggle = [
            KEY_CB_COLORS + 'Red', KEY_CB_COLORS + 'Yellow', KEY_CB_COLORS + 'Brown',
            KEY_CB_AUTOMOBILE + 'MASER', KEY_CB_AUTOMOBILE + 'FERRARI',
            KEY_CB_AUTOMOBILE + 'LAMB', KEY_CB_AUTOMOBILE + 'FIAT'
        ]

        for elem_key in elements_to_toggle:
            window[elem_key].update(visible=flipflopvisible)

    if event == KEY_BTN_RIASSUMI:
        print('\n=== RIASSUNTO VALORI ===')
        print(f'Name: {values.get(KEY_NAME, "")}')
        print(f'Surname: {values.get(KEY_SURNAME, "")}')

        # Per i checkbox, devi controllare manualmente ogni checkbox
        colors = []
        color_mapping = {
            KEY_CB_COLORS + 'Red': 'Red',
            KEY_CB_COLORS + 'Yellow': 'Yellow',
            KEY_CB_COLORS + 'Brown': 'Brown'
        }
        for key, display_name in color_mapping.items():
            if values.get(key, False):
                colors.append(display_name)

        if colors:
            print(colors)
            print(f'Preferred colours: {", ".join(colors)}')
        else:
            print('Preferred colours: Nessuna selezione')

        automobiles = []
        auto_mapping = {
            KEY_CB_AUTOMOBILE + 'MASER': 'MASER',
            KEY_CB_AUTOMOBILE + 'FERRARI': 'FERRARI',
            KEY_CB_AUTOMOBILE + 'LAMB': 'LAMB',
            KEY_CB_AUTOMOBILE + 'FIAT': 'FIAT'
        }
        for key, value in auto_mapping.items():
            if values.get(key, False):
                automobiles.append(value)

        if automobiles:
            print(automobiles)
            print(f'Automobile used: {", ".join(automobiles)}')
        else:
            print('Automobile used: Nessuna selezione')

        elements = []
        element_mapping = {
            KEY_CB_ELEMENTS + 'FIRST': 'FIRST',
            KEY_CB_ELEMENTS + 'SECOND': 'SECOND'
        }
        for key, value in element_mapping.items():
            if values.get(key, False):
                elements.append(value)

        if elements:
            print(elements)
            print(f'Elements used: {", ".join(elements)}')
        else:
            print('Elements used: Nessuna selezione')

        # Radio buttons - controlla quale è selezionato
        animal = ''
        radio_mapping = {
            KEY_RB_ANIMAL + 'TIG': 'TIG',
            KEY_RB_ANIMAL + 'OAK': 'OAK',
            KEY_RB_ANIMAL + 'CAT': 'CAT'
        }
        for key, value in radio_mapping.items():
            if values.get(key, False):
                animal = value
                break

        if animal:
            print('Animal', animal)
        else:
            print('Animal : Nessuna selezione')

        # Listbox - restituisce una lista dei valori selezionati
        weapons = values.get(KEY_LB_WEAPON, [])
        if weapons:
            print('Weapons', weapons)

        # Multiline
        note_ampie = values.get(KEY_ML_NOTE, "")
        if note_ampie.strip():
            print(f'Note ampie: {note_ampie}')
        else:
            print('Note ampie: Nessun contenuto')

        print('========================\n')

window.close()