print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
print("Enter starting number:", end=" ") 
print("Sequence:", end=" ")

step_count = 0 
print(current_number, end=" ")

while current_number != 1: 
    if current_number % 2 == 0: 
        current_number //= 2
    else: 
        current_number = 3 * current_number + 1 
    print(current_number, end=" ") 
    step_count += 1

print() 
print("Steps:", step_count)
