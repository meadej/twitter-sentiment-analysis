"""
A utility to assist in logging data
"""
import datetime as dt

def generateTimestamp():
    currtime = dt.datetime.now()
    minute = str(currtime.minute)
    hour = str(currtime.hour)
    if currtime.minute < 10:
        minute = "0" + str(currtime.minute)
    if currtime.hour < 10:
        hour = "0" + str(currtime.hour)

    datestr = str(currtime.day) + "/" + str(currtime.month) + "/" + str(currtime.year)
    timestr = hour + ":" + minute
    return "[" + datestr + " " + timestr + "]"

def logData(data, filename):
    fhandle = open(filename, "a")
    fhandle.write(generateTimestamp() + " " + data + "\n")
    fhandle.close()
    return 0

def printData(data):
    print(generateTimestamp() + " " + data)
    return 0

def convertToCSV(input_file):
    """
    Takes a log file created by the logData method and converts it to a .csv format
    :param input_file: The log file to convert
    :return: The name of the output CSV file
    """
    output_file = input_file.split(".")[0] + ".csv"

    inhandle = open(input_file, 'r')
    input = inhandle.readlines()

    outhandle = open(output_file, 'w+')
    outhandle.close()
    outhandle = open(output_file, 'a')
    for line in input[:-1]:
        line = line.strip()
        line_arr = line.split(" ")
        outhandle.write(line_arr[1].strip(']') + "," + line_arr[2].strip('%P') + "," + line_arr[3].strip("%N") + "\n")
    line_arr = input[len(input) - 1].strip().split(" ")
    outhandle.write(line_arr[1].strip(']') + "," + line_arr[2].strip('%P') + "," + line_arr[3].strip("%N"))


    inhandle.close()
    outhandle.close()
    return output_file