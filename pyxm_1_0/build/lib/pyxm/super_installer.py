import os

api_key = raw_input('Please enter your api key here: \n>')

os.system('pip install -r requirements.txt')
os.system('touch ./bin/api_key.py')
os.system('echo "__API_KEY__ = \'' + api_key + '\'" > "./bin/api_key.py"')
os.system('python setup.py install')

