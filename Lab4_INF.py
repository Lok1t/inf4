
def MainTask():
    json_file = open('json_Main.txt', 'w', encoding='utf-8')
    json_file.write('{' + '\n' + '\t')
    with open('xml_Main.txt', encoding='utf-8') as file:
        names = []
        count_of_blocks = 0
        count_of_options = 0
        for line in file:
            options = []
            for i in line:
                if i == '<' and (('/lesson' in line) or ('/day' in line) or ('/schedule' in line)):
                    line = ''

                if i == '<' and (('/lesson' not in line) and ('/day' not in line) and ('/schedule' not in line)):
                    line = line.replace('<', '"', 1)

                if i == 'n' and ('name' in line):
                    names.append('"_name": ' + line[line.find('=') + 1:line.find('>')])
                    line = '\t' + line[:line.rfind('n') - 1] + '>'

                if i == 'a' and ('audience=' and 'building=' in line):
                    options.append('"_audience": ' + line[line.find('=') + 1:line.find('b') - 1] + ',')
                    options.append('"_building": ' + line[line.rfind('=') + 1:line.find('/') - 1])
                    line = '\t' + line[:line.rfind('a') - 1] + '/>'

                if i == 't' and ('time=' in line):
                    options.append('"_time": ' + line[(line.find('=') + 1):line.find('/') - 1])
                    line = '\t' + line[:line.rfind('t') - 1] + '/>'

                if i == 'p' and ('practician=' in line):
                    options.append('"_practician": ' + line[line.find('=') + 1:line.find('/') - 1])
                    line = '\t' + line[:line.rfind('p') - 1] + '/>'

                if i == 't' and ('trainer=' in line):
                    options.append('"_trainer": ' + line[line.find('=') + 1:line.find('/') - 1])
                    line = '\t' + line[:line.rfind('t') - 1] + '/>'

                if i == 'f' and ('format=' in line):
                    options.append('"_format": ' + line[line.find('=') + 1:line.find('/') - 1])
                    line = '\t' + line[:line.rfind('f') - 1] + '/>'

                if i == '/' and ('/>' in line):
                    line = line.replace('/>', '": {', 1)

                if i == '>' and ('/>' not in line):
                    line = line.replace('>', '": {', 1)

            json_file.write(line + "\n")
            if len(options) != 0:
                for option in options:
                    json_file.write('\t' * 5 + option + '\n')
                json_file.write('\t' * 4 + '},' + '\n')
                count_of_options += len(options)

                if count_of_options == 5:
                    count_of_options -= 5
                    json_file.write('\t' * 4 + names[1] + '\n')
                    names.pop(1)
                    json_file.write('\t' * 3 + '},')
                    count_of_blocks += 1

                    if count_of_blocks == 3:
                        json_file.write('\n')
                        json_file.write('\t' * 3 + names[0] + '\n')
                        for j in range(3):
                            json_file.write('\t' * (2 - j) + '}' + '\n')
    file.close()
    json_file.close()
    json_file1 = open('json_Main.txt', encoding='utf-8').readlines()
    json_file1.pop(2)
    with open('json_Main.txt', 'w', encoding='utf-8') as json_file2:
        json_file2.writelines(json_file1)
    json_file2.close()



original = open('xml_Main.txt', encoding='utf-8').readlines()
MainTask()
