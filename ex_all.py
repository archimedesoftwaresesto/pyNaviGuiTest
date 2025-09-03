import runner, pyNaviGui as ng

window = ng.Ng()

(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_CB_COLORS, KEY_RB_ANIMAL, KEY_TABELLA, KEY_LB_WEAPON, KEY_NOTE1, KEY_NOTE2, KEY_COMBOBOX, KEY_CB_AUTOMOBILE, KEY_BTN_RIASSUMI,KEY_CB_ELEMENTS,
KEY_EMAIL, KEY_BTN_INVISIBILITA,KEY_ML_NOTE,   *_) = window.set_keys()

(window.win_title('Titolo della finestra').win_size('1300x600'))

(window.move_to(30, 20).set_text_size(10).set_input_size(20, 1).

 text('Name',s='ana').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br(spacing=10).
 text('Note ').input('', k=KEY_NOTE1).br().
 text('Note altre').input('', k=KEY_NOTE2).br(spacing=100)
 )

tableconf={'NOME':['Nome',10], 'COGNOME':['Cognome',20], 'ANNI':['Anni',5]}
tabledata = [
    ['Dario', 'Giacomelli', 50],
    ['Marco', 'Rossi', 35],
    ['Laura', 'Bianchi', 42],
    ['Andrea', 'Ferrari', 28],
    ['Giulia', 'Romano', 33],
    ['Federica', 'Fontana', 34],
    ['Roberto', 'Martini', 41],
    ['Simona', 'Greco', 38],
    ['Alessandro', 'Costa', 30],
    ['Elena', 'Giordano', 27],
    ['Stefano', 'Mancini', 46],
    ['Paola', 'Lombardi', 32],
    ['Giuseppe', 'Moretti', 48]
]
colors=[]
for i,r in enumerate(tabledata):
    colsfondo='white'
    colcarattere='black'
    if r[2]>40:
        colsfondo='yellow'
        colcarattere='red'
    colors.append([i, colsfondo, colcarattere])

window.move_to(400,10).table('Tabella anagrafica', conf=tableconf, data= tabledata,  rowcolors= colors, nr_rows=7, k=KEY_TABELLA).br()

(window.move_to(10,230).set(s='c1').
 checkboxes('Preferred colours aaaaaaaaaaaaaaaaaa', ('Red', 'Yellow', 'Brown'), k=KEY_CB_COLORS).
 checkboxes('Automobile used', ('Maserati|MASER', 'Ferrari|FERRARI', 'Lamborghini|LAMB', 'Fiat|FIAT'), k=KEY_CB_AUTOMOBILE).
 set(s='').
 text('Email').input('', k=KEY_EMAIL).
 multiline('Note ampie','', nr_rows=10, nr_cols=20, k=KEY_ML_NOTE).
combobox('Engine',('|', 'Engine A|CODA', 'Engine B|CODB', 'Engine C|CODC', 'Engine D|CODD',  'Engine E|CODE'), default='CODD', nr_rows=3, k=KEY_COMBOBOX).
 radio('Select one',['tiger|TIG','oak|OAK','a good cat|CAT'],k=KEY_RB_ANIMAL).
listbox('Weapons',('Bomb','Missile','Star'),   nr_rows=12, k=KEY_LB_WEAPON).
 checkboxes('Choose', ('First element|FIRST', 'Secon element|SECOND'), k=KEY_CB_ELEMENTS).br().
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
        if colors:
            print(colors)
            print(f'Preferred colours: {", ".join(colors)}')
        else:
            print('Preferred colours: Nessuna selezione')

        automobiles = values.get(KEY_CB_AUTOMOBILE, [])
        if automobiles:
            print(automobiles)
            print(f'Automobile used: {", ".join(automobiles)}')
        else:
            print('Automobile used: Nessuna selezione')

        elements = values.get(KEY_CB_ELEMENTS, [])
        if elements:
            print(elements)
            print(f'Elements used: {", ".join(elements)}')
        else:
            print('Elements used: Nessuna selezione')

        animals = values.get(KEY_RB_ANIMAL, [])
        if animals:
            print('Animal',animals)

        else:
            print('Animal : Nessuna selezione')

        weapons = values.get(KEY_LB_WEAPON, [])
        if weapons:
            print('Weapons',weapons)

        # Aggiungi questa sezione per il multiline
        note_ampie = values.get(KEY_ML_NOTE, "")
        if note_ampie.strip():  # .strip() rimuove spazi vuoti e newline
            print(f'Note ampie: {note_ampie}')
        else:
            print('Note ampie: Nessun contenuto')

        # Aggiungi questa sezione per il multiline
        combo = values.get(KEY_COMBOBOX, "")
        if combo.strip():  # .strip() rimuove spazi vuoti e newline
            print(f'combo: {combo}')
        else:
            print('combo: Nessun combo')

        print('========================\n')

        selected = values[KEY_TABELLA]
        print(selected)
        for x in selected:
            print(tabledata[x])

window.close()