# Pairs Trading with Stocks Toyota(TM) & Subaru(FUJHY) :chart_with_upwards_trend:
by [Victoria Uriostegui](https://www.linkedin.com/in/victoria-uriostegui-3a031a26a) and [Erika Dickson](https://www.linkedin.com/in/erika-dickson?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) from Cal State University, Fullerton. :elephant:

## Personal Motivation :trophy:
In the summer of 2024, Erika and I participated in Project RAISE as research assistant interns employed through CSUF's Auxiliary Services Corporation under the direction of Dr. Bein. Throughout our 8-week internship, we had multiple setbacks attempting to implement pairs trading. Unfortunately, we determined through multiple tests that our stocks were not cointegrated nor correlated. Although our internship ended and we no longer work with Dr. Bien, Erika and I stayed in touch and vowed to finish our Pairs Trading Project. This project serves as a reminder that setbacks do *not* have to define you. We hope you enjoy our ongoing Pairs Trading Project.

## Project Description: What is Pairs Trading? :monocle_face:
According to the [Wharton School of the University of Pennsylvania](http://stat.wharton.upenn.edu/~steele/Courses/434/434Context/PairsTrading/PairsTradingQFin05.pdf), Pairs Trading is an investment stategy involving two similar stocks trading at a certain spread. Wharton states, "if the spread widens [short](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/stock-purchases-and-sales-long-and) the high stock and buy the low stock. As the spread narrows again to some [equilibrium value](https://dictionary.cambridge.org/us/dictionary/english/equilibrium-price), a profit results." 

#### What does this mean? #### 
In our case, shorting means selling the higher-value stock to then buying the cheaper stock. A profit occurs once the stocks normalize in value because the higher stock is sold at a greater value, and the lower stock is bought at a cheaper rate. 

### How do you find two stocks optimal for Pairs Trading? ###
Pairs trading *needs* two or more stocks with high correlation. Two companies with similar characteristics and work in a similar sector may have a high correlation between stocks because they carry similar risks. In theory, both stocks should have similar prices. [Correlation](https://openstax.org/books/principles-finance/pages/14-1-correlation-analysis) is a statistic that measures the degree to which two variables move in relation to each other. The correlation coefficient is a value between -1 and 1. A near-zero correlation means a weak relationship, while a value closer to 1 indicates a strong relationship. We must also have at least two stocks that are [cointergrated](https://pmc.ncbi.nlm.nih.gov/articles/PMC6744394/). Cointegration tests analyze variances and means varying over time, also known as the stock's non-stationary time series. 
Co-integration looks for a stationary pair where the mean of the spread is fixed. Whenever the spread deviates from the mean, it generates trading opportunities, and the spread may revert back to the mean value. Essentially two time series, over a long period of time, move together.
They might deviate from each other for a short duration, but in the long run they move in tandem. This property is used in finance to execute carry trade. When two cointegrated stocks deviate, they are expected to fall in line, and accordingly, the trade is executed using a pairs trading signal to earn profit. 

### Key Takeaways :memo:
In order to execute pairs trading successfully, you must have at least two stocks that are correlated and cointegrated. Lastly, the use of a pairs trading signal will be used to know when to buy and sell each respective stock. 

***Note:** We are currently working on a pairs trading signal. More detail about a pairs trading signal will be added once completed*

## Tools and Technologies :desktop_computer:

- **Google Colab**: is a free cloud-based platform provided by Google that allows users to write and execute Python code collaboratively in a Jupyter Notebook environment
- **Jupyter Notebook**: is an Integrated Development Environment (IDE)
- **Python**: is the main programming language utilized
- **Numpy**: is the fundamental package for scientific computing in Python
- **Pandas**: is a fundamental high-level building block for doing practical, real-world data analysis in Python
- **Pandas Data Reader**: allows the creation of pandas DataFrame by using some popular data sources available on the internet
- **Date Time**: is a class in Python to supply dates and times
- **MatPlotLib**: is a comprehensive library for creating static, animated, and interactive visualizations in Python
- **Seaborn**: is a Python data visualization library based on matplotlib
- **Stats Model API**: is a Python module that provides classes and functions for the estimation of many different statistical models, conducting statistical tests, and statistical data exploration
- **Yahoo Finance API**: is a free tool that allows developers to access and retrieve real-time and historical financial data from Yahoo Finance

## Poster for Cal State Univeristy, Fullerton first Computer Science Showcase on April 8th, 2024 💻🐘
We were honrored to be selected to present and compete in the first Computer Science Showcase at CSUF! Our poster contains many insights into our logic, methods, and conclusions. Feel free to peak! 

![Computer Science Showcase Poster](CS-Showcase-Poster.png)

## Conlcusion 💭
In conclusion, our research yields unexpected findings. Our hypothesis stipulates that our implementation of a pairs trading strategy will yield sizeable profits given two cointegrated stocks and will be convenient for the average trader to utilize. However, our findings show that although more than $200 was accrued through our pairs trading implementation, our results were not up to par with expectations and fell short of other comparable projects. Limitations encountered include using stocks that were cointegrated but had large price gaps, which made the process of purchasing and buying equivalent amounts of stocks complicated. In terms of our goal of minimizing human intervention in our program to have a relatively automated system, we fall short of our goal to simplify the process of pairs trading, as much analysis and computation must still be completed manually. Despite these setbacks, our research remains compelling in the merits of the pairs trading strategy and sets the foundation for further study.

## Future Work ⚒️
In future revisions, we aim to broaden the functionality and scalability of our project, as well as increase the return on investment. Implementations and edits to accomplish this goal include implementing machine learning to allow the system to learn from the pairs trading algorithm to make more sophisticated real-time decisions, adapting the program to be easier to use for the average user, and utilizing more sophisticated statistical analysis practices to have more accurate and relevant figures upon which the pairs trading strategy can be utilized, such as testing which specific rolling window expanse is most effective.

## References 📔
James, Chen. “Pairs Trade: Definition, How Strategy Works, and Example.” Investopedia, 26 June 2021, www.investopedia.com/terms/p/pairstrade.asp.
Auquan. “Tutorials/Pairs Trading.ipynb at Master · Auquan/Tutorials.” GitHub, 2025, github.com/Auquan/Tutorials/blob/master/Pairs%20Trading.ipynb.
Kramer, Leslie . “Long Position vs. Short Position: What’s the Difference?” Investopedia, 2019, www.investopedia.com/ask/answers/100314/whats-difference-between-long-and-short-position-market.asp.








