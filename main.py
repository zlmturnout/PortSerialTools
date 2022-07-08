from re import I

from sympy import im
from Serial_COM_tool import *

"""Main entrance  

Start Project program
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Serial_COM_tool()
    window.show()
    app.exec()