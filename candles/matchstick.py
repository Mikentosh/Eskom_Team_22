# This is the main package source code file for EDSA Team 22


# Function 1
def metric_dictionary():

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
    if len(items) == 0:
        return {}
    
    return {
        "mean": round(np.mean(items), 2),
        "median": round(np.median(items), 2),
        "var": round(np.var(items, ddof=1), 2),
        "std": round(np.std(items, ddof=1), 2),
        "min": round(np.min(items), 2),
        "max": round(np.max(items), 2)
    }    


# Function 2
def five_num_summary(items):

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
    if len(items) == 0:
        return {}
    
    return {
        "max": round(np.max(items), 2),
        "median": round(np.median(items), 2),
        "min": round(np.min(items), 2),
        "q1": round(np.percentile(items, 25), 2),
        "q3": round(np.percentile(items, 75), 2)
    }


# Function 3
def date_parser():

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
    return [date[:10] for date in dates if dates]


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
    # Explain in one sentence what the function does
    
    Args:
        # add args details here
    
    Returns:
        # add returns details here
    
    Examples:
        >>> tweet_number(#)
        ###        
        >>> tweet_number(#)
        ###
        >>> tweet_number(#)
        ###
    """
    return 0


# Function 6
def word_splitter():

    """
    # Explain in one sentence what the function does
    
    Args:
        # add args details here
    
    Returns:
        # add returns details here
    
    Examples:
        >>> word_splitter(#)
        ###        
        >>> word_splitter(#)
        ###
        >>> word_splitter(#)
        ###
    """
    return 0


# Function 7
def stop_word_remover():

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