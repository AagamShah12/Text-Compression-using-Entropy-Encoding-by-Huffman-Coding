from collections import Counter
import numpy as np
import copy
import csv
import io

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def is_leaf(self):
        if (self.left is None) and (self.right is None):
            return True
        else:
            return False

def create_freq_table(input_file):
    freq_count = dict(Counter(list(input_file)))
    return freq_count

def create_tree(freq_table):
    ip_data_freq_node = []
    for data in freq_table.items():
        n = Node(data)
        ip_data_freq_node.append(n)
    ip_data_freq_node.sort(key=lambda x: x.data[1])
    while(len(ip_data_freq_node) > 1):
        left_child = ip_data_freq_node[0]
        right_child = ip_data_freq_node[1]
        val = left_child.data[1] + right_child.data[1]
        parent = Node((left_child.data[0]+right_child.data[0],val))
        parent.left = left_child
        parent.right = right_child
        ip_data_freq_node.pop(0)
        ip_data_freq_node.pop(0)
        ip_data_freq_node.append(parent)
        ip_data_freq_node.sort(key=lambda x: x.data[1])
    return ip_data_freq_node[0]


def decode_code(input_file,root):
    decode_stream = []
    temp_root = copy.deepcopy(root)
    s = ""
    for i in input_file:
        if i=='0':
            temp_root = temp_root.left
        else:
            temp_root = temp_root.right
        if temp_root.is_leaf():
            decode_stream.append(temp_root.data[0])
            temp_root = copy.deepcopy(root)
    return decode_stream


# In[6]:


def find_codeword(root):
    encoded_data = dict()
    def printcodeword(root,code):
        if root:
            printcodeword(root.left,code+'0')
            printcodeword(root.right,code+'1')
            if root.is_leaf():
                encoded_data[root.data[0]] = code
#             print(root.data)
    printcodeword(root,"")
    return encoded_data


# In[7]:


def create_encoding_csv(encoded_data):
    csv_data = [["Symbol","Encoding"]]
    for Symbol,code in encoded_data.items():
        csv_data.append([Symbol , code])
    with open('encoding.csv', 'w', newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(["Symbol" , "code"])
        for Symbol,code in encoded_data.items():
            writer.writerow([Symbol , code])


# In[8]:


def generate_encode_file(encode_table):
    encoding_stream = ""
    for i in input_data:
        encoding_stream += encode_table[i]
    f = open("EncodedNamarie.txt", "a")
    f.write(encoding_stream)
    f.close()


input_file = io.open("Namarie.txt", mode="r", encoding="utf-8")
input_data = input_file.read()
# print(len(input_data))
freq_table = create_freq_table(input_data)
root = create_tree(freq_table)
encode_table = find_codeword(root)
create_encoding_csv(encode_table)
generate_encode_file(encode_table)

