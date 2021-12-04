import pandas as pd
import statistics
import numpy as np
import csv


# open the file in the write mode
with open('C:/Users/dlean/PycharmProjects/BigData/yearly.csv', 'w', encoding='UTF8') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write the header
    header = ["Year", "Mean", "Standard Deviation"]
    writer.writerow(header)

    df = pd.read_csv(r"data.csv", parse_dates=['time'])
    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

    print("Year Mean")
    for x in years:
        current_year = df.loc[df['time'].dt.year == x]
        open_column = current_year["open"]
        open_values = open_column.values
        if open_values.size > 0:
            df_mean = np.mean(open_values, dtype=np.float64)
            df_sd = statistics.pstdev(current_year["open"])
            roi = current_year["open"]/current_year["close"]
            data = [x, df_mean, df_sd]
            # write a row to the csv file
            writer.writerow(data)
