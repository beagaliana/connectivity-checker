import urllib.request

def get_status_code(url):
    return urllib.request.urlopen(url).getcode()

def main():
    url = str(input('Type the site you want to check: '))
    print(get_status_code(url))

if __name__=='__main__':
    main()
