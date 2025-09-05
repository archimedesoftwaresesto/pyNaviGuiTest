import runner, pyNaviGui as ng


window = ng.Ng()

(KEY_INPUT_CODICE_ART, KEY_INPUT_DESCRIZIONE, KEY_BTN_FILTRI, KEY_INPUT_ART_DA_CODICE,
 KEY_INPUT_ART_AL_CODICE,
 KEY_INPUT_RAGGRUPPAMENTO, KEY_INPUT_COLLEZZIONE, KEY_INPUT_FAMIGLIA, KEY_INPUT_CAMPAGNA,
 KEY_INPUT_SOTTOFAMIGLIA, KEY_INPUT_CATALOGO, KEY_TABELLA_PRODOTTI, KEY_TABELLA_CARRELLO,
 KEY_BTN_CERCA, KEY_QTA, KEY_IND_2, KEY_ALTRO, KEY_PANEL_SEL, KEY_BTN_AGGIUNGI,
 KEY_BTN_CHIUDI_PANEL, *_) = window.set_keys()


window.win_title('Titolo della finestra').win_size('1500x800')

col1_x = 30
col2_y= 20
(window.move_to(col1_x, col2_y).set_text_size(20).set_input_size(20, 1).

 text('Inizio Codice Articolo').br().
 input('', set_focus=True,  k=KEY_INPUT_CODICE_ART).
 button('FILTRI', k=KEY_BTN_FILTRI).br().
 text('Descrizione').br().
 input('', k=KEY_INPUT_DESCRIZIONE).
 button('CERCA', k=KEY_BTN_CERCA)

)
#colonna 1
(
    window.move_to(col1_x+200, col2_y).set_text_size(20).set_input_size(20, 1).set(s='FILTRI').
    text('Articolo dal Codice').br().
    input('', k=KEY_INPUT_ART_DA_CODICE).br().
    text('Articolo al Codice').br().
    input('', k=KEY_INPUT_ART_AL_CODICE).
    set(s='')
)
#colonna 2
(
    window.move_to(col1_x+350, col2_y).set_text_size(20).set_input_size(20, 1).set(s='FILTRI').
    text('Raggruppamento').br().
    input('', k=KEY_INPUT_RAGGRUPPAMENTO).br().
    text('Collezzione').br().
    input('', k=KEY_INPUT_COLLEZZIONE).
    set(s='')
)
#colonna 3
(
    window.move_to(col1_x + 500, col2_y).set_text_size(20).set_input_size(20, 1).set(s='FILTRI').
    text('Famiglia').br().
    input('', k=KEY_INPUT_FAMIGLIA).br().
    text('Campagna').br().
    input('', k=KEY_INPUT_CAMPAGNA).
    set(s='')

)
#colonna 4
(
    window.move_to(col1_x + 650, col2_y).set_text_size(20).set_input_size(20, 1).set(s='FILTRI').
    text('Sottofamiglia').br().
    input('', k=KEY_INPUT_SOTTOFAMIGLIA).br().
    text('Catalogo').br().
    input('', k=KEY_INPUT_CATALOGO).
    set(s='')
)
(window.visible(False, shas='FILTRI'))

#colonna carrello
(
    window.move_to(col1_x + 900, col2_y).set_text_size(30).
    text('P R O D O T T I   O R D I N A T I')
)
#colonna elenco
conf_tab_prodotti = {'CODICE': ['Codice', 8], 'DESCRIZIONE': ['Descrizione', 25], 'PREZZO': ['Prezzo', 8]}
product = [
# [CODICE, DESCRIZIONE, PREZZO, NOME_IMMAGINE] <- SEMPRE ultima colonna per l'immagine
    ['A001', 'ORGANZA D. TONE CM.145X3MT VERDE', '34.66', '034M 10.jpg'],
    ['A002', 'ORGANZA D. TONE CM.145X3MT ARANCIO','23.50', '012 04.jpg'],
    ['A003', 'NASTRO PARADISE', '10.99', '034M 06.jpg'],
    ['A004', 'BUSTA DORATA', '4.99', '041 10.jpg'],
    ['A005', 'BORSA UOVO', '12.99', '040 01.jpg'],
    ['A006', 'BORSA COLOMBA', '9.99', '038 04.jpg'],
    ['A007', 'BUSTA CALANDRATA', '8.99', '038 08.jpg'],
    ['A008', 'ORGANZA D. TONE CM.145X3MT ARGENTO', '29.99', '034P 24.jpg'],
]
(
    window.move_to(col1_x, col2_y + 150).set_text_size(20)
    .navtable('P R O D O T T I', conf=conf_tab_prodotti, data=product, nr_rows=5,
                folder_images='./tableimages/img', k=KEY_TABELLA_PRODOTTI)

)
conf_tab_carrello = {'CODICE': ['Codice', 8], 'DESCRIZIONE': ['Descrizione', 25], 'PREZZO': ['Prezzo', 8],
                     'QTA':['Qta', 8]}

carrello = []

sw_filtri_closed = True
filtro = [item for item in product if item[0] == "A006"]

window.finalize_layout()


(window.move_to(col1_x + 75, col2_y + 225).  # Position for panel
 panel('Aggiungi quantita al carrello', geometry='250x200', s='PANNELLO_SEL',
       vpadding=5, bg='lightgrey', k=KEY_PANEL_SEL).
 button('X', k= KEY_BTN_CHIUDI_PANEL).br().br().
 text('QTA').br().
 input('', k=KEY_QTA).br().br().
 button('AGGIUNGI AL CARRELLO', k=KEY_BTN_AGGIUNGI).
 panel('')  # End panel
 )
window.visible(False, shas='PANNELLO_SEL')


def aggiungi_carrello(clicked_data, qta):
    sw_trovato = False
    codice = clicked_data[0]
    prezzo_unitario = float(clicked_data[2])
    img = clicked_data[3]
    for item in carrello:
        if item[0] == codice:
            item[3] += int(qta)
            item[2] = round(prezzo_unitario * item[3], 2)
            sw_trovato = True
    if sw_trovato is False:
        prezzo_totale = round(prezzo_unitario * float(qta), 2)
        new_item = [clicked_data[0], clicked_data[1], prezzo_totale, int(qta), img]
        carrello.append(new_item)
    print(carrello)
    window.delete(k=KEY_TABELLA_CARRELLO)
    (
        window.move_to(col1_x + 800, col2_y + 80).set_text_size(20)
        .navtable('C A R E L L O', conf=conf_tab_carrello, data=carrello, nr_rows=5,
                  folder_images='./tableimages/img', k=KEY_TABELLA_CARRELLO)
    )
while True:
    event, values = window.read()

    if event == None:
        print('Window closed')
        break

    if event == KEY_BTN_FILTRI:

        if sw_filtri_closed:
            (window.visible(sw_filtri_closed, shas='FILTRI'))
            sw_filtri_closed = False
        else:
            (window.visible(sw_filtri_closed, shas='FILTRI'))
            sw_filtri_closed = True
    elif event and event.endswith('_IMG_ROW_0') or event.endswith('_IMG_ROW_1') or event.endswith(
            '_IMG_ROW_2') or event.endswith('_IMG_ROW_3') or event.endswith('_IMG_ROW_4') or event.endswith(
            '_IMG_ROW_5'):
        # Gestione click su immagini
        if '_clicked_data' in values and values['_clicked_data']:
            window.to_front(shas='PANNELLO_SEL')
            window.set_focus(KEY_QTA)
            window.visible(not window.is_visible(k=KEY_PANEL_SEL), shas='PANNELLO_SEL')
            clicked_data = values['_clicked_data']
    if event == KEY_BTN_CERCA:
        codice_articolo = values.get(KEY_INPUT_CODICE_ART)
        descrizione = values.get(KEY_INPUT_DESCRIZIONE)
        print(codice_articolo)
        filtro = [item for item in product if codice_articolo.lower() in item[0].lower()]
        if codice_articolo == '':
            filtro = product
        filtro = [item for item in filtro if descrizione.lower() in item[1].lower()]
        print(filtro)
        window.delete(k=KEY_TABELLA_PRODOTTI)
        (
            window.move_to(col1_x, col2_y + 150).set_text_size(20)
            .navtable('P R O D O T T I', conf=conf_tab_prodotti, data=filtro, nr_rows=5,
                      folder_images='./tableimages/img', k=KEY_TABELLA_PRODOTTI)

        )
    if event == KEY_BTN_CHIUDI_PANEL:
        window.set_focus(KEY_INPUT_CODICE_ART)
        window.visible(not window.is_visible(k=KEY_PANEL_SEL), shas='PANNELLO_SEL')
    if event == KEY_BTN_AGGIUNGI:
        qta = values.get(KEY_QTA)
        if qta == '':
            print('Errore inserire una quantita')
        else:
            window.set_focus(KEY_INPUT_CODICE_ART)
            window.visible(not window.is_visible(k=KEY_PANEL_SEL), shas='PANNELLO_SEL')
            aggiungi_carrello(clicked_data, qta)
window.close()
