
def add():
    with open("text.txt","a") as f:
        m=input("ENTER THE TASK ")
        f.writelines(f"{m}\n")
        print("TASK WAS ADDED!! ")
        
        
def view():
    with open ("text.txt",'r') as q:
        e=q.readlines()
        for i,v in enumerate(e) :
            print(i,v)

def dell():
    with open ("text.txt",'r') as q:
        e=q.readlines()
        for i,q in enumerate(e):
            print(i,q.strip())
            
        f=int(input())
        if 0<=f<len(e):
            del e[f]
            with open ("text.txt",'w') as m:
                m.writelines(e)
                print("TASK DELETED SUCCESSFULY")
                
            
while True:

    print("Your To-Do List\n")
    
    print("Enter 1 to add Task\n")
    
    print("Enter 2 to View Task\n")
    
    print("Enter 3 to delete completed task \n")
    
    print("Enter 4 to Exit\n")
    try:
        a=int(input("1 / 2 / 3 / 4 : "))
        if a==1:
            add()
        
        elif a==2:     
            view()
        
        elif a==3:    
            dell()
        
        elif a==4:
            break
        
        else:
            print("\nINVALID INPUT!!\n")
    
    except ValueError:
        print("\nINPUT MUST BE INTEGER  \n")