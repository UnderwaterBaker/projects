import nmap #imports the nmap module

print("""=======================================
Simple nmap scanner(type 'die' to quit)
=======================================""")

running = True
while running == True:

    ns = nmap.PortScanner() #assigns the variable ns

    ip_addr = input("Ip to scan: ") #lets the user specifiy the ip to scan
        
    if ip_addr == 'die': #breaks the loop if users says 'die'
        print("dont forget to leave a like comment and subscribe")
        break

    port_range= input("port range: ") #lets the user specify the port range
    print("""<----------------------------------------->
Please wait while your scan is completed...
<----------------------------------------->""")

    ns.scan(ip_addr, port_range ,' -T5') #gives nmap the details to peform the scan

    print("""-
-
-
<------------------->
Scan details below
<-------------------> """)

    print(ns.command_line()) #shows the command nmap used in the terminal window
    print(ns.scaninfo()) #shows details about the scan is the terminal window
    print(ns.csv()) #show open and closed ports in console
