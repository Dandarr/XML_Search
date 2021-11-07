#-------------imports----------------
import re
import os

#-----------load files---------------
fileList = []
#for each file in /input/
#add all files in /input/ into fileList
here = os.getcwd() + '/input/'
for fileName in os.listdir(here):
    fileList.append(fileName)
numberOfFiles = len(fileList)
for x in range(0, numberOfFiles):
    #change file extension to txt
    thisFile = os.getcwd() + '/input/' + fileList[x]
    print('attempting to rename: ' + thisFile)
    splitFileName = os.path.splitext(thisFile)
    os.rename(thisFile, splitFileName[0] + '.txt')
print('files loaded and preProcessing is complete')

#reset fileList as the names have technically changed
fileListPost = []
for filename in os.listdir(here):
    fileListPost.append(fileName)


for c in range(0, numberOfFiles):
    with open((here + fileListPost[c]), encoding="utf8") as f:
        lines = f.readlines()
#-----------process data------------
    postArray = str(lines).split('<post')
    arrayLength = len(postArray)
#add any additional search parameters to wordlist[] be aware that wildcards are assumed after the word so diagnos can find diagnose and diagnosis as well as any other variations
    wordlist = ['diagnos','dx']
    wordlistLength = len(wordlist)
    for i in range(0, arrayLength):
        postArray[i] = postArray[i].replace('\n', ' ').replace('\r', '')
        for z in range (0, wordlistLength):
            if wordlist[z] in postArray[i]:
                with open("output.txt", "a", encoding="utf8") as myfile:
                    myfile.write('<post' + postArray[i])
                    myfile.write(("\n"))
                    myfile.write(("\n"))
print('finished')


