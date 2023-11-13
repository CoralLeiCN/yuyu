**Pandas allows to write the complex UDF**. before jump to the code, not sure if the output data is wrong.
- index 2: the l1 is different between input and output . `data = {'l1': [2,3,np.nan` but in output `output_data = {'l1': [2,3,1`
- index 4 ,the output is not correct based on the formula, `0.6*4 + 0.4*14.0 = 8` instead of `13.44`
- index 6, similar to above, `23*0.4+123*0.6=83.0` instead of 678.96
- index 10-12, similar to above, for instance, `87*0.6+65*0.4 = 78.2` instead of `1357`
_______
The example below applied the correction mentioned above.

    import numpy as np
    import pandas as pd
    
    def calculate_output(row):
        mon = row['mon']
        l1 = row['l1']
        l2 = row['l2']
        l3 = row['l3']
    
        if pd.isna(l1) and pd.isna(l2) and pd.isna(l3):
            return pd.Series({'output_val': 0, 'output_col': ' '})
    
        if mon < 5:
            if pd.notna(l1):
                return pd.Series({'output_val': l1, 'output_col': 'l1'})
            elif pd.notna(l3):
                return pd.Series({'output_val': l3, 'output_col': 'l3'})
            else:
                return pd.Series({'output_val': l2, 'output_col': 'l2'})
    
        if 5 <= mon <=7:
            if pd.isna(l1):
                return pd.Series({'output_val': l2, 'output_col': '1*l2'})
            elif pd.isna(l2):
                return pd.Series({'output_val': l1, 'output_col': '1*l1'})
            elif mon == 5:
                output_val = 0.60 * l1 + 0.40 * l2
                output_col = '0.60*l1+0.40*l2'
                return pd.Series({'output_val': output_val, 'output_col': output_col})
            elif mon == 6:
                output_val = 0.50 * (l1+l2)
                output_col = '0.50*(l1+l2)'
                return pd.Series({'output_val': output_val, 'output_col': output_col})
            elif mon == 7:
                output_val = 0.40 * l1 + 0.60 * l2
                output_col = '0.40*l1+0.60*l2'
                return pd.Series({'output_val': output_val, 'output_col': output_col})
    
        elif 8 <= mon <= 10:
            if pd.notna(l2):
                return pd.Series({'output_val': l2, 'output_col': 'l2'})
            elif pd.notna(l1):
                return pd.Series({'output_val': l1, 'output_col': 'l1'})
            elif pd.notna(l3):
                return pd.Series({'output_val': l3, 'output_col': 'l3'})
            else:
                return pd.Series({'output_val': 0, 'output_col': ' '})
        if 11 <= mon <= 13:
            if pd.isna(l2):
                return pd.Series({'output_val': l3, 'output_col': '1*l3'})
            elif pd.isna(l3):
                return pd.Series({'output_val': l2, 'output_col': '1*l2'})        
            elif mon == 11:
                output_val = 0.60 * l2 + 0.40 * l3
                output_col = '0.60*l2+0.40*l3'
                return pd.Series({'output_val': output_val, 'output_col': output_col})
            elif mon == 12:
                output_val = 0.50 * (l2+l3)
                output_col = '0.50*(l2+l3)'
                return pd.Series({'output_val': output_val, 'output_col': output_col})
            elif mon == 13:
                output_val = 0.40 * l2 + 0.60 * l3
                output_col = '0.40*l2+0.60*l3'
                return pd.Series({'output_val': output_val, 'output_col': output_col})
        else:
            if pd.notna(l3):
                return pd.Series({'output_val': l3, 'output_col': 'l3'})
            elif pd.notna(l2):
                return pd.Series({'output_val': l2, 'output_col': 'l2'})
            elif pd.notna(l1):
                return pd.Series({'output_val': l1, 'output_col': 'l1'})
            else:
                return pd.Series({'output_val': 0, 'output_col': ' '})


Call the UDF

    import numpy as np
    import pandas as pd
    
    data = {
        "l1": [2, 3, np.nan, 3, 4, 1, 23, 5, np.nan, 100, 101, 200, 121, 431, 341],
        "l2": [12, 13, np.nan, 13, 14, np.nan, 123, 15, np.nan, 200, 87, 65, 23, 54, np.nan],
        "l3": [np.nan,333,111,np.nan,334,111,123,5,np.nan,np.nan,65,154,341,np.nan,np.nan,
        ],
        "mon": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    }
    data = pd.DataFrame(data)
    output_df = data.apply(calculate_output, axis=1)
    result_df = pd.concat([data, output_df], axis=1)`

Validation

    from pandas.testing import assert_frame_equal
    
    output_data = {'l1': [2,3,np.nan,3,4,1,23,5,np.nan, 100, 101, 200, 121, 431, 341],
           'l2': [12,13,np.nan,13,14,np.nan,123,15,np.nan, 200, 87, 65, 23, 54, np.nan],
           'l3': [np.nan,333,111,np.nan,334,111,123,5,np.nan, np.nan, 65, 154, 341, np.nan, np.nan],
           'mon':[1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15],
           'output_val': [2,3,111, 3, 8, 1, 83.0, 15, 0, 200, 78.2, 109.5, 213.8, 54, 341],
           'output_col':['l1', 'l1', 'l3', 'l1', '0.60*l1+0.40*l2', '1*l1', '0.40*l1+0.60*l2', 'l2', ' ', 'l2', '0.60*l2+0.40*l3', '0.50*(l2+l3)', '0.40*l2+0.60*l3', 'l2', 'l1']}
    
    output_data = pd.DataFrame(output_data)
    
    assert_frame_equal(result_df, output_data)

