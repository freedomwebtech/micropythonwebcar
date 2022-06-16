import socket
s = socket.socket()
s.bind(('0.0.0.0',80))
s.listen(4)
html="""
      <html><h1><center>"ESP8266 WEB SERVER"</center></h1></html>
     """

while True:
      cs,addr=s.accept()
      response=cs.recv(1048)
      response=str(response)
      cs.sendall(html)
      cs.close()