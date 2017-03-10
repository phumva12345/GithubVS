from rabbitgit1 import *
from rabbitgit2 import *
from rabbitgit3 import *
                   
def main():
    app = QApplication(sys.argv)
    s1 = Simple_drawing_window1()
    s1.show()
    s2 = Simple_drawing_window2()
    s2.show()
    s3 = Simple_drawing_window2()
    s3.show()
    sys.exit(app.exec_())

main()
