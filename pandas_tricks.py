import pandas as pd

def optimize_datatypes(df, datetime):
    '''
    This function will downcast the columns types of dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        Filepath of csv file
    datetime: str
        convert date to object to datetime

    Returns
    -------
    pandas.DataFrame
        downcasted dataframe
    '''
    ints = df.select_dtypes(include=['int64']).columns.tolist()
    df[ints] = df[ints].apply(pd.to_numeric, downcast='integer')
    for col in df.select_dtypes(include=['object']):
        if col not in datetime:
            num_unique_values = len(df[col].unique())
            num_total_values = len(df[col])
            if float(num_unique_values) / num_total_values < 0.5:
                df[col] = df[col].astype('category')
        else:
            df[col] = pd.to_datetime(df[col])
    return df
    
    def read_csv(filepath, date_col=None):
    '''
    This function will read csv file.

    Parameters
    ----------
    filepath : str
        Filepath of csv file
    date_col : str or list
        Name or list of datetime column 
    

    Returns
    -------
    pandas.DataFrame
        Dataframe of csv file
    '''
    assert os.path.exists(filepath), f'{filepath} does not exist.'
    df = pd.read_csv(filepath)
    df = optimize_datatypes(df, date_col)
    return df
