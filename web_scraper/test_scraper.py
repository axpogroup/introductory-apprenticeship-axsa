import pandas as pd

def parse_price(value):
    if pd.isna(value):
        return None
    if str(value) == 'Free':
        return 0.0
    try:
        s = str(value).replace(',', '.')
        s = ''.join(ch for ch in s if ch.isdigit() or ch == '.')
        return float(s) if s else None
    except Exception:
        return None


def test_parse_price():
    assert parse_price('Free') == 0.0
    assert parse_price('CHF 26.73') == 26.73
    assert parse_price(None) is None


def test_deduplication():
    df = pd.DataFrame([
        {'name': 'Counter-Strike 2', 'release_date': '21 Aug, 2012'},
        {'name': 'Counter-Strike 2', 'release_date': '21 Aug, 2012'},
    ])
    df_unique = df.drop_duplicates(subset=['name', 'release_date'])
    assert len(df_unique) == 1