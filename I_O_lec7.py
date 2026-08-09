# f = open("demo.txt", "a")
# data = f.read()
# line1 = f.readline()
# print(data)
# print(line1)
# print(type(data))

# f.write("This is me")
# f.write("\nWhat is your name?")
# f.close()

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    
with open("demo.txt", "w") as f:
    f.write("This is me --- IGNORE ---")

# delete file
import os
os.remove("demo.txt")