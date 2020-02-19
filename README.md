# Eskom Team 22

Project repo for the Analyse sprint

<hr/>

# The module **matchstick** is within the package **candles**

# Function 1 - dictionary_of_metrics()

Takes a list of integers and returns a dictionary of the mean, median, variance, standard deviation, min and max.
    
### Args:

items: List of integers


### Returns:

Dictionary of the mean, median, variance, standard deviation, min and max.


### Examples:
>>> dictionary_of_metrics(none)
none      
>>> dictionary_of_metrics(none)
none
>>> dictionary_of_metrics(none)
none

---


# Function 2 - five_num_summ()

Takes a list of integers and returns a dictionary of the five number summary.
    

### Args:
    Items: list of integers
    

### Returns:
    Dictionary of the five number summary
    

### Examples:

>>> five_num_summ(none)
none      
>>> five_num_summ(none)
none
>>> five_num_summ(none)
none

---

# Function 3 - date_parser()

Takes a list of datetime strings and converts it into a list of strings with only the date.

### Args:
    list_dates: list of datetime strings
    
### Returns:
    list of strings with only the date
    
### Examples:
>>> date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53'])
['2019-11-29', '2019-11-29']
>>> date_parser(['2019-10-25 12:50:54'])
['2019-10-25]
>>> date_parser(#)


---


# Function 4 - extract_municipality_hashtags()

Takes a pandas dataframe and returns the same dataframe which has the name of the munincipality.

    
### Args:
    df: pandas dataframe with Tweet data

    
### Returns:
    pandas dataframe with extracted municipality name

    
### Examples:
>>> hashtag_extractor(none)
none       
>>> hashtag_extractor(none)
none
>>> hashtag_extractor(none)
none


---


# Function 5 - number_of_tweets_per_day()

Calculates the number of tweets that were posted per day.
    
### Args:
    df: pandas dataframe 

    
### Returns:
    Returns a new dataframe with columns 'Date' & 'Number of Tweets'

    
### Examples:
>>> tweet_number(none)
none     
>>> tweet_number(none)
none
>>> tweet_number(none)
none


---

# Function 6 - word_splitter()

Splits a sentence into a list of the separate words.
    
### Args:
    df: pandas dataframe 
    
### Returns:
    Returns a 
    
### Examples:
>>> word_splitter(none)
none        
>>> word_splitter(none)
none
>>> word_splitter(none)
none


---


# Function 7 - stop_words_http_remover()

Explain in one sentence what the function does
    
### Args:
    df: pandas dataframe
    
### Returns:
    # add returns details here
    
### Examples:
>>> stop_words_http_remover(none)
none
>>> stop_words_http_remover(none)
none
>>> stop_words_http_remover(none)
none

