import imp
from camera import Camera
from shapes.plane import Plane
from shapes.shape import Shape
from utils import scale, minus, product
from vector import Vector
from scene import Scene
from shapes.sphere import Sphere
from canvas import Canvas
from light import Light
from reflexivity import Reflexivity

wCanvas = 500
hCanvas = 500
dJanela = 30
rEsfera = 40
wJanela = 60
hJanela = 60
esfColor = (255, 0, 0)
planeColor = (255, 255, 0)
planeColor2 = (255, 255, 0)
bgColor = (100, 100, 100)
nLin = 500
nCol = 500
z = -dJanela

I_F = Vector([0.7, 0.7, 0.7])  # Intensidade da fonte pontual
P_F = Vector(
    [
        0,
        60,
        -30,
    ]
)  # Posição da fonte pontual situada a 5 metros acima do olho do observador.
I_A = Vector([0.3, 0.3, 0.3])

light = Light(I_F, P_F)

ambient_light = Light(I_A, Vector([0, 0, 0]), "ambient")

cam = Camera(Vector([0, 0, 0]))

# Reflexivity(KD, KE, M)
sphere: Shape = Sphere(
    rEsfera,
    Vector([0, 0, -100]),
    esfColor,
    Reflexivity(
        Vector([0.7, 0.2, 0.2]), Vector([0.7, 0.2, 0.2]), Vector([0.7, 0.2, 0.2]), 10
    ),
)

floor: Shape = Plane(
    Vector([0, -rEsfera, 0]),
    Vector([0, 1, 0]),
    planeColor,
    Reflexivity(Vector([0.7, 0.2, 0.2]), Vector([0, 0, 0]), Vector([0.7, 0.2, 0.2]), 1),
)

background: Shape = Plane(
    Vector([0, 0, -200]),
    Vector([0, 0, 1]),
    planeColor2,
    Reflexivity(Vector([0.3, 0.3, 0.7]), Vector([0, 0, 0]), Vector([0.3, 0.3, 0.7]), 1),
)

canvas = Canvas(wCanvas, hCanvas, nLin, nCol)

scene = Scene([sphere, floor, background], canvas, light, ambient_light)
scene.take_a_picture(cam, (wJanela, hJanela, -dJanela), bgColor)
