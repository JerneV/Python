# This script needs to periodically check all files in the 'pool' folder
# Data neesd to go the correct folder
# Configs of new masts need to be standardized and catalogued

import glob
import yaml
import ntpath


def getDataExtensions(dir):
    """
    Dynamically gets all file extensions of the raw data
    """
    data_extensions = set()
    with open(r'C:\Users\jvi\Desktop\Gitlab\SQ Windcampaigns\dataloggers\allLoggers.yml', 'r') as file:
        data = yaml.safe_load(file)
    for logger in data:
        header = data[logger]['format']['header']
        raw = data[logger]['format']['raw']
        if header is not None:
            data_extensions.add(header)
        if raw is not None:
            data_extensions.add(raw)
    return list(data_extensions)


def checkForNewFile(dir):
    config_files = glob.glob(dir + "/*.yml", recursive = False)
    if config_files:
        parseConfigs(config_files)
    else:
        print("No new config files found!")

    data_files = []
    for ext in getDataExtensions(dir):
        files = glob.glob(dir + "\\" + "*" + ext)
        if files:
            data_files += files
    if data_files:
        parseData(data_files)
    else:
        print("No new data files found!")


def parseConfigs(fileList):
    """
    Gets a list of files from checkForNewFile() and will parse each one of them
    """
    print(fileList)


def parseData(fileList):
    """
    Checks each data file and puts it in the right place
    """
    file_names = [path_leaf(path) for path in fileList]
    site_names = siteList()
    for files in file_names:
        try:
            siteName, date, tail =  files.split('-')
            logger, extension = tail.split('.')
            if siteName in site_names:
                print(f"Sitename is {siteName}, the date of the data is {date} and the logger is {logger}.")
            else:
                print(f"That site ({siteName}) does not exist yet. First configure it.")
        except:
            print(f"The data file {files} hasn't been named correctly.")


def siteList():
    with open(r'C:\Users\jvi\Desktop\Gitlab\SQ Windcampaigns\dataloggers\plants.yml', 'r') as file:
        plants = yaml.safe_load(file)
    names = set()
    for plant in plants:
        name = plants[plant]['name']
        if name is not None:
            names.add(name)
    #print(f"The list with names is {names}")
    return names


def path_leaf(path):
    # gets file name on all OSs
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


if __name__ == '__main__':
    checkForNewFile(r"C:\Users\jvi\Desktop\Gitlab\pool")
    #doesSiteExist("hello")
