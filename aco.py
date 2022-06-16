import network

ssid = 'FREEDOMTECH'
password = '123456789'
def do_connect():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    while ap.active() == False:
          pass
    print('Connection successful')
    print(ap.ifconfig())
    
do_connect()    
