# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Project 4

---

### Table of Contents

1. [Problem Statement](#Problem-Statement)
2. [Data Dictionary](#Data-Dictionary)
3. [Preprocessing & Modeling](#Preprocessing-and-Modeling)
4. [Conclusion and Recommendations](#Conclusion-and-Recommendations)
5. [Datasets](#Datasets)

---

### Problem Statement

Using data from UC Irvine Machine Learning build a model that can predict if a person's income is in excess of $50,000 given certain profile information

---

### Data Dictionary

|Feature                     |Type    |Dataset             |Description              |
|---                         |---     |---                 |---                      |
|age                         |int64   |large_train_sample  |person's age             |
|education-num               |int64   |large_train_sample  |years of education       |
|capital-gain                |int64   |large_train_sample  |capital gained                      |
|capital-loss                |int64   |large_train_sample  |capital lost                        |
|hours-per-week              |int64   |large_train_sample  |average hours worked per week       |
|native-country              |int64   |large_train_sample  |1: from United States, 0: other, engineered feature           |
|wage                        |int64   |large_train_sample  |1: made over 50k, 0: made under 50k, engineered feature       |
|relationship_Other-relative |int64   |large_train_sample  |engineered feature       |
|relationship_Own-child      |int64   |large_train_sample  |engineered feature       |
|relationship_Unmarried      |int64   |large_train_sample  |engineered feature       |
|relationship_Wife           |int64   |large_train_sample  |engineered feature       |
|workclass_Local-gov         |int64   |large_train_sample  |engineered feature       |
|workclass_Private           |int64   |large_train_sample  |engineered feature       |
|workclass_Self-emp-inc      |int64   |large_train_sample  |engineered feature       |
|workclass_Self-emp-not-inc  |int64   |large_train_sample  |engineered feature       |
|workclass_State-gov         |int64   |large_train_sample  |engineered feature       |
|workclass_ Without-pay      |int64   |large_train_sample  |engineered feature       |

---

### Preprocessing and Modeling

Data cleaning included dropping the following features: final weight, education, marital status, and occupation. Null values or non numerical values were dropped. The wage and native country columns were binarized and the sex, relationship and workclass columns were dummied.

The models used were a Random Forest Classifier, XGBoost Classifier, and XGBoost-Dart Classifer. First, a baseline score was established then I used GridSearchCV to identify the best scores and parameters generated from the models. The models consisted of 18 features.

|Model                       |Average Cross Val Score    |
|---                         |---                        |
|Random Forest               |0.842                      |
|XGBoost Classifer           |0.856                      |
|XGBoost-Dart Classifer      |0.854                      |                    

---

### Conclusion and Recommendations

In summary, the 3 models used performed better in predicting wage under 50k that it was predicting over 50k. Precision scores across the 3 models were fairly similar, but the best score came from the Random Forest Classifier with 0.80. The model with the highest accuracy score was XGBoost Classifier with .8529

---

### Datasets

* [large_train_sample.csv]('data/large_train_sample.csv'): Train Sample Data
* [test_data.csv]('data/test_data.csv'): Test Data
* [sub.csv]('../data/sub.csv'): Submission Data
