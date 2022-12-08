class Sorting:
    def __init__(self,array):
        self.array=array
    def BubbleSort(self):
        for i in range(0,len(self.array)-1):
            flag=False
            for j in range(0,len(self.array)-i-1):
                if self.array[j]>self.array[j+1]:
                    temp=self.array[j]
                    self.array[j]=self.array[j+1]
                    self.array[j+1]=temp
                    flag=True
            if not flag:
                break
a=Sorting([1,7,8,9,0,3])
a.BubbleSort()
print(a.array)