import os

def create_pos():
    for file_type in ['pos']:
        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('pos.txt', 'a') as f:
                    f.write(line)

create_pos()