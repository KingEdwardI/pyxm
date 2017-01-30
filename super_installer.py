import os

api_key = raw_input('Please enter your api key here: \n>')

os.system('pip install -r requirements.txt')

os.system('mkdir ~/.pyxm')
os.system('touch ~/.pyxm/api_key')
os.system('echo "' + api_key + '" > "~/.pyxm/api_key"')
os.system('cd pyxm_1_0/')
os.system('python setup.py install')

