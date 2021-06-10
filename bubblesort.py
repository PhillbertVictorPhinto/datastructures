def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1] ,lst[j]
lst =[99,44,6,2,1,5,63,87,283,4,0]
bubblesort(lst)
print(lst)