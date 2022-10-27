print("Welcome to my computer quiz game")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's run this now")
score = 0

# Question 1
answer = input("What does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("Who is known as the father of computers? ")
if answer.lower() == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("When was the first computer invented? ")
if answer.lower() == "1943":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5
answer = input("Which popular company designed the first CPU? ")
if answer.lower() == "intel":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 6
answer = input("In which year '@' sign was first chosen for its use in e-mail address? ")
if answer.lower() == "1972":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 7
answer = input("A folder in Windows computer can't be made with the name? ")
if answer.lower() == "con":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 8
answer = input("Which type of number system a computer uses to calculate and store data? ")
if answer.lower() == "binary":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 9
answer = input("Total number of function keys in a computer keyboard? ")
if answer.lower() == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 10
answer = input("First computer virus is known as? ")
if answer.lower() == "creeper virus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# game over
print("Your got " + str(score) + " questions correct!")
print("Questions answered correctly " + str(int(score / 10 * 100)) + "%")
