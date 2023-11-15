#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:34:13 2023

@author: robertisaksen
"""

from math import log, sqrt

# Calculate Log Return
def calculate_log_return(start_price, end_price):
    return log(end_price / start_price)

# Calculate Variance
def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    numerator = sum((data - mean) ** 2 for data in dataset)
    return numerator / len(dataset)

# Calculate Standard Deviation
def calculate_stddev(dataset):
    variance = calculate_variance(dataset)
    return sqrt(variance)

# Calculate Correlation Coefficient
def calculate_correlation(set_x, set_y):
    sum_x = sum(set_x)
    sum_y = sum(set_y)

    sum_x2 = sum(x ** 2 for x in set_x)
    sum_y2 = sum(y ** 2 for y in set_y)

    sum_xy = sum(x * y for x, y in zip(set_x, set_y))

    n = len(set_x)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

    return numerator / denominator

# Display as Percentage
def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)

# Calculate Logarithmic Rates of Return
def get_returns(prices):
    returns = []

    for i in range(1, len(prices)):
        start_price = prices[i - 1]
        end_price = prices[i]
        log_return = calculate_log_return(start_price, end_price)
        returns.append(log_return)

    return returns

# Stock Prices
amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# Calculate Monthly Log Rates of Return
amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)

# Display Monthly Returns as Percentage
amazon_returns_percentage = [display_as_percentage(return_value) for return_value in amazon_returns]
ebay_returns_percentage = [display_as_percentage(return_value) for return_value in ebay_returns]

print("Amazon Monthly Returns as Percentage:", amazon_returns_percentage)
print("eBay Monthly Returns as Percentage:", ebay_returns_percentage)

# Calculate and Display Annual Returns
amazon_annual_return = sum(amazon_returns)
ebay_annual_return = sum(ebay_returns)

print("Amazon Annual Return as Percentage:", display_as_percentage(amazon_annual_return))
print("eBay Annual Return as Percentage:", display_as_percentage(ebay_annual_return))

# Calculate and Display Variance
amazon_variance = calculate_variance(amazon_returns)
ebay_variance = calculate_variance(ebay_returns)

print("Amazon Variance:", amazon_variance)
print("eBay Variance:", ebay_variance)

# Calculate and Display Standard Deviation
amazon_stddev = calculate_stddev(amazon_returns)
ebay_stddev = calculate_stddev(ebay_returns)

print("Amazon Standard Deviation:", display_as_percentage(amazon_stddev))
print("eBay Standard Deviation:", display_as_percentage(ebay_stddev))

# Calculate and Display Correlation
correlation = calculate_correlation(amazon_returns, ebay_returns)
print("Correlation between Amazon and eBay Returns:", correlation)