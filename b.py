import array as arr
a1=arr.array('i',[1,3,5,7,9,6,3,9])
print("Original Array :",a1)
print('Number of occurrenses of 3 =',a1.count(3))
a1.reverse()
print("Reverse the order of items : ")
print(str(a1))
a1.append(30)
a1.insert(3,1000)
print(a1)

n=int(input("Enter n : "))
c=0
for x in a1:
    if x==n:
        c+=1
print(x,"is present",c,"items in the array")