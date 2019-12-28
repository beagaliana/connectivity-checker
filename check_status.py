import pycurl, validators


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
			errno, errstr = err
			raise OSError('An error occurred: {}'.format(errstr))
	else:
		raise ValueError('"{}" is not a valid url'.format(url))


print("WEB CONNECTIVITY CHECKER TOOL")
host = input('Host: ')

if (url_exists("http://"+host)):
	print("CONNECTION SUCCESSFUL: website up.")
else:
	print("CONNECTION FAILED: website down.")
