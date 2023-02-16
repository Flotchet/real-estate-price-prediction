# Real estate price prediction (Machine Learning README.md)

## Project descritpion

This project is part of the data science training from Becode.org.

It aims to predict prices for houses or appartment considering the current state of the market.

## Current state

* Finalized

## What it does (In order)

### Train the models

* Prepare the data
* Separate the datset into provinces - region - country
* Adapt each dataset depending on the model
* Train the models

| Model                                                       | Average Prceision in %                      |
| ----------------------------------------------------------- | ------------------------------------------- |
| DecisionTreeRegressor                                       | 77,38                                       |
| ElasticNet                                                  | 67,67                                       |
| GradientBoostingRegressor                                   | 80,47                                       |
| KNeighborsRegressor<br />k = 10-200                         | 76,11 k=200 to 78,87 k=21                   |
| Lasso                                                       | 76,96                                       |
| LinearRegression                                            | 76,95                                       |
| RandomForestRegressor<br />d  = 50 - 350<br />n = 20 - 295 | 80,28 d=350 & n=20<br />81,33 d=150 & n=170 |
| Ridge                                                       | 76,95                                       |
| SVR                                                         | 71,11                                       |
| XGBoost<br />Absolute error mode                            | 69,86                                       |
| XGBoost<br />Squared  error mode                           | 82,78                                       |

#### Results analysis

From the result that I obtained, It's obvious that there is a model that is clearly ahead in term of precision

| Province            | Model     | R2    | Mean<br />Squared<br />Error | Mean<br />Absolute <br />Precision |
| ------------------- | --------- | ----- | ---------------------------- | ---------------------------------- |
| Belgique            | XGBoostSE | 0.601 | 1054082.709                  | 81.6%                              |
| Bruxelles-Capitale  | XGBoostSE | 0.325 | 984378.209                   | 84.0%                              |
| Region Flamande     | XGBoostSE | 0.602 | 1006036.804                  | 84.1%                              |
| Region Wallone      | XGBoostSE | 0.478 | 633641.906                   | 78.7%                              |
| Province d'Anvers   | XGBoostSE | 0.505 | 695801.057                   | 85.2%                              |
| Flandre-Occidentale | XGBoostSE | 0.632 | 1516085.148                  | 83.3%                              |
| Flandre-Orientale   | XGBoostSE | 0.607 | 836908.587                   | 85.1%                              |
| Limbourg            | XGBoostSE | 0.633 | 573336.521                   | 86.1%                              |
| Liège              | XGBoostSE | 0.398 | 538363.532                   | 79.7%                              |
| Luxembourg          | XGBoostSE | 0.547 | 625537.802                   | 81.2%                              |
| Namur               | XGBoostSE | 0.503 | 577347.691                   | 80.3%                              |
| Brabant flamand     | XGBoostSE | 0.635 | 702516.832                   | 88.3%                              |
| Brabant flamand 2   | XGBoostSE | 0.888 | 2794071.127                  | 87.4%                              |
| Brabant wallon      | XGBoostSE | 0.726 | 880901.734                   | 89.4%                              |
| Hainaut 1           | XGBoostSE | 0.506 | 291272.189                   | 81.5%                              |
| Hainaut 2           | XGBoostSE | 0.430 | 354904.131                   | 79.1%                              |

The table shows the results of the best models applied to different provinces or region in Belgium. The R-squared value, mean squared error (MSE), mean absolute error (MAE), and mean absolute precision (MAP) are shown for each province.

In general, the R-squared values of the model are moderate to high, with a range of 0.32 to 0.89. This suggests that the model is able to explain a moderate to high amount of the variability in the data. However, it should be noted that a high R-squared value does not necessarily indicate a good model, as it may be overfitting.

The MSE values are also moderate to high, ranging from 695801.05 to 2794071.12. Lower MSE values indicate that the model makes smaller errors in its predictions.

The MAP values range from 0.79 to 0.89, which indicates that the model's predictions are relatively accurate. However, it should be noted that the MAP values are not that high, which means that the model may not be accurate in all cases and that further analysis is needed.

It's worth noting that the XGBoostSE model performed better in some provinces like Province du Brabant flamand 2, Province du Brabant wallon and Province de Limbourg, with R-squared values higher than 0.8 and MAP values less than 0.85. On the other hand, provinces and regions like Bruxelles-Capitale, Province de Liège, Province de Namur, Region Wallone and Province du Hainaut 2 show lower performance.

It's also important to note that these results are based on a single training and testing set, and additional evaluation methods such as cross-validation should be performed to confirm the robustness of the model.

I also estimate that in a perfect world, we could have a maximum precision of 3777 euros due to the fact that some propreties are perfectly similar except for the price.

## Prerequises (Global)

Python 3.11.1 64-bit

Firefox

*Tested on Fedora release 37 (Thirty Seven) x86_64 kernel 6.0.15-300.fc37.x86_64 but it should works on most linux distro

* PySimpleGUI

Other requierements can be directly installed from the user interface from main.py

## Recommended system requirements

CPU: 8core (Intel i7-10875H)

RAM: 64GB (works with 32GB with no other software running)

GPU: /

Vram: /

HDD: 15GB of free space (SSD recommanded because of the large number of small files)
