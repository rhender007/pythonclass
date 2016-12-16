'''
Created on Nov 29, 2016

@author: Student
'''
from urllib.request import urlopen

def read_url_data(urlName):
    if urlName.startswith(('http:', "https:", "ftp:")):
        return urlopen(urlName).read()
    else:
        with open(urlName) as f:
            return f.read()
        
if __name__ == '__main__':
    print(read_url_data("http://www.baidu.cn"))
    