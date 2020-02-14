# This is the main package source code file for EDSA Team 22


# Function 1
def metric_dictionary():
    # Nyaravho
    # to be implemented
    # Remember to properly use docstrings!
    """
    # Explain in one sentence what the function does
    
    Args:
        # add args details here
    
    Returns:
        # add returns details here
    
    Examples:
        >>> metric_dictionary(#)
        ###        
        >>> metric_dictionary(#)
        ###
        >>> metric_dictionary(#)
        ###
    """
    return 0    


# Function 2
def five_number_summary():
    # Thabo
    # to be implemented
    # Remember to properly use docstrings!
    """
    # Explain in one sentence what the function does
    
    Args:
        # add args details here
    
    Returns:
        # add returns details here
    
    Examples:
        >>> five_number_summary(#)
        ###        
        >>> five_number_summary(#)
        ###
        >>> five_number_summary(#)
        ###
    """
    return 0


# Function 3
def date_parser():
    # Michael
    # to be implemented
    # Remember to properly use docstrings!
    """
    # Explain in one sentence what the function does
    
    Args:
        # add args details here
    
    Returns:
        # add returns details here
    
    Examples:
        >>> date_parser(#)
        ###        
        >>> date_parser(#)
        ###
        >>> date_parser(#)
        ###
    """
    return 0


# Function 4
def hashtag_extractor():
    # Lineo
    # to be implemented
    # Remember to properly use docstrings!
    """
    # Explain in one sentence what the function does
    
    Args:
        # add args details here
    
    Returns:
        # add returns details here
    
    Examples:
        >>> hashtag_extractor(#)
        ###        
        >>> hashtag_extractor(#)
        ###
        >>> hashtag_extractor(#)
        ###
    """
    return 0


# Function 5
def tweet_number():


    """
    # Function calculates the number of tweets per day.
    
    Args:
        # input a pandas dataframe which has a date-time column.
    
    Returns:
        # a new pandas dataframe with the number of tweets per (grouped by) day.
    
    Examples:
        >>> tweet_number(#)
        ###        
        >>> tweet_number(#)
        ###
        >>> tweet_number(#)
        ###
    """
    dates_only = df['Date'].apply(lambda x:x.split()[0])
   
    new_df = dates_only.value_counts().reset_index(name='Tweets').rename(columns={'index': 'Date'})
    
    new_df['Date'] = pd.to_datetime(new_df['Date'])
    new_df = new_df.set_index('Date')

    
    return new_df.sort_index(axis=0)


# Function 6
def word_splitter():

    """
    # Function Splits Tweets into seperate words & changes all words into lower case 
    
    Args:
        input a pandas dataframe as an argument in the function.
    
    Returns:
        # the inputted pandas dataframe with a new added column ('Split Tweets') which has the Tweets as separate words 
        
    
    Examples:
        >>> word_splitter(#)
        ###        
        >>> word_splitter(#)
        ###
        >>> word_splitter(#)
        ###
    """
    splitter = df['Tweets'].apply(lambda x: x.lower().split())
    df['Split Tweets'] = splitter
    
    return df


# Function 7
def stop_word_remover():
    # Whole team
    # to be implemented
    # Remember to properly use docstrings!
    """
    # Explain in one sentence what the function does
    
    Args:
        # add args details here
    
    Returns:
        # add returns details here
    
    Examples:
        >>> stop_word_remover(#)
        ###        
        >>> stop_word_remover(#)
        ###
        >>> stop_word_remover(#)
        ###
    """
    return 0