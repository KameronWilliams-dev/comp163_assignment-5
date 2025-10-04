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

print("=== Challenge 2: Prime Number Checker ===")
n = int(input())
print("Enter a number:", end=" ")

print(f"Testing divisors from 2 to {n-1}...")

is_prime = True 
divisor_found = None

for i in range(2, n): 
    if n % i == 0: 
        is_prime = False 
        divisor_found = i 
        break


if is_prime: 
    print(f"{n} is prime!")

else: 
    print(f"{n} is not prime (divisible by {divisor_found})")

print()

print("=== Challenge 3: Multiplication Table ===") 
print("Multiplication Table:")

print(" ", end="") 
for i in range(1, 11): 
    print(f"{i:4}", end="") 
print()

for row in range(1, 11): 
    print(f"{row:2}", end=" ") 
    for col in range(1, 11): 
        product = row * col 
        print(f"{product:4}", end="") 
    print()
