# Palindromatic Sums

https://projecteuler.net/problem=125

## Notes

I used AI to setup my python environment. 
The rest was done myself. 
It's taken me roughly over 2 hours so far. 

### Improvements (not done due to time)

There are improvements to be made, but due to time constraints, I'm happy to discuss in person. 
I also feel this is best worked out on paper as well, which I didn't have time to do. 

* I used combinatorials (repetition allowed, unordered) to check all ranges and windows. A better approach would be for no repetition allowed (and still unordered) that way there are less results. 
*  Because we wanted to find all palindromatic sums under 10^8, I further limited the range so it didn't check beyond a reasonable number: and that was the square root of 10^8 which was 10000. Because 10000^2 = 100000000. This was just a high level assumption (and kind of an embarrassing one), and range and window can be limited much more deterministically, but I felt this was outside the scope of the task. 

I'm happy to disucss further in person.


## Install

Setup python environment:
```
python3 -m venv .venv
source .venv/bin/activate
```

## Run

```
python3 main.py
```