import temporizador

t = temporizador.Temporizador("teste.log", ["x","y"], "Registro de chamadas")
for x in range(100):
    for y in range(100):
        t.inicio([x,y])
        print "(x,y)=(%d,%d)" % (x,y)
        t.fim()
t=None
