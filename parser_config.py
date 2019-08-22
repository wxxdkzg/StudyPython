import configparser
config = configparser.ConfigParser()
config.read('parser.ini')
str1 = config['bitbucket.org']['User']
print(str1)
str2 = config['DEFAULT']['Compression']
print(str2)
