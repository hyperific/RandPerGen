def getlist(path, ContainsHeader=True):
    try:
        file = open(path,'r')
        contents = file.readlines()
        lines = []
        if len(contents) > 0:   
            if ContainsHeader == True:
                min = 1
            else:
                min = 0
            for n in range(min, len(contents)):
                x = contents[n].strip('\n')
                x = x.split('\t')
                lines.append(x)
            return lines
        else:
            print('Error in tsv2list')
    except Exception as e:
        print('Error in tsv2list.py')
        print(e)