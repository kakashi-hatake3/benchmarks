import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:.4f}'.format)


def json_to_table(json_data) -> pd.DataFrame:
    df = pd.DataFrame(json_data['benchmarks'])

    df[['test_name', 'parameter']] = df['name'].str.extract(r'(\w+)\[(\d+)\]')

    df = df[['test_name', 'parameter', 'min', 'max', 'mean']]

    df['parameter'] = df['parameter'].astype(int)
    df['min'] = df['min'].astype(float)
    df['max'] = df['max'].astype(float)
    df['mean'] = df['mean'].astype(float)

    return df
