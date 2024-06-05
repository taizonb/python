import flet as ft
from flet import colors
from decimal import Decimal

#botões que serão usados na tela
botoes = [
        {'operador': 'AC', 'fonte' : colors.BLACK, 'fundo': colors.BLUE_GREY_100},
        {'operador': '#', 'fonte' : colors.BLACK, 'fundo': colors.BLUE_GREY_100},
        {'operador': '%', 'fonte' : colors.BLACK, 'fundo': colors.BLUE_GREY_100},
        {'operador': '/', 'fonte' : colors.WHITE, 'fundo': colors.ORANGE},
        {'operador': '7', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '8', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '9', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '*', 'fonte' : colors.WHITE, 'fundo': colors.ORANGE},
        {'operador': '4', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '5', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '6', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},       
        {'operador': '-', 'fonte' : colors.WHITE, 'fundo': colors.ORANGE},
        {'operador': '1', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '2', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '3', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': '+', 'fonte' : colors.WHITE, 'fundo': colors.ORANGE},
        {'operador': '0', 'fonte' : colors.WHITE, 'fundo': colors.WHITE24},
        {'operador': ',', 'fonte' : colors.WHITE, 'fundo': colors.ORANGE},
        {'operador': '=', 'fonte' : colors.WHITE, 'fundo': colors.ORANGE},
]

# Conteúdo da tela
def main(page: ft.Page):
        page.bgcolor = '#000'
        page.window_resizable = False
        page.window_width = 270
        page.window_height = 400
        page.title = 'Calculadora'
        page.window_always_on_top = True

        result = ft.Text(value = '0', color = colors.WHITE, size = 20)

        def calculate(operador, value_at):
                try:
                        value = eval(value_at) #faz o calculo aritmetico com strings

                        if operador == '%':
                                value /= 100
                        elif operador == '#':
                                value = -value
                except:

                        return 'Error'
                
                digits = min(abs(Decimal(value).as_tuple().exponent), 5)
                return format(value, f'.{digits}f')
                        

        def select(e):
                value_at = result.value if result.value not in ('0', 'Error') else ''
                value = e.control.content.value

                # Verifica o que foi digitado
                if value.isdigit():
                        value = value_at + value
                elif value == 'AC':
                        value = '0'
                else:
                        if value_at and value_at[-1] in ('/','*','-','+',','):  # verifica se apertou 2x um operador lógico
                                value_at = value_at[:-1]
                        
                        value = value_at + value

                        # Calcula o resultado da operação
                        if value[-1] in ('=','%','#'):
                                value = calculate(operador=value[-1], value_at=value_at)
                
                result.value = value
                result.update() # Atualiza a tela
 

        # Cria onde será mostrado o resultado
        display = ft.Row(
                width = 250, #tamanho do local do resultado
                controls = [result], # conteúdo
                alignment = 'end' # alinhamento
        )

        # Cria os botões
        btn = [ft.Container(
                content=ft.Text(value=btn['operador'], color=btn['fonte']), # pega da lista os valores e fonte
                width=50, #tamanho do botão
                height=50, #tamanho do botão
                bgcolor=btn['fundo'], #pega da lista a cor do fundo
                border_radius=100, 
                alignment=ft.alignment.center, #alinha o conteúdo do botão
                on_click=select # Diz o que fazer quando clica em algo                
        ) for btn in botoes]

        # Cria o padrão visual para os botões (em linhas)
        keyboard = ft.Row(
                width=270, #tamanho da linha
                wrap=True, #quebra os elementos quando acaba o espaço
                controls=btn, #pega os valores dos botões
                alignment='end' #alinha a direita
        )

        # Adiciona na tela os conteúdos
        page.add(display, keyboard)


# manda abrir a tela
ft.app(target = main)