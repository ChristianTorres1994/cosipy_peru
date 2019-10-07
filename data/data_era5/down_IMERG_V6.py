# Codigo para descargar archivos MODIS
# Autor :  Christian Torres
# christian1994@furg.br
# Fecha: 26/06/2018
# Version : V01

import urllib.request
import urllib.error
import http.cookiejar
from base64 import b64encode

registro = open('IMERG_2018.txt').readlines() # registro

for i in range(len(registro)):
  
    #URL de la imagen preliminar
    urlimagen = registro[i]
      
    #Nombre de la imagen
    nombreimagen = registro[i][74:-1]

    try:
        userAndPass = b64encode(b"christian010194@gmail.com:Torres1994").decode("ascii")
        header = { 'Authorization' : 'Basic %s' %  userAndPass }

        class MyHTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
            def http_error_302(self, req, fp, code, msg, headers):
                return urllib.request.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

        cookieprocessor = urllib.request.HTTPCookieProcessor()

        opener = urllib.request.build_opener(MyHTTPRedirectHandler, cookieprocessor)
        urllib.request.install_opener(opener)

        req = urllib.request.Request(urlimagen,headers = header)
        req.add_header('Authorization' , 'Basic %s' %  userAndPass)
        x = urllib.request.urlopen(req)

        f = open('2018/'+nombreimagen, 'wb')
        f.write(x.read())
        f.close()

        print('Save file: '+ nombreimagen)

    except urllib.error.URLError as e:
        print(e)
