def outf():#2
    var=10#3
    def innf():#5
        var=20#6
        print('inner var',var)#7
    innf()#4
    print('outer',var)#8
outf()#1
