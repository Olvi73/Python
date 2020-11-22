Map = ["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def result(Str):
    newstr = ""
    for i in Str:
        if i in Map:
            if Map.index(i)+2>25:
                newstr += Map[abs(len(Map)-(Map.index(i)+2))]
                continue
            
            else:
                newstr += Map[Map.index(i)+2]
                continue
        newstr += i
    return newstr



if __name__ == '__main__':
    Str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(result(Str))
    intab="abcdefghijklmnopqrstuvwxyz"
    outtab="cdefghijklmnopqrstuvwxyzab"
    trantab = Str.maketrans(intab, outtab)
    print(Str.translate(trantab))
    Str="map"
    print(Str.translate(trantab))