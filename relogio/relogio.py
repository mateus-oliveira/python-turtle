from turtle import Turtle, Screen, time

class Ponteiro:
    
    def __init__(self, nome:str):
        self._nome = nome
        self._desenho = Turtle()
        self._desenho.speed('fastest')
        self._desenho.color("white")
        self._desenho.setheading(90)
        self._definir_forma()
        self._eixo_de_giro = 0

    def _definir_forma(self):
        if self._nome == "segundos":
            tela.register_shape(self._nome, ((-2, 0),
                                             (-2, 235),
                                             (2, 235),
                                             (2, 0)) )
            self._desenho.color('red')
            self._desenho.shape(self._nome)

        elif self._nome == "minutos":
            tela.register_shape(self._nome, ((-2, 0),
                                             (-2, 235),
                                             (2, 235),
                                             (2, 0)) )
            self._desenho.shape(self._nome)

        elif self._nome == "horas":
            tela.register_shape(self._nome, ((-2, 0),
                                             (-2, 150),
                                             (2, 150),
                                             (2, 0)) )
            self._desenho.shape(self._nome)        

    def girar(self, angulo:float):
        self._desenho.circle(self._eixo_de_giro,
                             angulo*(-1) )

        tela.update()


class Relogio:
    
    def __init__(self, ponteiros:tuple):
        
        self._desenho = Turtle()
        
        self._hora_digital = Turtle()
        self._hora_digital.hideturtle()
        self._hora_digital.color('white')
        self._hora_digital.up()
        self._hora_digital.goto(0,-180)
        
        self._ponteiros = ponteiros

    def desenhar_numeros(self):
        self._desenho.speed('fastest')
        self._desenho.color("white")
        self._desenho.up()
        self._desenho.goto(0, 240)
        self._desenho.down()
        self._desenho.circle(-240)
        self._desenho.hideturtle()

        self._desenho.up()
        self._desenho.goto(0, 260)
        
        digito_hora = 1
        for i in range(1, 360+1):
            
            self._desenho.circle(-270, 1)
            
            if i % 30 == 0:
                self._desenho.write(digito_hora,
                                    False,
                                    "center",
                                    ('Arial', 15, 'normal'))
                digito_hora += 1

            elif i % 6 == 0:
                self._desenho.write(".",
                                    False,
                                    "center",
                                    ('Arial', 30, 'normal'))
        
        self._desenho.goto(0, 300)
        self._desenho.down()
        self._desenho.circle(-300)

    def exibir_hora(self, digital:bool=False):
        
        self._exibir_hora_atual()

        hours = time.localtime().tm_hour
        minutes = time.localtime().tm_min
        seconds = time.localtime().tm_sec

        doze_minutos = minutes % 12
            
        while True:            
               
            for sec in range(seconds, 60):
                
                self._ponteiros[0].girar(ANGULO_SEGUNDO)

                if sec == 59:
                    self._ponteiros[1].girar(ANGULO_SEGUNDO)
                    doze_minutos += 1
                    minutes += 1
                    if minutes == 60:
                        minutes = 0
                        hours += 1 if hours < 24 else 0

                if doze_minutos == 12:
                    self._ponteiros[2].girar(ANGULO_SEGUNDO)
                    doze_minutos = 0

                if digital:                   
                    
                    relogio_digital = "%02d:%02d:%02d" % (hours,
                                                          minutes,
                                                          sec)                    
                    self._hora_digital.clear()
                    self._hora_digital.write(relogio_digital,
                                             False,
                                             "center",
                                             ('Arial', 15, 'normal'))
                time.sleep(1)


            tela.update()
            time.sleep(1e-100000000000000)
                
            seconds = 0
            
            

    def _exibir_hora_atual(self):
        
        hours = time.localtime().tm_hour
        minutes = time.localtime().tm_min
        seconds = time.localtime().tm_sec

        self._ponteiros[0].girar( ANGULO_SEGUNDO * (seconds-1) )
        
        self._ponteiros[1].girar( ANGULO_SEGUNDO * minutes )


        doze_minutos = 0

        for i in range(1, minutes + 1):
            if i % 12 == 0:
                doze_minutos += 1
        
        self._ponteiros[2].girar( 30 * hours + 6 * doze_minutos)
        


def main():
    try:
        global tela, ANGULO_SEGUNDO

        ANGULO_SEGUNDO = 360/60
        
        tela = Screen()
        tela.title("Relógio")
        tela.tracer(0,0)
        tela.bgcolor(0,0,0)
        tela.delay(0)
        tela.setup(700, 700)
        
        segundos = Ponteiro("segundos")
        minutos = Ponteiro("minutos")
        horas = Ponteiro("horas")

        clock = Relogio((segundos, minutos, horas))
        clock.desenhar_numeros()          
        clock.exibir_hora(True)

    except: pass

    
if __name__ == "__main__": main()
