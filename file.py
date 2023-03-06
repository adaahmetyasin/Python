#f = open("test.txt", "w")
#f.write("Now the file has more content!")
#f.close()

#f = open("test.txt", "r")
#print(f.read())

import os
f = open("myfile.txt", "w")
f.write("Now the file has more content!")
f = open("myfile.txt", "r")
print(f.read())
f.close()

os.remove("test.txt")

