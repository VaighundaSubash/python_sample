import urllib.request;

import re;

url = input("Please enter the Valid URL : ");

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE);

if re.match(regex, url):
    request = urllib.request.urlopen(url);
    
    html = request.read();
    print(html);
    print("Status code = ", request.getcode());
    
else:
    print("Please enter the valid URL!!!");