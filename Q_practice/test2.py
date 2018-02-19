def f_filt(src,des,filt):
    f = open(src)
    li = []
    count = 0
    for word in f:
        word = word.strip()
        if filt in word:
            li.append(word)
            count = count+1
    return count
    f.close()
    f = open(des,'w')
    for word in li:
        f.write(word+'\n')