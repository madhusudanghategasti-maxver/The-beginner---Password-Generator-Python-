import random

def letters(let):
    lette=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in range(let):
        global password
        password.append(random.choice(lette))

def numbers(num):
    nums=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for n in range(num):
        global password
        password.append(random.choice(nums))
def symbols(sym):
    syms=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    for s in range(sym):
        global password
        password.append(random.choice(syms))

password=[]
print("welcome to the password generator")
let=int(input("how many letters do you like to be there in your passwords\n"))
letters(let)
num=int(input("how many numbers would you like to be there in your passwords\n"))
numbers(num) 
sym=int(input("how many symbols would you like to be there in your passwords:\n"))
symbols(sym)
print(password)
final_password=[]
for i in range(len(password)):
    final_password.append(random.choice(password))
print(final_password)
print(f"your final password is: {''.join(final_password)}")
