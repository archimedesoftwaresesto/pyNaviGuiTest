import runner,  pyNaviGui as ng

window = ng.Ng()
(KEY_TABLENAV_PERSONE, KEY_TABLENAV2_PRODOTTI, KEY_TABLENAV_PRODOTTI_IDEM, KEY_BTN_LEGGI, KEY_BTN_RICREA, *_) = window.set_keys()

# Configurazione della finestra
window.win_title('Demo Tabelle Navigabili').win_size('1200x800')

# Prima tabella navigabile - CONVENZIONE: ultima colonna = nome immagine
tableconf1 = {'NOME': ['Nome', 10], 'COGNOME': ['Cognome', 20], 'ANNI': ['Anni', 5]}
tabledata1 = [
    # [NOME, COGNOME, ANNI, NOME_IMMAGINE] <- SEMPRE ultima colonna per l'immagine
    ['Dario', 'Giacomelli', 50, '012 04.jpg'],
    ['Marco', 'Rossi', 35, '034G 06.jpg'],
    ['Laura', 'Bianchi', 42, '034M 10.jpg'],
    ['Andrea', 'Ferrari', 28, '034P 24.jpg'],
    ['Giulia', 'Romano', 33, 'giulia.png'],
    ['Federica', 'Fontana', 34, 'federica.png'],
    ['Roberto', 'Martini', 41, 'roberto.png'],
    ['Simona', 'Greco', 38, 'simona.png'],
    ['Alessandro', 'Costa', 30, 'alessandro.png'],
    ['Elena', 'Giordano', 27, 'elena.png'],
    ['Stefano', 'Mancini', 46, 'stefano.png'],
    ['Paola', 'Lombardi', 32, '038 04.jpg'],
    ['Giuseppe', 'Moretti', 48, 'giuseppe.png'],
    ['Luca', 'Costa', 30, 'luca.png'],
    ['Actarus', 'Giordano', 27, 'actarus.png'],
    ['Goldrake', 'Mancini', 46, '041 10.jpg'],
    ['Luke', 'Lombardi', 32, 'luke.png'],
    ['Geeg', 'Moretti', 48, '038 08.jpg']
]

# Seconda tabella navigabile - CONVENZIONE: ultima colonna = nome immagine
tableconf2 = {'CODICE': ['Codice', 8], 'DESCRIZIONE': ['Descrizione', 25], 'PREZZO': ['Prezzo', 8]}
tabledata2 = [
    # [CODICE, DESCRIZIONE, PREZZO, NOME_IMMAGINE] <- SEMPRE ultima colonna per l'immagine
    ['A001', 'Smartphone Samsung Galaxy', '599.99', 'phone1.jpg'],
    ['A002', 'Laptop Dell Inspiron', '899.99', '012 04.jpg'],
    ['A003', 'Tablet iPad Pro', '1099.99', 'tablet1.jpg'],
    ['A004', 'Monitor LG UltraWide', '449.99', 'monitor1.jpg'],
    ['A005', 'Tastiera Meccanica', '129.99', '012 04.jpg'],
    ['A006', 'Mouse Wireless Logitech', '79.99', 'mouse1.jpg'],
    ['A007', 'Webcam HD Logitech', '89.99', 'webcam1.jpg'],
    ['A008', 'Cuffie Sony Noise Cancelling', '299.99', 'headphones1.jpg'],
]

(window.move_to(30, 50).navtable('Persone', conf=tableconf1, data=tabledata1, nr_rows=5, alternate_rowcolor='#CCCCCC',
                                folder_images='./tableimages/img', size_img='25x25',    vnavgap=20,     k=KEY_TABLENAV_PERSONE).
 move_to(20, 400).navtable('Prodotti', conf=tableconf2, data=tabledata2, nr_rows=3, size_img='40x40',   vgap=30,
alternate_rowcolor='#CCCCCC',
                folder_images='./tableimages/img', k=KEY_TABLENAV_PRODOTTI_IDEM)
 )

# Bottone per leggere i valori
window.move_to(900, 550).button('Rileggi i prodotti',k=KEY_BTN_RICREA).button('Leggi Valori', k=KEY_BTN_LEGGI)

window.finalize_layout()

while True:
    event, values = window.read()

    if event == KEY_BTN_LEGGI:
        print("=== VALORI CORRENTI ===")
        if KEY_TABLENAV_PERSONE in values:
            tab1 = values[KEY_TABLENAV_PERSONE]
            print(f"Tabella Persone - Pagina {tab1['pagina_corrente'] + 1}/{tab1['totale_pagine']}")
            print("Dati pagina corrente:", tab1['dati_pagina_corrente'])

        if KEY_TABLENAV2_PRODOTTI in values:
            tab2 = values[KEY_TABLENAV2_PRODOTTI]
            print(f"Tabella Prodotti - Pagina {tab2['pagina_corrente'] + 1}/{tab2['totale_pagine']}")
            print("Dati pagina corrente:", tab2['dati_pagina_corrente'])

    elif event and event.endswith('_IMG_ROW_0') or event.endswith('_IMG_ROW_1') or event.endswith(
            '_IMG_ROW_2') or event.endswith('_IMG_ROW_3') or event.endswith('_IMG_ROW_4') or event.endswith(
            '_IMG_ROW_5'):
        # Gestione click su immagini
        if '_clicked_data' in values and values['_clicked_data']:
            clicked_row = values['_clicked_row']
            clicked_data = values['_clicked_data']
            print(f"Cliccato sulla riga {clicked_row + 1}: {clicked_data}")

        # Determina quale tabella è stata cliccata
        if KEY_TABLENAV_PERSONE in event:
            print("Click sulla tabella Persone")
        elif KEY_TABLENAV2_PRODOTTI in event:
            print("Click sulla tabella Prodotti")

    elif event == KEY_BTN_RICREA:
        #if window.exists(k=KEY_TABLENAV2_PRODOTTI):
        #    window.delete(k=KEY_TABLENAV2_PRODOTTI)
        window.delete(k=KEY_TABLENAV2_PRODOTTI)
        window.move_to(600, 50).navtable('Prodotti', conf=tableconf2, data=tabledata2, nr_rows=6,
                                        alternate_rowcolor='#CCCCCC',
                                 folder_images='./tableimages/img', size_img='50x50', k=KEY_TABLENAV2_PRODOTTI)


    elif event is None:
        print('Finestra chiusa')
        break




window.close()