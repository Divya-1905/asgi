# from ctypes import addressof
# from os import name


# class new():
#     def __init__(self,name,phone) -> None:
#         self.name=name
#         self.phone=phone
#     def ti(self):
#         print(self.name +' '+str(self.phone))
# class new2(new):
#     def __init__(self,name,phone,address) -> None:
#         super().__init__(name,phone)
#         self.address=address
#         self.name=name
#     def t2(self):
#         print('from inherited ' + self.name + ' ' + self.address)
#         super().ti()
#     def __str__(self):
#         return self.name
# p=new2('siva',9942945428,'usilampatti')
# p.t2()
# print (p)
from operator import length_hint

class Solution():
    def __init__(self,a,n) -> None:
        self.a=a
        self.n=n
    def sum(self):
        k=0
        d=len(self.a)
        e=[]
        for i in range(len(self.a)):
            f=[]
            for j in self.a[i:d]:
                k=k+j
            e.append(k)
            if k==12:
                return self.a[i:d]
            else:
                k=0
                d= d-1
        return e
s=Solution([1,2,3,7,5],12)
print(s.sum())           
                