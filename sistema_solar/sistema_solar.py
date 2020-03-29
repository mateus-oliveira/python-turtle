# sistema_solar.py

from turtle import Turtle, Screen
from math import sqrt, sin, cos, pi

raio = 60

class Astro(Turtle):
    def __init__(self, nome, tamanho, cor):
        Turtle.__init__(self)
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor

class Estrela(Astro):
    def __init__(self, nome, tamanho, cor):
        Astro.__init__(self, nome, tamanho, cor)
        self.shape('circle')
        self.color(cor)
        self.shapesize(tamanho, tamanho)
        
class Planeta(Astro):
    def __init__(self, nome, tamanho, cor, posicao_orbita):
        Astro.__init__(self, nome, tamanho, cor)
        self.posicao_orbita = posicao_orbita
        self.shape('circle')
        self.color(cor)
        self.shapesize(tamanho, tamanho,0)
        self.pencolor('blue')
        self.pensize(1.5)
        self.speed('fastest')
        self.hideturtle()

    def translacao(self, angulo):
        global raio
        # Se for o planeta Plutão, sua órbita tem que ser uma elipse inclinada em relação ao Sol.
        if self.posicao_orbita == 9:
            angulo *= (10 - self.posicao_orbita)
            a = self.posicao_orbita * raio
            b = a/2        
            r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)            
            x = r*cos(pi*angulo/180)
            y = r*sin(pi*angulo/180)
            x1 = x*cos(30*180/pi) - y*sin(30*180/pi)
            y1 = x*sin(30*180/pi) + y*cos(30*180/pi)
            if angulo == 0:
                self.up()
                self.setpos(x1, y1)
                self.down()
                self.showturtle()  
            self.setpos(x1, y1)

        # Os outros planetas não têm uma órbita inclinada em relação ao Sol.
        else:
            angulo *= (10 - self.posicao_orbita)
            a = self.posicao_orbita * raio
            b = a/2        
            r = (a * b)/sqrt(a**2*sin(pi*angulo/180)**2 + b**2*cos(pi*angulo/180)**2)            
            x = r*cos(pi*angulo/180)
            y = r*sin(pi*angulo/180)
            if angulo == 0:
                self.up()
                self.setpos(x,y)
                self.down()
                self.showturtle()  
            self.setpos(x,y)

def main():
    tela = Screen()
    tela.setup(1200, 800, 0, 0)
    tela.bgcolor('black')
    tela.title('Sistema Solar')
    tela.tracer(2)

    sol = Estrela('Sol',2,'gold')

    mercurio = Planeta('Mercúrio', 0.3, 'gray', 1)
    venus = Planeta('Vênus', 0.5, 'darkorange', 2)
    terra = Planeta('Terra', 0.6, 'blue', 3)
    marte = Planeta('Marte', 0.4, 'red', 4)
    jupiter = Planeta('Júpiter', 1, 'sandybrown', 5)
    saturno = Planeta('Saturno', 0.9, 'goldenrod', 6)
    urano = Planeta('Urano', 0.8, 'mediumseagreen', 7)
    netuno = Planeta('Netuno', 0.7, 'steelblue', 8)
    plutao = Planeta('Plutão', 0.2, 'peachpuff', 9)

    i = 0
    while True:
        mercurio.translacao(i)
        venus.translacao(i)
        terra.translacao(i)
        marte.translacao(i)
        jupiter.translacao(i)
        saturno.translacao(i)
        urano.translacao(i)
        netuno.translacao(i)
        plutao.translacao(i)
        if i == 360:
            i = 0
        i += 1

if __name__ == '__main__':
    main()
