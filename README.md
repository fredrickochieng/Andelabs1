WORD COUNT

This function takes a string and first replaces new line character and tab character with a space.
It then splits the string into a list of words and stores them in a list as shown below.
The for loop iterates over the list to check for a word and ignores if a space.Every interger is converted into a word and then counted.The counted words are then stored in a dictionary and returned.
Check the code here!

```python

def words(string):  

    new_list = string.replace('\n', ' ').replace('\t', ' ').split()  

    string_dict = {}

    

    for word in new_list:

        # ignore spaces

        if not word:

            continue

        

        #this  count word

        word_count = new_list.count(word)

        if word.isdigit():      

            word = int(word)

        # add word to string dict

        string_dict[word] = word_count

    return string_dict  
print words("I am Fred.Fred i am")

    

```

FINDING MAXIMUM AND MINIMUM NUMBER

Below is a function which takes in a list as an input and returns the minimum and maximum values of the list in an array .
`maximum=max(list)`-gets the maximum number 
`minimum=min(list)`-gets the minimum number
`if maximum !=minimum:`checks for equality
`return [minimum,maximum]`-returns the two numbers in an array,that is if they are not equal
`	else:
return [minimum]`-returns the minimum value which is the same as the maximum number if the numbers are equal.
Check it out!

```python
def find_max_min(list):
	maximum=max(list)
	minimum=min(list)
	if maximum !=minimum:
		return [minimum,maximum]
	else:
return [minimum]```
