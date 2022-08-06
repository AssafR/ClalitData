import click
import pathlib
import pandas as pd
from datetime import datetime

filename_template = 'PersonList*.csv'


@click.command()
@click.option('--dirname', required=True, type=str)
@click.option('--outputfile', required=True, type=str)
def ingest_files(**kwargs):
    output_file = kwargs['outputfile']
    print(f'Reading database from file: [{output_file}]')
    previous_df = read_output_file_or_empty(output_file)

    dir_name = kwargs['dirname']
    print(f'Reading files from directory: [{dir_name}]')
    dirpath = pathlib.Path(dir_name)
    files = list(dirpath.glob(filename_template))
    combined_df = process_files(previous_df, files)
    combined_df.to_csv(output_file, encoding='utf_8_sig')


def read_output_file_or_empty(filename):
    try:
        output_df = pd.read_csv(
            filename, header=0, index_col=0, encoding='utf_8_sig',
            error_bad_lines=None)
        # output_df.loc[:, 'Time'] = pd.to_datetime(output_df['Time'])
    except Exception as e:
        output_df = pd.DataFrame()

    return output_df


def read_regular_file_to_dataframe(file):
    # Read the beginning of the file, only metadata
    df = pd.read_csv(
        str(file), sep=' ', header=None, encoding='utf_8_sig',
        error_bad_lines=None, skiprows=(lambda x: x > 5), on_bad_lines='skip')

    # Convert the two fields into one datetime
    test_time = df.iloc[2, 2]
    test_date = df.iloc[2, 3].split(',')[0]
    full_time = test_date + ' ' + test_time
    time = datetime.strptime(full_time, '%d.%m.%Y %H:%M')

    test_no = df.iloc[1, 3].split(',')[0]

    # Read the rest of the file, table of results
    df = pd.read_csv(str(file), header=4, encoding='utf_8_sig').dropna()
    df = df.drop(columns=[' '])  # Don't know why there's an extra column named " "
    df.insert(0, 'Time', time)
    df.insert(1, 'TestNo', test_no)
    df.columns = [c.strip() for c in df.columns]
    return df


def process_files(previous_df, filenames):
    dfs = [previous_df]
    for f in filenames:
        file_df = read_regular_file_to_dataframe(f)
        dfs.append(file_df)
    # Combine all to one dataframe
    df = pd.concat(dfs, ignore_index=True)

    # Convert all columns from object to string (except Time)
    for col in (set(df.columns)):
        df.loc[:, col] = df[col].convert_dtypes().astype('string').str.strip()
    df.loc[:, 'Time'] = pd.to_datetime(df['Time'])
    df = df.drop_duplicates(subset=['שם הבדיקה', 'תוצאה', 'TestNo'])
    df = (df
          .sort_values(by=['שם הבדיקה', 'Time'])
          .reset_index(drop=True)  # .drop('index', axis=1)
          )
    return df


if __name__ == "__main__":
    ingest_files()
