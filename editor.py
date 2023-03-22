def run():
    def load_file():
        filename = input('open file: ')
        my_file = open(filename, 'r')
        data = my_file.readlines()
        for i in range(len(data)):
            data[i] = data[i][:-1]
        my_file.close()
        return data

    def print_data(data):
        print()
        line_number = 1
        for line in data:
            print(str(line_number)+' '+line)
            line_number += 1
        print()

    def edit_data(data):
        edit_line = int(input('Enter line number: '))
        index = edit_line -1
        print(data[index]) 
        line_data = input()
        return line_data, index

    def remove_line():
        remove_line = int(input('remove line (if 0 then abort): '))
        if remove_line == 0:
            return 0
        else:
            index = remove_line
        return index

    def save_file(data):
        filename = input('save as: ')
        new_file = open(filename, 'w')
        for line in data:
            new_file.write(line+'\n')
        new_file.close()

    def new_file():
        run = True
        data = []
        counter = 1
        while run:
            code_line = input(str(counter)+' ')
            
            counter += 1    
            if code_line == '/exit':
                run = False
            else:
                data.append(code_line)
        return data

    run = True
    commands = '1-Open 2-Print 3-Edit 4-Remove 5-Save 6-Exit 7-New_file'
    data = None
    while run:
        print(commands)
        command = input('Enter command: ')
        if command == '1':
            data = load_file()
        elif command == '2':
            print_data(data)
        elif command == '3':
            line_data, index = edit_data(data)
            data[index] = line_data
        elif command == '4':
            index = remove_line()
            if index != 0:
                data.pop(index-1)
        elif command == '5':
            save_file(data)
        elif command == '6':
            run = False
        elif command == '7':
            data = new_file()
        else:
            print('Wrong command')
