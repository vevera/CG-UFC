import imp
from camera import Camera
from utils import scale, minus, product
from vector import Vector
from scene import Scene
from sphere import Sphere
from canvas import Canvas
from light import Light

wCanvas = 500
hCanvas = 500
dJanela = 1
rEsfera = 2
wJanela = 3
hJanela = 3
esfColor = (255, 0, 0)
bgColor  = (100, 100, 100)
nLin = 500
nCol = 500
z = -(dJanela + rEsfera)

I_F = (0.7, 0.7, 0.7) # Intensidade da fonte pontual
P_F = (0, 5, 0)  #Posição da fonte pontual situada a 5 metros acima do olho do observador.


light = Light(I_F, P_F)

cam = Camera(Vector([0,0,0]))

sphere = Sphere(rEsfera, Vector([0,0,z]), esfColor)

canvas = Canvas(wCanvas, hCanvas, nLin, nCol)

scene = Scene([sphere], canvas, light)
scene.take_a_picture(cam,(wJanela,hJanela,-dJanela), bgColor)