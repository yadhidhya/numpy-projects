''' unlike previous code if you do not have url containing csv data or you have a csv file which is already downloaded,
    add that file in folder which contains this code.

    This is a code to read csv values from txt file, parsing the header, parsing each line converting data into float values
    and adding them to the dictionary which contains headers as keys and data as values and then printing them. 
'''



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

def read_csv(file):
    result=[]
    # open the file in read mode
    with open(file,'r') as f:
        # get a list of lines
        lines=f.readlines()
        # parse the header
        header=parse_headers(lines[0])
        # loop over the remaining lines
        for data_line in lines[1:]:
            # parse the values
            values = parse_values(data_line)
            # create a dictionary using values and headers
            item_dict=create_item_dict(values,header)
            # add the dictionary to the result
            result.append(item_dict)
    return result

with open('hello.txt') as file1:
    print(file1.read())
    data = read_csv('hello.txt')
    for row in data:
        print(row)
