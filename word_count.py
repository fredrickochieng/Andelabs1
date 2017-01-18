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