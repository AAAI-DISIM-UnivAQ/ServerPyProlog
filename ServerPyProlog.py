__author__ = 'Agnese'

import re
import json

class ServerPyProlog:

    def __init__(self):
        self.result="" #risultato, stato attuale della conversione

    def addToResult(self,string): #aggiunge una stringa al risultato
        string=string+"\r\n"
        self.result=self.result+string

    def getResult(self): #restituisce la stringa risultato
        return self.result

    def delResult(self): #cancella la stringa contenuta in result
        self.result=""

    def notificationTXT(txtName,path): #crea un file testuale vuoto di notifica
        path=path+"/"+txtName+".txt"
        handle=False
        while handle is False:
            file=open(path,"w")
        file.close()

    def RESULTtoPL(self,plName,path,newFile): #scrive result su un file Prolog, sovrascrivendo o meno in base al valore del booleano newFile
        path=path+"/"+plName+".pl"
        handle=False
        if newFile is False:
            while handle is False:
                file=open(path,"a+")
        else:
            while handle is False:
                file=open(path,"w")
        file.write("\r\n"+self.getResult())
        file.close()

    def RESULTtoTXT(self,txtName,path,newFile): #scrive result su un file di testo, sovrascrivendo o meno in base al valore del booleano newFile
        path=path+"/"+txtName+".txt"
        handle=False
        if newFile is False:
            while handle is False:
                file=open(path,"a")
        else:
            while handle is False:
                file=open(path,"w")
        file.write("\r\n"+self.getResult())
        file.close()

    def cleanName(self,string): # "pulisce" una stringa da trasformare in nome Prolog da caratteri non contemplati da esso
             string= string.replace(' ', '_')
             string= string.replace('.', '')
             string= string.replace(',', '')
             string= string.replace('=', '')
             string= re.sub("/[^a-zA-Z0-9_-]/", "", string)
             string=string.lower()
             if re.findall('/^[a-z]+$/i',string[0]) is False:
                 string=string[1:]
             return string

    def cleanJson(self,string): #"pulisce" il Json da caratteri non contemplati da Prolog
             string = string.replace("{", "")
             string = string.replace("}", "")
             string = string.replace('"', "")
             string = string.replace(' ', "")
             string=string.lower()
             return string

    def idConverter(self,numericId): # converte i numeri degli id numerici in lettere (il Prolog non gestisce gli id numerici)
        string=str(numericId)
        string= string.replace('0', 'a')
        string=string.replace('1', 'b')
        string=string.replace('2', 'c')
        string=string.replace('3', 'd')
        string=string.replace('4', 'e')
        string=string.replace('5', 'f')
        string=string.replace('6', 'g')
        string=string.replace('7', 'h')
        string=string.replace('8', 'i')
        string=string.replace('9', 'l')
        return string

    def JSONtoPmap(self,json,mapName): # Converte una stringa Json in una stringa lista Prolog
        json=str(json)
        list=self.cleanJson(json)
        mapName=self.cleanName(mapName)
        risultato=""
        array=list.strip().split(',') #strip() rimuove gli spazi; split() splitta la stringa in un array
        l=len(array)
        for i in range(0,l):
            map=array[i].split(':')
            r=mapName+"("+map[0].lower()+","+map[1]+").\r\n"
            risultato=risultato+r
        return risultato

    def cleanDictionary(self,dict): # "pulisce" i dictionary per elaborarli in Prolog
        dict=json.dumps(dict)
        return dict

    def DICTIONARYtoPmap(self,dict,mapName): # trasforma un dictionary in una mappa Prolog
        mapName=self.cleanName(mapName)
        dict=self.cleanDictionary(dict)
        dict=self.cleanJson(dict)
        risultato=self.JSONtoPmap(dict,mapName)
        return risultato

    def DICTIONARYtoPpredicate(self,dict,predicateName): #trasforma un dictionary in un insieme di predicati Prolog
        predicateName=self.cleanName(predicateName)
        dict=str(dict)
        #print(dict)
        dict=self.cleanJson(dict)
        array=dict.split(',')
        #print(array)
        a=""
        risultato=""
        l=len(array)
        #print(l)
        for i in range(0,l):
            subarray=str(array[i]).split(':')
            #print(subarray)
            pred=predicateName+"("+subarray[0]+","+subarray[1]+").\r\n"
            #print(pred)
            risultato=risultato+pred
        #print(risultato)
        return risultato

    def VALUEStoPlist(self,valuesArray,listName): # trasforma un'array di valori in una lista Prolog
        v=str(valuesArray[0])
        l=len(valuesArray)
        for i in range(1,l-1):
            v=v+","+str(valuesArray[i])
        name=self.cleanName(listName)
        risultato=name+"=["+v+"].\r\n"
        return risultato
