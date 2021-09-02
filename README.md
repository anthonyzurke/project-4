# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Project 4

---

### Table of Contents

1. [Problem Statement](#Problem-Statement)
2. [Data Dictionary](#Data-Dictionary)
3. [Preprocessing & Modeling](#Preprocessing-and-Modeling)
4. [Conclusion and Recommendations](#Conclusion-and-Recommendations)

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

### Preprocessing & Modeling

Data cleaning included dropping the following features: final weight, education, marital status, and occupation. Null values or non numerical values were dropped. The wage and native country columns were binarized and the sex, relationship and workclass columns were dummied.

---

### Conclusion & Recommendations


