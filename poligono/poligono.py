import turtle
tela = turtle.Screen()
cursor = turtle.Turtle()
cursor.shape('turtle')
pol = 1
while pol == 1:
    lados = int(tela.textinput('POLÍGONO', 'Quantidade de Lados:'))
    angulo_externo = 360/lados
    for i in range(lados):
        cursor.forward(30)
        cursor.left(angulo_externo)
    pol = int(tela.textinput('NOVO POLÍGONO', '1 - SIM\n2 - NÃO:'))
    cursor.clear()
    cursor.home()

tela.exitonclick()
