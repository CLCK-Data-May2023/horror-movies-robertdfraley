import os
import pandas as pd
import pytest
import numpy as np
import math

CSV_FILE = "data/movies.csv"

def test_file_exists():
    assert os.path.exists(CSV_FILE) == True, "csv file does not exist"

def test_columns_exist():
    expected_columns = ['Movie_ID','Movie_Title','Rating']
    try:
        df = pd.read_csv(CSV_FILE)
        for col in expected_columns:
            assert col in df.columns
    except Exception as e:
        assert False, e

def test_num_rows():
    try:
        df = pd.read_csv(CSV_FILE)
        assert len(df) == 3
    except Exception as e:
        assert False, e

@pytest.mark.parametrize("expected_id,expected_title,expected_rating",
                        [[226,"The Shining",8.4],
                        [100,"Gremlins",7.2],
                        [116,"The Amityville Horror",6.2]])
def test_values_exist(expected_id, expected_title, expected_rating):
    try:
        df = pd.read_csv(CSV_FILE)
        assert df.loc[df['Movie_ID'] == expected_id]['Movie_Title'].iloc[0] == expected_title
        assert df.loc[df['Movie_ID'] == expected_id]['Rating'].iloc[0] == expected_rating
    except Exception as e:
        assert False, e