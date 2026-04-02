import pandas as pd

def invoiceDate_calcVar(df):
    df['days_between_invoices'] = df.groupby('Client_id')['invoice_date'].diff().dt.days
    variance = df['days_between_invoices'].var()
    return df