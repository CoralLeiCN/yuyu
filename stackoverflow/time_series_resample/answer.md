https://stackoverflow.com/questions/77473807/resampling-huge-pandas-dataframe-throws-arraymemoryerror/77477536#77477536

Resample is time-based groupby, so not necessary to expand the dataframe in the begining, can use an apply to treat the dataframe by chunks (frequency)

If I understand correctly, the error is negligible if we split the data by days when has millisecond accuracy

For example, start a date range of 9 days

    import pandas as pd
    index = pd.date_range('1/1/2000', periods=9, freq='D')
    series = pd.Series(range(9), index=index)

Applied the actual UDF operation on the chunks of each day. For each chunks (days). It will resample to 1ms (lambda function)



    series.resample('D').apply(lambda x: x.resample('1ms').asfreq().interpolate().resample('1s').asfreq())

or 30 minutes

    series.resample('30T').apply(lambda x: x.resample('1ms').asfreq().interpolate().resample('1s').asfreq())

And I do have kernel dead (memory issues) when I try to directly resample to 1ms

`series.resample("1ms").asfreq()`

