from rabbitgit import *

class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(25,127,0))
        p.setBrush(QColor(25,127,0))

        p.drawPolygon([
            QPoint(50,200),QPoint(150,200), QPoint(100,300),
            ])

        p.drawImage(QRect(200,100,320,320), self.rabbit)
        p.end()
                
