from django import forms

CURRENCY = (
    ('USD', 'USD'),
    ('RUB', 'RUB'),
    ('TRY', 'TRY'),
    ('EUR', 'EUR'),
    ('CHF', 'CHF'),
    ('GBP', 'GBP'),
    ('JPY', 'JPY'),
    ('UAH', 'UAH'),
    ('KZT', 'KZT'),
    ('BYN', 'BYN'),
    ('CNY', 'CNY'),
    ('PLN', 'PLN'),
)


class CurrencyPair(forms.Form):
    currency_count = forms.DecimalField(min_value=0.1)
    from_currency = forms.ChoiceField(choices=CURRENCY)
    to_currency = forms.ChoiceField(choices=CURRENCY)

