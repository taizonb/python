import flet as ft
from flet import colors

#botões que serão usados na tela
botoes = [
        {'operador': 'AC', 'fonte' : colors.BLACK, 'fundo': colors.BLUE_GREY_100},
        {'operador': '+-', 'fonte' : colors.BLACK, 'fundo': colors.BLUE_GREY_100},
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
        page.window_height = 380
        page.title = 'Calculadora'
        page.window_always_on_top = True

        result = ft.Text(value = '0', color = colors.WHITE, size = 20)

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
                alignment=ft.alignment.center #alinha o conteúdo do botão
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