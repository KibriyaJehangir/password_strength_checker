# Keep asking for password input until a strong password is entered
while True:
    # Get password input from the user
    password = input("Enter your current password: ")

    # Import string module (should be moved to the top ideally)
    import string

    # Define character sets for checking password strength
    symbols = string.punctuation            # All punctuation symbols
    characters = string.ascii_lowercase     # Lowercase letters (not used directly)
    letters = string.ascii_uppercase        # Uppercase letters
    digits = string.digits                  # Numeric digits

    # This list keeps track of:
    # [0] -> whether the password is common
    # [1] -> contains symbols
    # [2] -> contains uppercase letters
    # [3] -> contains digits
    loop_repeating_limit_list = [0, 0, 0, 0]

    # Loop through each character in the password and update the flags
    for i in password:
        if i in symbols and loop_repeating_limit_list[1] != 1:
            loop_repeating_limit_list[1] = 1  # Contains symbol
        elif i in letters and loop_repeating_limit_list[2] != 1:
            loop_repeating_limit_list[2] = 1  # Contains uppercase letter
        elif i in digits and loop_repeating_limit_list[3] != 1:
            loop_repeating_limit_list[3] = 1  # Contains digit
        else:
            pass  # Ignore lowercase letters or already counted characters

    # Check if the password is in the list of common passwords
    with open("10k-most-common.txt", "r") as common_password_file:
        for i in common_password_file:
            if password == str(i).strip():
                loop_repeating_limit_list[0] = 1  # Mark as common password

    # Print suggestions based on what the password contains
    print("Suggestions →")
    if loop_repeating_limit_list[1] == 1:
        print("✔ Contains symbols")
    else:
        print("❌ Does not contain symbols")

    if loop_repeating_limit_list[2] == 1:
        print("✔ Contains uppercase letters")
    else:
        print("❌ Does not contain uppercase letters")

    if loop_repeating_limit_list[3] == 1:
        print("✔ Contains digits")
    else:
        print("❌ Does not contain digits")

    # Evaluate password strength based on contents and length
    if (
        loop_repeating_limit_list[1] == 0 and
        loop_repeating_limit_list[2] == 0 and
        loop_repeating_limit_list[3] == 0 or
        loop_repeating_limit_list[0] == 1 or
        len(password) < 9
    ):
        print("❌ Very Weak — also check the length (minimum is 8 characters)")
    elif (
        loop_repeating_limit_list[2] == 1 and
        loop_repeating_limit_list[3] == 1 and
        loop_repeating_limit_list[1] != 1
    ):
        print("⚠️ Medium")
    elif (
        loop_repeating_limit_list[1] == 1 and
        loop_repeating_limit_list[2] == 1 and
        loop_repeating_limit_list[3] != 1
    ):
        print("⚠️ Medium")
    elif (
        loop_repeating_limit_list[1] == 1 and
        loop_repeating_limit_list[3] == 1 and
        loop_repeating_limit_list[2] != 1
    ):
        print("⚠️ Medium")
    elif (
        loop_repeating_limit_list[1] == 1 and
        loop_repeating_limit_list[2] == 1 and
        loop_repeating_limit_list[3] == 1
    ):
        print("✅ Strong")
        print("Your password is strong now.")
        break  # Exit the loop if password is strong
    else:
        print("❌ Weak")

    print("Type again\n")  # Prompt for another try if password is not strong
