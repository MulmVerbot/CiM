import requests
import json
import sys
import hashlib
from tkinter import messagebox

prot = 'https'
host = '192.168.60.240'
user = '0003'
pw = 'CmsWsf22'

if (len(sys.argv) > 1):
    host = sys.argv[1]
    if (len(sys.argv) > 2):
        user = sys.argv[2]
        if (len(sys.argv) > 3):
            pw = sys.argv[3]
            if (len(sys.argv) > 4):
                prot=sys.argv[4]
url = prot + '://' + host + '/rest/login'
print("Verbinde mich zu: " ,url)
 
templateResponse = requests.get(url, headers={'Content-Type':'application/json', 'X-Version':'2'}, verify=False)
empf = "Dings: ", templateResponse
messagebox.showinfo(message=empf)
templateJson = json.loads(templateResponse.content)
#print(templateResponse.text)
userandnonce=(user+templateJson['nonce']).encode(encoding='utf_8', errors='strict')
hpassword=hashlib.sha512(pw.encode(encoding='utf_8', errors='strict')).hexdigest()
passwordHashed=hpassword.encode(encoding='utf_8')
hsecret = hashlib.sha512(userandnonce+passwordHashed).hexdigest().encode(encoding='utf_8')
#print ('secret: ' , hsecret)
messagebox.showinfo(message=hsecret)
 
secretCompound=user+':'+hsecret.decode(encoding='utf_8')
templateJson['secret'] = secretCompound
print (templateJson)
messagebox.showinfo(message=secretCompound)
messagebox.showinfo(message=templateJson)
authTokenResponse = requests.post(url, data=json.dumps(templateJson), headers={'Content-Type':'application/json', 'X-Version':'2'}, verify=False)
 
#authtoken = json.loads(authTokenResponse.content)['token']
authtoken = json.loads(authTokenResponse.content['token'])
#print('authToken: ' + authtoken)
messagebox.showinfo(message=authtoken)

