# 8] Write a program that prompts the user to input number of calls and calculate the monthly   telephone bills as per the following rule:
#    Minimum Rs. 200 for up to 100 calls.
#    Plus Rs. 0.60 per call for next 50 calls.
#    Plus Rs. 0.50 per call for next 50 calls.
#    Plus Rs. 0.40 per call for any call beyond 200 calls.

# Function to calculate telephone bill
def calculate_bill(num_calls):
    bill = 200  # Base charge for up to 100 calls

    if num_calls > 100:
        extra_calls = num_calls - 100

        if extra_calls <= 50:
            bill += extra_calls * 0.60
        else:
            bill += 50 * 0.60  # Charge for the next 50 calls
            extra_calls -= 50  

            if extra_calls <= 50:
                bill += extra_calls * 0.50
            else:
                bill += 50 * 0.50  # Charge for the next 50 calls
                extra_calls -= 50  

                # For calls beyond 200
                bill += extra_calls * 0.40

    return bill

# Taking user input
num_calls = int(input("Enter the number of calls: "))

# Calculating bill
total_bill = calculate_bill(num_calls)

# Displaying the result
print(f"Your total telephone bill is: Rs. {total_bill:.2f}")
