# M5 Forecasting - Uncertainty

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and LSTM and bootstrapped residuals.

### Project Structure

```
Importing Dataset :- https://www.kaggle.com/c/m5-forecasting-uncertainty/data?select=sample_submission.csv
```
### Install Anaconda
configure the Jupyter Notebook to create a Enviornment for the Project

1. Basic idea 
Here we are using the Frequentist perspective of probability:
2. The model parameters  w  are assumed to be fixed and we estimate it using our estimator.
3. The estimation depends on the dataset D we observe and consequently we can obtain error bars for our estimated parameters  west  by considering multiple datasets.
4. One way to do this is by creating new datasets, for example with bootstrapping.
5. We are creating new datasets by using bootstrapped residuals:
6. We only assume uncorrelated residuals that need not be normally distributed.

### Install Python Environment
```
calendar.csv - Contains information about the dates on which the products are sold.
```

```
sales_train_validation.csv - Contains the historical daily unit sales data per product and store [d_1 - d_1913]
```
```
sample_submission.csv - The correct format for submissions. Reference the Evaluation tab for more info.
```

```
sell_prices.csv - Contains information about the price of the products sold per store and date.
```

```
sales_train_evaluation.csv - Includes sales [d_1 - d_1941] (labels used for the Public leaderboard)

```
