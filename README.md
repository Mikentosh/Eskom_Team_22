# Eskom Team 22

Project repo for the Analyse sprint

<hr/>

# The module **matchstick** is within the package **candles**

# candles
This package is a python package that contains seven functions within the matchstick module,which compute and calculate data related to Eskom. See # Functions_brief for general information and see doctrings for detailed information.

## building this package locally
python setup.py sdist

## installing this package from GitHub
pip install git+https://github.com/Mikentosh/candles.git

## updating this package from GitHub
pip install --upgrade git+https://github.com/Mikentosh/candles.git

## License
MIT License. Visit https://choosealicense.com/licenses/mit/ for license details.

## Support
For a installation or updating and/or any errors/issues arising, or to also contribute to the project,please contact the following authors/contributors:
        Keabetswe   -   Lefifikea@gmail.com
        Michael     -   lunarfoxel@gmail.com
        Thabo       -   thaboalexm@gamil.com

For queries about errors please screenshot the error and attach the screenshot as part of your email query. If we take time to reply, know that Eskom as it again.

## contribution
To contribute to the project please contact any one of the authors/contributors mentioned above. Eskom employees and their family members are NOT welcomed :).

## needed packages/modules
for this package to work you would have to pandas and numpy packages installed already. If not installed use 'pip install pandas' and 'pip install numpy'.

## Functions_brief

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
>>> ['2019-11-29', '2019-11-29']
>>> date_parser(['2019-10-25 12:50:54'])
>>> ['2019-10-25']
>>> date_parser(['2020-10-22 11:30:54'])
>>> ['2020-10-22']

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

