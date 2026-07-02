#!/usr/bin/env python3

import math

def is_palindrome(number):
    # check if palindrome number
    as_string = str(number)
    length = len(as_string)
    # print("check if palindrome: %", as_string)

    if length > 0:
        if length % 2 != 0:
            half = int((length / 2) - 0.5)
            left = as_string[:half]
            right = as_string[half + 1:length]
        
            if left == right[::-1]: # does first half equate to second half?
                return "true"
        elif length == 1:
            return "true"
        else:
            half = int((length / 2))
            left = as_string[:half]
            right = as_string[half:length]
        
            if left == right[::-1]: # does first half equate to second half?
                return "true"

    
    return "false"

def main():
    print("=" * 50)
    print("🐍 Palindromatic Sums")
    print("A palindrome is a word, phrase, number, or sequence that reads the same backward as forward (e.g., racecar, madam, 121). The term originates from the Greek words palin (\"again\" or \"back\") and dromos (\"running\").")
    print("=" * 50)
    
    # centralised variables
    max_limit = 10 ** 8
    max_length = int(math.sqrt(max_limit))
    palindrome_max_limit = 1000
    palindromes_list = []

    # we need to check ranges: a-b of range x. 
    # Assumptions:
    # r is the starting point of a range, and w is the length; r - w is the range we check.
    # we want to check all combinations of r-w where total is < 10^8

    # TODO: since we are checking combinations where repetition doesn't matter we get results twice. 
    # So we solve with set() function to save only unique palindromes
    for r in range(1, max_length):
        total_sum = 0
        total_sum_user_friendly = "" # display cumulative sum

        for w in range(0, 100):
            # check all range and window combinations
            x = (r + w) ** 2

            if total_sum + x <= palindrome_max_limit:
                # accumulate sum
                total_sum_user_friendly = total_sum_user_friendly + " + " + str(r + w) + "^2"
                total_sum = total_sum + x

                # Yes: check if palindrome (is_palindrome)
                if is_palindrome(total_sum) == "true" and w != 0:
                    palindromes_list.append(total_sum)
                    # yes: print numbers to sum + palindrome
                    print("You found a palindrome! ", total_sum)
                    print("Sum: ", total_sum_user_friendly)
                    print(f"Check range in window: {str(r)} {str(w)}")
                    print("\n\n")
            else:
                break

    # print all palindromes
    palindromes = set(palindromes_list)

    print("palindromes: ", palindromes)

    sum_of_palindromes_under_1000 = sum(palindromes)

    print(f"The sum of all the palindromes: {palindromes} is {sum_of_palindromes_under_1000}")
    print("\n" * 20)

if __name__ == "__main__":
    main()