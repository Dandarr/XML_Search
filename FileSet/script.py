#load file
with open('xml1.txt', encoding="utf8") as f:
    lines = f.readlines()
    postArray = str(lines).split('<post')
    for i in len(postArray){
        if postArray[i].find(word):
            
    }
    
    print(postArray[1])
    