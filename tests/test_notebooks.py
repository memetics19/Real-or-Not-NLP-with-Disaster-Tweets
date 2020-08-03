"""Test for contradiction of the actual test """

import pandas as pd 
import pytest
import notebooks.data_cleaning

def test_df_add():
    new_df =pd.read_csv("./data/train.csv")
    assert new_df is not None



