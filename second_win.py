# write a code for the second screen of app
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Experiment():
    def __init__(self, person, test1, test2, test3):
        self.person = person
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3