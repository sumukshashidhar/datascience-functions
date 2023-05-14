"""
Python function to drop all columns in a dataframe that contain only one value.
"""
# processed
import pandas as pd
from _dataframe_guard_clauses import __guard_clauses


def drop_single_value(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Takes a dataframe and drops all columns that contain only one value.

    Args:
        data_frame: A pandas dataframe to be processed.

    Returns:
        A pandas dataframe with the single value columns dropped.

    Raises:
        TypeError: If data_frame is not of type pandas.DataFrame.
    """
    # basic guard clauses
    __guard_clauses(data_frame)
    # get the number of unique values in each column
    unique_values = data_frame.nunique()
    # get the columns that contain only one unique value
    columns_to_drop = unique_values[unique_values == 1].index

    # drop the columns
    data_frame = data_frame.drop(columns=columns_to_drop)

    return data_frame
