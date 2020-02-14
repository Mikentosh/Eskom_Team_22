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
        >>> hashtag_extractor(#)
        ###        
        >>> hashtag_extractor(#)
        ###
        >>> hashtag_extractor(#)
        ###
    """
    hash_tag=[]
    for x in range(len(df.iloc[:,0])):
        rowz = [ i for i in df.iloc[x][0].split() if i.startswith('#')]
        hash_tag.append(rowz)
        hash_tag = [[x.lower() for x in a] for a in hash_tag]
 
    Municip_hash=[]
    Municip_name=[]
    for j in range(len(df.iloc[:,0])):
        rowz = [ i for i in df.iloc[j][0].split() if i.startswith('@')]
        Municip_hash.append(rowz)

    for k in range(len(Municip_hash)):
        name_munic=[mun_dict[x] for x in  Municip_hash[k] if x in mun_dict]
        Municip_name.append(name_munic)
  
    df = df.assign(municipality = [','.join(map(str,l)) for l in Municip_name ])
    df['municipality']=df['municipality'].apply(lambda y: np.nan if len(y)==0 else y)

    df = df.assign(hashtags = hash_tag)
    df['hashtags']=df['hashtags'].apply(lambda y: np.nan if len(y)==0 else y)
    return df


# Function 5
def tweet_number():
    # Kea
    # to be implemented
    # Remember to properly use docstrings!
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
        >>> stop_word_remover(#)
        ###        
        >>> stop_word_remover(#)
        ###
        >>> stop_word_remover(#)
        ###
    """

    stop_words_items=stop_words_dict.get('stopwords')

    split_tweets=[]
    for x in range(len(df.iloc[:,0])):
        split_tweets.append([df.iloc[:,0][x].replace(' ',', ')])
        split_tweets = [[x.lower() for x in a] for a in split_tweets]  #Splitted tweets in smaller letters  
        
    list_to_string=[]
    for i in range(len(split_tweets)):
        words=' '.join(map(str, split_tweets[i])).replace(',','').split()
        list_to_string.append(words)
        
    without_stop_words=[]
    for k in range(len(df.iloc[:,0])):
 
        without_stop=[j for j in list_to_string[k] if j not in stop_words_items]
        without_stop_words.append(without_stop)

    df['Without Stop Words']=without_stop_words 


    return df