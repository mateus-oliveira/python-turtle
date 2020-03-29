import os
import turtle
import pygame


class Piano:
    
    def __init__(self, teclas:dict):
        self.teclas = teclas
        self.notas = ('C', 'D', 'E', 'F', 'G', 'A', 'B',
                      'C#', 'D#', 'F#', 'G#', 'A#',
                      'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1',
                      'C#1', 'D#1', 'F#1', 'G#1', 'A#1')

    def desenhar_piano(self):
        x, y = -350.0, -125.0
        for nota in self.notas:
            if nota in 'CDEFGABC1D1E1F1G1A1B1':
                self.teclas[nota].desenhar_tecla(x, y)
                x += 50

        x, y = (-350 + 100/3), 0.0
        for nota in self.notas:
            if nota in ('C#', 'D#', 'F#', 'G#', 'A#',
                        'C#1', 'D#1', 'F#1', 'G#1', 'A#1'):
                self.teclas[nota].desenhar_tecla(x, y)

                if nota in 'D#D#1A#A#1': x += 100
                else: x += 50

    def tocar_nota_do(self): self.teclas['C'].tocar_tecla()
    def tocar_nota_re(self): self.teclas['D'].tocar_tecla()
    def tocar_nota_mi(self): self.teclas['E'].tocar_tecla()
    def tocar_nota_fa(self): self.teclas['F'].tocar_tecla()
    def tocar_nota_sol(self): self.teclas['G'].tocar_tecla()
    def tocar_nota_la(self): self.teclas['A'].tocar_tecla()
    def tocar_nota_si(self): self.teclas['B'].tocar_tecla()
    
    def tocar_nota_do1(self): self.teclas['C1'].tocar_tecla()
    def tocar_nota_re1(self): self.teclas['D1'].tocar_tecla()
    def tocar_nota_mi1(self): self.teclas['E1'].tocar_tecla()
    def tocar_nota_fa1(self): self.teclas['F1'].tocar_tecla()
    def tocar_nota_sol1(self): self.teclas['G1'].tocar_tecla()
    def tocar_nota_la1(self): self.teclas['A1'].tocar_tecla()
    def tocar_nota_si1(self): self.teclas['B1'].tocar_tecla()
    
    def tocar_nota_doS(self): self.teclas['C#'].tocar_tecla()
    def tocar_nota_reS(self): self.teclas['D#'].tocar_tecla()
    def tocar_nota_faS(self): self.teclas['F#'].tocar_tecla()
    def tocar_nota_solS(self): self.teclas['G#'].tocar_tecla()
    def tocar_nota_laS(self): self.teclas['A#'].tocar_tecla()
    
    def tocar_nota_doS1(self): self.teclas['C#1'].tocar_tecla()
    def tocar_nota_reS1(self): self.teclas['D#1'].tocar_tecla()
    def tocar_nota_faS1(self): self.teclas['F#1'].tocar_tecla()
    def tocar_nota_solS1(self): self.teclas['G#1'].tocar_tecla()
    def tocar_nota_laS1(self): self.teclas['A#1'].tocar_tecla()
        
    

class Tecla:
    
    def __init__(self, nota:str, caractere:str):
        self._desenho = turtle.Turtle()
        self._desenho.speed('fastest')
        self._desenho.color('black', 'white')
        self._desenho.hideturtle()
        self.nota = nota
        self.caractere = caractere

        if self.nota in 'CFC1F1': self._desenho.shape('cf')
        elif self.nota in 'DGAD1G1A1': self._desenho.shape('dga')
        elif self.nota in 'EBE1B1': self._desenho.shape('eb')
        else:
            self._desenho.color('black')
            self._desenho.shape('#')

    def desenhar_tecla(self, x:float, y:float):
        self._desenho.left(90)
        if self.nota in 'CFC1F1DGAD1G1A1EBE1B1':
            x1 = x + 25
            y1 = y - 20
        else:
            x1 = x + 50/3
            y1 = y + 130
                       

        self._desenho.up()
        self._desenho.setposition(x1, y1)
        self._desenho.down
        self._desenho.write(self.caractere,
                            False,
                            align='center',
                            font=('Times', 10, 'normal'))

        self._desenho.up()
        self._desenho.setposition(x, y)
        self._desenho.down
        self._desenho.showturtle()
        

    def tocar_tecla(self):
        
        self._desenho.speed(0)
        self._desenho.color('grey')
        self._desenho.color('grey')
        self._desenho.color('grey')

        pygame.mixer.music.stop()
        pygame.mixer.music.load('./sounds/{}.wav'.format(self.nota))
        pygame.mixer.music.play()
        
        if self.nota in 'CFC1F1DGAD1G1A1EBE1B1':
            self._desenho.color('black', 'white')
            self._desenho.speed('fastest')
        else:
            self._desenho.color('black')
            self._desenho.speed('fastest')
            

def main():
    try:
        pygame.init()
        tela = turtle.Screen()
        tela.title('Piano')
        tela.tracer(10)
        tela.setup(800, 350)
        tela.register_shape('cf', ( (0, 0),
                                    (50, 0),
                                    (50, 125),
                                    (2*(50/3), 125),
                                    (2*(50/3), 250),
                                    (0, 250)  ))
        
        tela.register_shape('dga', ((0, 0),
                                    (50, 0),
                                    (50, 125),
                                    (2*(50/3), 125),
                                    (2*(50/3), 250),
                                    ((50/3), 250),
                                    ((50/3), 125),
                                    (0, 125)  ))

        tela.register_shape('eb', ( (0, 0),
                                    (50, 0),
                                    (50, 250),
                                    ((50/3), 250),
                                    ((50/3), 125),
                                    (0, 125)  ))

        tela.register_shape('#', ( (0, 0),
                                   (2*(50/3), 0),
                                   (2*(50/3), 125),
                                   (0, 125)  ))
        
        
        teclas = {'C': Tecla('C', 'Z'),
                  'D': Tecla('D', 'X'),
                  'E': Tecla('E', 'C'),
                  'F': Tecla('F', 'V'),
                  'G': Tecla('G', 'B'),
                  'A': Tecla('A', 'N'),
                  'B': Tecla('B', 'M'),
                  'C#': Tecla('C#', 'S'),
                  'D#': Tecla('D#', 'D'),
                  'F#': Tecla('F#', 'G'),
                  'G#': Tecla('G#', 'H'),
                  'A#': Tecla('A#', 'J'),
                  'C1': Tecla('C1', 'Q'),
                  'D1': Tecla('D1', 'W'),
                  'E1': Tecla('E1', 'E'),
                  'F1': Tecla('F1', 'R'),
                  'G1': Tecla('G1', 'T'),
                  'A1': Tecla('A1', 'Y'),
                  'B1': Tecla('B1', 'U'),
                  'C#1': Tecla('C#1', '2'),
                  'D#1': Tecla('D#1', '3'),
                  'F#1': Tecla('F#1', '5'),
                  'G#1': Tecla('G#1', '6'),
                  'A#1': Tecla('A#1', '7'),}
                  
        piano = Piano(teclas)
        piano.desenhar_piano()

        tela.tracer(1)
        
        tela.onkey(piano.tocar_nota_do, 'z')
        tela.onkey(piano.tocar_nota_re, 'x')
        tela.onkey(piano.tocar_nota_mi, 'c')
        tela.onkey(piano.tocar_nota_fa, 'v')
        tela.onkey(piano.tocar_nota_sol, 'b')
        tela.onkey(piano.tocar_nota_la, 'n')
        tela.onkey(piano.tocar_nota_si, 'm')
        
        tela.onkey(piano.tocar_nota_do1, 'q')
        tela.onkey(piano.tocar_nota_re1, 'w')
        tela.onkey(piano.tocar_nota_mi1, 'e')
        tela.onkey(piano.tocar_nota_fa1, 'r')
        tela.onkey(piano.tocar_nota_sol1, 't')
        tela.onkey(piano.tocar_nota_la1, 'y')
        tela.onkey(piano.tocar_nota_si1, 'u')

        tela.onkey(piano.tocar_nota_doS, 's')
        tela.onkey(piano.tocar_nota_reS, 'd')
        tela.onkey(piano.tocar_nota_faS, 'g')
        tela.onkey(piano.tocar_nota_solS, 'h')
        tela.onkey(piano.tocar_nota_laS, 'j')

        tela.onkey(piano.tocar_nota_doS1, '2')
        tela.onkey(piano.tocar_nota_reS1, '3')
        tela.onkey(piano.tocar_nota_faS1, '5')
        tela.onkey(piano.tocar_nota_solS1, '6')
        tela.onkey(piano.tocar_nota_laS1, '7')
        
        tela.listen()
                                    
    except: pass


if __name__ == '__main__':
    main()
