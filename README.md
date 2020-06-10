# cse163-project

**_Analyzing the Effect of COVID-19 on the Financials of the Premier League_**

_Reproducing the Results:_
For our project, there's only three steps to take to fully reproduce the
results. First is that you run the market_values_scrape.py and
transfers_scrape.py. The transfers_scrape.py should run smoothly, but the
market_values_scrape.py can be difficult. The server would reset the connection
if you ran through the for loop sometimes, but other times not. That's why
there's such a long sleep timer so the connection isn't broken. You'd have to
change the urllib2 request header for your machine, and additionally if the for
loop continually fails, just run one list at a time(first, second, etc.).
After that's done, run the project_main.py for the outputs and correct graphs.
All the necessary Python libraries should be imported by the files. If any
issue occurs with the scraping files, take note that the correctly created
files are already there. The TransferMarkt server shuts down connection
randomly, so we apologize if that error occurs.
