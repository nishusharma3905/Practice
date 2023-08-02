# Solution 02 Roman to Integer
def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in s:
        current_value = roman_numerals[char]

        # Check if the current value is greater than the previous value
        # If so, subtract the previous value twice to account for the addition in the previous iteration
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        prev_value = current_value

    return total

s = "LVIII"
result = roman_to_int(s)
print(result)




   
