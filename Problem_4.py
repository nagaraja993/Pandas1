import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cust = orders['customerId']
    return customers[~customers['id'].isin(cust)][['name']].rename(columns = {'name': 'Customers'})