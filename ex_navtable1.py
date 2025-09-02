import runner, pyNaviGui as ng, os

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_BTN_LEGGI, KEY_SEX, KEY_MACHINE, KEY_IMKMAGINE,
 KEY_BTN_AVANTI, KEY_BTN_INDIETRO,
 *_) = window.set_keys()

# Configurazione generale della finestra
window.winTitle('Tabella Navigabile').winGeometry('800x800')

# Input iniziali
(window.gotoxy(30, 80).setRowHeigh(20).setInputSize(30, 1).
 text('Name').crlf().
 input('', k=KEY_NAME).crlf().
 text('Surname').crlf().
 input('', k=KEY_SURNAME).crlf()
 )

# Configurazione tabella
tableconf = {'NOME': ['Nome', 10], 'COGNOME': ['Cognome', 20], 'ANNI': ['Anni', 5]}
tabledata = [
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

# Variabili per la paginazione
RIGHE_PER_PAGINA = 7
pagina_corrente = 0
totale_pagine = (len(tabledata) + RIGHE_PER_PAGINA - 1) // RIGHE_PER_PAGINA


def visualizza_pagina(pagina):
    """Aggiorna il contenuto degli elementi esistenti per mostrare la pagina richiesta"""
    # Calcola gli indici di inizio e fine per questa pagina
    inizio = pagina * RIGHE_PER_PAGINA
    fine = min(inizio + RIGHE_PER_PAGINA, len(tabledata))

    # Aggiorna il contenuto degli elementi esistenti
    for i in range(RIGHE_PER_PAGINA):
        riga_dati_index = inizio + i

        if riga_dati_index < len(tabledata):
            # Questa riga ha dati da mostrare
            window.visible(True, shas=f'riga_{i}')

            # Aggiorna l'immagine
            image_key = f'IMG_ROW_{i}'
            if image_key in window.element_keys:
                image_element = window.element_keys[image_key]

                # Carica la nuova immagine
                image_filename = tabledata[riga_dati_index][3]
                new_image_path = f'./tableimages/img/{image_filename}'

                try:
                    if os.path.exists(new_image_path):
                        # Carica e ridimensiona la nuova immagine
                        from PIL import Image, ImageTk
                        pil_image = Image.open(new_image_path)
                        pil_image = pil_image.resize((50, 50), Image.Resampling.LANCZOS)
                        new_photo = ImageTk.PhotoImage(pil_image)

                        # Aggiorna l'immagine nell'elemento
                        image_element.config(image=new_photo)
                        image_element.image = new_photo  # Mantieni riferimento
                    else:
                        # Crea placeholder se il file non esiste
                        placeholder_image = Image.new('RGB', (50, 50), color='lightgray')
                        try:
                            from PIL import ImageDraw
                            draw = ImageDraw.Draw(placeholder_image)
                            draw.line([(0, 0), (49, 49)], fill='gray', width=2)
                            draw.line([(0, 49), (49, 0)], fill='gray', width=2)
                            draw.rectangle([(0, 0), (49, 49)], outline='gray', width=1)
                        except ImportError:
                            pass

                        placeholder_photo = ImageTk.PhotoImage(placeholder_image)
                        image_element.config(image=placeholder_photo)
                        image_element.image = placeholder_photo

                except Exception as e:
                    print(f"Errore caricamento immagine {new_image_path}: {e}")

            # Metodo più diretto: trova tutti i testi di questa riga e aggiornali in sequenza
            elementi_riga = []
            for element_key, element in window.element_keys.items():
                if f'riga_{i}' in window.element_strings.get(element_key, ''):
                    if hasattr(element, 'config') and not element_key.startswith('IMG_'):
                        elementi_riga.append(element)

            # Aggiorna i testi in ordine (solo le prime 3 colonne: nome, cognome, età)
            keylist = list(tableconf.keys())
            for j, element in enumerate(elementi_riga):
                if j < len(keylist) and j < len(tabledata[riga_dati_index]) - 1:  # -1 per escludere il nome file
                    element.config(text=str(tabledata[riga_dati_index][j]))
        else:
            # Questa riga non ha dati, nascondila
            window.visible(False, shas=f'riga_{i}')

    print(f"Pagina {pagina + 1}/{totale_pagine} - Righe {inizio + 1} a {fine}")


def crea_tabella():
    """Crea solo gli elementi visibili della prima pagina"""
    window.setTextSize(20)

    # Salva la posizione iniziale
    pos_x_iniziale = window.current_x
    pos_y_iniziale = window.current_y

    # Crea solo le prime 7 righe (o meno se i dati sono meno)
    righe_da_creare = min(RIGHE_PER_PAGINA, len(tabledata))

    for i in range(righe_da_creare):
        # Posiziona all'inizio della riga
        riga_y = pos_y_iniziale + i * 60  # 60 pixel tra le righe
        window.gotoxy(pos_x_iniziale, riga_y)

        # Immagine specifica per questa riga (se esiste il file, altrimenti usa placeholder)
        image_filename = tabledata[i][3]  # Nome file dalla quarta colonna
        image_path = f'./tableimages/img/{image_filename}'
        if not os.path.exists(image_path):
            image_path = ''  # Usa placeholder se il file non esiste

        window.image(image_path, size='50x50', k=f'IMG_ROW_{i}', s=f'riga_{i}')

        # Dati della riga (prendi dalla pagina corrente)
        keylist = list(tableconf.keys())
        for j, key in enumerate(keylist):
            text_size = tableconf[key][1]
            window.setTextSize(text_size).text(tabledata[i][j], s=f'riga_{i}')


# Crea la tabella
crea_tabella()

# Bottoni di navigazione e altre funzioni
(window.crlf().button('  <<  ', k=KEY_BTN_INDIETRO).button('  >>  ', k=KEY_BTN_AVANTI).
setTextSize(50).text(f' Pagina 1/{totale_pagine}', k='lbl_pagina').crlf().
 button('Leggi', k=KEY_BTN_LEGGI).crlf()
 )

window.finalize_layout()


def aggiorna_label_pagina():
    """Aggiorna il testo della label della pagina"""
    # Trova e aggiorna il testo della label
    for key, element in window.element_keys.items():
        if key == 'lbl_pagina':
            element.config(text=f' Pagina {pagina_corrente + 1}/{totale_pagine}')
            break


while True:
    event, values = window.read()

    if event == KEY_BTN_INDIETRO:
        if pagina_corrente > 0:
            pagina_corrente -= 1
            visualizza_pagina(pagina_corrente)
            aggiorna_label_pagina()

    elif event == KEY_BTN_AVANTI:
        if pagina_corrente < totale_pagine - 1:
            pagina_corrente += 1
            visualizza_pagina(pagina_corrente)
            aggiorna_label_pagina()

    elif event.startswith('IMG_ROW_'):
        # Gestisce il click su un'immagine
        riga_clicked = int(event.split('_')[-1])
        riga_effettiva = pagina_corrente * RIGHE_PER_PAGINA + riga_clicked
        if riga_effettiva < len(tabledata):
            print(f'Immagine cliccata! Riga {riga_effettiva + 1}: {tabledata[riga_effettiva]}')

    elif event == KEY_BTN_LEGGI:
        print("Valori correnti:", values)
        print(f"Pagina corrente: {pagina_corrente + 1}/{totale_pagine}")

    elif event is None:
        print('Finestra chiusa')
        break

window.close()