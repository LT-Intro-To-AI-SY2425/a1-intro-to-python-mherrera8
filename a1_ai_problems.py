# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# Prime number checker

def is_prime(num):
    # Check if the number is less than 2
    if num < 2:
        return False
    # Check for factors from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
assert is_prime(5) == False, "is_prime test on 5"
assert is_prime(3) == False, "is_prime test on 3"
assert is_prime(25) == True, "is prime test on 25" 

#Word count 
def count_words(sentence):
    # Split the sentence into words based on whitespace
    words = sentence.split()
    # Return the number of words
    return len(words)
assert count_words("Hello World!") == 2, "count_words test on Hello World"
assert count_words("one two three for five") == 5, "count_words test one two three four five"


#Reverse words in a string
def reverse_string(s):
    # Reverse the string using slicing
    return s[::-1]

assert reverse_string("Hello world") == "world Hello", "reverse_string on Hello world"
assert reverse_string("one two three four five") == "five four three two one", "reverse_string on one two three four five"
