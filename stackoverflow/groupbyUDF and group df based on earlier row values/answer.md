https://stackoverflow.com/questions/77477249/python-3-9-code-to-get-pandas-dataframe-column-to-reference-earlier-row-value-i/77477365#77477365

with a new Temp helper columns, the dataframe can be splitted to the correct group, and because the row with True value need to be filled with 0, a small UDF is used.

    import pandas as pd
    
    print("pandas version:", pd.__version__)
    T = True
    F = False
    # Sample DataFrame
    df = pd.DataFrame(
        {
            "Close_Delta": [1, -2, -3, -1, 2, 1, 3, -1, 2, 4, -2, -1],
            "Flag": [T, T, F, F, T, F, F, T, T, F, T, F],
        }
    )
    
    # Create a helper column identify consecutive F values in 'Flag'
    df["helper"] = df["Flag"].cumsum()
    cond = df["Flag"] == False
    df.loc[cond, "helper"] = df.loc[cond, "helper"] + 1
    
    
    def udf_cumulative_sum(x):
        x["Cumulative_Sum"] = x["Close_Delta"].cumsum()
        x.loc[x["Flag"] == True, "Cumulative_Sum"] = 0
        return x
    
    
    df = df.groupby("helper", group_keys=False).apply(udf_cumulative_sum)
    
    # remove helper
    df = df.drop("helper", axis=1)
    print(df)

The output

    pandas version: 1.5.3
        Close_Delta   Flag  Cumulative_Sum
    0             1   True               0
    1            -2   True               0
    2            -3  False              -3
    3            -1  False              -4
    4             2   True               0
    5             1  False               1
    6             3  False               4
    7            -1   True               0
    8             2   True               0
    9             4  False               4
    10           -2   True               0
    11           -1  False              -1

