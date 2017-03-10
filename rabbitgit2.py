from rabbitgit import *

class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(25,127,0))
        p.setBrush(QColor(25,127,0))
        p.drawPie(50,150,100,100,0,180*10)

        p.drawImage(QRect(200,100,320,320), self.rabbit)
        p.end()
                
