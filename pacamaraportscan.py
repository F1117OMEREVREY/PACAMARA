import socket

def is_host_up(host, ports=[80]):
    try:
        ip = socket.gethostbyname(host)
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)  # Set a timeout value for the connection 
attempt
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open on {host} ({ip})")
            else:
                print(f"Port {port} is closed on {host} ({ip})")
            sock.close()
    except socket.gaierror:
        print(f"Invalid hostname: {host}")
    except socket.error:
        print(f"Couldn't connect to {host}")

# Usage example
target_host = "testhtml5.vulnweb.com" #domain only
common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 443, 445, 1433, 1521, 
3306, 3389]
is_host_up(target_host, common_ports)
