def cwff():
    count=0
    fname=input("Enter the file name- ")
    file=open(fname,'r')
    for line in file:
        word=line.split( )
        count=count+len(word)

    print("number of words are - ")
    print(count)
cwff()