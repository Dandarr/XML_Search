#importing reguular expression library
import re


#load file
#replace 'xml.txt' with the text file you are trying to process
with open('xml1.txt', encoding="utf8") as f:
    lines = f.readlines()

#process data
    postArray = str(lines).split('<post')
arrayLength = len(postArray)
for i in range(0, arrayLength):
    postArray[i] = postArray[i].replace('\n', ' ').replace('\r', '')
    if 'diagnose' in postArray[i]:
        with open("output.txt", "a", encoding="utf8") as myfile:
            myfile.write(postArray[i])
            myfile.write(("\n"))
            myfile.write(("\n"))

    if 'dx' in postArray[i]:
        with open("output.txt", "a", encoding="utf8") as myfile:
            myfile.write(postArray[i])
            myfile.write(("\n"))
            myfile.write(("\n"))


print('finished')


