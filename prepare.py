"""Data prepare using pandas."""

import glob

import pandas as pd


def aggregate_csv(files, csv_cols, destnation=''):
    """Merge seperated csv files into one pandas dataframe."""
    print(files)
    total_files = len(files)
    print("Total old news files: {}".format(total_files))

    main_df = pd.DataFrame
    for f in files:
        df = pd.read_csv(f)
        df = df[csv_cols]
        main_df.append(df, ignore_index=True)

    main_df.to_csv(destnation)
    return


def aggregate_data(path, extention='*.csv', csv_cols=None, destnation=''):
    """Main interface for aggregating data."""
    files = glob.glob(path + extention)
    if extention == '*.csv':
        aggregate_csv(files, csv_cols, destnation)
    return
