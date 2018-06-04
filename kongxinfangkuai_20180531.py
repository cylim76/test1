import os

print ("test text is here")
print ("test text is here")
print ("test text is here")

input()

os.system("cls")
for i in range(5):
    for k in range(6):
        if i==0 or i==4:
            print("* ",end="")
        if i>0 and i<4:
            if k==0 or k==5:
                 print("* ",end="")
            else:
                print("  ",end="")
  
    print()
 
input()