from flask import Flask
from flask import request
from flask import render_template
from Crypto.Cipher import AES
import string
from base64 import b64encode
import base64
import binascii
import random
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from pkcs7 import PKCS7Encoder
import time



key = input("Ingresa la llave de 16 caracteres:\n")
clear_text = input("Ingrese el mensaje a cifrar:\n")

master_key = bytes(key,'utf-8')
raw = bytes(clear_text,'utf-8')
key = base64.b64encode(master_key).decode()
raw = bytes(clear_text,'utf-8')

print('Llave en base64: ', key)
cipher = AES.new(master_key, AES.MODE_EAX)
encrypt = base64.b64encode(cipher.encrypt(pad(raw,AES.block_size))).decode()
nonce = base64.b64encode(cipher.nonce).decode()
print('Mensaje en base 64: ', encrypt)
print('Nonce en base 64: ',nonce)
time.sleep(10)

f = open('template/holamundo.html','w')

mensaje1 = """<html>
<head><title>Descifrado</title>   <script> 
        function printDiv() { 
            var divContents = document.getElementById(" e_data").innerHTML; 
            var a = window.open('', '', 'height=500, width=500'); 
            a.document.write('<html>'); 
            a.document.write('<body > <h1>Div contents are <br>'); 
            a.document.write(divContents); 
            a.document.write('</body></html>'); 
            a.document.close(); 
            a.print(); 
        } 
    </script> </head>
<body>
        <p id= "01">Este sitio contiene un mensaje secreto</p>
        <h1>Descifrado</h1>

"""

f.write(mensaje1)

#mensaje2 = '<div class="AES" id="'+str(encrypt)+'">'+str(encrypt)+'</div>'
mensaje2 = '<div class="AES" id="'+encrypt+'"></div>'
f.write(mensaje2)
mensaje3 = """
"""
f.write(mensaje3)

mensaje4 = '<div class="key" id="'+key+'"></div>'

f.write(mensaje4)
mensaje6 =  '<div class="iv" id="'+nonce+'"></div>'
#mensaje6 =  '<div class="nonce" id="'+nonce+'"></div>'
f.write(mensaje6)

mensaje5 = """<script>
function myFunction() {
  var x = document.getElementById("myBtn").value;
  document.getElementById("p01").innerHTML = x;
}
function myFunction2() {
  var x = document.getElementById("p01").innerHTML
  document.getElementById("myBtn").value = x;
}
</script>

</body> 
</html>  """

f.write(mensaje5)
f.close()


app = Flask(__name__,template_folder='template')

@app.route("/")
def hello():
    return render_template('holamundo.html')


app.run()
