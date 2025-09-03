import runner, pyNaviGui as ng

window = ng.Ng()
(KEY_CLOSE, KEY_NAME, KEY_SURNAME, KEY_OPTIONS, KEY_BTN_LEGGI, KEY_SEX, KEY_MACHINE, KEY_TABELLA, KEY_FILTRI,
 KEY_BTN_FILTRI, KEY_FILTRO_NOME, KEY_FILTRO_ETA, KEY_BTN_APPLICA_FILTRO, KEY_BTN_CHIUDI_FILTRO, KEY_BTN_DELETE,
KEY_OPZIONI_FILTRI, KEY_SELEZIONI,
 *_) = window.set_keys()

# Funzione per generare i colori delle righe in base ai dati
def generate_row_colors(data):
    colors = []
    for i, r in enumerate(data):
        colsfondo = 'white'
        colcarattere = 'black'
        if r[2] > 40:
            colsfondo = 'yellow'
            colcarattere = 'red'
        colors.append([i, colsfondo, colcarattere])
    return colors

# General settings of the window
(window.win_title('Titolo della finestra').win_size('800x600').
 move_to(30, 80).set_row_height(20).set_input_size(30, 1).
 text('Name').br().
 input('', k=KEY_NAME).br().
 text('Surname').br().
 input('', k=KEY_SURNAME).br().
 checkboxes(('Male', 'Female', 'Other'), k=KEY_SEX).
 checkboxes(('Maserati|MAS', 'Ferrari|FERR', 'Lamborghini|LAMB', 'Fiat|FIAT'), k=KEY_MACHINE).br()
 )

# Table configuration
tableconf = {'NOME': ['Nome', 10], 'COGNOME': ['Cognome', 20], 'ANNI': ['Anni', 5]}
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
    ['Giuseppe', 'Moretti', 48],
    ['Marco', 'Bianchi', 39],
    ['Laura', 'Rossi', 44],
    ['Marco', 'Corsini', 49],
]

# Generate colors for the initial table
colors = generate_row_colors(tabledata)

# Create table and buttons
table_x = window.current_x
table_y = window.current_y

(window.
 table('Tabella anagrafica', conf=tableconf, data=tabledata, nr_rows=7, rowcolors=colors, k=KEY_TABELLA).
 button('Filtra', k=KEY_BTN_FILTRI).br().
 button('Cancella tabella', k=KEY_BTN_DELETE).br().
 button('Leggi', k=KEY_BTN_LEGGI).

 move_below(k=KEY_BTN_FILTRI).
 panel('Filtri di ricerca', geometry='300x200', s='FILTRI_TABELLA', visible=False,  bg='orange',    k=KEY_FILTRI).
 text('Nome').
 input('', k=KEY_FILTRO_NOME).br().
 text('Età maggiore di').
 input('', k=KEY_FILTRO_ETA).br().
checkboxes('Opzioni',('A','B','C'),k=KEY_OPZIONI_FILTRI).
radio('Seleziona',('Uno','Due','Tre','Quattro'),k=KEY_SELEZIONI).br().
 button('Applica', k=KEY_BTN_APPLICA_FILTRO).
 panel('')
 )

window.finalize_layout()

# Save a copy of the original data
original_tabledata = tabledata.copy()
filtered_data = None  # Track current filtered data

# Application loop
while True:
    event, values = window.read()

    if event == KEY_BTN_LEGGI:
        print(values)
        if KEY_TABELLA in values:
            selected = values[KEY_TABELLA]
            print(selected)
            current_data = filtered_data if filtered_data is not None else tabledata
            for x in selected:
                if 0 <= x < len(current_data):
                    print(current_data[x])
                else:
                    print(f"Invalid index: {x}")

    if event is None:
        print('Window closed')
        break

    if event == KEY_BTN_FILTRI:
        window.visible(not window.is_visible(k=KEY_FILTRI), shas='FILTRI_TABELLA')

    if event == KEY_BTN_DELETE:
        window.delete(k=KEY_TABELLA)
        print('Tabella cancellata')

    if event == KEY_BTN_APPLICA_FILTRO:
        print("Applicazione filtro iniziata")
        nome_filtro = values[KEY_FILTRO_NOME].lower() if KEY_FILTRO_NOME in values else ""
        eta_filtro = values[KEY_FILTRO_ETA] if KEY_FILTRO_ETA in values else ""

        print(f"Filtri: Nome='{nome_filtro}', Età>'{eta_filtro}'")

        # Filtro i dati
        filtered_data = []
        for row in original_tabledata:
            # Controllo nome (case insensitive)
            nome_match = True if not nome_filtro else nome_filtro in row[0].lower()

            # Controllo età
            eta_match = True
            if eta_filtro and eta_filtro.isdigit():
                eta_match = row[2] > int(eta_filtro)

            # Se entrambi i filtri sono soddisfatti, aggiungo la riga
            if nome_match and eta_match:
                filtered_data.append(row)

        filtered_colors = generate_row_colors(filtered_data)
        print(filtered_data, filtered_colors)
        window.update(k=KEY_TABELLA, data=filtered_data, rowcolors=filtered_colors)
        print(f"Filtro applicato: {len(filtered_data)} risultati trovati")

window.close()