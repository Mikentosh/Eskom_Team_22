# This is the main package source code file for EDSA Team 22


# Function 1
def dictionary_of_metrics(items):

    """
    Takes a list of integers and returns a dictionary of the mean, median, variance, standard deviation, min and max.
    
    Args:
        items: list of integers
    
    Returns:
        dictionary of the mean, median, variance, standard deviation, min and max.
    
    Examples:
        >>> dictionary_of_metrics([39660.0,36024.0,32127.0,39488.0,18422.0,23532.0,8842.0,37416.0,16156.0,18730.0,19261.0,25275.0])

        {'mean': 26244.42,
         'median': 24403.5,
         'var': 108160153.17,
         'std': 10400.01,
         'min': 8842.0,
         'max': 39660.0} 

        >>> dictionary_of_metrics([1,2,3,4,5,6,7,8,9,10])

        {'mean': 5.5, 
         'median': 5.5,
         'var': 9.17,
         'std': 3.03,
         'min': 1,
         'max': 10}
    
    """
    
    if len(items) == 0:
        return 0

    return {
            "mean": round(np.mean(items), 2),
            "median": round(np.median(items), 2),
            "variance": round(np.var(items, ddof=1), 2),
            "standard deviation": round(np.std(items, ddof=1), 2),
            "min": round(np.min(items), 2),
            "max": round(np.max(items), 2)
           }   


# Function 2
def five_num_summ(items):

    """
    Takes a list of integers and returns a dictionary of the five number summary.
    
    Args:
        items: list of integers
    
    Returns:
        dictionary of the five number summary
    
    Examples:
        >>> five_num_summary([39660.0,36024.0,32127.0,39488.0,18422.0,23532.0,8842.0,37416.0,16156.0,18730.0,19261.0,25275.0])

        {'max': 39660.0,
         'median': 24403.5,
         'min': 8842.0,
         'q1': 18653.0,
         'q3': 36372.0}

        >>> five_num_summary([1,2,3,4,5,6,7,8,9,10])

        {'max': 10,
         'median': 5.5,
         'min': 1,
         'q1': 3.25,
         'q3': 7.75}
        
    """
    
    if len(items) == 0:
        return []
    
    return {
            "max": round(np.max(items), 2),
            "median": round(np.median(items), 2),
            "min": round(np.min(items), 2),
            "q1": round(np.percentile(items, 25), 2),
            "q3": round(np.percentile(items, 75), 2)
           }


# Function 3
def date_parser(list_dates):

    """
    Takes a list of datetime strings and converts it into a list of strings with only the date.
    
    Args:
        list_dates: list of datetime strings
    
    Returns:
        list of strings with only the date
    
    Examples:
        >>> date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53'])
        ['2019-11-29', '2019-11-29']
        >>> date_parser(['2019-10-25 12:50:54'])
        ['2019-10-25]
        >>> date_parser(#)
        ###
    """
    return [date[:10] for date in dates if dates]


# Function 4
def extract_municipality_hashtags(df):

    """
    Takes a pandas dataframe and returns the same dataframe which has the name of the muncipality.
    
    Args:
        df: pandas dataframe with Tweet data
    
    Returns:
        pandas dataframe with extracted municipality name and hashtags
    
    Examples:
        >>> extract_municipality_hashtags(twitter_df.copy())

                                    Tweets                                  Date	    municipality	hashtags
            0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	    NaN	            NaN
            1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53 	NaN	            NaN
            2	@BongaDlulane Query escalated to media desk.	    2019-11-29 12:46:10	    NaN	            NaN
            3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	    NaN 	        NaN
            4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	    NaN	            [#eskomfreestate, #mediastatement]
                    ....	...	...	...	...
            195	Eskom's Visitors Centres’ facilities include i...	2019-11-20 10:29:07	    NaN	            NaN
            196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	    NaN	            [#eskom, #eskom, #poweringyourworld]


          
        >>> extract_municipality_hashtags(twitter_df.copy()).loc[4, "hashtags"]

                    ['#eskomfreestate', '#mediastatement']
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
def number_of_tweets_per_day(df):

    """
    Calculates the number of tweets that were posted per day.
    
    Args:
        df: pandas dataframe 
    
    Returns:
        Returns a new dataframe with columns 'Date' & 'Number of Tweets'
    
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
    """
    dates_only = df['Date'].apply(lambda x:x.split()[0])
   
    new_df = dates_only.value_counts().reset_index(name='Tweets').rename(columns={'index': 'Date'})
    
    new_df['Date'] = pd.to_datetime(new_df['Date'])
    new_df = new_df.set_index('Date')

    
    return new_df.sort_index(axis=0)


# Function 6
def word_splitter(df):

    """
    Splits a sentence into a list of the separate words.
    
    Args:
        df: pandas dataframe 
    
    Returns:
        # the inputted pandas dataframe with a new added column ('Split Tweets') which has the Tweets as separate words 
        
    
    Examples:
        >>> word_splitter(twitter_df())

                            Tweets	                                    Date	                Split Tweets
        0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	    [@bongadlulane, please, send, an, email, to, m...
        1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53	    [@saucy_mamiie, pls, log, a, call, on, 0860037...
        2	@BongaDlulane Query escalated to media desk.	    2019-11-29 12:46:10	    [@bongadlulane, query, escalated, to, media, d...
        3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	    [before, leaving, the, office, this, afternoon...
        4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	    [#eskomfreestate, #mediastatement, :, eskom, s...
        ...	...	...	...
        195	Eskom's Visitors Centresâ€™ facilities include i...	2019-11-20 10:29:07 	[eskom's, visitors, centresâ€™, facilities, incl...
        196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	    [#eskom, connected, 400, houses, and, in, the,...
        197	@ArthurGodbeer Is the power restored as yet?	    2019-11-20 10:07:59	    [@arthurgodbeer, is, the, power, restored, as,...
        198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	    [@muthambipaulina, @sabcnewsonline, @iol, @enc...
        199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	    [rt, @gp_dhs:, the, @gautengprovince, made, a,...       
        >>> 
        ###
    """
    splitter = df['Tweets'].apply(lambda x: x.lower().split())
    df['Split Tweets'] = splitter
    
    return df


# Function 7
def stop_words_remover(df):

    """
    Function that takes a pandas dataframe as input and removes stop words from the tokenised list of tweets and returns the results as a new modified dataframe. 
    
    Args:
        df: pandas dataframe
    
    Returns:
             Returns a modified dataframe with a new column called 'Without Stop Words' that contains a tokenised list of tweets without stop words
    
    Examples:
        >>> stop_words_remover(df)

                                Tweets	                                Date	                Without Stop Words
        0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	    [@bongadlulane, send, email, mediadesk@eskom.c...
        1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53	    [@saucy_mamiie, pls, log, 0860037566]
        2	@BongaDlulane Query escalated to media desk.	    2019-11-29 12:46:10	    [@bongadlulane, query, escalated, media, desk.]
        3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	    [leaving, office, afternoon,, heading, weekend...
        4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	    [#eskomfreestate, #mediastatement, :, eskom, s...
        ....	...	...	...
        195	Eskom's Visitors Centresâ€™ facilities include i...	2019-11-20 10:29:07	    [eskom's, visitors, centresâ€™, facilities, incl...
        196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	    [#eskom, connected, 400, houses, process, conn...
        197	@ArthurGodbeer Is the power restored as yet?	    2019-11-20 10:07:59	    [@arthurgodbeer, power, restored, yet?]
        198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	    [@muthambipaulina, @sabcnewsonline, @iol, @enc...
        199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	    [rt, @gp_dhs:, @gautengprovince, commitment, e...     
        
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