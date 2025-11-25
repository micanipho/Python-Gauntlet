
# =========================================================
# THE PYTHON GAUNTLET 
# =========================================================

# ---------------------------------------------------------
# LEVEL 1: WARM UP (Strings)
# ---------------------------------------------------------

def clean_and_reverse(text):
    """
    1. Receive a string (e.g., "  Hello World  ").
    2. Remove any leading/trailing whitespace.
    3. Convert the entire string to lowercase.
    4. Return the reversed version of that cleaned string.
    
    Example: "  Python  " -> "nohtyp"
    """
    # TODO: Write your code here
    pass


# ---------------------------------------------------------
# LEVEL 2: DATA RESTRUCTURING (Dictionaries)
# ---------------------------------------------------------

def group_by_department(employees):
    """
    1. Receive a list of dictionaries. Each dict represents an employee:
       [{'name': 'Alice', 'dept': 'Sales'}, {'name': 'Bob', 'dept': 'Sales'}, {'name': 'Charlie', 'dept': 'IT'}]
    2. Return a NEW dictionary where the keys are departments and the values are LISTS of names.
    
    Example Output:
    {
        'Sales': ['Alice', 'Bob'],
        'IT': ['Charlie']
    }
    """
    # TODO: Write your code here
    pass


# ---------------------------------------------------------
# LEVEL 3: LOGIC & MATH (Loops)
# ---------------------------------------------------------

def sum_of_primes(n):
    """
    1. Receive an integer n.
    2. Return the SUM of all prime numbers up to (and including) n.
    3. Recall: A prime number is greater than 1 and only divisible by 1 and itself.
    
    Example: n=5. Primes are 2, 3, 5. Sum = 10.
    """
    # TODO: Write your code here
    pass


# ---------------------------------------------------------
# LEVEL 4: ALGORITHMIC THINKING (Compression)
# ---------------------------------------------------------

def compress_string(text):
    """
    1. Implement Run-Length Encoding.
    2. Receive a string of characters (e.g., "AAABBCCCA").
    3. Return a compressed string showing the character and its count.
    
    Example Input: "AAABBCCCA"
    Example Output: "3A2B3C1A"
    
    Note: If the input is empty, return empty string.
    """
    # TODO: Write your code here
    pass


# ---------------------------------------------------------
# LEVEL 5: LOGIC TRAPS (State Tracking)
# ---------------------------------------------------------

def get_second_largest(numbers):
    """
    1. Receive a list of distinct integers.
    2. Return the SECOND largest number in the list.
    3. Do NOT use the built-in .sort() method or sorted() function.
    
    Example: [10, 20, 4, 45, 99] -> 45
    """
    # TODO: Write your code here
    pass


# ---------------------------------------------------------
# LEVEL 6: 2D ARRAYS (Matrices)
# ---------------------------------------------------------

def sum_main_diagonal(matrix):
    """
    1. Receive a list of lists (a square matrix).
    2. Calculate the sum of the numbers on the main diagonal (top-left to bottom-right).
    
    Example Input: 
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    Logic: 1 + 5 + 9 
    Example Output: 15
    """
    # TODO: Write your code here
    pass


# ---------------------------------------------------------
# LEVEL 7: COMPLEX VALIDATION (The Boss)
# ---------------------------------------------------------

def validate_ipv4(ip_string):
    """
    1. Receive a string (e.g., "192.168.0.1").
    2. Return True if it is a valid IPv4 address, False otherwise.
    3. Rules for Valid:
       - Must contain exactly 4 parts separated by dots.
       - Each part must be a number.
       - Each number must be between 0 and 255 (inclusive).
       - Examples: 
         "192.168.1.1" -> True
         "256.0.0.0"   -> False (256 is too high)
         "192.168.1"   -> False (Not enough parts)
         "abc.0.0.1"   -> False (Not a number)
    """
    # TODO: Write your code here
    pass
