"""
# Date : 2023.03.21 18:29
# PyQt5 UI
# Copyright 2023 EPICGRAM
# Released under the EPICGRAM license
# Original Code
# Git COMMIT-MSG for validating commit message
# See http://211.169.234.147/git/Repository/Commit/9c3a8018-be8e-4dad-869e-2c83c9396e9c?commit=57fbd921c21764d29fc8319d68771cbdaf9ef953
# modified by justin
"""
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from RegPopup import *          #regPopup ,UserregPopup, UserregPopup1, UserregPopup2, UserregPopup3, UserregPopup4, UserregPopup5, UserregPopup6, UserregPopup7
from RetPopup import *
from Datacsv import DataCsv

from PyQt5 import QtWidgets, QtGui, QtMultimedia, QtCore

import sys
import re
#import os

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
from threading import Lock, Thread, Event
from time import time, ctime, sleep

# video
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget 

# TTS
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
#import time

main_win = uic.loadUiType('SPR_GUI_Maindesign_20230117.ui')[0]
customer_win = uic.loadUiType('customer.ui')[0]
DURATION_INT = 0
timeval = 0
HBPORT = 8080
CHECKWAIT = 5
SERVERIP_PASS = "192.168.0.71"
SERVERPORT_PASS = 8081

#timercnt = 0

def secs_to_minsec(secs: int):
    mins = secs // 60
    secs = secs % 60
    minsec = f'{mins:02}:{secs:02}'
    return minsec

class BeatDict:
    def __init__(self):                       #초기화
        self.beatDict = {}                    #beatDict 호출
        if __debug__:
            self.beatDict['192.168.0.83'] = time()
            self.beatDict['192.168.0.79'] = time()
            self.beatDict['192.168.0.78'] = time()
        self.dictLock = Lock()
    
    def __repr__(self):
      list = ''
      self.dictLock.acquire()             # 얻다 ? 잠금
      for key in self.beatDict.keys():
        list = "%sIP address: %s - Last time: %s\n" % (list,key,ctime(self.beatDict[key]))
      self.dictLock.release()             # 풀어 주다 ? 해제
      return list
    
    def update(self, entry):
      self.dictLock.acquire()
      self.beatDict[entry] = time()
      self.dictLock.release()
    
    def extractSilent(self, howPast):
      silent = []
      when = time() - howPast
      self.dictLock.acquire()
      for key in self.beatDict.keys():
        if self.beatDict[key] < when:
          silent.append(key)
      self.dictLock.release()
      return silent

class BeatRec(Thread):
    def __init__(self, goOnEvent, updateDictFunc, port):
        Thread.__init__(self)
        self.goOnEvent = goOnEvent
        self.updateDictFunc = updateDictFunc
        self.port = port
        self.recSocket = socket(AF_INET, SOCK_DGRAM)
        self.recSocket.bind(('',port))
    
    def __repr__(self):
        return "Heartbeat Server on port: %d\n" % self.port

    def run(self):
        while self.goOnEvent.isSet():
            if __debug__:
                print("Waiting to receive...")
            
            data, addr = self.recSocket.recvfrom(1024)
            self.socketmsg = str(data.decode())
            self.socketmsgsplit = self.socketmsg.split(",")
            self.CsvParsingmsg = DataCsv()
            # 모듈 , 안테나 #1
            # RFID 모듈 상태 측정
            if self.socketmsgsplit[0] == "R01":
                self.CsvParsingmsg.Data_Module_state_write(self.socketmsgsplit[1],self.socketmsgsplit[2])
            # 안테나 모듈 상태 측정    
            if self.socketmsgsplit[0] == "A01":
                self.CsvParsingmsg.Data_Antenna_state_write(self.socketmsgsplit[1],self.socketmsgsplit[2])
            # RFID 데이터 전송
            if self.socketmsgsplit[0] == "V01":
                self.CsvParsingmsgpass = self.CsvParsingmsg.Data_Rfid_write(self.socketmsgsplit[1],self.socketmsgsplit[2])
                self.CsvParsingmsgpass1 = str(self.CsvParsingmsgpass).encode('utf-8')
                self.recSocket.sendto(self.CsvParsingmsgpass1,(SERVERIP_PASS,SERVERPORT_PASS))
            # 모듈 , 안테나 #2
            # RFID 모듈 상태 측정
            if self.socketmsgsplit[0] == "R02":
                #self.CsvParsingmsg = DataCsv()
                self.CsvParsingmsg.Data_Module_state_write(self.socketmsgsplit[1] , self.socketmsgsplit[2])    
            # 안테나 모듈 상태 측정
            if self.socketmsgsplit[0] == "A02":
                #self.CsvParsingmsg = DataCsv()
                self.CsvParsingmsg.Data_Antenna_state_write(self.socketmsgsplit[1],self.socketmsgsplit[2])
            # RFID 데이터 전송
            if self.socketmsgsplit[0] == "V02":
                self.CsvParsingmsgpass = self.CsvParsingmsg.Data_Rfid_write(self.socketmsgsplit[1],self.socketmsgsplit[2])
                self.CsvParsingmsgpass1 = str(self.CsvParsingmsgpass).encode('utf-8')
                self.recSocket.sendto(self.CsvParsingmsgpass1,(SERVERIP_PASS,SERVERPORT_PASS))
            
            if __debug__:
                print("Received packet from " + 'addr')
            self.updateDictFunc(addr[0])

class Worker(QObject):
    def __init__(self):
        super(Worker,self).__init__()
        self.working = True
    
    def work(self):
        global HBPORT, CHECKWAIT
        if len(sys.argv) > 1:
            HBPORT=sys.argv[1]
        if len(sys.argv) > 2:
            CHECKWAIT=sys.argv[2]
        
        beatRecGoOnEvent = Event()
        beatRecGoOnEvent.set()
        beatDictObject = BeatDict()
        beatRecThread = BeatRec(beatRecGoOnEvent,beatDictObject.update,HBPORT)
        
        if __debug__:
            print(beatRecThread)
        beatRecThread.start()
        print("PyHeartBeat server listening on port %d" % HBPORT)
        print("\n*** Press Ctrl-C to stop ***\n")
        while self.working:
            try:
                if __debug__:
                    print("Beat Dictionary")
                    print(beatDictObject)
                
                silent = beatDictObject.extractSilent(CHECKWAIT)
                if silent:
                    #print("Silent clients")
                    #print(silent)
                    self.CsvParsingmsg = DataCsv()
                    #self.AdminIPvalue = self.CsvParsingmsg.Data_Rfid_IP_Read()
                    #print(len(silent))
                    if len(silent) == 3:
                        self.AdminIPvalue = self.CsvParsingmsg.Data_Rfid_IP_Read()
                        if str(silent[0]) == self.AdminIPvalue[0]:
                            self.CsvParsingmsg.Data_Module_state_write("M01" , "2")
                            self.CsvParsingmsg.Data_Module_state_write("M02" , "2")
                        if str(silent[1]) == self.AdminIPvalue[2]:
                            self.CsvParsingmsg.Data_Module_state_write("M03" , "2")
                            self.CsvParsingmsg.Data_Module_state_write("M04" , "2")            
                    
                    if len(silent) == 2:
                        self.AdminIPvalue = self.CsvParsingmsg.Data_Rfid_IP_Read()
                        if str(silent[0]) == self.AdminIPvalue[0]:
                            self.CsvParsingmsg.Data_Module_state_write("M01" , "2")
                            self.CsvParsingmsg.Data_Module_state_write("M02" , "2")
                        if str(silent[0]) == self.AdminIPvalue[2]:
                            self.CsvParsingmsg.Data_Module_state_write("M03" , "2")
                            self.CsvParsingmsg.Data_Module_state_write("M04" , "2")
                    sleep(CHECKWAIT)
            except KeyboardInterrupt:
                print("Exiting.")
                beatRecGoOnEvent.clear()
                beatRecThread.join()


class MainWindow(QMainWindow,QWidget,QtCore.QThread,main_win):
    def __init__(self, sec = 0, parent = None):
        # 초기 메인화면 로드
        super().__init__()
        self.show()
        self.thread = None
        self.worker = None
        self.initUI()
    
    def initUI(self):
        # 메인 화면 구성
        self.setupUi(self)
        #self.showFullScreen()
        self.show()
        print("PyQt5 버전:", PYQT_VERSION_STR)
        
        # Thread Process
        self.worker = Worker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.work)
        self.thread.start()

        self.recSocket1 = socket(AF_INET, SOCK_DGRAM)
        
        self.timeVal = QtCore.QTimer(self)
        self.timeVal.setInterval(1000)
        self.timeVal.timeout.connect(self.printTime)
        self.timeVal.start()

        self.Timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.Timerlb1.setAlignment(QtCore.Qt.AlignCenter)

        # 초기 데이터 로드
        self.rfidmodulecsv = DataCsv()
        self.rfidmodulename = self.rfidmodulecsv.Data_Rfid_AntennaID_Read()
        self.rfidnote = self.rfidmodulecsv.Data_Rfid_note_Read()
        self.CarIDlabelData = self.rfidmodulecsv.CarID_Read()
        self.RfidmoduleIP = self.rfidmodulecsv.Data_Rfid_IP_Read()
        self.CarHWname = self.rfidmodulecsv.Data_read()
        
        if self.CarIDlabelData[0] == "N":
             self.CarID1btIN.hide()
             self.CarID1btOut.hide()
             self.Car1Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
             self.Car1Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[0] != "N":
             self.Car1Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
             self.Car1Statelb.setAlignment(QtCore.Qt.AlignCenter)       
        
        if self.CarIDlabelData[1] == "N":
             self.CarID2btIN.hide()
             self.CarID2btOut.hide()
             self.Car2Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
             self.Car2Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[1] != "N":
             self.Car2Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
             self.Car2Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[2] == "N":
             self.CarID3btIN.hide()
             self.CarID3btOut.hide()
             self.Car3Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
             self.Car3Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[2] != "N":
            self.Car3Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car3Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[3] == "N":
            self.CarID4btIN.hide()
            self.CarID4btOut.hide()
            self.Car4Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car4Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[3] != "N":
            self.Car4Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car4Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[4] == "N":
            self.CarID5btIN.hide()
            self.CarID5btOut.hide()
            self.Car5Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car5Statelb.setAlignment(QtCore.Qt.AlignCenter)   
        if self.CarIDlabelData[4] != "N":
            self.Car5Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car5Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[5] == "N":
            self.CarID6btIN.hide()
            self.CarID6btOut.hide()
            self.Car6Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car6Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[5] != "N":
            self.Car6Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car6Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[6] == "N":
            self.CarID7btIN.hide()
            self.CarID7btOut.hide()
            self.Car7Statelb.setPixmap(QtGui.QPixmap("state_black.png"))   
            self.Car7Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[6] != "N":
            self.Car7Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car7Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[7] == "N":
            self.CarID8btIN.hide()
            self.CarID8btOut.hide()
            self.Car8Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car8Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[7] != "N":
            self.Car8Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car8Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[8] == "N":
            self.CarID9btIN.hide()
            self.CarID9btOut.hide()
            self.Car9Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car9Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[8] != "N":
            self.Car9Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car9Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[9] == "N":
            self.CarID10btIN.hide()
            self.CarID10btOut.hide()
            self.Car10Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car10Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[9] != "N":
            self.Car10Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car10Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[10] == "N":
            self.CarID11btIN.hide()
            self.CarID11btOut.hide()
            self.Car11Statelb.setPixmap(QtGui.QPixmap("state_black.png"))   
            self.Car11Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[10] != "N":
            self.Car11Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car11Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[11] == "N":
            self.CarID12btIN.hide()
            self.CarID12btOut.hide()
            self.Car12Statelb.setPixmap(QtGui.QPixmap("state_black.png")) 
            self.Car12Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[11] != "N":
            self.Car12Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car12Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[12] == "N":
            self.CarID13btIN.hide()
            self.CarID13btOut.hide()
            self.Car13Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car13Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[12] != "N":
            self.Car13Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car13Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[13] == "N":
            self.CarID14btIN.hide()
            self.CarID14btOut.hide()
            self.Car14Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car14Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[13] != "N":
            self.Car14Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car14Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[14] == "N":
            self.CarID15btIN.hide()
            self.CarID15btOut.hide()
            self.Car15Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car15Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[14] != "N":
            self.Car15Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car15Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[15] == "N":
            self.CarID16btIN.hide()
            self.CarID16btOut.hide()
            self.Car16Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car16Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[15] != "N":
            self.Car16Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car16Statelb.setAlignment(QtCore.Qt.AlignCenter)    
        
        if self.CarIDlabelData[16] == "N":
            self.CarID17btIN.hide()
            self.CarID17btOut.hide()
            self.Car17Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car17Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[16] != "N":
            self.Car17Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car17Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[17] == "N":
            self.CarID18btIN.hide()
            self.CarID18btOut.hide()
            self.Car18Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car18Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[17] != "N":
            self.Car18Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car18Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[18] == "N":
            self.CarID19btIN.hide()
            self.CarID19btOut.hide()
            self.Car19Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car19Statelb.setAlignment(QtCore.Qt.AlignCenter)            
        if self.CarIDlabelData[18] != "N":
            self.Car19Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car19Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[19] == "N":
            self.CarID20btIN.hide()
            self.CarID20btOut.hide()
            self.Car20Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car20Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[19] != "N":
            self.Car20Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car20Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[20] == "N":
            self.CarID21btIN.hide()
            self.CarID21btOut.hide()
            self.Car21Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car21Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[20] != "N":
            self.Car21Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car21Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[21] == "N":
            self.CarID22btIN.hide()
            self.CarID22btOut.hide()
            self.Car22Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car22Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[21] != "N":
            self.Car22Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car22Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[22] == "N":
            self.CarID23btIN.hide()
            self.CarID23btOut.hide()
            self.Car23Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car23Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[22] != "N":
            self.Car23Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car23Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[23] == "N":
            self.CarID24btIN.hide()
            self.CarID24btOut.hide()
            self.Car24Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car24Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[23] != "N":
            self.Car24Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car24Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[24] == "N":
            self.CarID25btIN.hide()
            self.CarID25btOut.hide()
            self.Car25Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car25Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[24] != "N":
            self.Car25Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car25Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[25] == "N":
            self.CarID26btIN.hide()
            self.CarID26btOut.hide()
            self.Car26Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car26Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[25] != "N":
            self.Car26Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car26Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[26] == "N":
            self.CarID27btIN.hide()
            self.CarID27btOut.hide()
            self.Car27Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car27Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[26] != "N":
            self.Car27Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car27Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[27] == "N":
            self.CarID28btIN.hide()
            self.CarID28btOut.hide()
            self.Car28Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car28Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[27] != "N":
            self.Car28Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car28Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[28] == "N":
            self.CarID29btIN.hide()
            self.CarID29btOut.hide()
            self.Car29Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car29Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[28] != "N":
            self.Car29Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car29Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[29] == "N":
            self.CarID30btIN.hide()
            self.CarID30btOut.hide()
            self.Car30Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car30Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[29] != "N":
            self.Car30Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car30Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[30] == "N":
            self.CarID31btIN.hide()
            self.CarID31btOut.hide()
            self.Car31Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car31Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[30] != "N":
            self.Car31Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car31Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[31] == "N":
            self.CarID32btIN.hide()
            self.CarID32btOut.hide()
            self.Car32Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car32Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[31] != "N":
            self.Car32Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car32Statelb.setAlignment(QtCore.Qt.AlignCenter)    
        
        if self.CarIDlabelData[32] == "N":
            self.CarID33btIN.hide()
            self.CarID33btOut.hide()
            self.Car33Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car33Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[32] != "N":
            self.Car33Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car33Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[33] == "N":
            self.CarID34btIN.hide()
            self.CarID34btOut.hide()
            self.Car34Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car34Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[33] != "N":
            self.Car34Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car34Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[34] == "N":
            self.CarID35btIN.hide()
            self.CarID35btOut.hide()
            self.Car35Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car35Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[34] != "N":
            self.Car35Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car35Statelb.setAlignment(QtCore.Qt.AlignCenter)       
        
        if self.CarIDlabelData[35] == "N":
            self.CarID36btIN.hide()
            self.CarID36btOut.hide()
            self.Car36Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car36Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[35] != "N":
            self.Car36Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car36Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[36] == "N":
            self.CarID37btIN.hide()
            self.CarID37btOut.hide()
            self.Car37Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car37Statelb.setAlignment(QtCore.Qt.AlignCenter)   
        if self.CarIDlabelData[36] != "N":
            self.Car37Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car37Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[37] == "N":
            self.CarID38btIN.hide()
            self.CarID38btOut.hide()
            self.Car38Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car38Statelb.setAlignment(QtCore.Qt.AlignCenter)   
        if self.CarIDlabelData[37] != "N":
            self.Car38Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car38Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[38] == "N":
            self.CarID39btIN.hide()
            self.CarID39btOut.hide()
            self.Car39Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car39Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[38] != "N":
            self.Car39Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car39Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        if self.CarIDlabelData[39] == "N":
            self.CarID40btIN.hide()
            self.CarID40btOut.hide()
            self.Car40Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
            self.Car40Statelb.setAlignment(QtCore.Qt.AlignCenter)
        if self.CarIDlabelData[39] != "N":
            self.Car40Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car40Statelb.setAlignment(QtCore.Qt.AlignCenter)
        
        #print(str(self.CarIDlabelData[0]) == "N")
        self.RFIDaidm1.setText(str(self.rfidmodulename[0]))
        self.RFIDaidm1.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm2.setText(str(self.rfidmodulename[1]))
        self.RFIDaidm2.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm3.setText(str(self.rfidmodulename[2]))
        self.RFIDaidm3.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm4.setText(str(self.rfidmodulename[3]))
        self.RFIDaidm4.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm5.setText(str(self.rfidmodulename[4]))
        self.RFIDaidm5.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm6.setText(str(self.rfidmodulename[5]))
        self.RFIDaidm6.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm7.setText(str(self.rfidmodulename[6]))
        self.RFIDaidm7.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm8.setText(str(self.rfidmodulename[7]))
        self.RFIDaidm8.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm9.setText(str(self.rfidmodulename[8]))
        self.RFIDaidm9.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm10.setText(str(self.rfidmodulename[9]))
        self.RFIDaidm10.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm11.setText(str(self.rfidmodulename[10]))
        self.RFIDaidm11.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm12.setText(str(self.rfidmodulename[11]))
        self.RFIDaidm12.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm13.setText(str(self.rfidmodulename[12]))
        self.RFIDaidm13.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm14.setText(str(self.rfidmodulename[13]))
        self.RFIDaidm14.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm15.setText(str(self.rfidmodulename[14]))
        self.RFIDaidm15.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm16.setText(str(self.rfidmodulename[15]))
        self.RFIDaidm16.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm17.setText(str(self.rfidmodulename[16]))
        self.RFIDaidm17.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm18.setText(str(self.rfidmodulename[17]))
        self.RFIDaidm18.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm19.setText(str(self.rfidmodulename[18]))
        self.RFIDaidm19.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDaidm20.setText(str(self.rfidmodulename[19]))
        self.RFIDaidm20.setAlignment(QtCore.Qt.AlignCenter)
        
        self.RFIDnote1.setText(str(self.rfidnote[0]))
        self.RFIDnote1.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote2.setText(str(self.rfidnote[1]))
        self.RFIDnote2.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote3.setText(str(self.rfidnote[2]))
        self.RFIDnote3.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote4.setText(str(self.rfidnote[3]))
        self.RFIDnote4.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote5.setText(str(self.rfidnote[4]))
        self.RFIDnote5.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote6.setText(str(self.rfidnote[5]))
        self.RFIDnote6.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote7.setText(str(self.rfidnote[6]))
        self.RFIDnote7.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote8.setText(str(self.rfidnote[7]))
        self.RFIDnote8.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote9.setText(str(self.rfidnote[8]))
        self.RFIDnote9.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote10.setText(str(self.rfidnote[9]))
        self.RFIDnote10.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote11.setText(str(self.rfidnote[10]))
        self.RFIDnote11.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote12.setText(str(self.rfidnote[11]))
        self.RFIDnote12.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote13.setText(str(self.rfidnote[12]))
        self.RFIDnote13.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote14.setText(str(self.rfidnote[13]))
        self.RFIDnote14.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote15.setText(str(self.rfidnote[14]))
        self.RFIDnote15.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote16.setText(str(self.rfidnote[15]))
        self.RFIDnote16.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote17.setText(str(self.rfidnote[16]))
        self.RFIDnote17.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote18.setText(str(self.rfidnote[17]))
        self.RFIDnote18.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote19.setText(str(self.rfidnote[18]))
        self.RFIDnote19.setAlignment(QtCore.Qt.AlignCenter)
        self.RFIDnote20.setText(str(self.rfidnote[19]))
        self.RFIDnote20.setAlignment(QtCore.Qt.AlignCenter)
        
        #Car ID 표시
        self.Caridlb_a1.setText(str(self.CarIDlabelData[0]))
        self.Caridlb_a2.setText(str(self.CarIDlabelData[1]))
        self.Caridlb_a3.setText(str(self.CarIDlabelData[2]))
        self.Caridlb_a4.setText(str(self.CarIDlabelData[3]))
        self.Caridlb_a5.setText(str(self.CarIDlabelData[4]))
        self.Caridlb_a6.setText(str(self.CarIDlabelData[5]))
        self.Caridlb_a7.setText(str(self.CarIDlabelData[6]))
        self.Caridlb_a8.setText(str(self.CarIDlabelData[7]))
        self.Caridlb_a9.setText(str(self.CarIDlabelData[8]))
        self.Caridlb_a0.setText(str(self.CarIDlabelData[9]))
        self.Caridlb_b1.setText(str(self.CarIDlabelData[10]))
        self.Caridlb_b2.setText(str(self.CarIDlabelData[11]))
        self.Caridlb_b3.setText(str(self.CarIDlabelData[12]))
        self.Caridlb_b4.setText(str(self.CarIDlabelData[13]))
        self.Caridlb_b5.setText(str(self.CarIDlabelData[14]))
        self.Caridlb_b6.setText(str(self.CarIDlabelData[15]))
        self.Caridlb_b7.setText(str(self.CarIDlabelData[16]))
        self.Caridlb_b8.setText(str(self.CarIDlabelData[17]))
        self.Caridlb_b9.setText(str(self.CarIDlabelData[18]))
        self.Caridlb_b0.setText(str(self.CarIDlabelData[19]))
        self.Caridlb_c1.setText(str(self.CarIDlabelData[20]))
        self.Caridlb_c2.setText(str(self.CarIDlabelData[21]))
        self.Caridlb_c3.setText(str(self.CarIDlabelData[22]))
        self.Caridlb_c4.setText(str(self.CarIDlabelData[23]))
        self.Caridlb_c5.setText(str(self.CarIDlabelData[24]))
        self.Caridlb_c6.setText(str(self.CarIDlabelData[25]))
        self.Caridlb_c7.setText(str(self.CarIDlabelData[26]))
        self.Caridlb_c8.setText(str(self.CarIDlabelData[27]))
        self.Caridlb_c9.setText(str(self.CarIDlabelData[28]))
        self.Caridlb_c0.setText(str(self.CarIDlabelData[29]))
        self.Caridlb_d1.setText(str(self.CarIDlabelData[30]))
        self.Caridlb_d2.setText(str(self.CarIDlabelData[31]))
        self.Caridlb_d3.setText(str(self.CarIDlabelData[32]))
        self.Caridlb_d4.setText(str(self.CarIDlabelData[33]))
        self.Caridlb_d5.setText(str(self.CarIDlabelData[34]))
        self.Caridlb_d6.setText(str(self.CarIDlabelData[35]))
        self.Caridlb_d7.setText(str(self.CarIDlabelData[36]))
        self.Caridlb_d8.setText(str(self.CarIDlabelData[37]))
        self.Caridlb_d9.setText(str(self.CarIDlabelData[38]))
        self.Caridlb_d0.setText(str(self.CarIDlabelData[39]))
        #Car name 표시
        #self.A1Carnamelb.setText(str(self.CarHWname[0]))

        #모듈 주소 표시
        self.M01IPlb.setText(str(self.RfidmoduleIP[0]))
        self.M01IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M02IPlb.setText(str(self.RfidmoduleIP[1]))
        self.M02IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M03IPlb.setText(str(self.RfidmoduleIP[2]))
        self.M03IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M04IPlb.setText(str(self.RfidmoduleIP[3]))
        self.M04IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M05IPlb.setText(str(self.RfidmoduleIP[4]))
        self.M05IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M06IPlb.setText(str(self.RfidmoduleIP[5]))
        self.M06IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M07IPlb.setText(str(self.RfidmoduleIP[6]))
        self.M07IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M08IPlb.setText(str(self.RfidmoduleIP[7]))
        self.M08IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M09IPlb.setText(str(self.RfidmoduleIP[8]))
        self.M09IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M10IPlb.setText(str(self.RfidmoduleIP[9]))
        self.M10IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M11IPlb.setText(str(self.RfidmoduleIP[10]))
        self.M11IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M12IPlb.setText(str(self.RfidmoduleIP[11]))
        self.M12IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M13IPlb.setText(str(self.RfidmoduleIP[12]))
        self.M13IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M14IPlb.setText(str(self.RfidmoduleIP[13]))
        self.M14IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M15IPlb.setText(str(self.RfidmoduleIP[14]))
        self.M15IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M16IPlb.setText(str(self.RfidmoduleIP[15]))
        self.M16IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M17IPlb.setText(str(self.RfidmoduleIP[16]))
        self.M17IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M18IPlb.setText(str(self.RfidmoduleIP[17]))
        self.M18IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M19IPlb.setText(str(self.RfidmoduleIP[18]))
        self.M19IPlb.setAlignment(QtCore.Qt.AlignCenter)
        self.M20IPlb.setText(str(self.RfidmoduleIP[19]))
        self.M20IPlb.setAlignment(QtCore.Qt.AlignCenter)
        
        # 초기 화면
        """
        self.Car1Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car1Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car2Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car2Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car3Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car3Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car4Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car4Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car5Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car5Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car6Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car6Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car7Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car7Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car8Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car8Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car9Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car9Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car10Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car10Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car11Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car11Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car12Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car12Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car13Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car13Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car14Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car14Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car15Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car15Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car16Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car16Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car17Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car17Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car18Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car18Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car19Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car19Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car20Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car20Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car21Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car21Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car22Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car22Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car23Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car23Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car24Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car24Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car25Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car25Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car26Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car26Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car27Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car27Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car28Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car28Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car29Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car29Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car30Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car30Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car31Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car31Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car32Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car32Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car33Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car33Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car34Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car34Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car35Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car35Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car36Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car36Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car37Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car37Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car38Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car38Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car39Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car39Statelb.setAlignment(QtCore.Qt.AlignCenter)
        self.Car40Statelb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.Car40Statelb.setAlignment(QtCore.Qt.AlignCenter)
        """
        self.marklb.setPixmap(QtGui.QPixmap("state_green.png"))
        self.marklb.setAlignment(QtCore.Qt.AlignCenter)
        self.marklb1.setPixmap(QtGui.QPixmap("state_white.png"))
        self.marklb1.setAlignment(QtCore.Qt.AlignCenter)
        self.marklb2.setPixmap(QtGui.QPixmap("state_red.png"))
        self.marklb2.setAlignment(QtCore.Qt.AlignCenter)
        
        # 모듈 상태 표시
        self.StateM01lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM01lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM02lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM02lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM03lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM03lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM04lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM04lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM05lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM05lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM06lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM06lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM07lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM07lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM08lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM08lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM09lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM09lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM10lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM10lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM11lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM11lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM12lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM12lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM13lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM13lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM14lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM14lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM15lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM15lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM16lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM16lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM17lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM17lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM18lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM18lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM19lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM19lb.setAlignment(QtCore.Qt.AlignCenter)
        self.StateM20lb.setPixmap(QtGui.QPixmap("state_black.png"))
        self.StateM20lb.setAlignment(QtCore.Qt.AlignCenter)
        
        self.A1timerlb.setText("N")
        self.A1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A2timerlb.setText("N")
        self.A2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A3timerlb.setText("N")
        self.A3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A4timerlb.setText("N")
        self.A4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A5timerlb.setText("N")
        self.A5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A6timerlb.setText("N")
        self.A6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A7timerlb.setText("N")
        self.A7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A8timerlb.setText("N")
        self.A8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A9timerlb.setText("N")
        self.A9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.A0timerlb.setText("N")
        self.A0timerlb.setAlignment(QtCore.Qt.AlignCenter)

        self.B1timerlb.setText("N")
        self.B1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B2timerlb.setText("N")
        self.B2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B3timerlb.setText("N")
        self.B3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B4timerlb.setText("N")
        self.B4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B5timerlb.setText("N")
        self.B5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B6timerlb.setText("N")
        self.B6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B7timerlb.setText("N")
        self.B7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B8timerlb.setText("N")
        self.B8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B9timerlb.setText("N")
        self.B9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.B0timerlb.setText("N")
        self.B0timerlb.setAlignment(QtCore.Qt.AlignCenter)

        self.C1timerlb.setText("N")
        self.C1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C2timerlb.setText("N")
        self.C2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C3timerlb.setText("N")
        self.C3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C4timerlb.setText("N")
        self.C4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C5timerlb.setText("N")
        self.C5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C6timerlb.setText("N")
        self.C6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C7timerlb.setText("N")
        self.C7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C8timerlb.setText("N")
        self.C8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C9timerlb.setText("N")
        self.C9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.C0timerlb.setText("N")
        self.C0timerlb.setAlignment(QtCore.Qt.AlignCenter)

        self.D1timerlb.setText("N")
        self.D1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D2timerlb.setText("N")
        self.D2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D3timerlb.setText("N")
        self.D3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D4timerlb.setText("N")
        self.D4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D5timerlb.setText("N")
        self.D5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D6timerlb.setText("N")
        self.D6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D7timerlb.setText("N")
        self.D7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D8timerlb.setText("N")
        self.D8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D9timerlb.setText("N")
        self.D9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        self.D0timerlb.setText("N")
        self.D0timerlb.setAlignment(QtCore.Qt.AlignCenter)

        # 자동차 이름 표시
        self.A1Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A2Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A3Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A4Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A5Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A6Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A7Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A8Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A9Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.A0Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        
        self.B1Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B2Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B3Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B4Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B5Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B6Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B7Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B8Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B9Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.B0Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        
        self.C1Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C2Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C3Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C4Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C5Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C6Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C7Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C8Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C9Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C10Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C11Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C12Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C13Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C14Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C15Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C16Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C17Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C18Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C19Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
        self.C20Carnamelb.setAlignment(QtCore.Qt.AlignCenter)

        
        # 입고 관련 이벤트
        self.CarID1btIN.clicked.connect(self.CarID1btIN_Popupcall)
        self.CarID2btIN.clicked.connect(self.CarID2btIN_Popupcall)
        self.CarID3btIN.clicked.connect(self.CarID3btIN_Popupcall)
        self.CarID4btIN.clicked.connect(self.CarID4btIN_Popupcall)
        self.CarID5btIN.clicked.connect(self.CarID5btIN_Popupcall)
        self.CarID6btIN.clicked.connect(self.CarID6btIN_Popupcall)
        self.CarID7btIN.clicked.connect(self.CarID7btIN_Popupcall)
        self.CarID8btIN.clicked.connect(self.CarID8btIN_Popupcall)
        self.CarID9btIN.clicked.connect(self.CarID9btIN_Popupcall)
        self.CarID10btIN.clicked.connect(self.CarID10btIN_Popupcall)
        self.CarID11btIN.clicked.connect(self.CarID11btIN_Popupcall)
        self.CarID12btIN.clicked.connect(self.CarID12btIN_Popupcall)
        self.CarID13btIN.clicked.connect(self.CarID13btIN_Popupcall)
        self.CarID14btIN.clicked.connect(self.CarID14btIN_Popupcall)
        self.CarID15btIN.clicked.connect(self.CarID15btIN_Popupcall)
        self.CarID16btIN.clicked.connect(self.CarID16btIN_Popupcall)
        self.CarID17btIN.clicked.connect(self.CarID17btIN_Popupcall)
        self.CarID18btIN.clicked.connect(self.CarID18btIN_Popupcall)
        self.CarID19btIN.clicked.connect(self.CarID19btIN_Popupcall)
        self.CarID20btIN.clicked.connect(self.CarID20btIN_Popupcall)
        self.CarID21btIN.clicked.connect(self.CarID21btIN_Popupcall)
        self.CarID22btIN.clicked.connect(self.CarID22btIN_Popupcall)
        self.CarID23btIN.clicked.connect(self.CarID23btIN_Popupcall)
        self.CarID24btIN.clicked.connect(self.CarID24btIN_Popupcall)
        self.CarID25btIN.clicked.connect(self.CarID25btIN_Popupcall)
        # 추가 버튼
        self.CarID26btIN.clicked.connect(self.CarID26btIN_Popupcall)
        """
        self.CarID27btIN.clicked.connect(self.CarID27btIN_Popupcall)
        self.CarID28btIN.clicked.connect(self.CarID28btIN_Popupcall)
        self.CarID29btIN.clicked.connect(self.CarID29btIN_Popupcall)
        self.CarID30btIN.clicked.connect(self.CarID30btIN_Popupcall)
        self.CarID31btIN.clicked.connect(self.CarID31btIN_Popupcall)
        self.CarID32btIN.clicked.connect(self.CarID32btIN_Popupcall)
        self.CarID33btIN.clicked.connect(self.CarID33btIN_Popupcall)
        self.CarID34btIN.clicked.connect(self.CarID34btIN_Popupcall)
        self.CarID35btIN.clicked.connect(self.CarID35btIN_Popupcall)
        self.CarID36btIN.clicked.connect(self.CarID36btIN_Popupcall)
        self.CarID37btIN.clicked.connect(self.CarID37btIN_Popupcall)
        self.CarID38btIN.clicked.connect(self.CarID38btIN_Popupcall)
        self.CarID39btIN.clicked.connect(self.CarID39btIN_Popupcall)
        self.CarID40btIN.clicked.connect(self.CarID40btIN_Popupcall)
        """
        # 출고 관련 이벤트
        self.CarID1btOut.clicked.connect(self.CarID1btOut_Popupcall)
        self.CarID2btOut.clicked.connect(self.CarID2btOut_Popupcall)
        self.CarID3btOut.clicked.connect(self.CarID3btOut_Popupcall)
        self.CarID4btOut.clicked.connect(self.CarID4btOut_Popupcall)
        self.CarID5btOut.clicked.connect(self.CarID5btOut_Popupcall)
        self.CarID6btOut.clicked.connect(self.CarID6btOut_Popupcall)
        self.CarID7btOut.clicked.connect(self.CarID7btOut_Popupcall)
        self.CarID8btOut.clicked.connect(self.CarID8btOut_Popupcall)
        self.CarID9btOut.clicked.connect(self.CarID9btOut_Popupcall)
        self.CarID10btOut.clicked.connect(self.CarID10btOut_Popupcall)
        self.CarID11btOut.clicked.connect(self.CarID11btOut_Popupcall)
        self.CarID12btOut.clicked.connect(self.CarID12btOut_Popupcall)
        self.CarID13btOut.clicked.connect(self.CarID13btOut_Popupcall)
        self.CarID14btOut.clicked.connect(self.CarID14btOut_Popupcall)
        self.CarID15btOut.clicked.connect(self.CarID15btOut_Popupcall)
        self.CarID16btOut.clicked.connect(self.CarID16btOut_Popupcall)
        self.CarID17btOut.clicked.connect(self.CarID17btOut_Popupcall)
        self.CarID18btOut.clicked.connect(self.CarID18btOut_Popupcall)
        self.CarID19btOut.clicked.connect(self.CarID19btOut_Popupcall)
        self.CarID20btOut.clicked.connect(self.CarID20btOut_Popupcall)
        self.CarID21btOut.clicked.connect(self.CarID21btOut_Popupcall)
        self.CarID22btOut.clicked.connect(self.CarID22btOut_Popupcall)
        self.CarID23btOut.clicked.connect(self.CarID23btOut_Popupcall)
        self.CarID24btOut.clicked.connect(self.CarID24btOut_Popupcall)
        self.CarID25btOut.clicked.connect(self.CarID25btOut_Popupcall)
        # 추가 버튼
        self.CarID26btOut.clicked.connect(self.CarID26btOut_Popupcall)
        self.CarID27btOut.clicked.connect(self.CarID27btOut_Popupcall)
        self.CarID28btOut.clicked.connect(self.CarID28btOut_Popupcall)
        self.CarID29btOut.clicked.connect(self.CarID29btOut_Popupcall)
        self.CarID30btOut.clicked.connect(self.CarID30btOut_Popupcall)
        self.CarID31btOut.clicked.connect(self.CarID31btOut_Popupcall)
        self.CarID32btOut.clicked.connect(self.CarID32btOut_Popupcall)
        self.CarID33btOut.clicked.connect(self.CarID33btOut_Popupcall)
        self.CarID34btOut.clicked.connect(self.CarID34btOut_Popupcall)
        self.CarID35btOut.clicked.connect(self.CarID35btOut_Popupcall)
        self.CarID36btOut.clicked.connect(self.CarID36btOut_Popupcall)
        self.CarID37btOut.clicked.connect(self.CarID37btOut_Popupcall)
        self.CarID38btOut.clicked.connect(self.CarID38btOut_Popupcall)
        self.CarID39btOut.clicked.connect(self.CarID39btOut_Popupcall)
        self.CarID40btOut.clicked.connect(self.CarID40btOut_Popupcall)
        # 입고 시간 체크 관련 타이머 활성화
        #1
        self.time_left_int = 0
        self.timercnt = 0
        self.myTimer = QtCore.QTimer(self)
        #2
        self.time_left_int1 = 0
        self.timercnt1 = 0
        self.myTimer1 = QtCore.QTimer(self)
        #3
        self.time_left_int2 = 0
        self.timercnt2 = 0
        self.myTimer2 = QtCore.QTimer(self)
        #4
        self.time_left_int3 = 0
        self.timercnt3 = 0
        self.myTimer3 = QtCore.QTimer(self)
        #5    
        self.time_left_int4 = 0
        self.timercnt4 = 0
        self.myTimer4 = QtCore.QTimer(self)
        #6
        self.time_left_int5 = 0
        self.timercnt5 = 0
        self.myTimer5 = QtCore.QTimer(self)
        #7
        self.time_left_int6 = 0
        self.timercnt6 = 0
        self.myTimer6 = QtCore.QTimer(self)
        #8
        self.time_left_int7 = 0
        self.timercnt7 = 0
        self.myTimer7 = QtCore.QTimer(self)
        #9
        self.time_left_int8 = 0
        self.timercnt8 = 0
        self.myTimer8 = QtCore.QTimer(self)
        #10
        self.time_left_int9 = 0
        self.timercnt9 = 0
        self.myTimer9 = QtCore.QTimer(self)
        #11
        self.time_left_int10 = 0
        self.timercnt10 = 0
        self.myTimer10 = QtCore.QTimer(self)
        #12
        self.time_left_int11 = 0
        self.timercnt11 = 0
        self.myTimer11 = QtCore.QTimer(self)
        #13
        self.time_left_int12 = 0
        self.timercnt12 = 0
        self.myTimer12 = QtCore.QTimer(self)
        #14
        self.time_left_int13 = 0
        self.timercnt13 = 0
        self.myTimer13 = QtCore.QTimer(self)
        #15
        self.time_left_int14 = 0
        self.timercnt14 = 0
        self.myTimer14 = QtCore.QTimer(self)
        #16
        self.time_left_int15 = 0
        self.timercnt15 = 0
        self.myTimer15 = QtCore.QTimer(self)
        #17
        self.time_left_int16 = 0
        self.timercnt16 = 0
        self.myTimer16 = QtCore.QTimer(self)
        #18
        self.time_left_int17 = 0
        self.timercnt17 = 0
        self.myTimer17 = QtCore.QTimer(self)
        #19
        self.time_left_int18 = 0
        self.timercnt18 = 0
        self.myTimer18 = QtCore.QTimer(self)
        #20
        self.time_left_int19 = 0
        self.timercnt19 = 0
        self.myTimer19 = QtCore.QTimer(self)
        #21
        self.time_left_int20 = 0
        self.timercnt20 = 0
        self.myTimer20 = QtCore.QTimer(self)
        #22
        self.time_left_int21 = 0
        self.timercnt21 = 0
        self.myTimer21 = QtCore.QTimer(self)
        #23
        self.time_left_int22 = 0
        self.timercnt22 = 0
        self.myTimer22 = QtCore.QTimer(self)
        #24
        self.time_left_int23 = 0
        self.timercnt23 = 0
        self.myTimer23 = QtCore.QTimer(self)
        #25
        self.time_left_int24 = 0
        self.timercnt24 = 0
        self.myTimer24 = QtCore.QTimer(self)
        #26
        self.time_left_int25 = 0
        self.timercnt25 = 0
        self.myTimer25 = QtCore.QTimer(self)
        #27
        self.time_left_int26 = 0
        self.timercnt26 = 0
        self.myTimer26 = QtCore.QTimer(self)
        #28
        self.time_left_int27 = 0
        self.timercnt27 = 0
        self.myTimer27 = QtCore.QTimer(self)
        #29
        self.time_left_int28 = 0
        self.timercnt28 = 0
        self.myTimer28 = QtCore.QTimer(self)
        #30
        self.time_left_int29 = 0
        self.timercnt29 = 0
        self.myTimer29 = QtCore.QTimer(self)
        #31
        self.time_left_int30 = 0
        self.timercnt30 = 0
        self.myTimer30 = QtCore.QTimer(self)
        #32
        self.time_left_int31 = 0
        self.timercnt31 = 0
        self.myTimer31 = QtCore.QTimer(self)
        #33
        self.time_left_int32 = 0
        self.timercnt32 = 0
        self.myTimer32 = QtCore.QTimer(self)
        #34
        self.time_left_int33 = 0
        self.timercnt33 = 0
        self.myTimer33 = QtCore.QTimer(self)
        #35
        self.time_left_int34 = 0
        self.timercnt34 = 0
        self.myTimer34 = QtCore.QTimer(self)
        #36
        self.time_left_int35 = 0
        self.timercnt35 = 0
        self.myTimer35 = QtCore.QTimer(self)
        #37
        self.time_left_int36 = 0
        self.timercnt36 = 0
        self.myTimer36 = QtCore.QTimer(self)
        #38
        self.time_left_int37 = 0
        self.timercnt37 = 0
        self.myTimer37 = QtCore.QTimer(self)
        #39
        self.time_left_int38 = 0
        self.timercnt38 = 0
        self.myTimer38 = QtCore.QTimer(self)
        #40
        self.time_left_int39 = 0
        self.timercnt39 = 0
        self.myTimer39 = QtCore.QTimer(self)
        
        self.csvread = DataCsv()
        
        for reset in range(1,41):
            self.csvread.Data_User_state_write(str(reset), 0)
            self.loadButtoninit = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtoninit)

    
    def printTime(self):
        global timeval
        timeval += 1
        if timeval == 5:       # 30  5
           self.rfidmodulecsv = DataCsv()
           self.RfidmoduleState =  self.rfidmodulecsv.Data_Module_State_Read()
           self.AntennaState = self.rfidmodulecsv.Date_Antenna_State_Read()
           
           # 중계기 1번 안테나 모듈 1
           if int(self.RfidmoduleState[0]) == 1 and int(self.AntennaState[0]) == 1:
                self.StateM01lb.setPixmap(QtGui.QPixmap("state_green.png"))
                self.StateM01lb.setAlignment(QtCore.Qt.AlignCenter)
           
           if int(self.RfidmoduleState[0]) == 1 and int(self.AntennaState[0]) == 2:
                self.StateM01lb.setPixmap(QtGui.QPixmap("state_orange.png"))
                self.StateM01lb.setAlignment(QtCore.Qt.AlignCenter)

           if int(self.RfidmoduleState[0]) == 2:
                self.StateM01lb.setPixmap(QtGui.QPixmap("state_red.png"))
                self.StateM01lb.setAlignment(QtCore.Qt.AlignCenter)

           # 중계기 1번 안테나 모듈 2 
           if int(self.RfidmoduleState[1]) == 1 and int(self.AntennaState[1]) == 1:
                self.StateM02lb.setPixmap(QtGui.QPixmap("state_green.png"))
                self.StateM02lb.setAlignment(QtCore.Qt.AlignCenter)
           
           if int(self.RfidmoduleState[1]) == 1 and int(self.AntennaState[1]) == 2:
                self.StateM02lb.setPixmap(QtGui.QPixmap("state_orange.png"))
                self.StateM02lb.setAlignment(QtCore.Qt.AlignCenter)
            
           if int(self.RfidmoduleState[1]) == 2:
                self.StateM02lb.setPixmap(QtGui.QPixmap("state_red.png"))
                self.StateM02lb.setAlignment(QtCore.Qt.AlignCenter)
           
           # 중계기 2번 안테나 모듈 1
           if int(self.RfidmoduleState[2]) == 1 and int(self.AntennaState[2]) == 1:
                self.StateM03lb.setPixmap(QtGui.QPixmap("state_green.png"))
                self.StateM03lb.setAlignment(QtCore.Qt.AlignCenter)
           
           if int(self.RfidmoduleState[2]) == 1 and int(self.AntennaState[2]) == 2:
                self.StateM03lb.setPixmap(QtGui.QPixmap("state_orange.png"))
                self.StateM03lb.setAlignment(QtCore.Qt.AlignCenter)
           
           if int(self.RfidmoduleState[2]) == 2:
                self.StateM03lb.setPixmap(QtGui.QPixmap("state_red.png"))
                self.StateM03lb.setAlignment(QtCore.Qt.AlignCenter)
           
           # 중계기 2번 안테나 모듈 2
           if int(self.RfidmoduleState[3]) == 1 and int(self.AntennaState[3]) == 1:
                self.StateM04lb.setPixmap(QtGui.QPixmap("state_green.png"))
                self.StateM04lb.setAlignment(QtCore.Qt.AlignCenter)
           
           if int(self.RfidmoduleState[3]) == 1 and int(self.AntennaState[3]) == 2:
                self.StateM04lb.setPixmap(QtGui.QPixmap("state_orange.png"))
                self.StateM04lb.setAlignment(QtCore.Qt.AlignCenter)
           
           if int(self.RfidmoduleState[3]) == 2:
                self.StateM04lb.setPixmap(QtGui.QPixmap("state_red.png"))
                self.StateM04lb.setAlignment(QtCore.Qt.AlignCenter)
           timeval = 0
           #return self.RfidmoduleState 
    ##### A1 timer ######
    def startTimer1(self,timermsg):
        self.time_left_int = timermsg + 1
        self.timercnt = 0
        self.myTimer = QtCore.QTimer(self)
        self.myTimer.setInterval(1000)
        self.myTimer.timeout.connect(self.timerTimeout1)
        self.myTimer.start()
    
    def timerTimeout1(self):
        self.timercnt += 1
        self.time_left_int_copy = self.time_left_int - self.timercnt
        self.minsec = secs_to_minsec(self.time_left_int_copy)
        # 차감되는 시간값을 저장??
        self.A1timerlb.setText(self.minsec)
        self.A1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy == 0:
            self.myTimer.stop()
            self.Car1Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car1Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ##### A2 timer #####
    def startTimer2(self, timermsg):
        self.time_left_int1 = timermsg + 1
        self.timercnt1 = 0
        self.myTimer1 = QtCore.QTimer(self)
        self.myTimer1.setInterval(1000)
        self.myTimer1.timeout.connect(self.timerTimeout2)
        self.myTimer1.start()
    
    def timerTimeout2(self):
        self.timercnt1 += 1
        self.time_left_int_copy1 = self.time_left_int1 - self.timercnt1
        self.minsec = secs_to_minsec(self.time_left_int_copy1)
        self.A2timerlb.setText(self.minsec)
        self.A2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy1 == 0:
            self.myTimer1.stop()
            self.Car2Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car2Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### A3 timer #####
    def startTimer3(self, timermsg):
        self.time_left_int2 = timermsg + 1
        self.timercnt2 = 0
        self.myTimer2 = QtCore.QTimer(self)
        self.myTimer2.setInterval(1000)
        self.myTimer2.timeout.connect(self.timerTimeout3)
        self.myTimer2.start()
        
    def timerTimeout3(self):
        self.timercnt2 += 1
        self.time_left_int_copy2 = self.time_left_int2 - self.timercnt2
        self.minsec = secs_to_minsec(self.time_left_int_copy2)
        self.A3timerlb.setText(self.minsec)
        self.A3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy2 == 0:
            self.myTimer2.stop()
            self.Car3Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car3Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### A4 timer #####
    def startTimer4(self, timermsg):
        self.time_left_int3 = timermsg + 1
        self.timercnt3 = 0
        self.myTimer3 = QtCore.QTimer(self)
        self.myTimer3.setInterval(1000)
        self.myTimer3.timeout.connect(self.timerTimeout4)
        self.myTimer3.start()
    
    def timerTimeout4(self):
        self.timercnt3 += 1
        self.time_left_int_copy3 = self.time_left_int3 - self.timercnt3
        self.minsec = secs_to_minsec(self.time_left_int_copy3)
        self.A4timerlb.setText(self.minsec)
        self.A4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy3 == 0:
            self.myTimer3.stop()
            self.Car4Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car4Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ###################
    ##### A5 timer #####
    def startTimer5(self, timermsg):
        self.time_left_int4 = timermsg + 1
        self.timercnt4 = 0
        self.myTimer4 = QtCore.QTimer(self)
        self.myTimer4.setInterval(1000)
        self.myTimer4.timeout.connect(self.timerTimeout5)
        self.myTimer4.start()
    
    def timerTimeout5(self):
        self.timercnt4 += 1
        self.time_left_int_copy4 = self.time_left_int4 - self.timercnt4
        self.minsec = secs_to_minsec(self.time_left_int_copy4)
        self.A5timerlb.setText(self.minsec)
        self.A5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy4 == 0:
            self.myTimer4.stop()
            self.Car5Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car5Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### A6 timer #####
    def startTimer6(self, timermsg):
        self.time_left_int5 = timermsg + 1
        self.timercnt5 = 0
        self.myTimer5 = QtCore.QTimer(self)
        self.myTimer5.setInterval(1000)
        self.myTimer5.timeout.connect(self.timerTimeout6)
        self.myTimer5.start()
    
    def timerTimeout6(self):
        self.timercnt5 += 1
        self.time_left_int_copy5 = self.time_left_int5 - self.timercnt5
        self.minsec = secs_to_minsec(self.time_left_int_copy5)
        self.A6timerlb.setText(self.minsec)
        self.A6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy5 == 0:
            self.myTimer5.stop()
            self.Car6Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car6Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### A7 timer #####
    def startTimer7(self, timermsg):
        self.time_left_int6 = timermsg + 1
        self.timercnt6 = 0
        self.myTimer6 = QtCore.QTimer(self)
        self.myTimer6.setInterval(1000)
        self.myTimer6.timeout.connect(self.timerTimeout7)
        self.myTimer6.start()
    
    def timerTimeout7(self):
        self.timercnt6 += 1
        self.time_left_int_copy6 = self.time_left_int6 - self.timercnt6
        self.minsec = secs_to_minsec(self.time_left_int_copy6)
        self.A7timerlb.setText(self.minsec)
        self.A7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy6 == 0:
            self.myTimer6.stop()
            self.Car7Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car7Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### A8 timer #####
    def startTimer8(self, timermsg):
        self.time_left_int7 = timermsg + 1
        self.timercnt7 = 0
        self.myTimer7 = QtCore.QTimer(self)
        self.myTimer7.setInterval(1000)
        self.myTimer7.timeout.connect(self.timerTimeout8)
        self.myTimer7.start()
    
    def timerTimeout8(self):
        self.timercnt7 += 1
        self.time_left_int_copy7 = self.time_left_int7 - self.timercnt7
        self.minsec = secs_to_minsec(self.time_left_int_copy7)
        self.A8timerlb.setText(self.minsec)
        self.A8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy7 == 0:
            self.myTimer7.stop()
            self.Car8Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car8Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### A9 timer #####
    def startTimer9(self, timermsg):
        self.time_left_int8 = timermsg + 1
        self.timercnt8 = 0
        self.myTimer8 = QtCore.QTimer(self)
        self.myTimer8.setInterval(1000)
        self.myTimer8.timeout.connect(self.timerTimeout9)
        self.myTimer8.start()
    
    def timerTimeout9(self):
        self.timercnt8 += 1
        self.time_left_int_copy8 = self.time_left_int8 - self.timercnt8
        self.minsec = secs_to_minsec(self.time_left_int_copy8)
        self.A9timerlb.setText(self.minsec)
        self.A9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy8 == 0:
            self.myTimer8.stop()
            self.Car9Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car9Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### A0 timer #####
    def startTimer10(self, timermsg):
        self.time_left_int9 = timermsg + 1
        self.timercnt9 = 0
        self.myTimer9 = QtCore.QTimer(self)
        self.myTimer9.setInterval(1000)
        self.myTimer9.timeout.connect(self.timerTimeout10)
        self.myTimer9.start()
    
    def timerTimeout10(self):
        self.timercnt9 += 1
        self.time_left_int_copy9 = self.time_left_int9 - self.timercnt9
        self.minsec = secs_to_minsec(self.time_left_int_copy9)
        self.A0timerlb.setText(self.minsec)
        self.A0timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy9 == 0:
            self.myTimer9.stop()
            self.Car10Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car10Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B1 timer #####
    def startTimer11(self, timermsg):
        self.time_left_int10 = timermsg + 1
        self.timercnt10 = 0
        self.myTimer10 = QtCore.QTimer(self)
        self.myTimer10.setInterval(1000)
        self.myTimer10.timeout.connect(self.timerTimeout11)
        self.myTimer10.start()
    
    def timerTimeout11(self):
        self.timercnt10 += 1
        self.time_left_int_copy10 = self.time_left_int10 - self.timercnt10
        self.minsec = secs_to_minsec(self.time_left_int_copy10)
        self.B1timerlb.setText(self.minsec)
        self.B1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy10 == 0:
            self.myTimer10.stop()
            self.Car11Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car11Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B2 timer #####
    def startTimer12(self, timermsg):
        self.time_left_int11 = timermsg + 1
        self.timercnt11 = 0
        self.myTimer11 = QtCore.QTimer(self)
        self.myTimer11.setInterval(1000)
        self.myTimer11.timeout.connect(self.timerTimeout12)
        self.myTimer11.start()
    
    def timerTimeout12(self):
        self.timercnt11 += 1
        self.time_left_int_copy11 = self.time_left_int11 - self.timercnt11
        self.minsec = secs_to_minsec(self.time_left_int_copy11)
        self.B2timerlb.setText(self.minsec)
        self.B2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy11 == 0:
            self.myTimer11.stop()
            self.Car12Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car12Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B3 timer #####
    def startTimer13(self, timermsg):
        self.time_left_int12 = timermsg + 1
        self.timercnt12 = 0
        self.myTimer12 = QtCore.QTimer(self)
        self.myTimer12.setInterval(1000)
        self.myTimer12.timeout.connect(self.timerTimeout13)
        self.myTimer12.start()
    
    def timerTimeout13(self):
        self.timercnt12 += 1
        self.time_left_int_copy12 = self.time_left_int12 - self.timercnt12
        self.minsec = secs_to_minsec(self.time_left_int_copy12)
        self.B3timerlb.setText(self.minsec)
        self.B3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy12 == 0:
            self.myTimer12.stop()
            self.Car13Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car13Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B4 timer #####
    def startTimer14(self, timermsg):
        self.time_left_int13 = timermsg + 1
        self.timercnt13 = 0
        self.myTimer13 = QtCore.QTimer(self)
        self.myTimer13.setInterval(1000)
        self.myTimer13.timeout.connect(self.timerTimeout14)
        self.myTimer13.start()
    
    def timerTimeout14(self):
        self.timercnt13 += 1
        self.time_left_int_copy13 = self.time_left_int13 - self.timercnt13
        self.minsec = secs_to_minsec(self.time_left_int_copy13)
        self.B4timerlb.setText(self.minsec)
        self.B4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy13 == 0:
            self.myTimer13.stop()
            self.Car14Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car14Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B5 timer #####
    def startTimer15(self, timermsg):
        self.time_left_int14 = timermsg + 1
        self.timercnt14 = 0
        self.myTimer14 = QtCore.QTimer(self)
        self.myTimer14.setInterval(1000)
        self.myTimer14.timeout.connect(self.timerTimeout15)
        self.myTimer14.start()
    
    def timerTimeout15(self):
        self.timercnt14 += 1
        self.time_left_int_copy14 = self.time_left_int14 - self.timercnt14
        self.minsec = secs_to_minsec(self.time_left_int_copy14)
        self.B5timerlb.setText(self.minsec)
        self.B5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy14 == 0:
            self.myTimer14.stop()
            self.Car15Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car15Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B6 timer #####
    def startTimer16(self, timermsg):
        self.time_left_int15 = timermsg + 1
        self.timercnt15 = 0
        self.myTimer15 = QtCore.QTimer(self)
        self.myTimer15.setInterval(1000)
        self.myTimer15.timeout.connect(self.timerTimeout16)
        self.myTimer15.start()
    
    def timerTimeout16(self):
        self.timercnt15 += 1
        self.time_left_int_copy15 = self.time_left_int15 - self.timercnt15
        self.minsec = secs_to_minsec(self.time_left_int_copy15)
        self.B6timerlb.setText(self.minsec)
        self.B6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy15 == 0:
            self.myTimer15.stop()
            self.Car16Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car16Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B7 timer #####
    def startTimer17(self, timermsg):
        self.time_left_int16 = timermsg + 1
        self.timercnt16 = 0
        self.myTimer16 = QtCore.QTimer(self)
        self.myTimer16.setInterval(1000)
        self.myTimer16.timeout.connect(self.timerTimeout17)
        self.myTimer16.start()
    
    def timerTimeout17(self):
        self.timercnt16 += 1
        self.time_left_int_copy16 = self.time_left_int16 - self.timercnt16
        self.minsec = secs_to_minsec(self.time_left_int_copy16)
        self.B7timerlb.setText(self.minsec)
        self.B7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy16 == 0:
            self.myTimer16.stop()
            self.Car17Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car17Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B8 timer #####
    def startTimer18(self, timermsg):
        self.time_left_int17 = timermsg + 1
        self.timercnt17 = 0
        self.myTimer17 = QtCore.QTimer(self)
        self.myTimer17.setInterval(1000)
        self.myTimer17.timeout.connect(self.timerTimeout18)
        self.myTimer17.start()
    
    def timerTimeout18(self):
        self.timercnt17 += 1
        self.time_left_int_copy17 = self.time_left_int17 - self.timercnt17
        self.minsec = secs_to_minsec(self.time_left_int_copy17)
        self.B8timerlb.setText(self.minsec)
        self.B8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy17 == 0:
            self.myTimer17.stop()
            self.Car18Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car18Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B9 timer #####
    def startTimer19(self, timermsg):
        self.time_left_int18 = timermsg + 1
        self.timercnt18 = 0
        self.myTimer18 = QtCore.QTimer(self)
        self.myTimer18.setInterval(1000)
        self.myTimer18.timeout.connect(self.timerTimeout19)
        self.myTimer18.start()
    
    def timerTimeout19(self):
        self.timercnt18 += 1
        self.time_left_int_copy18 = self.time_left_int18 - self.timercnt18
        self.minsec = secs_to_minsec(self.time_left_int_copy18)
        self.B9timerlb.setText(self.minsec)
        self.B9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy18 == 0:
            self.myTimer18.stop()
            self.Car19Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car19Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### B0 timer #####
    def startTimer20(self, timermsg):
        self.time_left_int19 = timermsg + 1
        self.timercnt19 = 0
        self.myTimer19 = QtCore.QTimer(self)
        self.myTimer19.setInterval(1000)
        self.myTimer19.timeout.connect(self.timerTimeout20)
        self.myTimer19.start()
    
    def timerTimeout20(self):
        self.timercnt19 += 1
        self.time_left_int_copy19 = self.time_left_int19 - self.timercnt19
        self.minsec = secs_to_minsec(self.time_left_int_copy19)
        self.B0timerlb.setText(self.minsec)
        self.B0timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy19 == 0:
            self.myTimer19.stop()
            self.Car20Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car20Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### C1 timer #####
    def startTimer21(self, timermsg):
        self.time_left_int20 = timermsg + 1
        self.timercnt20 = 0
        self.myTimer20 = QtCore.QTimer(self)
        self.myTimer20.setInterval(1000)
        self.myTimer20.timeout.connect(self.timerTimeout21)
        self.myTimer20.start()
    
    def timerTimeout21(self):
        self.timercnt20 += 1
        self.time_left_int_copy20 = self.time_left_int20 - self.timercnt20
        self.minsec = secs_to_minsec(self.time_left_int_copy20)
        self.C1timerlb.setText(self.minsec)
        self.C1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy20 == 0:
            self.myTimer20.stop()
            self.Car21Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car21Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### C2 timer #####
    def startTimer22(self, timermsg):
        self.time_left_int21 = timermsg + 1
        self.timercnt21 = 0
        self.myTimer21 = QtCore.QTimer(self)
        self.myTimer21.setInterval(1000)
        self.myTimer21.timeout.connect(self.timerTimeout22)
        self.myTimer21.start()
    
    def timerTimeout22(self):
        self.timercnt21 += 1
        self.time_left_int_copy21 = self.time_left_int21 - self.timercnt21
        self.minsec = secs_to_minsec(self.time_left_int_copy21)
        self.C2timerlb.setText(self.minsec)
        self.C2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy21 == 0:
            self.myTimer21.stop()
            self.Car22Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car22Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### C3 timer #####
    def startTimer23(self, timermsg):
        self.time_left_int22 = timermsg + 1
        self.timercnt22 = 0
        self.myTimer22 = QtCore.QTimer(self)
        self.myTimer22.setInterval(1000)
        self.myTimer22.timeout.connect(self.timerTimeout23)
        self.myTimer22.start()
    
    def timerTimeout23(self):
        self.timercnt22 += 1
        self.time_left_int_copy22 = self.time_left_int22 - self.timercnt22
        self.minsec = secs_to_minsec(self.time_left_int_copy22)
        self.C3timerlb.setText(self.minsec)
        self.C3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy22 == 0:
            self.myTimer22.stop()
            self.Car23Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car23Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### C4 timer #####
    def startTimer24(self, timermsg):
        self.time_left_int23 = timermsg + 1
        self.timercnt23 = 0
        self.myTimer23 = QtCore.QTimer(self)
        self.myTimer23.setInterval(1000)
        self.myTimer23.timeout.connect(self.timerTimeout24)
        self.myTimer23.start()
    
    def timerTimeout24(self):
        self.timercnt23 += 1
        self.time_left_int_copy23 = self.time_left_int23 - self.timercnt23
        self.minsec = secs_to_minsec(self.time_left_int_copy23)
        self.C4timerlb.setText(self.minsec)
        self.C4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy23 == 0:
            self.myTimer23.stop()
            self.Car24Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car24Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ####################
    ##### C5 timer #####
    def startTimer25(self, timermsg):
        self.time_left_int24 = timermsg + 1
        self.timercnt24 = 0
        self.myTimer24 = QtCore.QTimer(self)
        self.myTimer24.setInterval(1000)
        self.myTimer24.timeout.connect(self.timerTimeout25)
        self.myTimer24.start()
    
    def timerTimeout25(self):
        self.timercnt24 += 1
        self.time_left_int_copy24 = self.time_left_int24 - self.timercnt24
        self.minsec = secs_to_minsec(self.time_left_int_copy24)
        self.C5timerlb.setText(self.minsec)
        self.C5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy24 == 0:
            self.myTimer24.stop()
            self.Car25Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car25Statelb.setAlignment(QtCore.Qt.AlignCenter)
    ###################
    ##### 26 timer #####
    def startTimer26(self, timermsg):
        self.time_left_int25 = timermsg + 1
        self.timercnt25 = 0
        self.myTimer25 = QtCore.QTimer(self)
        self.myTimer25.setInterval(1000)
        self.myTimer25.timeout.connect(self.timerTimeout26)
        self.myTimer25.start()
    
    def timerTimeout26(self):
        self.timercnt25 += 1
        self.time_left_int_copy25 = self.time_left_int25 - self.timercnt25
        self.minsec = secs_to_minsec(self.time_left_int_copy25)
        self.C6timerlb.setText(self.minsec)
        self.C6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy25 == 0:
            self.myTimer25.stop()
            self.Car26Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car26Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 27 timer #####
    def startTimer27(self, timermsg):
        self.time_left_int26 = timermsg + 1
        self.timercnt26 = 0
        self.myTimer26 = QtCore.QTimer(self)
        self.myTimer26.setInterval(1000)
        self.myTimer26.timeout.connect(self.timerTimeout27)
        self.myTimer26.start()
    
    def timerTimeout27(self):
        self.timercnt26 += 1
        self.time_left_int_copy26 = self.time_left_int26 - self.timercnt26
        self.minsec = secs_to_minsec(self.time_left_int_copy26)
        self.C7timerlb.setText(self.minsec)
        self.C7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy26 == 0:
            self.myTimer26.stop()
            self.Car27Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car27Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 28 timer #####
    def startTimer28(self, timermsg):
        self.time_left_int27 = timermsg + 1
        self.timercnt27 = 0
        self.myTimer27 = QtCore.QTimer(self)
        self.myTimer27.setInterval(1000)
        self.myTimer27.timeout.connect(self.timerTimeout28)
        self.myTimer27.start()
    
    def timerTimeout28(self):
        self.timercnt27 += 1
        self.time_left_int_copy27 = self.time_left_int27 - self.timercnt27
        self.minsec = secs_to_minsec(self.time_left_int_copy27)
        self.C8timerlb.setText(self.minsec)
        self.C8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy27 == 0:
            self.myTimer27.stop()
            self.Car28Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car28Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 29 timer #####
    def startTimer29(self, timermsg):
        self.time_left_int28 = timermsg + 1
        self.timercnt28 = 0
        self.myTimer28 = QtCore.QTimer(self)
        self.myTimer28.setInterval(1000)
        self.myTimer28.timeout.connect(self.timerTimeout29)
        self.myTimer28.start()
    
    def timerTimeout29(self):
        self.timercnt28 += 1
        self.time_left_int_copy28 = self.time_left_int28 - self.timercnt28
        self.minsec = secs_to_minsec(self.time_left_int_copy28)
        self.C9timerlb.setText(self.minsec)
        self.C9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy28 == 0:
            self.myTimer28.stop()
            self.Car29Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car29Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 30 timer #####
    def startTimer30(self, timermsg):
        self.time_left_int29 = timermsg + 1
        self.timercnt29 = 0
        self.myTimer29 = QtCore.QTimer(self)
        self.myTimer29.setInterval(1000)
        self.myTimer29.timeout.connect(self.timerTimeout30)
        self.myTimer29.start()
    
    def timerTimeout30(self):
        self.timercnt29 += 1
        self.time_left_int_copy29 = self.time_left_int29 - self.timercnt29
        self.minsec = secs_to_minsec(self.time_left_int_copy29)
        self.C0timerlb.setText(self.minsec)
        self.C0timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy29 == 0:
            self.myTimer29.stop()
            self.Car30Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car30Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 31 timer #####
    def startTimer31(self, timermsg):
        self.time_left_int30 = timermsg + 1
        self.timercnt30 = 0
        self.myTimer30 = QtCore.QTimer(self)
        self.myTimer30.setInterval(1000)
        self.myTimer30.timeout.connect(self.timerTimeout31)
        self.myTimer30.start()
    
    def timerTimeout31(self):
        self.timercnt30 += 1
        self.time_left_int_copy30 = self.time_left_int30 - self.timercnt30
        self.minsec = secs_to_minsec(self.time_left_int_copy30)
        self.D1timerlb.setText(self.minsec)
        self.D1timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy30 == 0:
            self.myTimer30.stop()
            self.Car31Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car31Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 32 timer #####
    def startTimer32(self, timermsg):
        self.time_left_int31 = timermsg + 1
        self.timercnt31 = 0
        self.myTimer31 = QtCore.QTimer(self)
        self.myTimer31.setInterval(1000)
        self.myTimer31.timeout.connect(self.timerTimeout32)
        self.myTimer31.start()
    
    def timerTimeout32(self):
        self.timercnt31 += 1
        self.time_left_int_copy31 = self.time_left_int31 - self.timercnt31
        self.minsec = secs_to_minsec(self.time_left_int_copy31)
        self.D2timerlb.setText(self.minsec)
        self.D2timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy31 == 0:
            self.myTimer31.stop()
            self.Car32Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car32Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 33 timer #####
    def startTimer33(self, timermsg):
        self.time_left_int32 = timermsg + 1
        self.timercnt32 = 0
        self.myTimer32 = QtCore.QTimer(self)
        self.myTimer32.setInterval(1000)
        self.myTimer32.timeout.connect(self.timerTimeout33)
        self.myTimer32.start()
    
    def timerTimeout33(self):
        self.timercnt32 += 1
        self.time_left_int_copy32 = self.time_left_int32 - self.timercnt32
        self.minsec = secs_to_minsec(self.time_left_int_copy32)
        self.D3timerlb.setText(self.minsec)
        self.D3timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy32 == 0:
            self.myTimer32.stop()
            self.Car33Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car33Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 34 timer #####
    def startTimer34(self, timermsg):
        self.time_left_int33 = timermsg + 1
        self.timercnt33 = 0
        self.myTimer33 = QtCore.QTimer(self)
        self.myTimer33.setInterval(1000)
        self.myTimer33.timeout.connect(self.timerTimeout34)
        self.myTimer33.start()
    
    def timerTimeout34(self):
        self.timercnt33 += 1
        self.time_left_int_copy33 = self.time_left_int33 - self.timercnt33
        self.minsec = secs_to_minsec(self.time_left_int_copy33)
        self.D4timerlb.setText(self.minsec)
        self.D4timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy33 == 0:
            self.myTimer33.stop()
            self.Car34Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car34Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 35 timer #####
    def startTimer35(self, timermsg):
        self.time_left_int34 = timermsg + 1
        self.timercnt34 = 0
        self.myTimer34 = QtCore.QTimer(self)
        self.myTimer34.setInterval(1000)
        self.myTimer34.timeout.connect(self.timerTimeout35)
        self.myTimer34.start()
    
    def timerTimeout35(self):
        self.timercnt34 += 1
        self.time_left_int_copy34 = self.time_left_int34 - self.timercnt34
        self.minsec = secs_to_minsec(self.time_left_int_copy34)
        self.D5timerlb.setText(self.minsec)
        self.D5timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy34 == 0:
            self.myTimer34.stop()
            self.Car35Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car35Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 36 timer #####
    def startTimer36(self, timermsg):
        self.time_left_int35 = timermsg + 1
        self.timercnt35 = 0
        self.myTimer35 = QtCore.QTimer(self)
        self.myTimer35.setInterval(1000)
        self.myTimer35.timeout.connect(self.timerTimeout36)
        self.myTimer35.start()
    
    def timerTimeout36(self):
        self.timercnt35 += 1
        self.time_left_int_copy35 = self.time_left_int35 - self.timercnt35
        self.minsec = secs_to_minsec(self.time_left_int_copy35)
        self.D6timerlb.setText(self.minsec)
        self.D6timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy35 == 0:
            self.myTimer35.stop()
            self.Car36Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car36Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 37 timer #####
    def startTimer37(self, timermsg):
        self.time_left_int36 = timermsg + 1
        self.timercnt36 = 0
        self.myTimer36 = QtCore.QTimer(self)
        self.myTimer36.setInterval(1000)
        self.myTimer36.timeout.connect(self.timerTimeout37)
        self.myTimer36.start()
    
    def timerTimeout37(self):
        self.timercnt36 += 1
        self.time_left_int_copy36 = self.time_left_int36 - self.timercnt36
        self.minsec = secs_to_minsec(self.time_left_int_copy36)
        self.D7timerlb.setText(self.minsec)
        self.D7timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy36 == 0:
            self.myTimer36.stop()
            self.Car37Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car37Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 38 timer #####
    def startTimer38(self, timermsg):
        self.time_left_int37 = timermsg + 1
        self.timercnt37 = 0
        self.myTimer37 = QtCore.QTimer(self)
        self.myTimer37.setInterval(1000)
        self.myTimer37.timeout.connect(self.timerTimeout38)
        self.myTimer37.start()
    
    def timerTimeout38(self):
        self.timercnt37 += 1
        self.time_left_int_copy37 = self.time_left_int37 - self.timercnt37
        self.minsec = secs_to_minsec(self.time_left_int_copy37)
        self.D8timerlb.setText(self.minsec)
        self.D8timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy37 == 0:
            self.myTimer37.stop()
            self.Car38Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car38Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 39 timer #####
    def startTimer39(self, timermsg):
        self.time_left_int38 = timermsg + 1
        self.timercnt38 = 0
        self.myTimer38 = QtCore.QTimer(self)
        self.myTimer38.setInterval(1000)
        self.myTimer38.timeout.connect(self.timerTimeout39)
        self.myTimer38.start()
    
    def timerTimeout39(self):
        self.timercnt38 += 1
        self.time_left_int_copy38 = self.time_left_int38 - self.timercnt38
        self.minsec = secs_to_minsec(self.time_left_int_copy38)
        self.D9timerlb.setText(self.minsec)
        self.D9timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy38 == 0:
            self.myTimer38.stop()
            self.Car39Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car39Statelb.setAlignment(QtCore.Qt.AlignCenter)
    
    ##### 40 timer #####
    def startTimer40(self, timermsg):
        self.time_left_int39 = timermsg + 1
        self.timercnt39 = 0
        self.myTimer39 = QtCore.QTimer(self)
        self.myTimer39.setInterval(1000)
        self.myTimer39.timeout.connect(self.timerTimeout40)
        self.myTimer39.start()
    
    def timerTimeout40(self):
        self.timercnt39 += 1
        self.time_left_int_copy39 = self.time_left_int39 - self.timercnt39
        self.minsec = secs_to_minsec(self.time_left_int_copy39)
        self.D0timerlb.setText(self.minsec)
        self.D0timerlb.setAlignment(QtCore.Qt.AlignCenter)
        if self.time_left_int_copy39 == 0:
            self.myTimer39.stop()
            self.Car40Statelb.setPixmap(QtGui.QPixmap("state_red.png"))
            self.Car40Statelb.setAlignment(QtCore.Qt.AlignCenter)

    
    # 차량 입고 이벤트 함수    
    def CarID1btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup()
        self.allButtonDisable()                   
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID1btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID1btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car1Statelb.setPixmap(QtGui.QPixmap("state_green.png"))
            self.Car1Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("1", 1)     # 버튼 상태 쓰기
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60 
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[0])+","+str(self.Carname[0])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS)) 
            self.A1Carnamelb.setText(str(self.Carname[0]))
            self.A1Carnamelb.setAlignment(QtCore.Qt.AlignCenter)
            self.startTimer1(self.sec1)
            self.loadButtonstate = self.csvread.Data_User_State_Read()     # 버튼 상태 읽기
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
            
    def CarID2btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup1()
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID2btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID2btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car2Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car2Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("2", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[1])+","+str(self.Carname[1])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A2Carnamelb.setText(str(self.Carname[1]))                    # 수정 포인트5   
            self.A2Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer2(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
            
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def CarID3btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup2()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID3btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID3btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car3Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car3Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("3", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[2])+","+str(self.Carname[2])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A3Carnamelb.setText(str(self.Carname[2]))                    # 수정 포인트5   
            self.A3Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer3(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID4btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup3()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID4btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID4btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car4Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car4Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("4", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[3])+","+str(self.Carname[3])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A4Carnamelb.setText(str(self.Carname[3]))                    # 수정 포인트5   
            self.A4Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer4(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)    
    
    def CarID5btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup4()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID5btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID5btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car5Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car5Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("5", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[4])+","+str(self.Carname[4])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A5Carnamelb.setText(str(self.Carname[4]))                    # 수정 포인트5   
            self.A5Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer5(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID6btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup5()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID6btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID6btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car6Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car6Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("6", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[5])+","+str(self.Carname[5])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A6Carnamelb.setText(str(self.Carname[5]))                    # 수정 포인트5   
            self.A6Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer6(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
    def CarID7btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup6()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID7btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID7btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car7Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car7Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("7", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[6])+","+str(self.Carname[6])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A7Carnamelb.setText(str(self.Carname[6]))                    # 수정 포인트5   
            self.A7Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer7(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)        
    
    def CarID8btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup7()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID8btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID8btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car8Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car8Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("8", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[7])+","+str(self.Carname[7])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A8Carnamelb.setText(str(self.Carname[7]))                    # 수정 포인트5   
            self.A8Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer8(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID9btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup8()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID9btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID9btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car9Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car9Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("9", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[8])+","+str(self.Carname[8])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A9Carnamelb.setText(str(self.Carname[8]))                    # 수정 포인트5   
            self.A9Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer9(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
    def CarID10btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup9()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID10btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID10btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car10Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car10Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("10", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[9])+","+str(self.Carname[9])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.A0Carnamelb.setText(str(self.Carname[9]))                    # 수정 포인트5   
            self.A0Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer10(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)    
    
    def CarID11btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup10()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID11btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID11btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car11Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car11Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("11", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[10])+","+str(self.Carname[10])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B1Carnamelb.setText(str(self.Carname[10]))                    # 수정 포인트5   
            self.B1Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer11(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)    
    
    def CarID12btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup11()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID12btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID12btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car12Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car12Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("12", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[11])+","+str(self.Carname[11])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B2Carnamelb.setText(str(self.Carname[11]))                    # 수정 포인트5   
            self.B2Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer12(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID13btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup12()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID13btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID13btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car13Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car13Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("13", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[12])+","+str(self.Carname[12])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B3Carnamelb.setText(str(self.Carname[12]))                    # 수정 포인트5   
            self.B3Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer13(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)    
    
    def CarID14btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup13()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID14btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID14btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car14Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car14Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("14", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[13])+","+str(self.Carname[13])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B4Carnamelb.setText(str(self.Carname[13]))                    # 수정 포인트5   
            self.B4Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer14(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID15btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup14()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID15btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID15btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car15Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car15Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("15", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[14])+","+str(self.Carname[14])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B5Carnamelb.setText(str(self.Carname[14]))                    # 수정 포인트5   
            self.B5Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer15(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID16btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup15()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID16btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID16btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car16Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car16Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("16", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[15])+","+str(self.Carname[15])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B6Carnamelb.setText(str(self.Carname[15]))                    # 수정 포인트5   
            self.B6Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer16(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def CarID17btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup16()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID17btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID17btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car17Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car17Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("17", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[16])+","+str(self.Carname[16])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B7Carnamelb.setText(str(self.Carname[16]))                    # 수정 포인트5   
            self.B7Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer17(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID18btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup17()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID18btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID18btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car18Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car18Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("18", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[17])+","+str(self.Carname[17])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B8Carnamelb.setText(str(self.Carname[17]))                    # 수정 포인트5   
            self.B8Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer18(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID19btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup18()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID19btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID19btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car19Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car19Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("19", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[18])+","+str(self.Carname[18])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B9Carnamelb.setText(str(self.Carname[18]))                    # 수정 포인트5   
            self.B9Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer19(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID20btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup19()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID20btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID20btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car20Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car20Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("20", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[19])+","+str(self.Carname[19])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.B0Carnamelb.setText(str(self.Carname[19]))                    # 수정 포인트5   
            self.B0Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer20(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID21btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup20()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID21btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID21btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car21Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car21Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("21", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[20])+","+str(self.Carname[20])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C1Carnamelb.setText(str(self.Carname[20]))                    # 수정 포인트5   
            self.C1Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer21(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID22btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup21()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID22btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID22btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car22Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car22Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("22", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[21])+","+str(self.Carname[21])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C2Carnamelb.setText(str(self.Carname[21]))                    # 수정 포인트5   
            self.C2Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer22(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID23btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup22()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID23btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID23btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car23Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car23Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("23", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[22])+","+str(self.Carname[22])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C3Carnamelb.setText(str(self.Carname[22]))                    # 수정 포인트5   
            self.C3Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer23(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID24btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup23()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID24btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID24btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car24Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car24Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("24", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[23])+","+str(self.Carname[23])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C4Carnamelb.setText(str(self.Carname[23]))                    # 수정 포인트5   
            self.C4Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer24(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID25btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup24()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID25btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID25btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car25Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car25Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("25", 1)
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C5Carnamelb.setText(str(self.Carname[24]))                    # 수정 포인트5   
            self.C5Carnamelb.setAlignment(QtCore.Qt.AlignCenter)              # 수정 포인트6  
            self.startTimer25(self.sec1)                              # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID26btIN_Popupcall(self):                                 # 수정 포인트
        self.userRegPopupwin = UserregPopup25()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID26btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID26btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car26Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car26Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("26", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C6Carnamelb.setText(str(self.Carname[25]))                    # 수정 포인트5   
            self.C6Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer26(self.sec1)                                       # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    """
    def CarID27btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup26()                      # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID27btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID27btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car27Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car27Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("27", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C7Carnamelb.setText(str(self.Carname[26]))                    # 수정 포인트5   
            self.C7Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer27(self.sec1)                                       # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def CarID28btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup27()
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID28btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID28btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car28Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car28Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("28", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C8Carnamelb.setText(str(self.Carname[27]))                    # 수정 포인트5   
            self.C8Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer28(self.sec1)                                       # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def CarID29btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup28()
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID29btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID29btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car29Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car29Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("29", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C9Carnamelb.setText(str(self.Carname[28]))                    # 수정 포인트5   
            self.C9Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer29(self.sec1)                                       # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def CarID30btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup29()
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID30btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID30btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car30Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car30Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("30", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C10Carnamelb.setText(str(self.Carname[29]))                    # 수정 포인트5   
            self.C10Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer30(self.sec1)                                       # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID31btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup30()
        self.allButtonDisable()
        self.userRegPopupwin.exec()

        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID31btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID31btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car31Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car31Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("31", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C11Carnamelb.setText(str(self.Carname[30]))                    # 수정 포인트5   
            self.C11Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer31(self.sec1)                                       # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def CarID32btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup31()
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID32btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID32btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car32Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car32Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("32", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C12Carnamelb.setText(str(self.Carname[31]))                    # 수정 포인트5   
            self.C12Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer32(self.sec1)                                       # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID33btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup32()
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID33btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID33btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car33Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car33Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("33", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C13Carnamelb.setText(str(self.Carname[32]))                    # 수정 포인트5   
            self.C13Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer33(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID34btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup33()
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID34btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID34btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car34Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car34Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("34", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C14Carnamelb.setText(str(self.Carname[33]))                    # 수정 포인트5   
            self.C14Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer34(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID35btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup34()                                  # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID35btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID35btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car35Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car35Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("35", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C15Carnamelb.setText(str(self.Carname[34]))                    # 수정 포인트5   
            self.C15Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer35(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID36btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup35()                                  # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID36btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID36btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car36Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car36Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("36", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C16Carnamelb.setText(str(self.Carname[35]))                    # 수정 포인트5   
            self.C16Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer36(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID37btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup36()                                  # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID37btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID37btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car37Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car37Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("37", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C17Carnamelb.setText(str(self.Carname[36]))                    # 수정 포인트5   
            self.C17Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer37(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID38btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup37()                                  # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID38btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID38btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car38Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car38Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("38", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C18Carnamelb.setText(str(self.Carname[37]))                    # 수정 포인트5   
            self.C18Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer38(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID39btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup38()                                  # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID39btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID39btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car39Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car39Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("39", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C19Carnamelb.setText(str(self.Carname[38]))                    # 수정 포인트5   
            self.C19Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer39(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID40btIN_Popupcall(self):
        self.userRegPopupwin = UserregPopup39()                                  # 수정 포인트
        self.allButtonDisable()
        self.userRegPopupwin.exec()
        if self.userRegPopupwin.reg_okmsg1 == True:
            self.CarID40btIN.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")   #수정 포인트 1
            self.CarID40btOut.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")     #수정 포인트 2
            self.Car40Statelb.setPixmap(QtGui.QPixmap("state_green.png"))       # 수정 포인트3
            self.Car40Statelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트4 
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("40", 1)                         # 수정 포인트
            self.Timer1 = self.csvread.Data_Timer1()
            self.timerdatavi = str(self.Timer1[0]).encode('utf-8')
            self.timerdatavi1 = str(self.timerdatavi.decode()) 
            self.timerdatavi2 = self.timerdatavi1.split(":")
            self.sec = int(self.timerdatavi2[0]) * 60
            self.sec1 = self.sec + int(self.timerdatavi2[1])
            self.Carname = self.csvread.Data_read()
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkin"+","+str(self.CarID[24])+","+str(self.Carname[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.C20Carnamelb.setText(str(self.Carname[39]))                    # 수정 포인트5   
            self.C20Carnamelb.setAlignment(QtCore.Qt.AlignCenter)               # 수정 포인트6  
            self.startTimer40(self.sec1)                                        # 수정 포인트7  
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        if self.userRegPopupwin.reg_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    """
    
    def CarID1btOut_Popupcall(self):
        self.retPopupwin = UserretPopup()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID1btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID1btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car1Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car1Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A1timerlb.setText("N")
            self.csvload.Data_write("1","N")
            self.A1Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("1", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[0])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()     # 버튼 상태 읽기
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()     # 버튼 상태 읽기
            self.ButtonSelect(self.loadButtonstate)
            
    def CarID2btOut_Popupcall(self):
        self.retPopupwin = UserretPopup1()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID2btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID2btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car2Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car2Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A2timerlb.setText("N")
            self.csvload.Data_write("2","N")
            self.A2Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("2", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[1])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer1.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
            
    def CarID3btOut_Popupcall(self):
        self.retPopupwin = UserretPopup2()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID3btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID3btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car3Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car3Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A3timerlb.setText("N")
            self.csvload.Data_write("3","N")
            self.A3Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("3", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[2])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer2.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID4btOut_Popupcall(self):
        self.retPopupwin = UserretPopup3()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID4btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID4btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car4Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car4Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A4timerlb.setText("N")
            self.csvload.Data_write("4","N")
            self.A4Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("4", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[3])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer3.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID5btOut_Popupcall(self):
        self.retPopupwin = UserretPopup4()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID5btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID5btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car5Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car5Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A5timerlb.setText("N")
            self.csvload.Data_write("5","N")
            self.A5Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("5", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[4])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer4.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID6btOut_Popupcall(self):
        self.retPopupwin = UserretPopup5()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID6btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID6btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car6Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car6Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A6timerlb.setText("N")
            self.csvload.Data_write("6","N")
            self.A6Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("6", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[5])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer5.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID7btOut_Popupcall(self):
        self.retPopupwin = UserretPopup6()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID7btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID7btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car7Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car7Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A7timerlb.setText("N")
            self.csvload.Data_write("7","N")
            self.A7Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("7", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[6])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer6.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID8btOut_Popupcall(self):
        self.retPopupwin = UserretPopup7()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID8btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID8btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car8Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car8Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A8timerlb.setText("N")
            self.csvload.Data_write("8","N")
            self.A8Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("8", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[7])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer7.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID9btOut_Popupcall(self):
        self.retPopupwin = UserretPopup8()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID9btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID9btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car9Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car9Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A9timerlb.setText("N")
            self.csvload.Data_write("9","N")
            self.A9Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("9", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[8])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer8.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID10btOut_Popupcall(self):
        self.retPopupwin = UserretPopup9()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID10btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID10btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car10Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car10Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.A0timerlb.setText("N")
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("10", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[9])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.csvload.Data_write("10","N")
            self.A0Carnamelb.setText(str("N"))
            self.myTimer9.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID11btOut_Popupcall(self):
        self.retPopupwin = UserretPopup10()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID11btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID11btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car11Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car11Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B1timerlb.setText("N")
            self.csvload.Data_write("11","N")
            self.B1Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("11", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[10])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer10.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID12btOut_Popupcall(self):
        self.retPopupwin = UserretPopup11()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID12btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID12btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car12Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car12Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B2timerlb.setText("N")
            self.csvload.Data_write("12","N")
            self.B2Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("12", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[11])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer11.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID13btOut_Popupcall(self):
        self.retPopupwin = UserretPopup12()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID13btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID13btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car13Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car13Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B3timerlb.setText("N")
            self.csvload.Data_write("13","N")
            self.B3Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("13", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[12])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer12.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID14btOut_Popupcall(self):
        self.retPopupwin = UserretPopup13()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID14btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID14btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car14Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car14Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B4timerlb.setText("N")
            self.csvload.Data_write("14","N")
            self.B4Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("14", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[13])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer13.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID15btOut_Popupcall(self):
        self.retPopupwin = UserretPopup14()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID15btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID15btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car15Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car15Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B5timerlb.setText("N")
            self.csvload.Data_write("15","N")
            self.B5Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("15", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[14])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer14.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID16btOut_Popupcall(self):
        self.retPopupwin = UserretPopup15()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID16btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID16btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car16Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car16Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B6timerlb.setText("N")
            self.csvload.Data_write("16","N")
            self.B6Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("16", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[15])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer15.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID17btOut_Popupcall(self):
        self.retPopupwin = UserretPopup16()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID17btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID17btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car17Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car17Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B7timerlb.setText("N")
            self.csvload.Data_write("17","N")
            self.B7Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("17", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[16])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer16.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID18btOut_Popupcall(self):
        self.retPopupwin = UserretPopup17()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID18btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID18btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car18Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car18Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B8timerlb.setText("N")
            self.csvload.Data_write("18","N")
            self.B8Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("18", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[17])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer17.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID19btOut_Popupcall(self):
        self.retPopupwin = UserretPopup18()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID19btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID19btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car19Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car19Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B9timerlb.setText("N")
            self.csvload.Data_write("19","N")
            self.B9Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("19", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[18])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer18.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID20btOut_Popupcall(self):
        self.retPopupwin = UserretPopup19()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID20btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID20btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car20Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car20Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.B0timerlb.setText("N")
            self.csvload.Data_write("20","N")
            self.B0Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("20", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[19])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer19.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID21btOut_Popupcall(self):
        self.retPopupwin = UserretPopup20()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID21btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID21btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car21Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car21Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.C1timerlb.setText("N")
            self.csvload.Data_write("21","N")
            self.C1Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("21", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[20])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer20.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID22btOut_Popupcall(self):
        self.retPopupwin = UserretPopup21()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID22btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID22btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car22Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car22Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.C2timerlb.setText("N")
            self.csvload.Data_write("22","N")
            self.C2Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("22", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[21])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer21.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID23btOut_Popupcall(self):
        self.retPopupwin = UserretPopup22()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID23btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID23btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car23Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car23Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.C3timerlb.setText("N")
            self.csvload.Data_write("23","N")
            self.C3Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("23", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[22])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer22.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID24btOut_Popupcall(self):
        self.retPopupwin = UserretPopup23()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID24btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID24btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car24Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car24Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.C4timerlb.setText("N")
            self.csvload.Data_write("24","N")
            self.C4Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("24", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[23])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer23.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID25btOut_Popupcall(self):                       
        self.retPopupwin = UserretPopup24()
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID25btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.CarID25btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")
            self.Car25Statelb.setPixmap(QtGui.QPixmap("state_white.png"))
            self.Car25Statelb.setAlignment(QtCore.Qt.AlignCenter)
            self.C5timerlb.setText("N")
            self.csvload.Data_write("25","N")
            self.C5Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("25", 0)
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[24])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer24.stop()
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID26btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup25()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID26btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID26btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car26Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car26Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.C6timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("26","N")                                       # 수정 포인트
            self.C6Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("26", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[25])
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer25.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID27btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup26()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID27btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID27btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car27Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car27Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.C7timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("27","N")                                       # 수정 포인트
            self.C7Carnamelb.setText(str("N"))
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("27", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[26])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer26.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID28btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup27()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID28btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID28btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car28Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car28Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.C8timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("28","N")                                       # 수정 포인트
            self.C8Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("28", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[27])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer27.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def CarID29btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup28()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID29btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID29btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car29Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car29Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.C9timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("29","N")                                       # 수정 포인트
            self.C9Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("29", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[28])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer28.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID30btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup29()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID30btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID30btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car30Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car30Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.C0timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("30","N")                                       # 수정 포인트
            self.C10Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("30", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[29])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer29.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID31btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup30()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID31btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID31btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car31Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car31Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D1timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("31","N")                                       # 수정 포인트
            self.C11Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("31", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[30])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer30.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID32btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup31()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID32btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID32btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car32Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car32Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D2timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("32","N")                                       # 수정 포인트
            self.C12Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("32", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[31])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer31.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID33btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup32()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID33btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID33btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car33Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car33Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D3timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("33","N")                                       # 수정 포인트
            self.C13Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("33", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[32])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer32.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID34btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup33()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID34btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID34btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car34Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car34Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D4timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("34","N")                                       # 수정 포인트
            self.C14Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("34", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[33])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer33.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID35btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup34()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID35btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID35btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car35Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car35Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D5timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("35","N")                                       # 수정 포인트
            self.C15Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("35", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[34])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer34.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID36btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup35()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID36btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID36btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car36Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car36Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D6timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("36","N")                                       # 수정 포인트
            self.C16Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("36", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[35])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer35.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID37btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup36()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID37btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID37btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car37Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car37Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D7timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("37","N")                                       # 수정 포인트
            self.C17Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("37", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[36])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer36.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID38btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup37()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID38btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID38btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car38Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car38Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D8timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("38","N")                                       # 수정 포인트
            self.C18Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("38", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[37])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer37.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID39btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup38()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID39btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID39btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car39Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car39Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D9timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("39","N")                                       # 수정 포인트
            self.C19Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("39", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[38])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer38.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
    
    def CarID40btOut_Popupcall(self):                   # 수정 포인트                       
        self.retPopupwin = UserretPopup39()             # 수정 포인트
        self.csvload = DataCsv()
        self.allButtonDisable()
        self.retPopupwin.exec()
        
        if  self.retPopupwin.ret_okmsg1 == True:
            self.CarID40btIN.setStyleSheet("background-color: rgb(95, 95, 95);\n""color: rgb(146,146,146);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")             # 수정 포인트
            self.CarID40btOut.setStyleSheet("background-color: rgb(213, 213, 213);\n""color: rgb(101,101,101);\n""border: 2px solid rgb(0,0,0);\n""border-radius: 10px")         # 수정 포인트
            self.Car40Statelb.setPixmap(QtGui.QPixmap("state_white.png"))           # 수정 포인트
            self.Car40Statelb.setAlignment(QtCore.Qt.AlignCenter)                   # 수정 포인트
            self.D0timerlb.setText("N")                                             # 수정 포인트    
            self.csvload.Data_write("40","N")                                       # 수정 포인트
            self.C20Carnamelb.setText(str("N"))                                      # 수정 포인트
            self.csvread = DataCsv()
            self.csvread.Data_User_state_write("40", 0)                             # 수정 포인트
            self.CarID = self.csvread.CarID_Read()
            msg = "Checkout"+","+str(self.CarID[39])                                # 수정 포인트
            msg1 = str(msg).encode('utf-8')
            self.recSocket1.sendto(msg1,(SERVERIP_PASS,SERVERPORT_PASS))
            self.myTimer39.stop()                                                   # 수정 포인트
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)
        
        if  self.retPopupwin.ret_okmsg1 == False:
            self.loadButtonstate = self.csvread.Data_User_State_Read()
            self.ButtonSelect(self.loadButtonstate)

    def ButtonSelect(self, DataUserload):
        #Button 1
        if int(DataUserload[0]) == 0:
            self.CarID1btIN.setEnabled(True)
            self.CarID1btOut.setDisabled(True)
        if int(DataUserload[0]) == 1:
            self.CarID1btIN.setDisabled(True)   
            self.CarID1btOut.setEnabled(True)
        #Button 2
        if int(DataUserload[1]) == 0:
            self.CarID2btIN.setEnabled(True)
            self.CarID2btOut.setDisabled(True)
        if int(DataUserload[1]) == 1:
            self.CarID2btIN.setDisabled(True)   
            self.CarID2btOut.setEnabled(True)
        #Button 3
        if int(DataUserload[2]) == 0:
            self.CarID3btIN.setEnabled(True)
            self.CarID3btOut.setDisabled(True)
        if int(DataUserload[2]) == 1:
            self.CarID3btIN.setDisabled(True)   
            self.CarID3btOut.setEnabled(True)
        #Button 4
        if int(DataUserload[3]) == 0:
            self.CarID4btIN.setEnabled(True)
            self.CarID4btOut.setDisabled(True)
        if int(DataUserload[3]) == 1:
            self.CarID4btIN.setDisabled(True)   
            self.CarID4btOut.setEnabled(True)
        #Button 5
        if int(DataUserload[4]) == 0:
            self.CarID5btIN.setEnabled(True)
            self.CarID5btOut.setDisabled(True)
        if int(DataUserload[4]) == 1:
            self.CarID5btIN.setDisabled(True)   
            self.CarID5btOut.setEnabled(True)
        #Button 6
        if int(DataUserload[5]) == 0:
            self.CarID6btIN.setEnabled(True)
            self.CarID6btOut.setDisabled(True)
        if int(DataUserload[5]) == 1:
            self.CarID6btIN.setDisabled(True)   
            self.CarID6btOut.setEnabled(True)
        #Button 7
        if int(DataUserload[6]) == 0:
            self.CarID7btIN.setEnabled(True)
            self.CarID7btOut.setDisabled(True)
        if int(DataUserload[6]) == 1:
            self.CarID7btIN.setDisabled(True)   
            self.CarID7btOut.setEnabled(True)
        #Button 8
        if int(DataUserload[7]) == 0:
            self.CarID8btIN.setEnabled(True)
            self.CarID8btOut.setDisabled(True)
        if int(DataUserload[7]) == 1:
            self.CarID8btIN.setDisabled(True)   
            self.CarID8btOut.setEnabled(True)
        #Button 9
        if int(DataUserload[8]) == 0:
            self.CarID9btIN.setEnabled(True)
            self.CarID9btOut.setDisabled(True)
        if int(DataUserload[8]) == 1:
            self.CarID9btIN.setDisabled(True)   
            self.CarID9btOut.setEnabled(True)        
        #Button 10
        if int(DataUserload[9]) == 0:
            self.CarID10btIN.setEnabled(True)
            self.CarID10btOut.setDisabled(True)
        if int(DataUserload[9]) == 1:
            self.CarID10btIN.setDisabled(True)   
            self.CarID10btOut.setEnabled(True)
        #Button 11
        if int(DataUserload[10]) == 0:
            self.CarID11btIN.setEnabled(True)
            self.CarID11btOut.setDisabled(True)
        if int(DataUserload[10]) == 1:
            self.CarID11btIN.setDisabled(True)   
            self.CarID11btOut.setEnabled(True)
        #Button 12
        if int(DataUserload[11]) == 0:
            self.CarID12btIN.setEnabled(True)
            self.CarID12btOut.setDisabled(True)
        if int(DataUserload[11]) == 1:
            self.CarID12btIN.setDisabled(True)   
            self.CarID12btOut.setEnabled(True)
        #Button 13
        if int(DataUserload[12]) == 0:
            self.CarID13btIN.setEnabled(True)
            self.CarID13btOut.setDisabled(True)
        if int(DataUserload[12]) == 1:
            self.CarID13btIN.setDisabled(True)   
            self.CarID13btOut.setEnabled(True)
        #Button 14
        if int(DataUserload[13]) == 0:
            self.CarID14btIN.setEnabled(True)
            self.CarID14btOut.setDisabled(True)
        if int(DataUserload[13]) == 1:
            self.CarID14btIN.setDisabled(True)   
            self.CarID14btOut.setEnabled(True)
        #Button 15
        if int(DataUserload[14]) == 0:
            self.CarID15btIN.setEnabled(True)
            self.CarID15btOut.setDisabled(True)
        if int(DataUserload[14]) == 1:
            self.CarID15btIN.setDisabled(True)   
            self.CarID15btOut.setEnabled(True)
        #Button 16
        if int(DataUserload[15]) == 0:
            self.CarID16btIN.setEnabled(True)
            self.CarID16btOut.setDisabled(True)
        if int(DataUserload[15]) == 1:
            self.CarID16btIN.setDisabled(True)   
            self.CarID16btOut.setEnabled(True)
        #Button 17
        if int(DataUserload[16]) == 0:
            self.CarID17btIN.setEnabled(True)
            self.CarID17btOut.setDisabled(True)
        if int(DataUserload[16]) == 1:
            self.CarID17btIN.setDisabled(True)   
            self.CarID17btOut.setEnabled(True)
        #Button 18
        if int(DataUserload[17]) == 0:
            self.CarID18btIN.setEnabled(True)
            self.CarID18btOut.setDisabled(True)
        if int(DataUserload[17]) == 1:
            self.CarID18btIN.setDisabled(True)   
            self.CarID18btOut.setEnabled(True)
        #Button 19
        if int(DataUserload[18]) == 0:
            self.CarID19btIN.setEnabled(True)
            self.CarID19btOut.setDisabled(True)
        if int(DataUserload[18]) == 1:
            self.CarID19btIN.setDisabled(True)   
            self.CarID19btOut.setEnabled(True)
        #Button 20
        if int(DataUserload[19]) == 0:
            self.CarID20btIN.setEnabled(True)
            self.CarID20btOut.setDisabled(True)
        if int(DataUserload[19]) == 1:
            self.CarID20btIN.setDisabled(True)   
            self.CarID20btOut.setEnabled(True)
        #Button 21
        if int(DataUserload[20]) == 0:
            self.CarID21btIN.setEnabled(True)
            self.CarID21btOut.setDisabled(True)
        if int(DataUserload[20]) == 1:
            self.CarID21btIN.setDisabled(True)   
            self.CarID21btOut.setEnabled(True)
        #Button 22
        if int(DataUserload[21]) == 0:
            self.CarID22btIN.setEnabled(True)
            self.CarID22btOut.setDisabled(True)
        if int(DataUserload[21]) == 1:
            self.CarID22btIN.setDisabled(True)   
            self.CarID22btOut.setEnabled(True)
        #Button 23
        if int(DataUserload[22]) == 0:
            self.CarID23btIN.setEnabled(True)
            self.CarID23btOut.setDisabled(True)
        if int(DataUserload[22]) == 1:
            self.CarID23btIN.setDisabled(True)   
            self.CarID23btOut.setEnabled(True)
        #Button 24
        if int(DataUserload[23]) == 0:
            self.CarID24btIN.setEnabled(True)
            self.CarID24btOut.setDisabled(True)
        if int(DataUserload[23]) == 1:
            self.CarID24btIN.setDisabled(True)   
            self.CarID24btOut.setEnabled(True)
        #Button 25
        if int(DataUserload[24]) == 0:
            self.CarID25btIN.setEnabled(True)
            self.CarID25btOut.setDisabled(True)
        if int(DataUserload[24]) == 1:
            self.CarID25btIN.setDisabled(True)   
            self.CarID25btOut.setEnabled(True)
        #Button 26
        if int(DataUserload[25]) == 0:
            self.CarID26btIN.setEnabled(True)
            self.CarID26btOut.setDisabled(True)
        if int(DataUserload[25]) == 1:
            self.CarID26btIN.setDisabled(True)   
            self.CarID26btOut.setEnabled(True)
        #Button 27
        if int(DataUserload[26]) == 0:
            self.CarID27btIN.setEnabled(True)
            self.CarID27btOut.setDisabled(True)
        if int(DataUserload[26]) == 1:
            self.CarID27btIN.setDisabled(True)   
            self.CarID27btOut.setEnabled(True)
        #Button 28
        if int(DataUserload[27]) == 0:
            self.CarID28btIN.setEnabled(True)
            self.CarID28btOut.setDisabled(True)
        if int(DataUserload[27]) == 1:
            self.CarID28btIN.setDisabled(True)   
            self.CarID28btOut.setEnabled(True)
        #Button 29
        if int(DataUserload[28]) == 0:
            self.CarID29btIN.setEnabled(True)
            self.CarID29btOut.setDisabled(True)
        if int(DataUserload[28]) == 1:
            self.CarID29btIN.setDisabled(True)   
            self.CarID29btOut.setEnabled(True)
        #Button 30
        if int(DataUserload[29]) == 0:
            self.CarID30btIN.setEnabled(True)
            self.CarID30btOut.setDisabled(True)
        if int(DataUserload[29]) == 1:
            self.CarID30btIN.setDisabled(True)   
            self.CarID30btOut.setEnabled(True)
        #Button 31
        if int(DataUserload[30]) == 0:
            self.CarID31btIN.setEnabled(True)
            self.CarID31btOut.setDisabled(True)
        if int(DataUserload[30]) == 1:
            self.CarID31btIN.setDisabled(True)   
            self.CarID31btOut.setEnabled(True)
        #Button 32
        if int(DataUserload[31]) == 0:
            self.CarID32btIN.setEnabled(True)
            self.CarID32btOut.setDisabled(True)
        if int(DataUserload[31]) == 1:
            self.CarID32btIN.setDisabled(True)   
            self.CarID32btOut.setEnabled(True)
        #Button 33
        if int(DataUserload[32]) == 0:
            self.CarID33btIN.setEnabled(True)
            self.CarID33btOut.setDisabled(True)
        if int(DataUserload[32]) == 1:
            self.CarID33btIN.setDisabled(True)   
            self.CarID33btOut.setEnabled(True)
        #Button 34
        if int(DataUserload[33]) == 0:
            self.CarID34btIN.setEnabled(True)
            self.CarID34btOut.setDisabled(True)
        if int(DataUserload[33]) == 1:
            self.CarID34btIN.setDisabled(True)   
            self.CarID34btOut.setEnabled(True)
        #Button 35
        if int(DataUserload[34]) == 0:
            self.CarID35btIN.setEnabled(True)
            self.CarID35btOut.setDisabled(True)
        if int(DataUserload[34]) == 1:
            self.CarID35btIN.setDisabled(True)   
            self.CarID35btOut.setEnabled(True)
        #Button 36
        if int(DataUserload[35]) == 0:
            self.CarID36btIN.setEnabled(True)
            self.CarID36btOut.setDisabled(True)
        if int(DataUserload[35]) == 1:
            self.CarID36btIN.setDisabled(True)   
            self.CarID36btOut.setEnabled(True)
        #Button 37
        if int(DataUserload[36]) == 0:
            self.CarID37btIN.setEnabled(True)
            self.CarID37btOut.setDisabled(True)
        if int(DataUserload[36]) == 1:
            self.CarID37btIN.setDisabled(True)   
            self.CarID37btOut.setEnabled(True)
        #Button 38
        if int(DataUserload[37]) == 0:
            self.CarID38btIN.setEnabled(True)
            self.CarID38btOut.setDisabled(True)
        if int(DataUserload[37]) == 1:
            self.CarID38btIN.setDisabled(True)   
            self.CarID38btOut.setEnabled(True)
        #Button 39
        if int(DataUserload[38]) == 0:
            self.CarID39btIN.setEnabled(True)
            self.CarID39btOut.setDisabled(True)
        if int(DataUserload[38]) == 1:
            self.CarID39btIN.setDisabled(True)   
            self.CarID39btOut.setEnabled(True)
        #Button 40
        if int(DataUserload[39]) == 0:
            self.CarID40btIN.setEnabled(True)
            self.CarID40btOut.setDisabled(True)
        if int(DataUserload[39]) == 1:
            self.CarID40btIN.setDisabled(True)   
            self.CarID40btOut.setEnabled(True)

    
    def allButtonEnable(self):
        self.CarID1btIN.setEnabled(True)
        self.CarID1btOut.setEnabled(True)
        self.CarID2btIN.setEnabled(True)
        self.CarID2btOut.setEnabled(True)
        self.CarID3btIN.setEnabled(True)
        self.CarID3btOut.setEnabled(True)
        self.CarID4btIN.setEnabled(True)
        self.CarID4btOut.setEnabled(True)
        self.CarID5btIN.setEnabled(True)
        self.CarID5btOut.setEnabled(True)
        self.CarID6btIN.setEnabled(True)
        self.CarID6btOut.setEnabled(True)
        self.CarID7btIN.setEnabled(True)
        self.CarID7btOut.setEnabled(True)
        self.CarID8btIN.setEnabled(True)
        self.CarID8btOut.setEnabled(True)
        self.CarID9btIN.setEnabled(True)
        self.CarID9btOut.setEnabled(True)
        self.CarID10btIN.setEnabled(True)
        self.CarID10btOut.setEnabled(True)
        self.CarID11btIN.setEnabled(True)
        self.CarID11btOut.setEnabled(True)
        self.CarID12btIN.setEnabled(True)
        self.CarID12btOut.setEnabled(True)
        self.CarID13btIN.setEnabled(True)
        self.CarID13btOut.setEnabled(True)
        self.CarID14btIN.setEnabled(True)
        self.CarID14btOut.setEnabled(True)
        self.CarID15btIN.setEnabled(True)
        self.CarID15btOut.setEnabled(True)
        self.CarID16btIN.setEnabled(True)
        self.CarID16btOut.setEnabled(True)
        self.CarID17btIN.setEnabled(True)
        self.CarID17btOut.setEnabled(True)
        self.CarID18btIN.setEnabled(True)
        self.CarID18btOut.setEnabled(True)
        self.CarID19btIN.setEnabled(True)
        self.CarID19btOut.setEnabled(True)
        self.CarID20btIN.setEnabled(True)
        self.CarID20btOut.setEnabled(True)
        self.CarID21btIN.setEnabled(True)
        self.CarID21btOut.setEnabled(True)
        self.CarID22btIN.setEnabled(True)
        self.CarID22btOut.setEnabled(True)
        self.CarID23btIN.setEnabled(True)
        self.CarID23btOut.setEnabled(True)
        self.CarID24btIN.setEnabled(True)
        self.CarID24btOut.setEnabled(True)
        self.CarID25btIN.setEnabled(True)
        self.CarID25btOut.setEnabled(True)
        
    def allButtonDisable(self):
        self.CarID1btIN.setDisabled(True)
        self.CarID1btOut.setDisabled(True)
        self.CarID2btIN.setDisabled(True)
        self.CarID2btOut.setDisabled(True)
        self.CarID3btIN.setDisabled(True)
        self.CarID3btOut.setDisabled(True)
        self.CarID4btIN.setDisabled(True)
        self.CarID4btOut.setDisabled(True)
        self.CarID5btIN.setDisabled(True)
        self.CarID5btOut.setDisabled(True)
        self.CarID6btIN.setDisabled(True)
        self.CarID6btOut.setDisabled(True)
        self.CarID7btIN.setDisabled(True)
        self.CarID7btOut.setDisabled(True)
        self.CarID8btIN.setDisabled(True)
        self.CarID8btOut.setDisabled(True)
        self.CarID9btIN.setDisabled(True)
        self.CarID9btOut.setDisabled(True)
        self.CarID10btIN.setDisabled(True)
        self.CarID10btOut.setDisabled(True)
        self.CarID11btIN.setDisabled(True)
        self.CarID11btOut.setDisabled(True)
        self.CarID12btIN.setDisabled(True)
        self.CarID12btOut.setDisabled(True)
        self.CarID13btIN.setDisabled(True)
        self.CarID13btOut.setDisabled(True)
        self.CarID14btIN.setDisabled(True)
        self.CarID14btOut.setDisabled(True)
        self.CarID15btIN.setDisabled(True)
        self.CarID15btOut.setDisabled(True)
        self.CarID16btIN.setDisabled(True)
        self.CarID16btOut.setDisabled(True)
        self.CarID17btIN.setDisabled(True)
        self.CarID17btOut.setDisabled(True)
        self.CarID18btIN.setDisabled(True)
        self.CarID18btOut.setDisabled(True)
        self.CarID19btIN.setDisabled(True)
        self.CarID19btOut.setDisabled(True)
        self.CarID20btIN.setDisabled(True)
        self.CarID20btOut.setDisabled(True)
        self.CarID21btIN.setDisabled(True)
        self.CarID21btOut.setDisabled(True)
        self.CarID22btIN.setDisabled(True)
        self.CarID22btOut.setDisabled(True)
        self.CarID23btIN.setDisabled(True)
        self.CarID23btOut.setDisabled(True)
        self.CarID24btIN.setDisabled(True)
        self.CarID24btOut.setDisabled(True)
        self.CarID25btIN.setDisabled(True)
        self.CarID25btOut.setDisabled(True)
"""
class CustomerWindow(QMainWindow,QWidget,customer_win):
    def __init__(self, parent=None):
        super(CustomerWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.media_player = QMediaPlayer(self)
        
        self.video_widget = QVideoWidget(self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.video_widget)
        self.videowidget.setLayout(vbox)
        
        #self.setCentralWidget(self.video_widget)

        self.media_player.setVideoOutput(self.video_widget)
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("Video.mp4")))
        self.playlist.setCurrentIndex(0)
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)    
        media_content = QMediaContent(QUrl.fromLocalFile("Video.mp4"))
        self.media_player.setMedia(media_content)
        self.media_player.setPlaylist(self.playlist)
        self.media_player.play()
        self.setCursor(Qt.BlankCursor)
        self.show()
        
    def anyfunction(self, msg):
        self.lbtest.setText(msg) 
"""

class CustomerWindow(QMainWindow,QWidget,customer_win):
    def __init__(self, parent=None):
        super(CustomerWindow, self).__init__(parent)
        self.initUI()
        #self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("test.mp4")))
        #self.mediaPlayer.play()
        
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("Video.mp4")))
        self.playlist.setCurrentIndex(0)

        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.mediaPlayer.setPlaylist(self.playlist)
        self.mediaPlayer.setVolume(0)
        self.mediaPlayer.play()
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        self.videoOutput = self.makeVideoWidget()
        self.mediaPlayer = self.makeMediaPlayer()
    
    def makeMediaPlayer(self):
        mediaplayer = QMediaPlayer(self)
        mediaplayer.setVideoOutput(self.videoOutput)
        return mediaplayer
    
    def makeVideoWidget(self):
        videoOutput = QVideoWidget(self)
        videoOutput.setStyleSheet("background-color: black;")
        vbox = QVBoxLayout()
        vbox.addWidget(videoOutput)
        self.videowidget.setLayout(vbox)
        self.setCentralWidget(videoOutput)
        #vbox.addWidget.setLayout(vbox)
        return videoOutput
    
    """
    def makeConnections(self):
        self.playButton.clicked.connect(self.mediaPlayer.play)
        self.pauseButton.clicked.connect(self.mediaPlayer.pause)
        self.stopButton.clicked.connect(self.mediaPlayer.stop)
    """
    
    def anyfunction(self, msg):
        self.lbtest.setText(msg) 


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    w = CustomerWindow()
    #w.setWindowState(Qt.WindowFullScreen)
    w.move(1920,0)              # 1920
    #w.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    w.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
    w.showFullScreen()
    #w.show()
    sys.exit(app.exec_())    

if __name__ == "__main__":
    main()