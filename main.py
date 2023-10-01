import PySimpleGUI as sg

def gera_user():
    '''
    Gerar uma janela contendo o nome do usuário e um temporizador.
    Retorna uma janela com temporizador
    '''

    # CONFIGURAÇOES GERAIS
    sg.theme('DarkGray8') # definindo o tema geral


    # VARIÁVEIS DO PROGRAMA
    added_names=[] # aramazena os nomes que já foram adicionados
    counter_rows=0 # dá um ID único para cada usuário que for adicionado
    clickes=[] # armazena os nomes do que já tiveram seu nome removido

    
    # FUNÇÕES
    def gera_coluna(nome,num):
        '''
        função que gera a a coluna secundária com Timer e o botão para remover
        '''

        coluna2a=[
            [sg.Text(f'Nome: {nome}', 
                    size=(20,1),
                    justification='left',
                    key=str(num)+'name',
                    background_color='gray7')
                    ],
            [sg.Text('Tempo: 00:05',
                    size=(20,1),
                    justification='left', 
                    key=str(num)+'counter',
                    background_color='gray7')
                    ],
                    ]
        
        #parte 2 da coluna 2 (Botão de Excluir)
        coluna2b=[
            [sg.Button('X', size=(1,1),
                       key=str(num)+'Exit',
                       button_color='gray7')
                       ]
                       ]

        lo=[sg.Column(coluna2a,key=str(num),background_color='grey9'),
            sg.Column(coluna2b,key=str(num)+'button')] # layout de de saída (LayOut)

        return lo

    # COLUNA PRINCIPAL QUE ARAMZENA O NOME E O TIMER
    coluna1=[
        [sg.Text('Insira um nome:',
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

    # COLUNA VAZIA QUE RECEBERÁ OS NOMES COM TIMER GERADOS COM A FUNÇÃO GERA_COLUNA
    coluna2=[] 

    # COLUNAS AUXILIARES
    coluna_fillL=[[sg.Text('',background_color='gray10')]] # preenchimento para alinhamento esquerdo (Left)
    coluna_fillR=[[sg.Text('',background_color='gray10')]] # preenchimento para alinhamento direito (Right)


    layout=[[
        sg.Column(coluna_fillL,
                  expand_x=True,
                  background_color='gray10'),
        sg.Column(coluna1,
                background_color='gray5',
                element_justification='center'),
        sg.Column(coluna_fillR,
                  expand_x=True,
                  background_color='gray10'),
        sg.Column(coluna2,
                scrollable=True,
                vertical_scroll_only=True,
                background_color='gray5',
                key='Col2',
                element_justification='center',
                size=(220,300),
                )
    ]]

    window=sg.Window('Temporizador',
                     layout,
                     background_color='gray10',
                     element_justification='center',
                     size=(600,300))

    while True:
        event,values=window.read(timeout=1000)

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Add' and values['Input'] != '' and values['Input'] not in added_names:
            print(values['Input'])
            window.extend_layout(window['Col2'],[gera_coluna(values['Input'],counter_rows)])
            window['Input'].update('')
            window.refresh()
            window['Col2'].contents_changed()
            added_names.append(values['Input'])
            counter_rows+=1
        
        if 'Exit' in event:
            evento=str(event[:-4])                              # salva o numero do evento que foi realizado
            window[evento].update(visible=False)                # faz com que o nome referente ao evento fique invisivel
            window[evento].Widget.master.pack_forget()          # se livra do nome referente ao evento
            window[evento+'button'].update(visible=False)       # faz com que o botao referente ao evento fique invisivel
            window[evento+'button'].Widget.master.pack_forget() # se livra do botao referente ao evento
            window.refresh()    #recarrega a janela
            window['Col2'].contents_changed()   # recarrega os elementos modificados da coluna 2
            #added_names.remove(str(window[str(evento)+'name'].get())[6:])       #remove o nome da lista de nomes adicionados

        if event == '__TIMEOUT__':
            for i in range(counter_rows):
                try:
                    if window[str(i)+'counter'].get() == 'Tempo: 00:00':        # checa se o tempo zerou
                        nome=str(window[str(i)+'name'].get())[6:]               # salva o nome em uma variável
                        if nome not in clickes:                                 # checa se o botão de remover já foi clicado
                            window[str(i)+'Exit'].click()                       # realiza o clique o botão de exluir
                            clickes.append(nome)                                # registra o clique realizado
                            sg.Window(
                                "Aviso", 
                                [[sg.Text(f'Tempo de {nome} acabou!',size=(20,1))]],
                                element_justification='center',
                                ).finalize()
                    else:
                        tempo_restante=window[str(i)+'counter'].get()
                        tempo_restante=tempo_restante[-5:]
                        tempo_segundos=(int(tempo_restante[:2])*60)+(int((tempo_restante[3:])))
                        tempo_segundos-=1
                        window[str(i)+'counter'].update(f'Tempo: {(tempo_segundos//60):02}:{(tempo_segundos%60):02}')  
                except:
                    pass
            

    window.close()

if __name__ == '__main__':
    gera_user()