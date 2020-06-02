# cse163-project

*Analyzing the Effect of COVID-19 on the Financials of the Premier League*

Research Questions: 
What will the effect of COVID-19 be on the total revenue of the Premier League?
In comparison to the extremely high transfer fees paid before the coronavirus pandemic, how much will Premier League clubs pay for the same quality of player afterward?
What combination of qualitative variables best determines the market value of a player? Is it age, nationality, position, overall quality, or a mixture of multiple?

Motivation and background:
We believe this problem matters since the state of the world after shelter-in-place orders close worldwide will leave markets in shambles. As we find soccer really interesting, we were wondering how COVID-19 has and will affect the league. Answering the aforementioned questions will give us insight on how the future of the league may look.

Datasets:
https://www.theguardian.com/football/2018/jun/06/premier-league-finances-club-guide-2016-17
https://www.theguardian.com/football/2019/may/22/premier-league-finances-club-guide-2017-18-accounts-manchester-united-city
https://www.transfermarkt.us/premier-league/transfers/wettbewerb/GB1/plus/?saison_id=2019&s_w=&leihe=0&intern=0&intern=1
https://www.transfermarkt.us/premier-league/transfers/wettbewerb/GB1/plus/?saison_id=2018&s_w=&leihe=0&intern=0&intern=1
https://www.kaggle.com/kevinmh/fifa-18-more-complete-player-dataset
https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset

Challenge Goals:
Implementing Multiple Datasets: In our project we dive into multiple datasets to answer questions about the Premier League
Using Messy Data: We will need to use web scraping to acquire data from sites like The Guardian and TransferMarkt
Employing Machine Learning: We will be using machine learning libraries and algorithms to accurately predict information relevant to our questions.

Methodology:
Question 1: To answer this question, we will web scrape from sites like The Guardian to get a breakdown on each club’s finances by using a Python library called BeautifulSoup. From there, we can use Python libraries like Pandas to import the data into a script and perform various actions to prepare the data to be visualized using Matplotlib.
Question 2: Similar to the last question, we use web scraping techniques to get the data from TransferMarkt and load the result into a Python script. From there, we will use Pandas to prepare for the data to be used in a machine learning regression model. Our regression model comes from a library called Sklearn which we can use to split the data into a training and test set. Using this regression model enables us to predict quantitative values, transfer fees in our case, after COVID-19 based on current data.
Question 3: To answer this question, we get CSV data from Kaggle and import it into a Python script using Pandas. We then prepare the data by splitting it into a test and training set and feed it to a clustering machine learning model, again using the Sklearn library. From there, we train the model and use it to tell us which qualitative features of a player make them more or less attractive to a team.

Work Plan:
Web Scraping Script:
For this part of the project, we plan on collaborating on the web scraping tool by using GitHub to share code. Our goal is to get done with the script by 5/26 so we can begin the next part of the project. We expect to spend around 3-5 hours each on this part of the project.
Data Cleaning: 
We expect data cleaning to take till the end of that week, 5/29. Again, we will use GitHub to share code and verify that we have engineered an appropriate and accurate solution. We expect to spend 2-5 hours each on this part of the project.
Machine Learning Model:
We expect training the machine learning model and reasoning if we are doing so correctly will take the most amount of time as there will be more of a learning curve. We hope to be done with this part of the project by 6/2 and spend anywhere from 4-7 hours each on ensuring we are getting accurate results.
Visualizations and Result Presentation:
We do not expect this part of the project to take too long as we have already got the solutions from the previous steps. We hope to be done with the final project on 6/4 and spend 3-4 hours each making sure we have everything ready to submit.
Additional Comments:
Throughout this group project, we expect to be collaborating frequently through video calls and on platforms such as GitHub to ensure that we can be as streamline in delivering a finished project as possible.
