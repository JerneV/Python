import pandas as pd

# Another way of doing this would be to keep track of the last DateTime
# and work from that. That may be a better solution.
# Also if this ends up being used then 'newData.csv' should be
# renamed to the corresponding DateTime.


def readNewData():
    try:
        with open("lastRecord.txt", "r") as file:
            record = file.read()
    except IOError:
        file = open("lastRecord.txt", "w")
        record = 0

    data = pd.read_csv("Bra_Table1.dat", header=[0, 1], index_col=1)
    last_index = int(data.tail(1).index[0])
    print(last_index)

    if record != '':
        if int(last_index) > int(record):
            # read the new lines and make a file
            print("New data found")
            file = open("lastRecord.txt", "w")
            file.write(str(last_index))
            # WARNING: THIS DOES NOT WORK AS INTENDED! Indexes according
            # to absolute index and not the embedded one.
            new_data = data.iloc[int(record):int(last_index)]
            new_file = open("newData.csv", "w")
            new_data.to_csv("newData.csv", index=False)
        else:
            # do nothing really...
            print("No new data found")
    else:
        file = open("lastRecord.txt", "w")
        file.write(str(last_index))
        data.to_csv("newData.csv", index=False)


if __name__ == '__main__':
    readNewData()
