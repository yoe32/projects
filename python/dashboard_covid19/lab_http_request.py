import requests
import os
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r=requests.get(url)
r.status_code
#print(r.request.headers)

#print('request body:', r.request.body)

header = r.headers
#print(r.headers)

header['date']

header['Content-Type']

r.encoding

r.text[0:100]

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r = requests.get(url)

#print(r.headers)

r.headers['Content-Type']

path = os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)


URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

r = requests.get(URL)

path = os.path.join(os.getcwd(), 'example1.txt')

with open(path,'wb') as f:
    f.write(r.content)

###################################

url_get = 'http://httpbin.org/get'

payload = {'name':'Joseph', 'ID':'123'}

r = requests.get(url_get,params=payload)

print(r.url)
