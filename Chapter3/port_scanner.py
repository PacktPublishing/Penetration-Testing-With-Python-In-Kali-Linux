import socket 

 

def port_scanner(host, port_range): 

    open_ports = [] 

    for port in range(*port_range): 

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

        sock.settimeout(1)  # Timeout for the socket operation 

        result = sock.connect_ex((host, port)) 

        if result == 0: 

            print("Port ", port, "is open") 

            open_ports.append(port) 

        sock.close() 

    return open_ports 

 

if __name__ == "__main__": 

    target_host = 'localhost' 

    target_ports = (1, 65535)  # Define the range of ports to scan 

    print("Scanning ports on", target_host) 

    open_ports = port_scanner(target_host, target_ports) 

    print("Open ports:", open_ports) 
