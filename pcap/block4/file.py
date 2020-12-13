
def read_file(filepath):
    try:
        print('file opening...')
        file = open(filepath, 'r')
    except Exception as error:
        print('Error', error)
    else:
        print('printing file lines...')
        #file.readline(3) /read(3) =>read first characters of the first line
        # file.readlines(2) /file  =>read the 2 first lines 
        for line in file:
            print(line)
        print('file closing....')
        file.close()
    finally:
        print(filepath, 'closed: ', file.closed)
        
def write_into_file(file_path):
    try:
        print('file opening...')
        with open(file_path, 'w') as file:
            print('writing....')
            # file.write('fastapi')
            file.writelines(['sqlite3\n', 'pylint\n', 'pandas\n', 'scipy\n'])
    except Exception as error:
        print('Error', error)
    finally:
        print(file_path, 'closes: ', file.closed)
        

    
        

# read_file('./data/content.txt')
# 
write_into_file('./data/requirements.txt')