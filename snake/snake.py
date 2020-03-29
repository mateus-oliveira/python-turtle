from turtle import *
from random import randint
from math import sqrt, pow

velocidade = 3
pontuacao = 0

# Criando a janela.
tela = Screen()
tela.setup(688,688, 688/2,3)
tela.title('Jogo da Cobrinha')
tela.bgcolor('black')

# Desenhando área do jogo.
caneta = Turtle()
caneta.speed('fastest')
caneta.color('white')

caneta.up()
caneta.setposition(-300,-300)
caneta.down()
caneta.pensize(3)
for i in range(4):
    caneta.fd(600)
    caneta.left(90)
caneta.hideturtle()
caneta.up()
caneta.setposition(-290,310)
caneta.write('Pontuação: 0', False, align='left', font=('Times', 14, 'normal'))

# Criando a turtle/vetor cobra.
cobra = []
cobra[0:0] = [Turtle()]
cobra[0].speed('fastest')
cobra[0].shape('square')
cobra[0].color('red')
cobra[0].shapesize(0.5,0.5)
cobra[0].up()

# Criando a turtle comida.
comida = Turtle()
comida.speed('fastest')
comida.color('white')
comida.shape('square')
comida.shapesize(0.5,0.5)
comida.up()
comida.setposition(randint(-293, 293),randint(-293, 293))

# Funções!
#   Ir para a esquerda.
def esquerda():
    if cobra[0].heading() != 0:
        cobra[0].setheading(180)

#   Ir para a direita.
def direita():
    if cobra[0].heading() != 180:
        cobra[0].setheading(0)

#   Ir para cima.
def cima():
    if cobra[0].heading() != 270:
        cobra[0].setheading(90)

#   Ir para baixo.
def baixo():
    if cobra[0].heading() != 90:
        cobra[0].setheading(270)

#   Colidir com a parede.
def colisao_parede(t1,t2):
    dist = sqrt(pow(t1.xcor()-t2.xcor(),2) + pow(t1.ycor()-t2.ycor(),2))
    if dist <= 10:
        return True
    else:
        return False

#   Colidir com o prórpio corpo.
def colisao_corpo(t1,t2):
    dist = sqrt(pow(t1.xcor()-t2.xcor(),2) + pow(t1.ycor()-t2.ycor(),2))
    if dist < 4:
        return True
    else:
        return False

#  Aumentar velocidade de movimento de cobra[]. 
def acelerar():
    global velocidade
    if velocidade < 100:
        velocidade += 0.5

#  Diminuir velocidade de movimento de cobra[]. 
def frear():
    global velocidade
    if velocidade > 0:
        velocidade -= 1
    
# Eventos do teclado.    
tela.listen()
tela.onkey(esquerda, 'Left')
tela.onkey(direita, 'Right')
tela.onkey(cima, 'Up')
tela.onkey(baixo, 'Down')
tela.onkey(acelerar, 'a')
tela.onkey(frear, 's')


while velocidade != 0:
    #Movimentação do vetor cobra
    pos=0
    x, y = cobra[0].position()
    cobra[0].forward(velocidade)
    posx, posy = x, y
    for python in cobra[1::]:
        x,y = python.position()
        python.setpos(posx,posy)
        posx, posy = x, y
        if colisao_corpo(cobra[0],python) and pos>0:
            velocidade=0
            
        pos+=1
    # Área do jogo, caso o vetor cobra toque o limite, o programa para. 
    if cobra[0].xcor() > 293 or cobra[0].xcor() < -293:
        break
    if cobra[0].ycor() > 293 or cobra[0].ycor() < -293:
        break

    # Colisão do vetor cobra com a variável comida.
    if colisao_parede(cobra[0], comida):
        comida.setposition(randint(-293, 293),randint(-293, 293))
        cobra[-1:-1] = [cobra[0].clone()]
        cobra[-1].setposition(x,y)
        pontuacao += 1
        if velocidade < 100:
            velocidade += 0.5
        
        # Pontuação
        caneta.undo()
        caneta.hideturtle()
        pontos = 'Pontuação: %s' %pontuacao
        caneta.write(pontos, False, align='left', font=('Times', 14, 'normal'))

# Sair
caneta.up()
caneta.setposition(0,0)
mensagem = '        Você perdeu!\n    Sua pontuação é %d.\nClique (AQUI) para sair...' %pontuacao
caneta.write(mensagem, False, align='center', font=('Times', 14, 'normal'))
tela.exitonclick()
