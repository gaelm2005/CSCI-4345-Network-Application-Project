import socket # for connecting
from colorama import init, Fore

#We will use colorama here just for printing in green colors whenever a port is open, and gray when it is closed.
# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

print("This step is good.")


"""
    determine whether `host` has the `port` open
    """

def is_port_open(host, port):
    
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        # s.settimeout(0.2)
    except:
        # cannot connect, port is closed
        # return false
        return False
    else:
        # the connection was established, port is open!
        return True


# get the host from the user
host = input("Enter the host:")
# iterate over ports, from 1 to 1024 or 65535
for port in range(1, 1024):
    if is_port_open(host, port): #is_port_open is the function defined above
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
