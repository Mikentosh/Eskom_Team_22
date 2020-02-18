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
def tweet_number(df):


    """
    Function calculates the number of tweets per day.
    
    Args:
    Input a pandas dataframe which has a date-time column.
    
    Returns:
    A new pandas dataframe with the number of tweets per (grouped by) day.
    
    Examples:
        >>> number_of_tweets_per_day(twitter_df())
        
            	    Tweets
        Date	
        2019-11-20	18
        2019-11-21	11
        2019-11-22	25
        2019-11-23	19
        2019-11-24	14
        2019-11-25	20
        2019-11-26	32
        2019-11-27	13
        2019-11-28	32
        2019-11-29	16        
        >>> 
    
    """
    dates_only = df['Date'].apply(lambda x:x.split()[0])
   
    new_df = dates_only.value_counts().reset_index(name='Tweets').rename(columns={'index': 'Date'})
    
    new_df['Date'] = pd.to_datetime(new_df['Date'])
    new_df = new_df.set_index('Date')

    
    return new_df.sort_index(axis=0)


# Function 6
def word_splitter(df):

    """
    Function Splits Tweets/sentences in a panda dataframes's column into a list of seperate words & changes all words into lower case. 
    The result is stored as a new column on the dataframe.
    Args:
        Input a pandas dataframe df as an argument in the function.
    
    Returns:
        # the inputted pandas dataframe with a new added column ('Split Tweets') which has the Tweets as separate words 
        
    
    Examples:
        >>> word_splitter(twitter_df())
        Tweets	Date	Split Tweets
0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	[@bongadlulane, please, send, an, email, to, m...
1	@saucy_mamiie Pls log a call on 0860037566	2019-11-29 12:46:53	[@saucy_mamiie, pls, log, a, call, on, 0860037...
2	@BongaDlulane Query escalated to media desk.	2019-11-29 12:46:10	[@bongadlulane, query, escalated, to, media, d...
3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	[before, leaving, the, office, this, afternoon...
4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	[#eskomfreestate, #mediastatement, :, eskom, s...
...	...	...	...
195	Eskom's Visitors Centresâ€™ facilities include i...	2019-11-20 10:29:07	[eskom's, visitors, centresâ€™, facilities, incl...
196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	[#eskom, connected, 400, houses, and, in, the,...
197	@ArthurGodbeer Is the power restored as yet?	2019-11-20 10:07:59	[@arthurgodbeer, is, the, power, restored, as,...
198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	[@muthambipaulina, @sabcnewsonline, @iol, @enc...
199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	[rt, @gp_dhs:, the, @gautengprovince, made, a,...       
        >>> 
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