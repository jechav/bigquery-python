# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: venv-bigquery-course
#     language: python
#     name: venv-bigquery-course
# ---

# +
from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
# -

# %load_ext google.cloud.bigquery

import pandas as pd

# %%bigquery df
WITH
  gin_sales AS (
  SELECT
    DATE_TRUNC(date, MONTH) AS month,
    DATE_SUB(DATE_TRUNC(date, MONTH), INTERVAL 1 YEAR) AS month_year_before,
    SUM(volume_sold_liters) AS volume_sold_liters
  FROM
    `bigquery-public-data.iowa_liquor_sales.sales`
  WHERE
    UPPER(category_name) LIKE "%GIN%"
  GROUP BY
    month,
    month_year_before
  ORDER BY
    month DESC )
SELECT
  current_sales.month,
  current_sales.volume_sold_liters,
  year_ago_sales.volume_sold_liters AS volume_sold_year_ago,
  current_sales.volume_sold_liters - year_ago_sales.volume_sold_liters AS increase_liters
FROM
  gin_sales AS current_sales
JOIN
  gin_sales AS year_ago_sales
ON
  current_sales.month = year_ago_sales.month_year_before
ORDER BY
  1 DESC LIMIT 100; 

df.head()

df = pd.read_gbq("""
WITH
  gin_sales AS (
  SELECT
    DATE_TRUNC(date, MONTH) AS month,
    DATE_SUB(DATE_TRUNC(date, MONTH), INTERVAL 1 YEAR) AS month_year_before,
    SUM(volume_sold_liters) AS volume_sold_liters
  FROM
    `bigquery-public-data.iowa_liquor_sales.sales`
  WHERE
    UPPER(category_name) LIKE "%GIN%"
  GROUP BY
    month,
    month_year_before
  ORDER BY
    month DESC )
SELECT
  current_sales.month,
  current_sales.volume_sold_liters,
  year_ago_sales.volume_sold_liters AS volume_sold_year_ago,
  current_sales.volume_sold_liters - year_ago_sales.volume_sold_liters AS increase_liters
FROM
  gin_sales AS current_sales
JOIN
  gin_sales AS year_ago_sales
ON
  current_sales.month = year_ago_sales.month_year_before
ORDER BY
  1 DESC LIMIT 100; 
""", use_bqstorage_api=True)

df.to_gbq("experimental.test_table", "bigquery-course-xyz", if_exists='replace')


