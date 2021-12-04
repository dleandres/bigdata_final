import pandas as pd
import statistics
import csv


# open the file in the write mode
with open('C:/Users/dlean/PycharmProjects/BigData/weekly.csv', 'w', encoding='UTF8') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write the header
    header = ["Year", "Month", "Mean", "Standard Deviation"]
    writer.writerow(header)

    df = pd.read_csv(r"data.csv", parse_dates=['time'])
    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]


    for x in years:
        current_year = df.loc[df['time'].dt.year == x]

        for y in range(13):
            current_month = current_year.loc[current_year['time'].dt.month == y]
            first_day = current_month.loc[current_month['time'].dt.day == 1]
            #df_mean = current_month["open"].mean()
            ROI1yr_column = first_day["ROI1yr"]
            ROI1yr = ROI1yr_column.values
            ROI30d_column = first_day["ROI30d"]
            ROI30d = ROI30d_column.values
            #Just a check for missing data.
            if ROI1yr.size > 0 :
                #stdev = statistics.pstdev(opening)
                data = [x, y, ROI1yr, ROI30d]
                # write a row to the csv file
                writer.writerow(data)

