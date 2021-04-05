import glob  # used to grab dump files
import credentials  # pass in personal information from different file

for file in glob.glob('*.txt'):  # group dump files together
    with open(file) as f:  # read from files
        for line in f:  # read by line
            if credentials.my_number in line:  # find if personal information in dump
                print(line)