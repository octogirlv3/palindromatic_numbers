#!/usr/bin/env python3

from datetime import datetime

import platform
import math

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

def check_for_palindromes_in_range_and_window(start_range, window, max_limit):
    total_sum = 0
    total_sum_user_friendly = ""
    
    # loop through range to window
    for i in range(start_range, window):
        # from start_number and add square sum
        x = i ** 2
        # check if less than 10^8
        if x < max_limit:
            # accumulate sum
            total_sum = total_sum + x

            if total_sum < max_limit:
                total_sum_user_friendly = total_sum_user_friendly + " + " + str(i) + "^2"

                # Yes: check if palindrome (is_palindrome)
                if is_palindrome(total_sum) == "true":
                    # yes: print numbers to sum + palindrome
                    print("You found a palindrome! ", total_sum)
                    print("Sum: ", total_sum_user_friendly)
                    print("\n\n")
                # no: continue
            else:
                # No: end program (1)
                # print("No more valid numbers to check that won't exceed: 10^8")

                break

        else :
            # No: end program (1)
            # No more valid numbers to check that won't exceed: 10^8
            # print("No more valid numbers to check that won't exceed: 10^8")

            break

def main():
    print("=" * 50)
    print("🐍 Palindromatic Sums")
    print("A palindrome is a word, phrase, number, or sequence that reads the same backward as forward (e.g., racecar, madam, 121). The term originates from the Greek words palin (\"again\" or \"back\") and dromos (\"running\").")
    print("=" * 50)
    
    # centralised variables
    max_limit = 10 ** 8
    max_length = int(math.sqrt(max_limit))
    
    # we need to check ranges: a-b of range x. 
    # Assumptions:
    # r is the starting point of a range, and w is the length; r - w is the range we check.
    # we want to check all combinations of r-w where total is < 10^8

    # check all ranges
    # TODO: we can limit max length further by pre-checking if range and window exceed max limit. Somehow. Need to write this as equation on paper first. Can't do it off top of head.
    
    # TODO: since we are checking combinations where repetition doesn't matter we get results twice. 
    # TODO: We limited the window to max of 100 due to memory
    for r in range(1, max_length):
        for w in range(r, 100):
            # check all range and window combinations
            check_for_palindromes_in_range_and_window(r, w, max_length)

if __name__ == "__main__":
    main()