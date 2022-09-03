from turtle import width
from PIL import Image

class Canvas:

    def __init__(self, width, height, n_rows, n_column):
        self.width = width
        self.height =  height
        self.n_rows = n_rows
        self.n_column = n_column
        self.img = Image.new('RGB', (width, height))

    def putPixel(self, x, y, cor):
        self.img.putpixel((x, y), cor)

    def paintASquare(self, row, column, color):
        dx = self.width/self.n_column
        dy = self.height/self.n_rows
        
        #
        for i in range(int(row * dy),int((row+1) * dy)):
            for j in range(int(column * dx), int((column + 1) * dx)):
                self.putPixel(j, i, color)
        

    def show(self):
        self.img.save('imagem 2.png')
        self.img.show()

    
