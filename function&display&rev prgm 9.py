def get_number():
    num = int(input("Enter a number (minimum 4 digits): "))
    if num < 1000:
        print("Number must have at least 4 digits!")
        return get_number()
    return num

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = get_number()
r = reverse_number(n)

print("Original number:", n)
print("Reversed number:", r)
