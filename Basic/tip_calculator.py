#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")




def tip_calculator():
    # Step 1: Input the bill amount
    try:
        bill_amount = float(input("Enter the total bill amount: $"))
        if bill_amount <= 0:
            raise ValueError("Bill amount must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Step 2: Input the tip percentage
    try:
        tip_percentage = float(input("Enter the tip percentage (e.g., 10, 15, 20): "))
        if tip_percentage < 0:
            raise ValueError("Tip percentage cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Step 3: Calculate the total tip
    tip_amount = (tip_percentage / 100) * bill_amount
    total_bill = bill_amount + tip_amount
    print(f"\nTip Amount: ${tip_amount:.2f}")
    print(f"Total Bill (with Tip): ${total_bill:.2f}")
    
    # Step 4: Split the bill among people
    try:
        num_people = int(input("\nEnter the number of people to split the bill: "))
        if num_people <= 0:
            raise ValueError("Number of people must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Advanced feature: Custom split option
    split_choice = input("Do you want to split evenly or enter custom amounts? (even/custom): ").lower()
    
    if split_choice == "even":
        share_per_person = total_bill / num_people
        print(f"\nEach person pays: ${share_per_person:.2f}")
    elif split_choice == "custom":
        print("\nEnter the contributions for each person:")
        custom_contributions = []
        for i in range(num_people):
            try:
                contribution = float(input(f"Person {i+1}'s contribution: $"))
                if contribution < 0:
                    raise ValueError("Contribution cannot be negative.")
                custom_contributions.append(contribution)
            except ValueError as e:
                print(f"Invalid input: {e}")
                return
        
        # Verify if custom contributions match the total bill
        if sum(custom_contributions) != total_bill:
            print(f"\nError: Total contributions (${sum(custom_contributions):.2f}) do not match the total bill (${total_bill:.2f}).")
            return
        else:
            print("\nCustom Contributions Accepted!")
            for i, amount in enumerate(custom_contributions, start=1):
                print(f"Person {i} pays: ${amount:.2f}")
    else:
        print("Invalid choice. Defaulting to even split.")
        share_per_person = total_bill / num_people
        print(f"\nEach person pays: ${share_per_person:.2f}")
    
    print("\nThank you for using the Tip Calculator!")

# Run the program
if __name__ == "__main__":
    tip_calculator()
