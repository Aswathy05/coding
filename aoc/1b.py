def calculate_calibration_values(lines):
    calibration_sum = 0

    for line in lines:
        # Separate letters and digits
        letters = [char for char in line if char.isalpha()]
        digits = [char for char in line if char.isdigit()]

        # Convert spelled-out digits to numbers and calculate the calibration value
        calibration_value = sum(int(digit) if digit.isdigit() else ord(digit.lower()) - ord('a') + 1 for digit in digits + letters)

        # Add calibration value to the total sum
        calibration_sum += calibration_value

    return calibration_sum

# Example lines
lines = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

# Calculate and print the sum of calibration values
total_calibration_sum = calculate_calibration_values(lines)
print(f"The sum of all calibration values is: {total_calibration_sum}")
