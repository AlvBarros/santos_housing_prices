# Predicting House Prices

This is a simple implementation of linear regression with gradient descent in order to predict house prices.

![plot](./results/2025-08-09%2014:31:00/plot.png)

# Table of contents

- [Getting data](#getting-data)
- [Running the script](#running-the-script)
- [Predicting values](#predicting-values)

## Getting data

Currently, this repository includes a script that will fetch the data from [Invista Imóveis](https://www.invistaii.com.br/), a local real estate broker. To begin, run this command:
```sh
python get_data.py --sources invista
```

## Running the script

After getting the data, you can simply run the script:
```sh
python index.py
```

Then, the results will be exported inside the `results/` folder, alongside with another folder named after the timestamp.

## Predicting values

The file `predict_price.py` contains an easy way to use the specific model obtained after running the `index` script. For example:

```sh
python predict_price.py --area 100 --result-file "results/2025-08-09 14:31:00/results.csv"
```