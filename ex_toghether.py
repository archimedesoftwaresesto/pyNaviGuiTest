import runner
import FreeSimpleGUI as sg
import pyNaviGui as ng  # Con le modifiche per embed_mode

sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.T('FSG Nome'), sg.I('', key='fsg_nome')],
    [sg.T('FSG Cognome'), sg.I('', key='fsg_cognome')],
    [sg.Text('', size=(1, 5))],
    [sg.Button('Get All Values', key='get_values'), sg.Button('Exit')]
]

# Crea la finestra FreeSimpleGUI
window = sg.Window('Together', layout, size=(1300, 600), finalize=True)

# Ottieni il root Tkinter di FreeSimpleGUI
fsg_root = window.TKroot

# Crea pyNaviGui in modalità embedded (NESSUNA FINESTRA SEPARATA)
ngWin = ng.Ng(embed_mode=True, parent_root=fsg_root)

# Imposta le chiavi per pyNaviGui
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_CB_COLORS, KEY_NOTE1, KEY_NOTE2, KEY_CB_AUTOMOBILE, KEY_BTN_RIASSUMI,KEY_CB_ELEMENTS,
KEY_EMAIL, KEY_BTN_INVISIBILITA, KEY_BTN_PYNAVI,  *_) = ngWin.set_keys()

# Crea gli elementi pyNaviGui
(ngWin.gotoxy(530, 20).setTextSize(15, 1).setInputSize(30, 1).
 text('Name', s='ana').crlf().
 input('', k=KEY_NAME).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf().crlf().
 text('Note ').input('', k=KEY_NOTE1).crlf().
 text('Note altre').input('', k=KEY_NOTE2).crlf().crlf().
 gotoxy(130, 210).
 set(s='c1').
 checkboxes('Preferred colours', ('Red', 'Yellow', 'Brown'), k=KEY_CB_COLORS).
 checkboxes('Automobile used', ('Maserati|MASER', 'Ferrari|FERRARI', 'Lamborghini|LAMB', 'Fiat|FIAT'),
            k=KEY_CB_AUTOMOBILE).
 set(s='').
 text('Email').input('', k=KEY_EMAIL).
 checkboxes('Choose', ('First element|FIRST', 'Secon element|SECOND'), k=KEY_CB_ELEMENTS).crlf().
 button('Riassumi valori', k=KEY_BTN_RIASSUMI).crlf().
 button('Prime due colonne invisibili', k=KEY_BTN_INVISIBILITA).crlf().
 button('Leggi',k=KEY_BTN_PYNAVI)
 )
ngWin.finalize_layout()

flipflopvisible = True

while True:
    event, fsg_values = window.Read(timeout=50)

    if event == sg.WIN_CLOSED or event == None or event == 'Exit':
        break

    if event == 'get_values':
        print('\n=== VALORI COMBINATI ===')
        print('FreeSimpleGUI:')
        for key, value in fsg_values.items():
            print(f'  {key}: {value}')

        print('pyNaviGui:')
        pynavi_values = ngWin._get_values()
        for key, value in pynavi_values.items():
            print(f'  {key}: {value}')
        print('========================\n')

    try:
        pynavi_event, pynavi_values = ngWin.read()
        if pynavi_event == KEY_BTN_PYNAVI:
            print('Bottone pyNaviGui premuto!')
            print(event, fsg_values)

        if pynavi_event == KEY_BTN_INVISIBILITA:

            flipflopvisible = not flipflopvisible
            ngWin.visible(flipflopvisible, shas='c1')
    except:
        pass

# Chiusura pulita
window.close()  # pyNaviGui in embed_mode non ha una finestra propria da chiudere