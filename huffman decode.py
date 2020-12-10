import csv

def write_decoded_file(dict_table, file_data):
    cursor = 0
    decoded_file = ""
    def recur(cursor):
        for i in dict_table.items():
            codeword_length = len(i[1])
            if file_data[cursor:cursor+codeword_length] == i[1]:
                return (i[0],codeword_length)
    file_size = len(file_data)
    # print("filesize:", file_size)
    while cursor<file_size:
        t = recur(cursor)
        decoded_file +=t[0]
        cursor+=t[1]
    f = open("DecodedNamarie.txt", "a")
    f.write(decoded_file)
    f.close()
    return decoded_file


def read_encoded_file():
    f = open("EncodedNamarie.txt", "r")
    output = f.read()
    f.close()
    return output


def read_encoded_csv_file():
    f = open("encoding.csv", "r")
    output = csv.reader(f,delimiter=',')
    dict_table = dict()
    for i in output:
        dict_table[i[0]]=i[1]
    return dict_table

input_file = read_encoded_file()
csv_file = read_encoded_csv_file()
decoded_file = write_decoded_file(csv_file,input_file)
