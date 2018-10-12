# Discover / Requirements
We will be getting data from 5 different stocks by a monthly rate.
Our goal is to have a graph showing which one will be the best to invest in.
This is important because it is important to see trends in the stock market to help the investors make the best decision.
# Collection
My data was collected using alphavantage. I downloaded the data in a csv file
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=NFLX&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AAPL&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=DVMT&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MSFT&apikey=my-api-key&datatype=csv
https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=FB&apikey=my-api-key&datatype=csv
# Data Prep Cleaning
I wanted to have my charts showing the high and closing prices in the months of 2018. What I did was delete the data that was not in 2018. I did this for both my closing and high prices. I reordered my data from oldest to newest for each of the companies. I checked to make sure that none of my data had unwanted numbers or any typos.
# Planning
All my data was nice and clean. I noticed a trend in all companies. The companies stock values tended to drop than slowly rise.
# Modeling
I started to check my data more. I brought all my data from the different csv files into one csv file that had all the companies together with the data in order from oldest to newest. I did this for both of my csv files that included the high and closing values.
# Computation
In this step I know I wanted to use python and matplotlib. In this step I also knew that I wanted to create a line plot graph. So I could notice trends. I put the months in the bottom and the values to the side. I chose to do this because it would allow me to notice certain trends when viewing the graph. I did this for both my high and closing prices.
# Findings/Review
In this step I reviewed my graph to make my final decision on what company I would recommend the user to invest in. I saw the trends on some companies and saw other companies making a slow rise. At the end of the day my decision was based on budget and repeated trends on the market.
