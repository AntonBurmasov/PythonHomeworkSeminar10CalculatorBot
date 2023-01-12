def log(data):
    with open('logdata.txt', 'a') as file:
        file.write(data + '\n')
