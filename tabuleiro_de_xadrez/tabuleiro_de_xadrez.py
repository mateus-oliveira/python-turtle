import turtle
pincel = turtle.Pen()

tela = turtle.Screen()
tela.title('Tabuleiro de Xadrez')

tela.register_shape('casa_negra', ((-25, -25), (-25, 25), (25, 25), (25, -25), (-25,-25)))

tela.setup(600, 600)

linhas = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
}

colunas = {
    1: '8',
    2: '7',
    3: '6',
    4: '5',
    5: '4',
    6: '3',
    7: '2',
    8: '1',
}
    
def desenhar_linhas(x1, y1, x2, y2):
    pincel.up()
    pincel.setpos(x1, y1)
    pincel.down()
    pincel.setpos(x2, y2)
    
for k in range(8+1):
    x = -200 + k*50
    y = 200 - k*50
    desenhar_linhas(-200, y, 200, y)
    desenhar_linhas(x, 200, x, -200)

pincel.up()

def preencher_casas():
    pincel.shape('casa_negra')
    for linha in range(1, 9):
        y = 200 - (linha - 1) * 50
        for coluna in range(1, 9):
            x = -200 + (coluna - 1) * 50
            pincel.goto(x + 25, y - 25)
            
            if linha % 2 == 0 and coluna % 2 != 0:
                pincel.stamp()

            if linha % 2 != 0 and coluna % 2 == 0:
                pincel.stamp()

preencher_casas()
pincel.hideturtle()


def exibir_posicao(x, y):
    print('({}, {})'.format(x, y))
    
    i = ((200-y)//50)+1
    j = ((x+200)//50)+1
    
    print('casa: {}{}'.format(linhas[int(i)], colunas[int(j)]))

    pincel.goto(x, y)

    return
    
tela.listen()
tela.onclick(exibir_posicao)