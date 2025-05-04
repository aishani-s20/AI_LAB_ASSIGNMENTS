subjects=["maths","science","english","it"]
data = []
for i in range(2):
        print(f"Student {i + 1}:")
        student_scores = []
        for subject in subjects:
            score = int(input(f"  {subject} (out of 100): "))
            student_scores.append(score)
        data.append(student_scores)

for j in range(0,len(subjects)):
    max_marks=data[0][j]
    for i in range(1,len(data)):
        max_marks=max(data[i][j],max_marks)
    print('max in',subjects[j],':',max_marks)

for j in range(0,len(subjects)):
    min_marks=data[0][j]
    for i in range(1,len(data)):
        min_marks=min(data[i][j],min_marks)
    print('min in',subjects[j],':',min_marks)

for j in range(0,len(subjects)):
    total_marks=sum(row[j] for row in data)
    print('avg in',subjects[j],':',total_marks/len(data))

highest=data[0][0]
for j in range(0,len(subjects)):
    for i in range(0,len(data)):
        highest=max(data[i][j],highest)

print("overall highest marks:", highest)

lowest=data[0][0]
for j in range(0,len(subjects)):
    for i in range(0,len(data)):
        lowest=min(data[i][j],lowest)

print("overall lowest marks:", lowest)

total=0
for j in range(0,len(subjects)):
    for i in range(0,len(data)):
        total=total + data[i][j]

print("overall average marks:", total/(len(subjects)*len(data)))


salary=int(input("enter salary: "))
if salary<=10000:
    hra=0.2
    da=0.8
elif salary<=20000:
    hra=0.25
    da=0.9
else:
    hra=0.3
    da=0.95

final_salary=salary+hra*salary+da*salary
print("final salary:", final_salary)

# ---------------------------------------
# password validation
password=input("enter password")
small_letter=0
capital_letter=0
number=0
character=0
valid=True
if len(password)<6 or len(password)>16:
    valid =False

for el in password:
    if ord(el)>=65 and ord(el)<=90:
        small_letter+=1
    elif ord(el)>=97 and ord(el)<=122:
        capital_letter+=1
    elif el.isdigit():
        number+=1
    elif el in ['$','#','@']:
        character+=1

valid= small_letter>0 and capital_letter>0 and number>0 and character>0
if(valid):
    print("password is valid")
else:
    print("invalid password")


# -----------------------------------------------
list1=[10, 20, 30, 40, 50, 60, 70, 80]
list1.append(200)
list1.append(300)

print(list1)

list1.remove(10)
list1.remove(30)

list1.sort(reverse=False)
print(list1)

list1.sort(reverse=True)
print(list1)

# 

# list1.insert(2,100)



D= {1:"One", 2:"Two", 3:"Three", 4: "Four", 5:"Five"}
D[6]="Six"
print(D)

del D[2]
print(D)

if 6 in D:
    print("Key 6 is present in the dictionary.")
else:
    print("Key 6 is not present in the dictionary.")

count = len(D)
print("Number of elements in the dictionary:", count)

print(f"Sum of all values in D: {sum(D.keys())}")




import random

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generate a list of 100 random numbers between 100 and 900
random_numbers = [random.randint(100, 900) for el in range(100)]

# Initialize counters for odd, even, and prime numbers
odd_count = 0
even_count = 0
prime_count = 0

# Iterate over the list and count odd, even, and prime numbers
for num in random_numbers:
    if num % 2 == 0:
        even_count += 1  # Even number
    else:
        odd_count += 1  # Odd number

    if is_prime(num):
        prime_count += 1  # Prime number

# Print the results
# print(f"List of 100 random numbers: {random_numbers}")
print(f"odd numbers: {odd_count}")
print(f"even numbers: {even_count}")
print(f"prime numbers: {prime_count}")



