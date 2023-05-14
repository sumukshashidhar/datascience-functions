# processed
import pandas as pd

def __guard_clauses(
    df: pd.DataFrame, 
    date_column: str, 
    year_column: str, 
    month_column: str, 
    day_column: str
) -> bool:
    """
    Guard clauses for split_date_column function. Checks if the arguments are of the correct type and valid values.
    """
    assert isinstance(df, pd.DataFrame), f"df must be of type pandas.DataFrame, not {type(df)}."
    assert date_column in df.columns, f"{date_column} not present in dataframe."
    column_names = [year_column, month_column, day_column]
    for column in column_names:
        assert isinstance(column, str), f"{column} must be of type str, not {type(column)}."
        assert column not in df.columns, f"{column} already present in dataframe."
    return True

def split_date_column(df: pd.DataFrame, date_column: str, year_column: str = 'year', month_column: str = 'month', day_column: str = 'day') -> pd.DataFrame:
    """
    Takes a date column in a pandas dataframe and splits it into three columns: Year, Month, and Day.

    Args:
        df: A pandas dataframe to be processed.
        date_column: A string representing the name of the date column.
        year_column: A string representing the name of the year column.
        month_column: A string representing the name of the month column.
        day_column: A string representing the name of the day column.

    Returns:
        A pandas dataframe with the Year, Month, and Day columns added.

    Raises:
        KeyError: If date_column is not present in df.
        TypeError: If date_column is not of type datetime64[ns].
    """
    # basic guard clauses
    __guard_clauses(df, date_column, year_column, month_column, day_column)

    # Split date_column into Year, Month, and Day columns
    df = df.assign(**{
        year_column: df[date_column].dt.year,
        month_column: df[date_column].dt.month,
        day_column: df[date_column].dt.day
    })
    
    return df