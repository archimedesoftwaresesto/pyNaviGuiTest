import runner, pyNaviGui as ng

# Create window
window = ng.Ng(geometry='400x300')

# Sample data for combobox
options = ['Opzione 1|val1', 'Opzione 2|val2', 'Opzione 3|val3', 'Opzione 4|val4']

# Create combobox with change event
window.text('Seleziona un\'opzione:').br()
window.combobox('Combo con eventi:', options, k='my_combo', default='val2', event_change=True).br(10)

# Display area for events
window.text('Eventi ricevuti:').br()
window.multiline('', k='events_log', nr_rows=8, nr_cols=40)

# Event loop
while True:
    event, values = window.read()

    if event is None:  # Window closed
        break

    if event == 'my_combo':
        # Change event triggered
        selected_value = values.get('my_combo', '')
        log_text = values.get('events_log', '')
        new_log = f"{log_text}Selezione cambiata: {selected_value}\n"

        # Update log display
        window.update(k='events_log', text=new_log)

        print(f"Combobox changed to: {selected_value}")

window.close()