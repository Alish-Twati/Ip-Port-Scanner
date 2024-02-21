
import socket

def scanports(targetIp, startport, endport, outputfile):
    print(f"Scanning target IP: {targetIp}")
    openports = []  
    closeports = []  
    try:

        socket.inet_aton(targetIp)
    except socket.error:
        print("Invalid target IP address.")
        return

    if not(0 <= startport <= 65535) or not (0 <= endport <= 65535):
        print("Invalid port number. Port number must be between 0 and 65535.")
        return

    if startport > endport:
        print("Invalid port range. Start port must be less than or equal to end port.")
        return

    try:
        with open(outputfile, 'w') as file:
            for port in range(startport, endport + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.0001)
                result = sock.connect_ex((targetIp, port))
                if result == 0:
                    print(f"Port {port}: Open")
                    openports.append(port)
                else:
                    print(f"Port {port}: Closed")
                    closeports.append(port)
                sock.close()

            file.write(f"All open ports for target IP {targetIp}:\n")
            for port in openports:
                file.write(f"{port} Port\n")

            file.write(f"\nAll closed ports for target IP {targetIp}:\n")
            for port in closeports:
                file.write(f"{port} Port\n")

        print(f"\nOutput file saved at: {outputfile}")
    except OSError:
        print("Invalid output file path or name.")

targetIp = input("Enter the target IP address: ")
startport = int(input("Enter the start port: "))
endport = int(input("Enter the end port: "))
outputpath = input("Enter the output file path: ")
outputfile = outputpath.rstrip("/") + "/" + input("Enter the output file name: ")
scanports(targetIp, startport, endport, outputfile)
