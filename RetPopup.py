import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
from Datacsv import DataCsv

import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time

form_CarReturnwindow = uic.loadUiType('CarReturnPopup.ui')[0]
form_CarRetwindow = uic.loadUiType('Carreturn.ui')[0]

class Thread1(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[0] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[0] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice.mp3'
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
            voicemsg = str(csvloadCarname[1] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice1.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[1] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice1.mp3'
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
            voicemsg = str(csvloadCarname[2] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice2.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[2] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice2.mp3'
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
            voicemsg = str(csvloadCarname[3] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice3.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[3] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice3.mp3'
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
            voicemsg = str(csvloadCarname[4] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice4.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[4] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice4.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

class Thread6(QtCore.QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def run(self):
        csvloadcopy = DataCsv()
        csvloadCarname = csvloadcopy.Data_read()
        self.languagecopy = csvloadcopy.Data_language()
        
        if str(self.languagecopy[0]) == "ko":
            voicemsg = str(csvloadCarname[5] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice5.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[5] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice5.mp3'
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
            voicemsg = str(csvloadCarname[6] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice6.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[6] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice6.mp3'
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
            voicemsg = str(csvloadCarname[7] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice7.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[7] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice7.mp3'
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
            voicemsg = str(csvloadCarname[8] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice8.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[8] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice8.mp3'
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
            voicemsg = str(csvloadCarname[9] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice9.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[9] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice9.mp3'
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
            voicemsg = str(csvloadCarname[10] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice10.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[10] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice10.mp3'
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
            voicemsg = str(csvloadCarname[11] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice11.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[11] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice11.mp3'
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
            voicemsg = str(csvloadCarname[12] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice12.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[12] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice12.mp3'
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
            voicemsg = str(csvloadCarname[13] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice13.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[13] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice13.mp3'
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
            voicemsg = str(csvloadCarname[14] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice14.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[14] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice14.mp3'
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
            voicemsg = str(csvloadCarname[15] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice15.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[15] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice15.mp3'
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
            voicemsg = str(csvloadCarname[16] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice16.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[16] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice16.mp3'
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
            voicemsg = str(csvloadCarname[17] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice17.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[17] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice17.mp3'
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
            voicemsg = str(csvloadCarname[18] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice18.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[18] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice18.mp3'
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
            voicemsg = str(csvloadCarname[19] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice19.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[19] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice19.mp3'
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
            voicemsg = str(csvloadCarname[20] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice20.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[20] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice20.mp3'
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
            voicemsg = str(csvloadCarname[21] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice21.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[21] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice21.mp3'
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
            voicemsg = str(csvloadCarname[22] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice22.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[22] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice22.mp3'
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
            voicemsg = str(csvloadCarname[23] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice23.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[23] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice23.mp3'
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
            voicemsg = str(csvloadCarname[24] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice24.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[24] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice24.mp3'
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
            voicemsg = str(csvloadCarname[25] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice25.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[25] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice25.mp3'
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
            voicemsg = str(csvloadCarname[26] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice26.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[26] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice26.mp3'
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
            voicemsg = str(csvloadCarname[27] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice27.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[27] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice27.mp3'
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
            voicemsg = str(csvloadCarname[28] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice28.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[28] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice28.mp3'
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
            voicemsg = str(csvloadCarname[29] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice29.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[29] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice29.mp3'
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
            voicemsg = str(csvloadCarname[30] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice30.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[30] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice30.mp3'
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
            voicemsg = str(csvloadCarname[31] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice31.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[31] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice31.mp3'
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
            voicemsg = str(csvloadCarname[32] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice32.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[32] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice32.mp3'
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
            voicemsg = str(csvloadCarname[33] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice33.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[33] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice33.mp3'
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
            voicemsg = str(csvloadCarname[34] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice34.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[34] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice34.mp3'
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
            voicemsg = str(csvloadCarname[35] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice35.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[35] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice35.mp3'
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
            voicemsg = str(csvloadCarname[36] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice36.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[36] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice36.mp3'
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
            voicemsg = str(csvloadCarname[37] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice37.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[37] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice37.mp3'
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
            voicemsg = str(csvloadCarname[38] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice38.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[38] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice38.mp3'
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
            voicemsg = str(csvloadCarname[39] + "님이 체크아웃 되었습니다").encode('utf-8') 
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1, lang='ko')
            filename = 'retvoice39.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        
        if str(self.languagecopy[0]) == "en":
            voicemsg = str(csvloadCarname[39] + "has been checked out").encode('utf-8')
            voicemsg1 = str(voicemsg.decode())
            tts = gTTS(voicemsg1)
            filename = 'retvoice39.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)


# Button 1
class retPopup(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(retPopup,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[0])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[0])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)

    def initUI(self):
        self.setupUi(self)
        
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t1 = Thread1(self)
        t1.start()

    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        
        self.csvloaddata = DataCsv()
        self.caridcsvloaddata = self.csvloaddata.CarID_Read()  # CarID
        self.RegCarIDTextlb2.setText(self.caridcsvloaddata[0])
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[0]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)
        
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup":
                self.guicon = window
                self.guicon.close()
        self.close()
        t1 = Thread1(self)
        t1.start()
    
    def display(self):
        self.vi = retPopup()

    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.close()
    
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 2
class retPopup1(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(retPopup1,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[1])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[1])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t2 = Thread2(self)
        t2.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup1(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup1,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        
        self.csvloaddata = DataCsv()
        self.caridcsvloaddata = self.csvloaddata.CarID_Read()    # 수정 1
        self.RegCarIDTextlb2.setText(self.caridcsvloaddata[1])   # 수정 2
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[1]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)
    
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup1":
                self.guicon = window
                self.guicon.close()
        self.close()
        t2 = Thread2(self)
        t2.start()
    
    def display(self):
        self.vi = retPopup1()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 3
class retPopup2(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(retPopup2,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[2])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[2])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t3 = Thread3(self)
        t3.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup2(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup2,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        
        self.csvloaddata = DataCsv()
        self.caridcsvloaddata = self.csvloaddata.CarID_Read()    # 수정 1
        self.RegCarIDTextlb2.setText(self.caridcsvloaddata[2])   # 수정 2
        self.caridcsvloaddata = self.csvloaddata.CarID_Read()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[2]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)
        
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup2":
                self.guicon = window
                self.guicon.close()
        self.close()
        t3 = Thread3(self)
        t3.start()
    
    def display(self):
        self.vi = retPopup2()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 4
class retPopup3(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(retPopup3,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[3])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[3])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t4 = Thread4(self)
        t4.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup3(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup3,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[3]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)
        
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup3":
                self.guicon = window
                self.guicon.close()
        self.close()
        h4 = Thread4(self)
        h4.start()
    
    def display(self):
        self.vi = retPopup3()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 5
class retPopup4(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup4,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[4])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[4])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t5 = Thread5(self)
        t5.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup4(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup4,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[4]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup4":
                self.guicon = window
                self.guicon.close()
        self.close()
        t5 = Thread5(self)
        t5.start()
    
    def display(self):
        self.vi = retPopup4()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 6
class retPopup5(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup5,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[5])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[5])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t6 = Thread6(self)
        t6.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup5(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup5,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[5]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)
    
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup5":
                self.guicon = window
                self.guicon.close()
        self.close()
        t6 = Thread6(self)
        t6.start()
    
    def display(self):
        self.vi = retPopup5()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.close()
    
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 7
class retPopup6(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(retPopup6,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[6])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[6])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t7 = Thread7(self)
        t7.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup6(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup6,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[6]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup6":
                self.guicon = window
                self.guicon.close()
        self.close()
        t7 = Thread7(self)
        t7.start()
    
    def display(self):
        self.vi = retPopup6()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 8
class retPopup7(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup7,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[7])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[7])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t8 = Thread8(self)
        t8.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup7(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup7,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[7]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)
        
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup7":
                self.guicon = window
                self.guicon.close()
        self.close()
        t8 = Thread8(self)
        t8.start()
    
    def display(self):
        self.vi = retPopup7()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
    
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 9
class retPopup8(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(retPopup8,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[8])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[8])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t9 = Thread9(self)
        t9.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup8(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup8,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[8]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup8":
                self.guicon = window
                self.guicon.close()
        self.close()
        t9 = Thread9(self)
        t9.start()

    def display(self):
        self.vi = retPopup8()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
    
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 10
class retPopup9(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup9,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[9])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[9])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t10 = Thread10(self)
        t10.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup9(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup9,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[9]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()

    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup9":
                self.guicon = window
                self.guicon.close()
        self.close()
        t10 = Thread10(self)
        t10.start()

    def display(self):
        self.vi = retPopup9()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
    
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 11
class retPopup10(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(retPopup10,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[10])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[10])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t11 = Thread11(self)
        t11.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup10(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup10,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[10]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup10":
                self.guicon = window
                self.guicon.close()
        self.close()
        t11 = Thread11(self)
        t11.start()
    
    def display(self):
        self.vi = retPopup10()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 12
class retPopup11(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup11,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[11])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[11])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t12 = Thread12(self)
        t12.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup11(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup11,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[11]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup11":
                self.guicon = window
                self.guicon.close()
        self.close()
        t12 = Thread12(self)
        t12.start()
    
    def display(self):
        self.vi = retPopup11()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
    
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 13
class retPopup12(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup12,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[12])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[12])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t13 = Thread13(self)
        t13.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup12(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup12,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[12]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()

    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup12":
                self.guicon = window
                self.guicon.close()
        self.close()
        t13 = Thread13(self)
        t13.start()
        
    
    def display(self):
        self.vi = retPopup12()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 14
class retPopup13(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup13,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[13])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[13])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t14 = Thread14(self)
        t14.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup13(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup13,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[13]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup13":
                self.guicon = window
                self.guicon.close()
        self.close()
        t14 = Thread14(self)
        t14.start()

    def display(self):
        self.vi = retPopup13()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 15
class retPopup14(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup14,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[14])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[14])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t15 = Thread15(self)
        t15.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup14(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup14,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[14]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup14":
                self.guicon = window
                self.guicon.close()
        self.close()
        t15 = Thread15(self)
        t15.start()
    
    def display(self):
        self.vi = retPopup14()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
    
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 16
class retPopup15(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup15,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[15])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[15])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t16 = Thread16(self)
        t16.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup15(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup15,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[15]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup15":
                self.guicon = window
                self.guicon.close()
        self.close()
        t16 = Thread16(self)
        t16.start()

    def display(self):
        self.vi = retPopup15()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 17
class retPopup16(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup16,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[16])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[16])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t17 = Thread17(self)
        t17.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup16(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup16,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[16]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)
    
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup16":
                self.guicon = window
                self.guicon.close()
        self.close()
        t17 = Thread17(self)
        t17.start()
    
    def display(self):
        self.vi = retPopup16()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 18
class retPopup17(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup17,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[17])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[17])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t18 = Thread18(self)
        t18.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup17(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup17,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[17]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup17":
                self.guicon = window
                self.guicon.close()
        self.close()
        t18 = Thread18(self)
        t18.start()
    
    def display(self):
        self.vi = retPopup17()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 19
class retPopup18(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup18,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[18])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[18])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t19 = Thread19(self)
        t19.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup18(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup18,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[18]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup18":
                self.guicon = window
                self.guicon.close()
        self.close()
        t19 = Thread19(self)
        t19.start()
    
    def display(self):
        self.vi = retPopup18()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 20
class retPopup19(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup19,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[19])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[19])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t20 = Thread20(self)
        t20.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup19(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup19,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[19]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup19":
                self.guicon = window
                self.guicon.close()
        self.close()
        t20 = Thread20(self)
        t20.start()

    
    def display(self):
        self.vi = retPopup19()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 21
class retPopup20(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup20,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[20])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[20])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t21 = Thread21(self)
        t21.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup20(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup20,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[20]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup20":
                self.guicon = window
                self.guicon.close()
        self.close()
        h21 = Thread21(self)
        h21.start()
    
    def display(self):
        self.vi = retPopup20()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 22
class retPopup21(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup21,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[21])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[21])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t22 = Thread22(self)
        t22.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup21(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup21,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[21]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup21":
                self.guicon = window
                self.guicon.close()
        self.close()
        t22 = Thread22(self)
        t22.start()
    
    def display(self):
        self.vi = retPopup21()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 23
class retPopup22(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup22,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[22])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[22])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t23 = Thread23(self)
        t23.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup22(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup22,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[22]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter)

    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup22":
                self.guicon = window
                self.guicon.close()
        self.close()
        t23 = Thread23(self)
        t23.start()

    def display(self):
        self.vi = retPopup22()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 24
class retPopup23(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup23,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[23])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[23])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t24 = Thread24(self)
        t24.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup23(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup23,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[23]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 
    
    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup23":
                self.guicon = window
                self.guicon.close()
        self.close()
        t24 = Thread24(self)
        t24.start()
    
    def display(self):
        self.vi = retPopup23()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 25
class retPopup24(QDialog,QWidget,form_CarReturnwindow):
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup24,self).__init__()
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[24])
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[24])
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t25 = Thread25(self)
        t25.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup24(QDialog,QWidget,form_CarRetwindow):
    def __init__(self):
        super(UserretPopup24,self).__init__()
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[24]).encode('utf-8')
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup24":
                self.guicon = window
                self.guicon.close()
        self.close()
        t25 = Thread25(self)
        t25.start()
    
    def display(self):
        self.vi = retPopup24()
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 26
class retPopup25(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup25,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[25])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[25])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t26 = Thread26(self)                                                # 수정 포인트
        t26.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup25(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트                    
    def __init__(self):
        super(UserretPopup25,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[25]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup25":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t26 = Thread26(self)                                                                    # 수정 포인트
        t26.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup25()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 27
class retPopup26(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup26,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[26])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[26])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t27 = Thread27(self)                                                # 수정 포인트
        t27.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup26(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트                    
    def __init__(self):
        super(UserretPopup26,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[26]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup26":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t27 = Thread27(self)                                                                    # 수정 포인트
        t27.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup26()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 28
class retPopup27(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup27,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[27])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[27])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t28 = Thread28(self)                                                # 수정 포인트
        t28.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup27(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup27,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[27]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup27":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t28 = Thread28(self)                                                                    # 수정 포인트
        t28.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup27()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 29
class retPopup28(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup28,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[28])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[28])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t29 = Thread29(self)                                                # 수정 포인트
        t29.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup28(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup28,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[28]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup28":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t29 = Thread29(self)                                                                    # 수정 포인트
        t29.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup28()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 30
class retPopup29(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup29,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[29])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[29])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t30 = Thread30(self)                                                # 수정 포인트
        t30.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup29(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup29,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[29]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup29":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t30 = Thread30(self)                                                                    # 수정 포인트
        t30.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup29()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 30
class retPopup30(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup30,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[30])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[30])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t31 = Thread31(self)                                                # 수정 포인트
        t31.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup30(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup30,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[30]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup30":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t31 = Thread31(self)                                                                    # 수정 포인트
        t31.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup30()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 31
class retPopup31(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup31,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[31])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[31])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t32 = Thread32(self)                                                # 수정 포인트
        t32.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup31(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup31,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[31]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup31":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t32 = Thread32(self)                                                                    # 수정 포인트
        t32.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup31()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 32
class retPopup32(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup32,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[32])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[32])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t33 = Thread33(self)                                                # 수정 포인트
        t33.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup32(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup32,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[32]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup32":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t33 = Thread33(self)                                                                    # 수정 포인트
        t33.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup32()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 33
class retPopup33(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup33,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[33])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[33])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t34 = Thread34(self)                                                # 수정 포인트
        t34.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup33(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup33,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[33]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup33":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t34 = Thread34(self)                                                                    # 수정 포인트
        t34.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup33()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 34
class retPopup34(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup34,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[34])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[34])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t35 = Thread35(self)                                                # 수정 포인트
        t35.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup34(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup34,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[34]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup34":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t35 = Thread35(self)                                                                    # 수정 포인트
        t35.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup34()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 35
class retPopup35(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup35,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[35])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[35])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t36 = Thread36(self)                                                # 수정 포인트
        t36.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup35(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup35,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[35]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup35":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t36 = Thread36(self)                                                                    # 수정 포인트
        t36.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup35()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 36
class retPopup36(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup36,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[36])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[36])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t37 = Thread37(self)                                                # 수정 포인트
        t37.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup36(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup36,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[36]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup36":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t37 = Thread37(self)                                                                    # 수정 포인트
        t37.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup36()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 37
class retPopup37(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup37,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[37])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[37])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t38 = Thread38(self)                                                # 수정 포인트
        t38.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup37(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup37,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[37]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup37":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t38 = Thread38(self)                                                                    # 수정 포인트
        t38.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup37()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

# Button 38
class retPopup38(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup38,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[38])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[38])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t39 = Thread39(self)                                                # 수정 포인트
        t39.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup38(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup38,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[38]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup38":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t39 = Thread39(self)                                                                    # 수정 포인트
        t39.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup38()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()

class retPopup39(QDialog,QWidget,form_CarReturnwindow):                     # 수정 포인트
    command = QtCore.pyqtSignal(bool)
    command1 = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        super(retPopup39,self).__init__()                                   # 수정 포인트
        self.initUI()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        self.csvloaddata = DataCsv()
        self.CarIDname =self.csvloaddata.CarID_Read()
        self.RetCarIDTextlb.setText(self.CarIDname[39])                     # 수정 포인트
        self.nameUser = self.csvloaddata.Data_read()
        self.RetCarNameTextlb.setText(self.nameUser[39])                    # 수정 포인트
        self.RetReturnbt.clicked.connect(self.Ret_ok)
        self.RetCancelBt.clicked.connect(self.Ret_Cancel)
    
    def initUI(self):
        self.setupUi(self)
    
    QtCore.pyqtSlot(bool)
    def Ret_ok(self):
        self.ret_okmsg = True
        self.command.emit(self.ret_okmsg)
        self.close()
        t40 = Thread40(self)                                                # 수정 포인트
        t40.start()
    
    QtCore.pyqtSlot(bool)
    def Ret_Cancel(self):
        self.ret_okmsg = False
        self.command1.emit(self.ret_okmsg)
        self.close()

class UserretPopup39(QDialog,QWidget,form_CarRetwindow):                    # 수정 포인트   여기서 부터 ..                    
    def __init__(self):
        super(UserretPopup39,self).__init__()                               # 수정 포인트
        self.initUI()
        self.display()
        self.logic()
        self.logicCancel()
        self.show()
        self.csvloaddata = DataCsv()
        self.Username = self.csvloaddata.Data_read()
        self.Usermsg = str(self.Username[39]).encode('utf-8')         # 수정 포인트
        self.Usermsg1 = str(self.Usermsg.decode())
        self.Popuplb2.setText(self.Usermsg1)
        self.Popuplb2.setAlignment(QtCore.Qt.AlignCenter) 


    def initUI(self):
        self.setupUi(self)   
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Popuppushbutton2.clicked.connect(self.Custommer_Ret_ok)
        self.move(1920,0)
        self.showFullScreen()
    
    def Custommer_Ret_ok(self):
        self.ret_okmsg1 = True
        for window in QApplication.topLevelWidgets():
            if window.metaObject().className() == "retPopup39":                                 # 수정 포인트
                self.guicon = window
                self.guicon.close()
        self.close()
        t40 = Thread40(self)                                                                    # 수정 포인트
        t40.start()                                                                             # 수정 포인트
    
    def display(self):
        self.vi = retPopup39()                                                                  # 수정 포인트      
    
    def logic(self):
        self.vi.command.connect(self.logicsel)
    
    def logicsel(self, sel):
        self.ret_okmsg1 = sel
        self.csvloaddata = DataCsv()
        self.close()
        
    def logicCancel(self):
        self.vi.command1.connect(self.logicselCancel)
    
    def logicselCancel(self, sel):
        self.ret_okmsg1 = sel
        self.close()