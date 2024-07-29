import pandas as pd
import numpy as np

def clean_economic_impact(value):
    """
    Clean and convert the economic impact value to EUR equivalent.

    Args:
        value (str): The economic impact value.

    Returns:
        float: The value converted to EUR equivalent.
    """
    
    # if pd.isna(value):
    #     return np.nan
    # # Extract numeric value
    # numeric_value = ''.join(filter(str.isdigit, value))
    # if not numeric_value:
    #     return np.nan
    # numeric_value = float(numeric_value)

    if pd.isna(value):
        return np.nan
    
    # Remove any commas and potential spaces from the value
    value = value.replace(",", "").strip()
    
    # Extract numeric value
    numeric_value = ''.join(filter(lambda x: x.isdigit() or x == '.', value))
    if not numeric_value:
        return np.nan
    numeric_value = float(numeric_value)

    # Convert "million", "billion", and "trillion" to numeric values
    if 'million' in value.lower():
        numeric_value *= 1_000_000
    elif 'billion' in value.lower():
        numeric_value *= 1_000_000_000
    elif 'trillion' in value.lower():
        numeric_value *= 1_000_000_000_000
    
    # Extract numeric value
    numeric_value = ''.join(filter(lambda x: x.isdigit() or x == '.', value))
    if not numeric_value:
        return np.nan
    numeric_value = float(numeric_value)

    # Identify currency and adjust value to EUR equivalent
    if '£' in value:
        return numeric_value * 1.19  # Example conversion rate to EUR
    elif '€' in value:
        return numeric_value
    elif 'USD' in value:
        return numeric_value * 0.92
    elif 'DKK' in value:
        return numeric_value * 0.13
    elif 'AU$' in value:
        return numeric_value * 0.60
    elif 'CHF' in value:
        return numeric_value * 1.05
    elif 'MXN' in value:
        return numeric_value * 0.050
    elif 'PLN' in value:
        return numeric_value * 0.23
    elif 'SEK' in value:
        return numeric_value * 0.094  # Example conversion rate to EUR
    elif 'CAD' in value:
        return numeric_value * 0.74  # Example conversion rate to EUR
    elif 'NOK' in value:
        return numeric_value * 0.094  # Example conversion rate to EUR
    elif 'JPY' in value:
        return numeric_value * 0.0069  # Example conversion rate to EUR
    elif 'CLP' in value:
        return numeric_value * 0.0012  # Example conversion rate to EUR
    elif 'ARS' in value:
        return numeric_value * 0.0091  # Example conversion rate to EUR
    elif 'BRL' in value:
        return numeric_value * 0.19  # Example conversion rate to EUR
    elif 'NGN' in value:
        return numeric_value * 0.0024  # Example conversion rate to EUR
    elif 'INR' in value:
        return numeric_value * 0.013  # Example conversion rate to EUR
    elif 'RUB' in value:
        return numeric_value * 0.014  # Example conversion rate to EUR
    elif 'CNY' in value:
        return numeric_value * 0.16  # Example conversion rate to EUR
    elif 'KRW' in value:
        return numeric_value * 0.00067
    elif 'TRY' in value:
        return numeric_value * 0.11  # Example conversion rate to EUR
    elif 'ZAR' in value:
        return numeric_value * 0.067  # Example conversion rate to EUR
    elif 'BRL' in value:
        return numeric_value * 0.19  # Example conversion rate to EUR
    elif 'IDR' in value:
        return numeric_value * 0.000071  # Example conversion rate to EUR
    elif 'THB' in value:
        return numeric_value * 0.032  # Example conversion rate to EUR
    elif 'COP' in value:
        return numeric_value * 0.00027  # Example conversion rate to EUR
    elif 'CZK' in value:
        return numeric_value * 0.041  # Example conversion rate to EUR
    elif 'FKP' in value:
        return numeric_value * 1.35  # Example conversion rate to EUR
    elif 'BMD' in value:
        return numeric_value * 0.90  # Example conversion rate to EUR
    elif 'XCD' in value:
        return numeric_value * 0.41  # Example conversion rate to EUR
    elif 'BYN' in value:
        return numeric_value * 0.40  # Example conversion rate to EUR
    elif 'FJD' in value:
        return numeric_value * 0.49  # Example conversion rate to EUR
    elif 'MDL' in value:
        return numeric_value * 0.055  # Example conversion rate to EUR
    elif 'UAH' in value:
        return numeric_value * 0.033  # Example conversion rate to EUR
    elif 'KYD' in value:
        return numeric_value * 1.10  # Example conversion rate to EUR
    elif 'ZWL' in value:
        return numeric_value * 0.0011  # Example conversion rate to EUR
    elif 'NZD' in value:
        return numeric_value * 0.62  # Example conversion rate to EUR
    elif 'ZMW' in value:
        return numeric_value * 0.058  # Example conversion rate to EUR
    elif 'UGX' in value:
        return numeric_value * 0.00028  # Example conversion rate to EUR
    elif 'BZD' in value:
        return numeric_value * 0.50  # Example conversion rate to EUR
    elif 'TMT' in value:
        return numeric_value * 0.10  # Example conversion rate to EUR
    elif 'NPR' in value:
        return numeric_value * 0.0084  # Example conversion rate to EUR
    elif 'BDT' in value:
        return numeric_value * 0.0094  # Example conversion rate to EUR
    elif 'MMK' in value:
        return numeric_value * 0.00063  # Example conversion rate to EUR
    elif 'LAK' in value:
        return numeric_value * 0.00010  # Example conversion rate to EUR
    elif 'XOF' in value:
        return numeric_value * 0.0016  # Example conversion rate to EUR
    elif 'KRW' in value:
        return numeric_value * 0.00089  # Example conversion rate to EUR
    elif 'MYR' in value:
        return numeric_value * 0.22  # Example conversion rate to EUR
    elif 'PHP' in value:
        return numeric_value * 0.018  # Example conversion rate to EUR
    elif 'VND' in value:
        return numeric_value * 0.000043  # Example conversion rate to EUR
    elif 'EGP' in value:
        return numeric_value * 0.064  # Example conversion rate to EUR
    elif 'MAD' in value:
        return numeric_value * 0.10  # Example conversion rate to EUR
    elif 'AUD' in value:
        return numeric_value * 0.67  # Example conversion rate to EUR
    elif 'CAD' in value:
        return numeric_value * 0.74  # Example conversion rate to EUR
    elif 'JPY' in value:
        return numeric_value * 0.0069  # Example conversion rate to EUR
    elif 'KES' in value:
        return numeric_value * 0.0091  # Example conversion rate to EUR
    elif 'TZS' in value:
        return numeric_value * 0.00034
    elif 'BRL' in value:
        return numeric_value * 0.19  # Example conversion rate to EUR
    elif 'NGN' in value:
        return numeric_value * 0.0024  # Example conversion rate to EUR
    elif 'XAF' in value:
        return numeric_value * 0.0018  # Example conversion rate to EUR
    elif 'BWP' in value:
        return numeric_value * 0.091  # Example conversion rate to EUR
    elif 'NAD' in value:
        return numeric_value * 0.067  # Example conversion rate to EUR
    elif 'CLP' in value:
        return numeric_value * 0.0012  # Example conversion rate to EUR
    elif 'PEN' in value:
        return numeric_value * 0.26  # Example conversion rate to EUR
    elif 'ISK' in value:
        return numeric_value * 0.0079  # Example conversion rate to EUR
    elif 'GHS' in value:
        return numeric_value * 0.16  # Example conversion rate to EUR
    elif 'CHF' in value:
        return numeric_value * 1.10  # Example conversion rate to EUR
    elif 'MVR' in value:
        return numeric_value * 0.058  # Example conversion rate to EUR
    elif 'AUD' in value:
        return numeric_value * 0.67  # Example conversion rate to EUR
    elif 'SBD' in value:
        return numeric_value * 0.12  # Example conversion rate to EUR
    elif 'BND' in value:
        return numeric_value * 0.67  # Example conversion rate to EUR
    elif 'PGK' in value:
        return numeric_value * 0.22  # Example conversion rate to EUR
    elif 'VUV' in value:
        return numeric_value * 0.0091  # Example conversion rate to EUR
    elif 'WST' in value:
        return numeric_value * 0.40  # Example conversion rate to EUR
    elif 'TOP' in value:
        return numeric_value * 0.36  # Example conversion rate to EUR
    elif 'LKR' in value:
        return numeric_value * 0.0051  # Example conversion rate to EUR
    elif 'CRC' in value:
        return numeric_value * 0.0016  # Example conversion rate to EUR
    elif 'PYG' in value:
        return numeric_value * 0.00015  # Example conversion rate to EUR
    elif 'UYU' in value:
        return numeric_value * 0.011  # Example conversion rate to EUR
    elif 'BOB' in value:
        return numeric_value * 0.14  # Example conversion rate to EUR
    elif 'PAB' in value:
        return numeric_value * 0.90  # Example conversion rate to EUR
    elif 'KHR' in value:
        return numeric_value * 0.00022  # Example conversion rate to EUR
    elif 'HNL' in value:
        return numeric_value * 0.036  # Example conversion rate to EUR
    elif 'AMD' in value:
        return numeric_value * 0.0019  # Example conversion rate to EUR
    elif 'MKD' in value:
        return numeric_value * 0.016  # Example conversion rate to EUR
    elif 'BAM' in value:
        return numeric_value * 0.51  # Example conversion rate to EUR
    elif 'ARS' in value:
        return numeric_value * 0.0091  # Example conversion rate to EUR
    elif 'MSN' in value:
        return numeric_value * 0.0012  # Example conversion rate to EUR
    elif 'NOK' in value:
        return numeric_value * 0.094  # Example conversion rate to EUR
    elif 'AZN' in value:
        return numeric_value * 0.62  # Example conversion rate to EUR
    elif 'GEL' in value:
        return numeric_value * 0.30  # Example conversion rate to EUR
    elif 'UZS' in value:
        return numeric_value * 0.000094  # Example conversion rate to EUR
    elif 'ANG' in value:
        return numeric_value * 0.59  # Example conversion rate to EUR
    elif 'AWG' in value:
        return numeric_value * 0.59  # Example conversion rate to EUR
    elif 'BSD' in value:
        return numeric_value * 0.90  # Example conversion rate to EUR
    elif 'TTD' in value:
        return numeric_value * 0.13  # Example conversion rate to EUR
    elif 'JMD' in value:
        return numeric_value * 0.0069  # Example conversion rate to EUR
    elif 'BBD' in value:
        return numeric_value * 0.45  # Example conversion rate to EUR
    elif 'KZT' in value:
        return numeric_value * 0.0021  # Example conversion rate to EUR
    elif 'NIO' in value:
        return numeric_value * 0.028  # Example conversion rate to EUR
    elif 'GTQ' in value:
        return numeric_value * 0.11  # Example conversion rate to EUR
    elif 'DKK' in value:
        return numeric_value * 0.15  # Example conversion rate to EUR
    elif 'MXN' in value:
        return numeric_value * 0.055  # Example conversion rate to EUR
    elif 'KGS' in value:
        return numeric_value * 0.011  # Example conversion rate to EUR
    elif 'TJS' in value:
        return numeric_value * 0.090  # Example conversion rate to EUR
    elif 'MNT' in value:
        return numeric_value * 0.00035  # Example conversion rate to EUR
    elif 'SEK' in value:
        return numeric_value * 0.094  # Example conversion rate to EUR
    else:
        return np.nan