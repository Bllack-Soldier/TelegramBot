from utile import maxnum
import imoconv
x=imoconv.Imogi_converter
fa=input("Say Something:")
if ":/" not in fa:
    print("there is nothing to show")
else:
    x.converter(fa, fa)
    n=1
    k=1
    list1 = []
    while k<=5:
        inp = int(input("enter your number:"))
        list1.append(inp)
        k+=n
    maxnum(list1)