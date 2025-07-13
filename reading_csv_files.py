'''now we are going to download a csv file from the url, parsing header and each line seperately
then we will create a list of dictionaries which contains headers as keys and csv data as values.
all the values are converted into float values'''

# before starting the process lets create a directory which contains csv files 


import os
os.makedirs('./data', exist_ok=True)
url1='paste the url which contains csv file'
url2='paste the url which contains csv file'
url3='paste the url which contains csv file'
import urllib.request
urllib.request.urlretrieve(url1,'./data/file1_name.txt')
urllib.request.urlretrieve(url2,'./data/file2_name.txt')
urllib.request.urlretrieve(url3,'./data/file3_name.txt')

# now the data directory contains 3 csv files downloaded from urls

# process 1: defining the function for parsing the headers
def parse_headers(header_line):
    return header_line.strip().split(',')

# process 2: after dealing with headers, now let's settle down the data lines
def parse_values(data_line):
    values=[]
    for item in data_line.strip().split(','):
        ''' while splitting the line if there is any value missing in a data line,
         it will be consider as an empty string which gives error while converting 
         empty string to float so update the missing data with 0'''
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values
# it's time to create a dictionary which contains data and headers
def create_item_dict(values,headers):
    result={}
    for value, header in zip(values,headers):
        result[header]=value
    return result

# let's create an ultimate function which calls all the above functions

def read_csv(path):
    result=[]
    with open(path,'r') as f:
        lines=f.readlines()
        header=parse_headers(lines[0])
        for data_line in lines[1:]:
            values = parse_values(data_line)
            item_dict=create_item_dict(values,header)
            result.append(item_dict)
    return result

with open('./data/file1_name.txt') as file1:
    print(file1.read())
    read_csv('./data/file1_name.txt')

    
            