# Ip-Port-Scanner
Code Description:

The provided code is a Python script that performs a port scanning operation on a specified IP address. It allows the user to input a target IP address, a range of ports to scan, an output file path, and an output file name. The script then attempts to connect to each port within the specified range on the target IP address and determines whether the port is open or closed.

The main function in the code is `scanports()`, which takes the target IP address, start port, end port, and output file name as parameters. It validates the input parameters, checks for errors such as an invalid IP address, port range, or output file path, and performs the port scanning operation.

The port scanning process is implemented using the `socket` module in Python. It creates a socket object for each port within the specified range and attempts to establish a TCP connection with the target IP address and port. If the connection succeeds (`connect_ex()` returns 0), the port is considered open, and its number is added to the `openports` list. If the connection fails, the port is considered closed, and its number is added to the `closeports` list.

After scanning all the ports, the script writes the results to the specified output file. It first writes a list of all open ports for the target IP address, followed by a list of all closed ports. Each port number is written on a separate line in the output file.

The script provides informative console output during the scanning process, including the status (open or closed) of each port being scanned. It also prints the path where the output file is saved.

To use the code, the user is prompted to enter the target IP address, start and end port numbers, output file path, and output file name. The code then calls the `scanports()` function with the provided input parameters.

Overall, this code provides a basic implementation of a port scanner in Python, allowing users to scan a range of ports on a given IP address and save the results to a file.
