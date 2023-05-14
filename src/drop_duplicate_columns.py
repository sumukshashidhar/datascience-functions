"""
In a dataframe, drop duplicate columns. Not just column names, but the entire column.
"""
# processed
import pandas as pd
from _dataframe_guard_clauses import __guard_clauses


def drop_duplicate_columns(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Takes a dataframe and drops all duplicate columns.

    Args:
        data_frame: A pandas dataframe to be processed.

    Returns:
        A pandas dataframe with the duplicate columns dropped.

    Raises:
        TypeError: If data_frame is not of type pandas.DataFrame.
    """
    # basic guard clauses
    __guard_clauses(data_frame)
    # get the duplicate columns
    df_transposed = data_frame.T
    deduplicated = df_transposed.drop_duplicates().T
    return deduplicated
