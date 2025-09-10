import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_SEX, KEY_MACHINE,KEY_IND_1, KEY_IND_2,KEY_BTN_LIVELLO,
 KEY_FILTRO_NOME, KEY_FILTRO_ETA, KEY_FILTRI, KEY_CHIUDI, KEY_APRI, KEY_BTN_APRI,KEY_BTN_FILTRI,KEY_BTN_ALTRO,KEY_ALTRO,
 *_) = window.set_keys()

# general settings of the window
window.win_title('Titolo della finestra').win_size('800x600')

# Create UI elements
window.move_to(30, 80).set_row_height(20).set_input_size(30, 1)
(window.button('Apri/Chiudi', k=KEY_BTN_FILTRI).text('                ').
 button('Altro', k=KEY_BTN_ALTRO).
 text('                         ').button('Alza livello', k=KEY_BTN_LIVELLO).br().
text('aaaaaaaaaaaaa').br().
text('bbbbbbbbbbb').br().
text('cccccc').br()
)


# Create filter panel once, but make it initially invisible
(window.move_below(k=KEY_BTN_FILTRI).  # Position for panel
panel('Filtri di ricerca', geometry='400x200', s='PANNELLO1',    bg='yellow', k=KEY_FILTRI).
text('AAAAAAA').br().
text('Nome').input('', k=KEY_FILTRO_NOME).br().
text('Età maggiore di').input('', k=KEY_FILTRO_ETA).br().
panel('')  # End panel
 )

# Create filter panel once, but make it initially invisible
(window.move_below(k=KEY_BTN_ALTRO).  # Position for panel
panel('Filtri di ricerca', geometry='300x100', s='PANNELLO2', vpadding=5,  bg='orange', k=KEY_ALTRO).
text('Indirizzo 1').input('', k=KEY_IND_1).br().
text('Indirizzo 2').input('', k=KEY_IND_2).br().
panel('')  # End panel
 )

# Hide panel initially
window.visible(False, shas='PANNELLO1').visible(False, shas='PANNELLO2')
ssssssssssssssssssssssssssssssss 2222222222222222222
window.finalize_layout()

while True:
    event, values = window.read()

    if event == KEY_BTN_FILTRI:
        window.visible( not window.is_visible(k=KEY_FILTRI) , shas='PANNELLO1')

    if event == KEY_BTN_ALTRO:
        window.visible( not window.is_visible(k=KEY_ALTRO) , shas='PANNELLO2')

    if event == KEY_BTN_LIVELLO:
        window.to_front(shas='PANNELLO1')  # o il valore s che hai utilizzato

    if event == None:
        print('Window closed')
        break


window.close()