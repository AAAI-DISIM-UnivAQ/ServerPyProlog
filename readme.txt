/*


!!!!!! PAY ATTENTION ON THE PATH AND THE NAME YOU CHOOSE FOR YOUR LISTS AND WRITE JSON STRINGS CORRECTLY !!!!!!

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                                                                                                                       +
+                                    FOR MORE DETAILS agneses92@hotmail.it                                                         +
+                                                                                                                                       +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

*/

import PATH+'ServerPyProlog/ServerPyProlog.py'  #How to include.

json = '{"nome":"felix","cognome":"domesticus"}' #A JSON string (it could be a normal JSON too)

persona={            #A dictionary
    "nome":"agnese",
    "cognome":"salutari"
}

translator=serverPyProlog()     #Creation of a serverPyProlog object

translator.delResult()    #Delete old results collected by serverPyProlog in self.result. Use ADDtoResult(string)
                       #to add a Prolog string to add to result.

translator.JSONtoPmap(json, "gatto")   #Convert JSONs or JSON strings to Prolog maps. In this case, "gatto" is the name of the map

translator.VALUEStoPlist(["0",2,3], "numbers")  #Convert an array to a Prolog list (in this case, the list is called numbers)

translator.DICTIONARYtoPmap(persona, "persona") #Convert dictionaries to Prolog maps.

translator.RESULTtoTXT(fileName,path, false)  #Write on a text document without overwriting it.

translator.notificationTXT($txt_name, $path)   #Create a "notification" text file in the specified path.

translator.getResult() #It gives back the result (that is a string containing Prolog).

------------------------------------------------------------------------------------------------------------------
