import random
print("Welcome to Dodging Tabler")
table_start = input("Enter the table from which you want to start: \n")
table_end = input("Enter the table from which you want to end: \n")
nques = input("Enter the number of questions you want to play: \n")
print("Ok Let's Start. There is no negative marking!")
score = 0
for i in range(0, int(nques)):
    fnum = random.randint(int(table_start), int(table_end))
    snum = random.randint(2, 10)
    print(f"Q{int(i)+1}: {fnum} X {snum}")
    ans =  fnum * snum
    ansinput = input("Pls Enter Answer:\n")
    if ans == int(ansinput):
        print("Correct!\nPoints +1")
        score+=1
    else:
        print(f"Wrong the answer was {ans}")
print(f"Final Score: {int((int(score)/int(nques))*100)}%\nTotal Correct: {int(score)}\nTotal Wrong: {int(int(nques)-int(score))}")
