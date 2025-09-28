with open("practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# found learning word in the file or not
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

# find the line number of the word learning       
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())


# a file containing numbers separated by commas, read the file and print the count of even numbers.
with open("numbers.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,9")
    
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)
    
    nums =data.split(',')
    for val in nums:
        if(int(val) % 2 == 0):
            print(val)
    
    
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ','):
    #       print(int(num))
    #       num = ""
    #     else:
    #         num += data[i]
    