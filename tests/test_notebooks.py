"""Test for contradiction of the actual test """

import pandas as pd 
import pytest
import notebooks.data_cleaning




def test_read_csv():
    new_df =pd.read_csv("./data/train.csv")
    assert new_df is not None

def test_missing_columns():
    new_df = pd.read_csv("./data/train.csv")
    new_df = (new_df.isna().sum()/len(new_df))*100
    result = new_df.head()
