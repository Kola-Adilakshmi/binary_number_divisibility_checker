
def check_binary_divisibility(binary, divisor):
    remainder = 0
    transitions = []

    for position, bit in enumerate(binary, start=1):
        old_remainder = remainder
        remainder = (2 * remainder + int(bit)) % divisor

        transitions.append(
            f"Read {bit}: q{old_remainder} -> q{remainder}"
        )

    accepted = remainder == 0
    return accepted, transitions, remainder


print("BINARY NUMBER DIVISIBILITY CHECKER")
print("=" * 45)

binary = input("Enter a binary number: ").strip()

if not binary:
    print("Error: Please enter a binary number.")
elif any(bit not in "01" for bit in binary):
    print("Error: Binary numbers can contain only 0 and 1.")
else:
    for divisor in (2, 3, 5):
        print(f"\nChecking divisibility by {divisor}")
        print("-" * 35)

        accepted, transitions, remainder = (
            check_binary_divisibility(binary, divisor)
        )

        for step in transitions:
            print(step)

        print("Final remainder:", remainder)

        if accepted:
            print(f"RESULT: {binary} is divisible by {divisor}.")
        else:
            print(f"RESULT: {binary} is not divisible by {divisor}.")
