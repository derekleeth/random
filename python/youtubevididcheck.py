import urllib.request
import re

urlPre = "https://www.youtube.com/watch?v="

idSource = "https://kevingrahl.de/temp/ytids-m-18-07.txt"

response = urllib.request.urlopen(idSource)
html = response.read()

encoding = response.headers.get_content_charset('utf-8')
vidIdList = html.decode(encoding)



for vidID in vidIdList.splitlines():
    
    response = urllib.request.urlopen(urlPre+vidID)
    html = response.read()

    encoding = response.headers.get_content_charset('utf-8')
    html_text = html.decode(encoding)
    
    #path="C:\Temp\%s.html" % (vidID)
    #print(path)
    #file = open(path, 'w')
    #file.write(html_text)
    #file.close()

    regexp = re.compile(r'id=\Wunavailable-message\W')
    if bool(re.search(r'id=\Wunavailable-message\W', html_text)):
        print("Vid Not Online: "+vidID)
        print()
    else:
        print("Vid Online: "+vidID)
        print()


#response = urllib.request.urlopen(urlpre+vidid)
#html = response.read()

#print(html)