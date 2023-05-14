"""
Python function to split a 
date column in a pandas dataframe into three columns: Year, Month, and Day.
"""
# processed
import pandas as pd


def __guard_clauses(
    data_frame: pd.DataFrame,
    date_column: str,
    year_column: str,
    month_column: str,
    day_column: str,
) -> bool:
    """
    Guard clauses for split_date_column function.
    Checks if the arguments are of the correct type and valid values.
    """
    assert isinstance(
        data_frame, pd.DataFrame
    ), f"data_frame must be of type pandas.DataFrame, not {type(data_frame)}."
    assert date_column in data_frame.columns, f"{date_column} not present in dataframe."
    column_names = [year_column, month_column, day_column]
    for column in column_names:
        assert isinstance(
            column, str
        ), f"{column} must be of type str, not {type(column)}."
        assert (
            column not in data_frame.columns
        ), f"{column} already present in dataframe."
    return True


def split_date_column(
    data_frame: pd.DataFrame,
    date_column: str,
    year_column: str = "year",
    month_column: str = "month",
    day_column: str = "day",
) -> pd.DataFrame:
    """
    Takes a date column in a
    dataframe and splits it into three columns: Year, Month, and Day.

    Args:
        data_frame: A pandas dataframe to be processed.
        date_column: A string representing the name of the date column.
        year_column: A string representing the name of the year column.
        month_column: A string representing the name of the month column.
        day_column: A string representing the name of the day column.

    Returns:
        A pandas dataframe with the Year, Month, and Day columns added.

    Raises:
        KeyError: If date_column is not present in data_frame.
        TypeError: If date_column is not of type datetime64[ns].
    """
    # basic guard clauses
    __guard_clauses(data_frame, date_column, year_column, month_column, day_column)

    # Split date_column into Year, Month, and Day columns
    data_frame = data_frame.assign(
        **{
            year_column: data_frame[date_column].dt.year,
            month_column: data_frame[date_column].dt.month,
            day_column: data_frame[date_column].dt.day,
        }
    )

    return data_frame
