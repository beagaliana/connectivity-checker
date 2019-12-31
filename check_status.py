import pycurl, validators
import urllib.request
import sys
import socket

def url_exists(url):
	
	#Check if the given URL really exists
	
	if validators.url(url):
		c = pycurl.Curl()
		c.setopt(pycurl.NOBODY, True)
		c.setopt(pycurl.FOLLOWLOCATION, False)
		c.setopt(pycurl.CONNECTTIMEOUT, 10)
		c.setopt(pycurl.TIMEOUT, 10)
		c.setopt(pycurl.COOKIEFILE, '')
		c.setopt(pycurl.URL, url)
		try:
			c.perform()
			response_code = c.getinfo(pycurl.RESPONSE_CODE)
			c.close()
			return True if response_code < 400 else False
		except pycurl.error as err:
			errno = err
		except pycurl.error as err1:
			errstr = err1
			raise OSError('An error occurred: {}'.format(errstr))
	else:
		raise ValueError('"{}" is not a valid url'.format(url))

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

def test_url_exists():
    print("WEB CONNECTIVITY CHECKER TOOL")
    host = input('Host: ')

    if (url_exists("http://"+host)):
        print("CONNECTION SUCCESSFUL: website up.")
    else:
        print("CONNECTION FAILED: website down.")

def test_connection_urllib():
    url = str(input('Type the site you want to check: '))
    print(get_status_code(url))

def test_server_socket_connection():
    host = input('Host: ')
    port = int(input('Port: '))
    if check_socket_server(host, port):
        print("Server is UP")
    else:
        print("Server is DOWN")

def main():
#    test_connection_urllib()
#    test_server_socket_connection
    test_url_exists()

if __name__=='__main__':
    main()
