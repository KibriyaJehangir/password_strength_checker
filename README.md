# Password Strength Checker

This Python script ensures that a user enters a strong password by repeatedly prompting until the entered password meets strength requirements. It evaluates the password against common weaknesses and provides real-time feedback.

---

## Features
1. **Continuous Prompting**  
   The program keeps asking for a password until it meets the defined "strong" criteria.

2. **Password Validation**  
   - Checks if the password is in the `10k-most-common.txt` list.  
   - Requires at least one symbol (e.g., `!@#$%`).  
   - Requires at least one uppercase letter.  
   - Requires at least one digit.  
   - Enforces a minimum length of 8 characters.

3. **Feedback System**  
   After each attempt, the program outputs suggestions:
   - Whether symbols, uppercase letters, and digits are included.  
   - Whether the password is too short or common.  
   - Password strength level: **Very Weak, Weak, Medium, Strong**.  

4. **Exit Condition**  
   The loop terminates once the user provides a **Strong** password.

---

## Requirements
- Python 3.x
- `10k-most-common.txt` file containing common weak passwords (must be in the same directory).

---

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-checker.git
   cd password-checker
   
## File structure
├── password_checker.py   # Main script
├── 10k-most-common.txt   # List of common passwords
└── README.md             # Documentation

