#pip install chardet

import chardet
print(chardet.detect(b'Hello, world!'))  #{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

data = 'こんにちは'.encode('euc_jp')
print(chardet.detect(data)) #{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}


data = 'こんにちは'.encode('utf-8')
print(chardet.detect(data)) #{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''} 

