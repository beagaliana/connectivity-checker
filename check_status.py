import urllib.request
import sys
import socket
 
# Check status using urllib
def get_status_code(url):
    return urllib.request.urlopen(url).getcode()

# Check if socket on the server is listening
def check_socket_server(host, port):
    addr_info = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    for family, socktype, proto, canonname, sockaddr in addr_info:
        s = socket.socket(family, socktype, proto)
        try:
            s.connect(sockaddr)
        except socket.error:
            return False
        else:
            s.close()
            return True

def main():
#    url = str(input('Type the site you want to check: '))
#    print(get_status_code(url))
    host = input('Host: ')
    port = int(input('Port: '))
    if check_socket_server(host, port):
        print("Server is UP")
    else:
        print("Server is DOWN")

if __name__=='__main__':
    main()
