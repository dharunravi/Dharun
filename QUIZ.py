print('Welcome To General  Knowledge QUIZ')
print(" ")
print('It would greatfull to you')
print(" ")
GK=[
    {
        "question":"which is easy to learn ?",
        "option":["A)java","B)pyhton"],
        "answer":"B"
    },
    {
        "question":"who is father of the computer ?" ,
        "option":["A) Charless babbage","B) isaac newton"],
        "answer":"A"
     },
    {
        "question":"which gas is used to breath ?",
        "option":["A)CO2","B)oxygen"],
        "answer":"B"
    }
    
    ]
print(" ")
score=0
for x,y in enumerate(GK,start=1):
    print(f"{x},{y['question']}")
    
    for p in y["option"]:
        print(p)
    
    l=input("OPTION A OR B : ").upper()
    
    if y["answer"]==l :
        score+=1
        print('Right Answer')
    
    else:
        print('Wrong Answer')

print(f"You Scored{score}out of {len(GK)}")