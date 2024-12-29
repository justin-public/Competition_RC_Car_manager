import pandas as pd
import numpy as np
import csv
import time

no = "no"
CarID = "CarID"

Number = "1"
CarIDtag = "A1"

class DataCsv():
    def Data_write(self,value,namevalue):
        df1 = pd.read_csv('CarNameReg.csv')
        # 데이터를 비교 하여 조건안에 입출력이 가능
        df1.loc[df1["no"]==int(value),"CarName"] = str(namevalue) 
        df1.to_csv('CarNameReg.csv', index=False)
        df1.head()
    
    # 중계기 모듈에 상태 등록 정보를 기입하는 함수
    def Data_Module_state_write(self,value,statevalue):
        df1 = pd.read_csv('RfidModule.csv')
        df1.loc[df1["AntennaID"]==str(value),"Rstate"] = str(statevalue)
        df1.to_csv('RfidModule.csv', index=False)
        df1.head()
    
    # 안테나 모듈에 상태 등록 정보를 기입하는 함수
    def Data_Antenna_state_write(self,value,statevalue):
        df1 = pd.read_csv('RfidModule.csv')
        df1.loc[df1["AntennaID"]==str(value),"Astate"] = str(statevalue)
        df1.to_csv('RfidModule.csv', index=False)
        df1.head()
    
    def Data_User_state_write(self,value,statevalue):
        df1 = pd.read_csv('CarNameReg.csv')
        df1.loc[df1["no"]==int(value),"State"] = str(statevalue)
        df1.to_csv('CarNameReg.csv', index=False)
        df1.head()
    
    def Data_User_rfid_write(self,value,rfidvalue):
        print(value)
        df1 = pd.read_csv('CarNameReg.csv')
        df1.loc[df1["RFID#2"]==str(rfidvalue),"no"] = str(rfidvalue)
        df1.to_csv('CarNameReg.csv', index=False)    
    
    
    
    """
    def Data_ModuleIP_state_write(self, IPvalue):
        df1 = pd.read_csv('RfidModule.csv')
        self.ModuleIP = df1.loc[df1["IP"]==str(IPvalue),"IP"]
        print(IPvalue)
        for i in self.ModuleIP:
            str(i)
    """
    
    def Data_Rfid_write(self,ModuleID,rfidvalue):
        df1 = pd.read_csv('RfidModule.csv')
        df2 = pd.read_csv('CarNameReg.csv')
        
        self.index = df2.loc[df2["RFID#1"]==str(rfidvalue),"no"]
        self.index1 = df2.loc[df2["RFID#2"]==str(rfidvalue),"no"]
        self.AntennaID = df1.loc[df1["AntennaID"]==str(ModuleID),"AntennaID"]
        for i in self.AntennaID:
            message = str(i)
            #print(message)
        for i in self.index:                                       # 등록된 차량이 RFID #1 과 같으면 
            self.CarID = df2.loc[df2["no"]==int(i),"CarID"]        # RFID를 통한 차량 이름 검색 
            for j in self.CarID:
                message1 = str(j)
                #print(message1)
                self.packetmsg = "Tagging"+","+message+","+message1
                return self.packetmsg
                #print(self.packetmsg)       
        for i in self.index1:
            self.CarID = df2.loc[df2["no"]==int(i),"CarID"]
            for j in self.CarID:
                message1 = str(j)                                   
                #print(message1)
                self.packetmsg = "Tagging"+","+message+","+message1
                return self.packetmsg
                #print(self.packetmsg)
        #self.packetmsg = "Tagging"+","+message+","+message1
        #return self.packetmsg

    """
    def Data_Rfid_write(self,ModuleID,rfidvalue):
        df1 = pd.read_csv('RfidModule.csv')
        df2 = pd.read_csv('CarNameReg.csv')
        
        self.index = df1.loc[df1["RFID#1"]==str(rfidvalue),"no"]
        self.index1 = df1.loc[df1["RFID#2"]==str(rfidvalue),"no"]
        self.AntennaID = df1.loc[df1["AntennaID"]==str(ModuleID),"AntennaID"]
        
        for i in self.AntennaID:
            message = str(i)       
        
        for i in self.index:
            self.CarID = df2.loc[df2["no"]==int(i),"CarID"]
            self.RfidTag = df1.loc[df1["no"]==int(i),"RFID#1"]      # 등록된 RFID #1 와 같으면
            for j in self.CarID:
                message1 = str(j)
            for k in self.RfidTag:
                message2 = str(k)

        for i in self.index1:
            self.CarID = df2.loc[df2["no"]==int(i),"CarID"]
            self.RfidTag = df1.loc[df1["no"]==int(i),"RFID#2"]      # 등록된 RFID #2 와 같으면
            for j in self.CarID:
                message1 = str(j)
            for k in self.RfidTag:
                message2 = str(k)    

        self.packetmsg = "Tagging"+","+message+","+message1
        #print(self.packetmsg)
        return self.packetmsg
    """
    def Data_Module_write(self,ModuleIP):
        count = 0
        df1 = pd.read_csv('RfidModule.csv')

        self.ipcheck = df1.loc[df1["IP"]==str(ModuleIP),"IP"]
        for i in self.ipcheck:
            message = str(i)
            if message == str(i):
                return True

    def CarID_Read(self):
        df1 = pd.read_csv('CarNameReg.csv')
        find_row = (df1['CarID'])
        return find_row
    
    def Data_read(self):
        df1 = pd.read_csv('CarNameReg.csv')
        find_row = (df1['CarName'])
        return find_row
        #find_row = df1.loc[df1["CarID"]==str("A1"),"CarName"]
        #return find_row

    """
    def Data_Timer(self):
        df1 = pd.read_csv('CarNameReg.csv')
        find_row = (df1['Timer'])
        return find_row
    """
    
    def Data_Timer1(self):
        df1 = pd.read_csv('Config.csv')
        find_row = (df1['TIME'])
        return find_row
    
    def Data_language(self):
        df1 = pd.read_csv('Config.csv')
        find_row = (df1['LANG'])
        return find_row
    
    def Data_Rfid_AntennaID_Read(self):
        #df1 = pd.read_csv('RfidModule.csv',header=None)
        df1 = pd.read_csv('RfidModule.csv')
        find_row = (df1['AntennaID'])
        return find_row
    
    
    def Data_Module_State_Read(self):
        df1 = pd.read_csv('RfidModule.csv')
        find_row = (df1['Rstate'])
        return find_row
    
    def Date_Antenna_State_Read(self):
        df1 = pd.read_csv('RfidModule.csv')
        find_row = (df1['Astate'])
        return find_row
    
    def Data_Rfid_note_Read(self):
        df1 = pd.read_csv('RfidModule.csv')
        find_row = (df1['note'])
        return find_row
        
    def Data_Rfid_IP_Read(self):
        df1 = pd.read_csv('RfidModule.csv')
        find_row = (df1['IP'])
        return find_row
    
    def Data_User_State_Read(self):
        df1 = pd.read_csv('CarNameReg.csv')
        find_row = (df1['State'])
        return find_row
    
    
        