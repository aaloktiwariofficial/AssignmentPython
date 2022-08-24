aIter=iter(aDictionary)
print(next(aIter))

for x in aDictionary.items():
  print(x)


aset={"Aman","Kartik","Varun","Babloo","Zaid"}
print(aset)
aset.add("Ananya")
print(aset)
aset.remove("Aman")
print(aset)
del aset


set1={"a","b","c"}
set2={"d","e","e"}
set4={"apple",False,86}
set3=set1.union(set2)
set5=set1|set2|set4
del set5
print(set3)
