import os

def create_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('neg.txt','a') as f:
                    f.write(line)

create_neg()