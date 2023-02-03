import pandas as pd
import doubleagent

one = pd.read_csv('옥션 그냥등록.csv', engine='python')
one = one.values.tolist()
final = []
for li in one:
    print(li[0])
    final.append(str(li[0]))


doubleagent.picklemaker('actionfinal.pkl',final)

