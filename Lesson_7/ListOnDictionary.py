def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result

students=[[1, 'Jean','V'],[2,'Lula','V'],[3,'Brain','IV'], [4,'Lynne','VI'],[5,'Zachary','VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted lists to a dictionary:")
print(test(students))