import pandas as pd
import doubleagent
# one - two
one = pd.read_csv('g마켓 등록가능상품.csv', engine='python')
one = one.values.tolist()
onenum = []
for li in one:
    print(li[0])
    onenum.append(str(li[0]))

twonum = []
two = pd.read_csv('지마켓광고등록상품.csv', engine='python')
two = two.values.tolist()
for li in two:

    twonum.append(str(li[0]))

final = doubleagent.sublist(onenum,twonum)
doubleagent.picklemaker('gmarketfinal.pkl',final)

