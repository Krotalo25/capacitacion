from qgis.core import *
from qgis.gui import *
import string
#codigo de Luis Alejandro Canto Mena
@qgsfunction(args='auto', group='Custom')
def acentos(value1, feature, parent):
    nuevo = value1.replace('Ã“','Ó')
    nuevo = nuevo.replace('Ã�','Á')
    nuevo = nuevo.replace('Ã“','Ó')
    nuevo=nuevo.replace('Ã�','Í')
    nuevo=nuevo.replace('Ã‰','É')
    return nuevo