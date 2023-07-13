# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):

    if x == '2' and x == 2:
    
        return(True)
    
    else:
        
        return(False)



# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(input):
    
    if input in 'aeiou':
        
        return(True)
        
    else:
        
        return(False)


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(input):
    
    if is_vowel(input):
        
        return(False)
    
    else:
        
        return(True)


# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def word(x):
    
    x = input('Enter a word: ')
    
    if x[0] in 'bcdfghijklmnpqrstvwxyz':
        
        return (x.capitalize())


# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip():
    
    n = int(input('Enter an int: '))
    
    x = float(input('Enter an int: '))
    
    return(n * x)

calculate_tip()

# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount():
    
    n = int(input('Enter an int: '))
    
    x = float(input('Enter an int: '))
    
    return(n)  - (n * x)


# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas():
    
    n = input('Enter a big number with commas: ')
    
    return(n.replace(',', ''))




# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade():
    
    user_grade = int(input('Please enter a grade: '))
    
    if user_grade >= 88:
        
        return(f'{user_grade} is an A')
        
    elif user_grade >= 80:
        
        return(f'{user_grade} is a B')
        
    elif user_grade >= 67:
        
        return(f'{user_grade} is a C')
        
    elif user_grade >= 60:
        
        return(f'{user_grade} is a D')
        
    elif user_grade <= 59:
        
        return(f'{user_grade} is an F')
        
    else:
        
        return('Please enter a grade between 1-100')




# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels():
    
    random_word = input('Please enter a random word: ')
    
    for vowel in 'aeiouAEIOU':
    
        random_word = random_word.replace(vowel,'')
    
    return random_word




# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name():
    
    sentence = input('Please enter a phrase: ')
    
    py_id = '0123456789abcdefghijklmnopqrstuvwxyz_. '
    
    lower_case = sentence.lower()
    
    my_lst = []

    for n in lower_case:
        
        if n in py_id:
            
            my_lst.append(n)
            
    desired_phrase = ''.join(my_lst).strip().replace(' ','_').replace('__', '_')
        
    return desired_phrase 




# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list):
    
    x = 0
    
    n = []
    
    for a in list:
        
        x = x + a
        
        n.append(x)
        
    return n


