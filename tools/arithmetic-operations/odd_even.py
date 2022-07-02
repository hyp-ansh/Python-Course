# Getting input via STDIN
print("Whats the number : ")
userInput = int(input())
if userInput % 2 == 0 and userInput != 0:
    print("Your number is Even")
elif userInput % 2 != 0:
    print("Your number is Odd")
elif userInput == 0:
    print("Zero is neither odd or even")

