import pandas as pd


def import_df(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The input is is not a Dataframe")
    else:
        return df
    
def date_colunm(df,column_name):
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
    if pd.api.types.is_datetime64_any_dtype(df[column_name]):
        return df
    
    try:
        df[column_name] = pd.to_datetime(df[column_name])
        return df
    except Exception as e:
        raise ValueError("No date column could be identified")
    

if __name__ == "__main__":
    print('main1')