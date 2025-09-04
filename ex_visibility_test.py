import pyNaviGui as ng

win = ng.Ng()

(win.win_title('Test di visibilita').win_size('300x300').
 text('Testo 1',k='testo1'). button('visibile/invisibile',k='btnVisTesto1').br().
 input('Input 1',k='input1'). button('visibile/invisibile',k='btnVisInput1').
 finalize_layout()
 )

while True:
    event, values = win.read()
    if event == None:
        break

    if event == 'btnVisTesto1':
        print('='*40)
        sw_visibile = win.is_visible(k='testo1')
        print('testo1 visibile = ', sw_visibile)
        win.visible(not sw_visibile, k='testo1' )
        sw_visibile = win.is_visible(k='testo1')
        print('dopo il cambio di stato risulta visibile = ', sw_visibile )

    if event == 'btnVisInput1':
        print('=' * 40)
        sw_visibile = win.is_visible(k='input1')
        print('input1 visibile = ', sw_visibile)
        win.visible(not sw_visibile, k='input1' )
        sw_visibile = win.is_visible(k='input1')
        print('dopo il cambio di stato risulta visibile = ', sw_visibile )

win.close()

