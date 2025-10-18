setc1={"green","blue"}
setc2={"blue","yellow"}

print("Original sets: ")
print(setc1)
print(setc2)

setc=setc1.union(setc2)
print("\nUnion of above sets: ")
print(setc)

union_set= setc1 | setc2
print("Union: ", union_set)
