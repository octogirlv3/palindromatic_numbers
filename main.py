#!/usr/bin/env python3

from datetime import datetime
import platform

def is_palindrome(number):
    # check if palindrome number
    as_string = str(number)
    length = len(as_string)
    # print("check if palindrome: %", as_string)

    if length > 2 and length % 2 != 0: # its an odd number
        half = int((length / 2) - 0.5)
        left = as_string[:half]
        right = as_string[half + 1:length]
    
        if left == right[::-1]: # does first half equate to second half?
            return "true"
    
    return "false"

# we choose 10000 as square root of 10^8 is 10000 so this is the max number (squared) that is equal to 10^8
def check_for_palindromes_less_than_10_power_8(start_number, max_length=100000, limit_number=10):
    # centralised variables
    max_limit = 10 ** 8
    total_sum = 0
    total_sum_user_friendly = ""
    
    # TODO: we need to check ranges: a-b of range x. 

    # loop through start_number to max_length
    for i in range(start_number, max_length):
        # from start_number and add square sum
        x = i ** 2
        # check if less than 10^8
        if x < max_limit:
            # accumulate sum
            total_sum = total_sum + x
            total_sum_user_friendly = total_sum_user_friendly + " + " + str(i) + "^2"

            # Yes: check if palindrome (is_palindrome)
            if is_palindrome(total_sum) == "true":
                # yes: print numbers to sum + palindrome
                print("% is a palindrome! %", total_sum, total_sum_user_friendly)
            # no: continue
        else :
            # No: end program (1)
            print("No more valid numbers to check that won't exceed: 10^8")

            break

def main():
    print("=" * 50)
    print("🐍 Palindromatic Sums")
    print("A palindrome is a word, phrase, number, or sequence that reads the same backward as forward (e.g., racecar, madam, 121). The term originates from the Greek words palin (\"again\" or \"back\") and dromos (\"running\").")
    print("=" * 50)

    # run check_for_palindromes_less_than_10_power_8()
    check_for_palindromes_less_than_10_power_8(1)

if __name__ == "__main__":
    main()