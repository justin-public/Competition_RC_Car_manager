import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
from Datacsv import DataCsv

from PyQt5.QtCore import Qt , PYQT_VERSION_STR
from PyQt5.QtGui import QKeyEvent
#from PyQt5.QtCore import pyqtSignal
#from PyQt5.QtTextToSpeech import QTextToSpeech
#from main import MainWindow

import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time

form_Carnamewindow = uic.loadUiType('CarNameRegPopup.ui')[0]
form_UserRegwindow = uic.loadUiType('Carregister.ui')[0]
#reg_okmsg = False

loadindex1 = "1" 
loadindex2 = "2"
loadindex3 = "3"
loadindex4 = "4"
loadindex5 = "5"
loadindex6 = "6"
loadindex7 = "7"
loadindex8 = "8"
loadindex9 = "9"
loadindex10 = "10"
loadindex11 = "11"
loadindex12 = "12"
loadindex13 = "13"
loadindex14 = "14"
loadindex15 = "15"
loadindex16 = "16"
loadindex17 = "17"
loadindex18 = "18"
loadindex19 = "19"
loadindex20 = "20"
loadindex21 = "21"
loadindex22 = "22"
loadindex23 = "23"
loadindex24 = "24"
loadindex25 = "25"
loadindex26 = "26"
loadindex27 = "27"
loadindex28 = "28"
loadindex29 = "29"
loadindex30 = "30"
loadindex31 = "31"
loadindex32 = "32"
loadindex33 = "33"
loadindex34 = "34"
loadindex35 = "35"
loadindex36 = "36"
loadindex37 = "37"
loadindex38 = "38"
loadindex39 = "39"
loadindex40 = "40"

class Thread1(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[0] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[0] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread2(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[1] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice1.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[1] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice1.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread3(QtCore.QThread):    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[2] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice2.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[2] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice2.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread4(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[3] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice3.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[3] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice3.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread5(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[4] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice4.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[4] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice4.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

# 점검 필요
class Thread6(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[5] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice5.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[5] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice5.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread7(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[6] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice6.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[6] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice6.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread8(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[7] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice7.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[7] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice7.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread9(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[8] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice8.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[8] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice8.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread10(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[9] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice9.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[9] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice9.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread11(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[10] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice10.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[10] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice10.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread12(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[11] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice11.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[11] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice11.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread13(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[12] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice12.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[12] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice12.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread14(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[13] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice13.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[13] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice13.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread15(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[14] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice14.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[14] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice14.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread16(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[15] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice15.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[15] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice15.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread17(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[16] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice16.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[16] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice16.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread18(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[17] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice17.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[17] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice17.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread19(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[18] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice18.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[18] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice18.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread20(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[19] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice19.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[19] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice19.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread21(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[20] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice20.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[20] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice20.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread22(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[21] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice21.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[21] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice21.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread23(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[22] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice22.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[22] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice22.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread24(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[23] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice23.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[23] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice23.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread25(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[24] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice24.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[24] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice24.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread26(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[25] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice25.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[25] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice25.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

"""
class Thread26(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[25] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice25.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[25] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice25.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread27(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[26] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice26.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[26] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice26.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread28(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[27] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice27.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[27] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice27.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread29(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[28] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice28.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[28] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice28.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread30(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[29] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice29.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[29] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice29.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread31(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[30] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice30.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[30] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice30.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread32(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[31] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice31.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[31] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice31.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread33(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[32] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice32.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[32] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice32.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread34(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[33] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice33.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[33] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice33.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread35(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[34] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice34.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[34] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice34.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread36(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[35] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice35.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[35] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice35.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread37(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[36] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice36.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[36] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice36.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread38(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[37] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice37.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[37] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice37.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread39(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[38] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice38.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[38] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice38.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread40(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[39] + "님이 체크인 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'voice39.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[39] + "has been checked in").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'voice39.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
"""

# Button 1
class regPopup(QDialog,QWidget,form_Carnamewindow):
    strmsgparsing = ""
    command = QtCore.pyqtSignal(str)                         # 사용자 등록창에 실시간 데스트 표시 명령어
    command1 = QtCore.pyqtSignal(bool)                       # 팝업창 체크인동작 명령어   
    command2 = QtCore.pyqtSignal(bool)                       # 팝업창 취소동작 명령어
    
    def __init__(self, parent=None):
        super(regPopup,self).__init__(parent)
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.RegChkbt.clicked.connect(self.Reg_ok)
        self.RegCancelBt.clicked.connect(self.Reg_Cancel)
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RegCarIDTextlb.setText(self.CarIDname[0])
        self.ReglineEdit.setMaxLength(10)  
    
    def initUI(self):
        self.setupUi(self)
        
    QtCore.pyqtSlot(bool)
    def Reg_ok(self):
        self.regbt_enable = False
        if self.strmsgparsing == "":
            self.reg_okmsg = False
            self.command1.emit(self.reg_okmsg)
            self.close()
        if self.strmsgparsing != "":
            self.reg_okmsg = True
            self.command1.emit(self.reg_okmsg)
            csvload = DataCsv()                                   
            csvload.Data_write(loadindex1,self.strmsgparsing)
            self.close()        
            h1 = Thread1(self)
            h1.start()
        
    QtCore.pyqtSlot(bool)
    def Reg_Cancel(self):
        self.regbt_enable = False
        self.reg_okmsg = False
        self.command2.emit(self.reg_okmsg)                 # 취소버튼 동작 관련 명령어 전달            
        self.close()
    
    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        msg = self.ReglineEdit.text()
        self.ReglineEdit.textChanged.connect(self.text_chage) # 키이벤트 실시간 전달
        self.sendCommand(msg)
    
    QtCore.pyqtSlot(str)
    def text_chage(self, text):
        self.command.emit(text)
    
    def sendCommand(self, strmsg):
        self.strmsgparsing = strmsg

class UserregPopup(QDialog,QWidget,form_UserRegwindow):
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[0])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        
        shadow = QGraphicsDropShadowEffect(self.Popuppushbutton)
        shadow.setBlurRadius(8)
        shadow.setColor(QtGui.QColor(0, 0, 0, 50))
        
        shadow.setOffset(0, 4)
        self.Popuppushbutton.setGraphicsEffect(shadow)
        self.move(1920,0)
        self.showFullScreen()
    
    QtCore.pyqtSlot(str)
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex1,self.strmsgparsingcopy)
            h1 = Thread1(self)
            h1.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup()
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)

    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
        
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 2
class regPopup1(QDialog,QWidget,form_Carnamewindow):            #수정1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup1,self).__init__()                    #수정2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[1])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":   
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                # 수정6 
                csvload.Data_write(loadindex2,self.strmsgparsing)  # 수정7  
                self.close()
                h2 = Thread2(self)
                h2.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
        
        QtCore.pyqtSlot(str)
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)                             
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg
                 
class UserregPopup1(QDialog,QWidget,form_UserRegwindow):            # 수정8
        strmsgparsingcopy = ""
        commandcopy = QtCore.pyqtSignal(str)
        def __init__(self):
            super(UserregPopup1,self).__init__()                    # 수정9
            self.initUI()
            self.display()
            self.logic()
            self.logicCancel()
            self.show()
        
        def initUI(self):
            self.setupUi(self)
            self.caridcsvload = DataCsv()
            self.caridcsvloaddata = self.caridcsvload.CarID_Read()
            
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
            self.RegCarIDTextlb.setText(self.caridcsvloaddata[1])
            self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
            self.move(1920,0)
            self.showFullScreen()
            
        def Custommer_Reg_ok(self):
            if self.strmsgparsingcopy == "":
               self.reg_okmsg1 = False
               self.close() 

            if self.strmsgparsingcopy != "":
                self.regbt_enable = False
                self.reg_okmsg1 = True
                csvloadcopy = DataCsv()
                csvloadcopy.Data_write(loadindex2,self.strmsgparsingcopy)
                h2 = Thread2(self)
                h2.start()
            
            for window in QApplication.topLevelWidgets():
                if window.metaObject().className() == "regPopup1":
                    self.guicon = window
                    self.guicon.close()
            self.close()

        def display(self):
            self.vi = regPopup1()                                   # 수정10
            self.vi.command.connect(self.anyfunction)

        def logic(self):
            self.vi.command1.connect(self.logicsel)
        
        def logicCancel(self):
            self.vi.command2.connect(self.logicselCancel)
    
        def anyfunction(self, msg):
            self.Popuplb.setText(msg)
            self.commandcopy.emit(msg)
            self.sendcommandcopy(msg)
        
        def sendcommandcopy(self, strmsg):
            self.strmsgparsingcopy = strmsg
        
        def logicsel(self, sel):
            self.reg_okmsg1 = sel
            self.close()
    
        def logicselCancel(self, sel):
            self.reg_okmsg1 = sel
            self.close()

# Button 3
class regPopup2(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup2,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[2])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()    
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex3,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h3 = Thread3(self)
                h3.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)                             
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg
            
class UserregPopup2(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup2,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[2])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":                # <----------------
            self.reg_okmsg1 = False                     # <----------------
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex3,self.strmsgparsingcopy)
            h3 = Thread3(self)
            h3.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup2":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup2()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 4
class regPopup3(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup3,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[3])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()    
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex4,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h4 = Thread4(self)
                h4.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup3(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup3,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[3])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
        
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":                # <----------------
            self.reg_okmsg1 = False                     # <----------------
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex4,self.strmsgparsingcopy)
            h4 = Thread4(self)
            h4.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup3":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup3()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 5
class regPopup4(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup4,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[4])      #수정5
            self.ReglineEdit.setMaxLength(10)
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()    
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex5,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h5 = Thread5(self)
                h5.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)

        QtCore.pyqtSlot(str)                                    # <-----------------
        def text_chage(self, text):                             # <-----------------
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup4(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup4,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[4])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex5,self.strmsgparsingcopy)
            h5 = Thread5(self)
            h5.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup4":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup4()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 6
class regPopup5(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup5,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[5])      #수정5
            self.ReglineEdit.setMaxLength(10)
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()    
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex6,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h6 = Thread1(self)
                h6.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        #QtCore.pyqtSlot(str)
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup5(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup5,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[5])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()

    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex6,self.strmsgparsingcopy)
            h6 = Thread6(self)
            h6.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup5":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup5()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 7
class regPopup6(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup6,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[6])      #수정5
            self.ReglineEdit.setMaxLength(10)
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()    
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex7,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h7 = Thread7(self)
                h7.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)                             
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)                                    # <-----------------
        def text_chage(self, text):                             # <-----------------
            self.command.emit(text)    

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup6(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup6,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[6])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex7,self.strmsgparsingcopy)
            h7 = Thread7(self)
            h7.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup6":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup6()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 8
class regPopup7(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup7,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[7])      #수정5
            self.ReglineEdit.setMaxLength(10)
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex8,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h8 = Thread8(self)
                h8.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)                             
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)                                    # <-----------------
        def text_chage(self, text):                             # <-----------------
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup7(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup7,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[7])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()

    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex8,self.strmsgparsingcopy)
            h8 = Thread8(self)
            h8.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup7":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup7()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 9
class regPopup8(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup8,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[8])      #수정5
            self.ReglineEdit.setMaxLength(10)
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex9,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h9 = Thread9(self)
                h9.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)

        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup8(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup8,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[8])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex9,self.strmsgparsingcopy)
            h9 = Thread9(self)
            h9.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup8":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup8()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 10
class regPopup9(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup9,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[9])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex10,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h10 = Thread10(self)
                h10.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)

        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text) 
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup9(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup9,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[9])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex10,self.strmsgparsingcopy)
            h10 = Thread10(self)
            h10.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup9":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup9()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 11
class regPopup10(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       

        def __init__(self):
            super(regPopup10,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[10])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex11,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h11 = Thread11(self)
                h11.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup10(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup10,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[10])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
        
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex11,self.strmsgparsingcopy)
            h11 = Thread11(self)
            h11.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup10":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup10()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg

    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 12
class regPopup11(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup11,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[11])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex12,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h12 = Thread12(self)
                h12.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup11(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup11,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[11])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex12,self.strmsgparsingcopy)
            h12 = Thread12(self)
            h12.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup11":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup11()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 13
class regPopup12(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup12,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[12])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex13,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h13 = Thread13(self)
                h13.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup12(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup12,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[12])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = True
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex13,self.strmsgparsingcopy)
            h13 = Thread13(self)
            h13.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup12":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup12()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 14
class regPopup13(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup13,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[13])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex14,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h14 = Thread14(self)
                h14.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)                             
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup13(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup13,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[13])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex14,self.strmsgparsingcopy)
            h14 = Thread14(self)
            h14.start()    
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup13":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup13()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 15
class regPopup14(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup14,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[14])      #수정5
            self.ReglineEdit.setMaxLength(10)
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex15,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h15 = Thread15(self)
                h15.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)

        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup14(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup14,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[14])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex15,self.strmsgparsingcopy)
            h15 = Thread15(self)
            h15.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup14":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup14()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 16
class regPopup15(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup15,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[15])      #수정5
            self.ReglineEdit.setMaxLength(10)
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex16,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h16 = Thread16(self)
                h16.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_chage)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_chage(self, text):
            self.command.emit(text)
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup15(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup15,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[15])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex16,self.strmsgparsingcopy)
            h16 = Thread16(self)
            h16.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup15":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup15()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 17
class regPopup16(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup16,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[16])      #수정5
            self.ReglineEdit.setMaxLength(10) 
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex17,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h17 = Thread17(self)
                h17.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        #QtCore.pyqtSlot(str)
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup16(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup16,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[16])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex17,self.strmsgparsingcopy)
            h17 = Thread17(self)
            h17.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup16":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup16()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 18
class regPopup17(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup17,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[17])      #수정5
            self.ReglineEdit.setMaxLength(10) 
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex18,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h18 = Thread18(self)
                h18.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)    

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup17(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup17,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[17])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()

    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex18,self.strmsgparsingcopy)
            h18 = Thread18(self)
            h18.start()
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup17":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup17()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg

    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 19
class regPopup18(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup18,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[18])      #수정5
            self.ReglineEdit.setMaxLength(10)    
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex19,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h19 = Thread19(self)
                h19.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup18(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup18,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[18])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex19,self.strmsgparsingcopy)
            h19 = Thread19(self)
            h19.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup18":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup18()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 20
class regPopup19(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup19,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[19])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex20,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h20 = Thread20(self)
                h20.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup19(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup19,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[19])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex20,self.strmsgparsingcopy)
            h20 = Thread20(self)
            h20.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup19":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup19()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button21
class regPopup20(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup20,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[20])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex21,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h21 = Thread21(self)
                h21.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup20(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup20,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[20])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex21,self.strmsgparsingcopy)
            h21 = Thread21(self)
            h21.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup20":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup20()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)

    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button22
class regPopup21(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup21,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[21])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex22,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h22 = Thread22(self)
                h22.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup21(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup21,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[21])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True    
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex22,self.strmsgparsingcopy)
            h22 = Thread22(self)
            h22.start()    
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup21":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup21()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
        
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button23
class regPopup22(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup22,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[22])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex23,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h23 = Thread23(self)
                h23.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup22(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup22,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[22])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()    
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex23,self.strmsgparsingcopy)
            h23 = Thread23(self)
            h23.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup22":
                self.guicon = window
                self.guicon.close()
        self.close()
        

    def display(self):
        self.vi = regPopup22()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button24
class regPopup23(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup23,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[23])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex24,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h24 = Thread24(self)
                h24.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup23(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    def __init__(self):
        super(UserregPopup23,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[23])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex24,self.strmsgparsingcopy)
            h24 = Thread24(self)
            h24.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup23":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup23()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button25
class regPopup24(QDialog,QWidget,form_Carnamewindow):      # 수정 포인트 1
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)                       
    
        def __init__(self):
            super(regPopup24,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        #수정3
            self.CarIDname =self.csvloaddata.CarID_Read()       #수정4    
            self.RegCarIDTextlb.setText(self.CarIDname[24])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)
    
        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex25,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h25 = Thread25(self)
                h25.start()
    
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup24(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup24,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[24])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        #self.regbt_enable = False
        #self.reg_okmsg1 = True
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex25,self.strmsgparsingcopy)
            h25 = Thread25(self)
            h25.start()    
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup24":
                self.guicon = window
                self.guicon.close()
        self.close()
        
    
    def display(self):
        self.vi = regPopup24()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 26
class regPopup25(QDialog,QWidget,form_Carnamewindow):
    strmsgparsing = ""
    command = QtCore.pyqtSignal(str)
    command1 = QtCore.pyqtSignal(bool)
    command2 = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(regPopup25,self).__init__()                  # 수정 1
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.RegChkbt.clicked.connect(self.Reg_ok)
        self.RegCancelBt.clicked.connect(self.Reg_Cancel)
        self.csvloaddata = DataCsv()                        
        self.CarIDname =self.csvloaddata.CarID_Read()           
        self.RegCarIDTextlb.setText(self.CarIDname[25])     # 수정 2
        self.ReglineEdit.setMaxLength(10)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Reg_ok(self):
        self.regbt_enable = False
        if self.strmsgparsing == "":
            self.reg_okmsg = False
            self.command1.emit(self.reg_okmsg)
            self.close()
        if self.strmsgparsing != "":
            self.reg_okmsg = True
            self.command1.emit(self.reg_okmsg)
            csvload = DataCsv()
            csvload.Data_write(loadindex26,self.strmsgparsing)              # 수정 3
            self.close()
            #h26 = Thread26(self)                                            # 수정 4
            #h26.start()                                                     # 수정 5
    
    QtCore.pyqtSlot(bool)
    def Reg_Cancel(self):
        self.regbt_enable = False
        self.reg_okmsg = False
        self.command2.emit(self.reg_okmsg)
        self.close()
    
    def keyReleaseEvent(self, event):
        msg = self.ReglineEdit.text()
        self.ReglineEdit.textChanged.connect(self.text_change)
        self.sendCommand(msg)
    
    QtCore.pyqtSlot(str)
    def text_change(self, text):
        self.command.emit(text)
    
    def sendCommand(self, strmsg):
        self.strmsgparsing = strmsg

class UserregPopup25(QDialog,QWidget,form_UserRegwindow):
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)

    def __init__(self):
        super(UserregPopup25,self).__init__()                      
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[25])                      # 수정 1
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        """
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            #self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex26,self.strmsgparsingcopy)          # 수정 2
            #h26 = Thread26(self)                                                # 수정 3
            #h26.start()                                                         # 수정 4    
        """
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup25":                 # 수정 5
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup25()                                                  # 수정 6                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 26
"""
class regPopup25(QDialog,QWidget,form_Carnamewindow):
    strmsgparsing = ""
    command = QtCore.pyqtSignal(str)
    command1 = QtCore.pyqtSignal(bool)
    command2 = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(regPopup25,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    
    def initUI(self):
        self.setupUi(self)


class UserregPopup25(QDialog,QWidget,form_UserRegwindow):
    strmsgparsingcopy = ""
"""
"""
class regPopup25(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup25,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[25])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            #self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.regbt_enable = False
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex26,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h26 = Thread26(self)
                h26.start()
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        #QtCore.pyqtSlot(str)
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup25(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup25,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[25])
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex26,self.strmsgparsingcopy)
            h26 = Thread26(self)
            h26.start()    
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup25":
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup25()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 27
class regPopup26(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup26,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[26])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex27,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h27 = Thread27(self)
                h27.start()
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup26(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup26,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[26])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex27,self.strmsgparsingcopy)
            h27 = Thread27(self)
            h27.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup26":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup26()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 28
class regPopup27(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup27,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[27])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex28,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h28 = Thread28(self)
                h28.start()
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup27(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup27,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[27])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex28,self.strmsgparsingcopy)
            h28 = Thread28(self)
            h28.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup27":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup27()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 29
class regPopup28(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup28,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[28])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex29,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h29 = Thread29(self)
                h29.start()
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)                    

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup28(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup28,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[28])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex29,self.strmsgparsingcopy)
            h29 = Thread29(self)
            h29.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup28":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup28()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 30
class regPopup29(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup29,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[29])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex30,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h30 = Thread30(self)
                h30.start()
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup29(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup29,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[29])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex30,self.strmsgparsingcopy)
            h30 = Thread30(self)
            h30.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup29":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        
    def display(self):
        self.vi = regPopup29()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 31
class regPopup30(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup30,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[30])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex31,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h31 = Thread31(self)                                    # 수정 포인트
                h31.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup30(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup30,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[30])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex31,self.strmsgparsingcopy)
            h31 = Thread31(self)                                            # 수정 포인트
            h31.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup30":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             
    def display(self):
        self.vi = regPopup30()                                      # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 32
class regPopup31(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup31,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[31])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex32,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h32 = Thread32(self)                                    # 수정 포인트
                h32.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup31(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup31,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[31])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex32,self.strmsgparsingcopy)
            h32 = Thread32(self)                                            # 수정 포인트
            h32.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup31":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             
    def display(self):
        self.vi = regPopup31()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 33
class regPopup32(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup32,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[32])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex33,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h33 = Thread33(self)                                    # 수정 포인트
                h33.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup32(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup32,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[32])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex33,self.strmsgparsingcopy)
            h33 = Thread33(self)                                            # 수정 포인트
            h33.start()    
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup32":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             # 수정 포인트
    def display(self):
        self.vi = regPopup32()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 34
class regPopup33(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup33,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[33])      #수정5
            self.ReglineEdit.setMaxLength(10)    
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex34,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h34 = Thread34(self)                                    # 수정 포인트
                h34.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
        
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup33(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup33,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[33])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex34,self.strmsgparsingcopy)
            h34 = Thread34(self)                                            # 수정 포인트
            h34.start() 
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup33":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
    
    def display(self):
        self.vi = regPopup33()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 35
class regPopup34(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup34,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[34])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex35,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h35 = Thread35(self)                                    # 수정 포인트
                h35.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)    
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup34(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup34,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[34])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        self.regbt_enable = False
        self.reg_okmsg1 = True
        
        if self.strmsgparsingcopy != "":
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex35,self.strmsgparsingcopy)
        
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup34":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        h35 = Thread35(self)                                            # 수정 포인트
        h35.start()                                                     # 수정 포인트
    
    def display(self):
        self.vi = regPopup34()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 36
class regPopup35(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup35,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[35])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex36,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h36 = Thread36(self)                                    # 수정 포인트
                h36.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)
        
        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup35(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup35,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[35])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex36,self.strmsgparsingcopy)
            h36 = Thread36(self)                                            # 수정 포인트
            h36.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup35":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             
    def display(self):
        self.vi = regPopup35()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 37
class regPopup36(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup36,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[36])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex37,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h37 = Thread37(self)                                    # 수정 포인트
                h37.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup36(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup36,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[36])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex37,self.strmsgparsingcopy)
            h37 = Thread37(self)                                            # 수정 포인트
            h37.start()    
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup36":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             # 수정 포인트
    
    def display(self):
        self.vi = regPopup36()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 38
class regPopup37(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup37,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[37])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex38,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h38 = Thread38(self)                                    # 수정 포인트
                h38.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup37(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup37,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[37])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex38,self.strmsgparsingcopy)
            h38 = Thread38(self)                                            # 수정 포인트
            h38.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup37":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             
    def display(self):
        self.vi = regPopup37()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 39
class regPopup38(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup38,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[38])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex39,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h39 = Thread39(self)                                    # 수정 포인트
                h39.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
        
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup38(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup38,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[38])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex39,self.strmsgparsingcopy)
            h39 = Thread39(self)                                            
            h39.start()
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup38":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             
    def display(self):
        self.vi = regPopup38()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()

# Button 40
class regPopup39(QDialog,QWidget,form_Carnamewindow):
        strmsgparsing = ""
        command = QtCore.pyqtSignal(str)                         
        command1 = QtCore.pyqtSignal(bool)                          
        command2 = QtCore.pyqtSignal(bool)

        def __init__(self):
            super(regPopup39,self).__init__()                  # 수정 포인트 2
            self.initUI()
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(flags)
            self.show()
            self.RegChkbt.clicked.connect(self.Reg_ok)
            self.RegCancelBt.clicked.connect(self.Reg_Cancel)
            self.csvloaddata = DataCsv()                        
            self.CarIDname =self.csvloaddata.CarID_Read()           
            self.RegCarIDTextlb.setText(self.CarIDname[39])      #수정5
            self.ReglineEdit.setMaxLength(10)
        
        def initUI(self):
            self.setupUi(self)

        QtCore.pyqtSlot(bool)
        def Reg_ok(self):
            self.regbt_enable = False
            if self.strmsgparsing == "":
                self.reg_okmsg = False
                self.command1.emit(self.reg_okmsg)
                self.close()
            if self.strmsgparsing != "":
                self.reg_okmsg = True
                self.command1.emit(self.reg_okmsg)
                csvload = DataCsv()                                 
                csvload.Data_write(loadindex40,self.strmsgparsing)  # 수정 포인트 3  
                self.close()
                h40 = Thread40(self)                                    # 수정 포인트
                h40.start()                                             # 수정 포인트
        
        QtCore.pyqtSlot(bool)
        def Reg_Cancel(self):
            self.regbt_enable = False
            self.reg_okmsg = False
            self.command2.emit(self.reg_okmsg)                             
            self.close()
    
        def keyReleaseEvent(self, event):
            msg = self.ReglineEdit.text()
            self.ReglineEdit.textChanged.connect(self.text_change)
            self.sendCommand(msg)
        
        QtCore.pyqtSlot(str)
        def text_change(self, text):
            self.command.emit(text)

        def sendCommand(self, strmsg):
            self.strmsgparsing = strmsg

class UserregPopup39(QDialog,QWidget,form_UserRegwindow):           # 수정 포인트 1
    strmsgparsingcopy = ""
    commandcopy = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(UserregPopup39,self).__init__()                        # 수정 포인트 2
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.caridcsvload = DataCsv()
        self.caridcsvloaddata = self.caridcsvload.CarID_Read()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundlb.setPixmap(QtGui.QPixmap("black_50.png"))
        self.RegCarIDTextlb.setText(self.caridcsvloaddata[39])      # 수정 포인트 3
        self.Popuppushbutton.clicked.connect(self.Custommer_Reg_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Reg_ok(self):
        if self.strmsgparsingcopy == "":
            self.reg_okmsg1 = False
            self.close()
        if self.strmsgparsingcopy != "":
            self.regbt_enable = False
            self.reg_okmsg1 = True
            csvloadcopy = DataCsv()
            csvloadcopy.Data_write(loadindex40,self.strmsgparsingcopy)
            h40 = Thread40(self)                                            # 수정 포인트
            h40.start()    
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "regPopup39":         # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
                                                             
    def display(self):
        self.vi = regPopup39()                                          # 수정 포인트3                 
        self.vi.command.connect(self.anyfunction)

    def logic(self):
        self.vi.command1.connect(self.logicsel)
        
    def logicCancel(self):
        self.vi.command2.connect(self.logicselCancel)
    
    def anyfunction(self, msg):
        self.Popuplb.setText(msg)
        self.commandcopy.emit(msg)
        self.sendcommandcopy(msg)
    
    def sendcommandcopy(self, strmsg):
        self.strmsgparsingcopy = strmsg
    
    def logicsel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
    
    def logicselCancel(self, sel):
        self.reg_okmsg1 = sel
        self.close()
"""

