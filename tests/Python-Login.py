import requests
import json
import sys
import hashlib

prot = 'http'
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
 
templateResponse = requests.get(url, headers={'Content-Type':'application/json', 'X-Version':'2'}, verify=False)
print("Dings: ", templateResponse)
templateJson = json.loads(templateResponse.content)
print(templateResponse.text)
userandnonce=(user+templateJson['nonce']).encode(encoding='utf_8', errors='strict')
hpassword=hashlib.sha512(pw.encode(encoding='utf_8', errors='strict')).hexdigest()
passwordHashed=hpassword.encode(encoding='utf_8')
hsecret = hashlib.sha512(userandnonce+passwordHashed).hexdigest().encode(encoding='utf_8')
print ('secret: ' + hsecret)
 
secretCompound=user+':'+hsecret.decode(encoding='utf_8')
templateJson['secret'] = secretCompound
print (templateJson)
authTokenResponse = requests.post(url, data=json.dumps(templateJson), headers={'Content-Type':'application/json', 'X-Version':'2'}, verify=False)
 
authtoken = json.loads(authTokenResponse.content)['token']
print('authToken: ' + authtoken)

