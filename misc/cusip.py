# Author Dario Clavijo 2024

def cusip_check_digit(cusip):
    if len(cusip) != 8:
        raise ValueError("CUSIP must be exactly 8 characters long")
    
    sum_val = 0
    
    for i, c in enumerate(cusip):
        if c.isdigit():
            v = int(c)
        elif c.isalpha():
            v = ord(c.upper()) - ord('A') + 10  # A=10, B=11, ..., Z=35
        elif c == '*':
            v = 36
        elif c == '@':
            v = 37
        elif c == '#':
            v = 38
        else:
             raise ValueError(f"Invalid character '{c}' at pos {i} in CUSIP {cusip}")
        
        if i & 1 == 1:  # Odd index (1-based), which is even in 0-based indexing
            v *= 2
        
        sum_val += (v // 10) + (v % 10)
    
    return (10 - (sum_val % 10)) % 10

# Example usage:
#cusip = "12345678"
#check_digit = cusip_check_digit(cusip)
#print(f"Check digit for CUSIP {cusip} is: {check_digit}")

E="""Apple Inc.: 037833100
Cisco Systems: 17275R102
Google Inc.: 38259P508
Microsoft Corporation: 594918104
Oracle Corporation: 68389X105
Treasury Gilt 2068: EJ7125481"""
for e in E.split("\n"):
  company, cusip = e.split(":")
  cusip = cusip.strip()
  check = cusip_check_digit(cusip[0:8]) == int(cusip[-1])
  print(f"company: {company}, Cusip: {cusip}, valid: {check}")
