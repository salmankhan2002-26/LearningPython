QnA =[["What is name of the capital of Bangladesh?", 
       "What's the year of freedom fight of Bangladesh?", 
       "What is the national anmial of Bangladesh?",
       "What is the national fruit of Bangladesh?"],
      ["Dhaka", "1971","Royal Bengal Tiger","Jackfruit"]]
options = [["Delhi","New York","Dhaka","Sylhet"],
           ["1971","1945","1975","1789"],
           ["Cow","Royal Bengal Tiger","Dog","Deer"],
           ["Kiwi","Strawberry","Mango","Jackfruit"]]
grade=0
for x in range(0,len(QnA[0])):
    print(QnA[0][x])
    for y in range(0,len(options[x])):
        print(f"{y+1}. {options[x][y]}")
    guess = int(input("Guess (1-4):"))
    if(options[x][guess-1]==QnA[1][x]):
        print("Correct")
        grade+=10
    else:
        print(f"Incorrect: {options[x][guess-1]} |  Correct: {QnA[1][x]}")
print("Grade is: ",grade)