"""
combine multiple excel file
"""

import pandas, os


def read_excel_file(path_file, sheet):
    """
    read a single excel file
    :param path_file:
    :param sheet:
    :return:
    """
    return pandas.read_excel(open(path_file, 'rb'), sheetname=sheet, header=None, skiprows=1, verbose=True)


def combine_excel_in_dir(path_directory, sheet='disease'):
    """

    :param path_directory:
    :param sheet
    :return:
    """
    files = os.listdir(path_directory)
    path_files = [''.join((path_directory, f)) for f in files]
    result = [read_excel_file(path_file, sheet=sheet) for path_file in path_files]
    result = pandas.concat(result)
    return result


def write_csv(dataframe, path_csv, col):
    """

    :param path_csv:
    :param dataframe
    :param col:
    :return: None
    """
    dataframe.to_csv(path_csv, columns=col, encoding='utf-8', header=False, index=False)


##################################################
##################################################
##################################################
# training directory
path_dir = "../../data/training/vector-borne-label/"

res = combine_excel_in_dir(path_dir)
# add column names
res.columns = ["tweets", "sentiment", "theme"]

# read first n rows
n = 5
#print(res.head(n))

# change column value
# "Relevant: experiences and opinions of e-cig" --> R
# "News: news, policy and government themes" --> N
# "Advertisement: marketing messages"  --> A
# "Irrelevant: not about e-cig"  --> I
# "neutral: no emotions are implied"  --> "0"
# "positive: happiness, enthusiasm and kindness etc." --> "1"
# "negative: sadness, hate, violence, discrimination etc." --> "-1"
res = res.replace(["Relevant: disease symptoms, e.g., fever, diarrhea, …… ", "News: news, policy and government themes", "Advertisement: marketing messages", "Irrelevant: not a symptom", "neutral: no emotions are implied", "positive: happiness, enthusiasm and kindness etc.", "negative: sadness, hate, violence, discrimination etc."], ["R", "N", "A", "I", "0", "1", "-1"])

#print(res.head(n))

# print result to csv file --> input file for classification
path_sentiment = "../../data/training/pima_training_sentiment.csv"
columns_sentiment=["sentiment", "tweets"]
write_csv(res, path_sentiment, columns_sentiment)

path_theme = "../../data/training/pima_training_theme.csv"
columns_theme = ["theme", "tweets"]
write_csv(res, path_theme, columns_theme)



