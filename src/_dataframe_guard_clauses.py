"""
File containing a check for the dataframe
"""

import pandas as pd

def __guard_clauses(data_frame: pd.DataFrame) -> bool:
    """
    Guard clauses for drop_duplicate_columns function. 
    Checks if the arguments are of the correct type and valid values.
    """
    assert isinstance(
        data_frame, pd.DataFrame
    ), f"data_frame must be of type pandas.DataFrame, not {type(data_frame)}."
    return True
