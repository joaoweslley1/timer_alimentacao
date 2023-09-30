from tkinter import Scrollbar
import PySimpleGUI as sg

def gera_user():
    '''
    Gerar uma janela contendo o nome do usuário e um temporizador.
    Retorna uma janela com temporizador
    '''
    added_names=[]

    def gera_linha(nome,pos):
        return sg.Text(str(nome),size=(25,1),key=str(pos),background_color='gray5')

    coluna0=[sg.Text('',size=(50,1),background_color='gray5')]

    coluna1=[
        [sg.Text('Insira um nome:',
                 #size=(20,1), #alterar para ficar dinamico
                 key='Texto1',
                 background_color='gray5',
                 text_color='white',
                 justification='center',
                 font=('Calibri',15))],
        [sg.Input(default_text='',size=(25,1),key='Input')],
        [sg.Button('Adicionar',
                   size=(20,1),
                   key='Add',
                   button_color='gray1')]
    ]

    coluna2=[]

    layout=[[sg.Column(coluna1,
                  background_color='gray5',
                  element_justification='center',
                  ),
        sg.Column(coluna2,
                  scrollable=True,
                  vertical_scroll_only=True,
                  background_color='gray5',
                  key='Col2',
                  size=(200,300),
                  ),
    ]]

    window=sg.Window('Janela',
                     layout,
                     #size=(400,300),
                     background_color='gray10',
                     element_justification='center')
    
    
    counter_rows=1

    while True:
        event,values=window.read(timeout=1000)

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Add' and values['Input'] != '' and values['Input'] not in added_names:
            window.extend_layout(window['Col2'],[[gera_linha(values['Input'],counter_rows)]])
            window['Input'].update('')
            window.refresh()
            window['Col2'].contents_changed()
            added_names.append(values['Input'])
            counter_rows+=1
    window.close()

if __name__ == '__main__':
    gera_user()
