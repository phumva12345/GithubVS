from rabbitgit import *

                   

class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,0,0))

        p.drawPie(50,150,100,100,0,180*4)

 
        p.end()


