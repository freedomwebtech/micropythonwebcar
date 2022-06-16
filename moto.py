import socket
import machine


p = machine.PWM(machine.Pin(5), freq=10000)
p1 = machine.PWM(machine.Pin(4), freq=10000)
p2 = machine.PWM(machine.Pin(12), freq=10000)
p3 = machine.PWM(machine.Pin(13), freq=10000)


p.duty(0)
p1.duty(0)
p2.duty(0)
p3.duty(0)



html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
h1{color:#0f7663; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #680f76; border: none; 
border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
.button2{background-color:  #3f760f;}.button3{background-color:  #760f22;}.button4{background-color: #1e0f76;}}</style></head><body> <h1>ESP Web Server</h1> 
<p><a href="/?forward=on"><button class="button">FOWARD</button></a></p>
<p><a href="/?action=off"><button class="button button2">STOP</button></a></p>
<p><a href="/?reverse=on"><button class="button button3">REVERSE</button></a></p>
<p><a href="/?turn=on"><button class="button button4">TURN</button></a></p>
</body></html>"""
s = socket.socket()
s.bind(('0.0.0.0', 80))
s.listen(5)

while True:
    cs,addr=s.accept()
    response=cs.recv(1048)
    response=str(response)
    forward_on = response.find('/?forward=on')
    action_off = response.find('/?action=off')
    reverse_on = response.find('/?reverse=on')
    turn_on = response.find('/?turn=on')
   
    
    if forward_on == 6:
       print('FORWARD')
       for j in range(600):
            p.duty(0)
            p1.duty(j)
            p2.duty(j)
            p3.duty(0)
    if action_off == 6:
        print('STOP')
        p.duty(0)
        p1.duty(0)
        p2.duty(0)
        p3.duty(0)
        

    if reverse_on == 6:
       print("REVERSE") 
       for i in range(600): 
           p.duty(i)
           p1.duty(0)
           p2.duty(0)
           p3.duty(i)
       
          
       
    if turn_on == 6:
        print("TURN") 
        for h in range(900): 
           p.duty(0)
           p1.duty(h)
           p2.duty(0)
           p3.duty(h)
        
    
    cs.sendall(html)
    cs.close()
