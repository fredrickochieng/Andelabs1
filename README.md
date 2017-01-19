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

COMMANDLINE APPLICATION PROGRAMMING INTERFACE(API)
```python
import json
import urllib.request


def uni_search():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    jsonstr = response.read().decode()
    final_dict = json.loads(jsonstr)
    print(final_dict)


if __name__ == '__main__':
    uni_search()
    ```

UNISEARCH-is an API that searches for coordinates and time stamp of a location .In this case International Space Station.
Application program interface (API) is a set of routines, protocols, and tools for building software applications. An API specifies how software components should interact. Additionally, APIs are used when programming graphical user interface (GUI) components.
This application uses the `urllib library` to send a request to the ISS API `http://api.open-notify.org/iss-now.json` and return its coordinates and time stamp.It use the `Json` library to decode the coded response as per the request sent in an http protocol.
The coded response is then returned as a python dictionary as shown below!
```python
>>> import json
>>> import urllib.request
>>> 
>>> 
>>> def uni_search():
...     url = "http://api.open-notify.org/iss-now.json"
...     response = urllib.request.urlopen(url)
...     jsonstr = response.read().decode()
...     final_dict = json.loads(jsonstr)
...     print(final_dict)
... 
>>> 
>>> if __name__ == '__main__':
...     uni_search()
... 


{'message': 'success', 'iss_position': {'longitude': '148.4316', 'latitude': '5.7012'}, 'timestamp': 1484821669}
>>> 
```




