class SentimentData:
    """
    A class which reads in and stores data from files containing information about
    aspects of certain words, specifically their valence (pleasure) and arousal (intensity)
    Current data coming from https://link.springer.com/article/10.3758%2Fs13428-012-0314-x#Notes
    """
    def __init__(self, _filename):
        self.filename = _filename
        self.data_dict = None
        self.word_list = None

    def readLineData(self, _filename = None):

        """
        Reads sentiment data line-by-line from a .csv file
        :param _filename: The name of the file to read data from
        :return: A two-dimensional array containing arrays for each line in the file, seperated by commas
        """
        if _filename == None:
            _filename = self.filename
        data_arr = []
        data_file = open(_filename, 'r+')
        for line in data_file:
            arr = line.split(',')
            data_arr.append(arr)
        return data_arr

    def restructureData(self, data_arr):
        """
        Takes in a two-dimensional array of words returned by readLineData and restructures it in a more usable
        format.
        :param data_arr: Two-dimensional array of words we want to use to measure overall sentiment of a tweet.
        :return: A dictionary of dictionaries. Structured as word : {number, valence_mean, valence_deviation, arousal_mean,
        arousal_deviation}
        """
        ret_dict = {}
        for word_arr in data_arr:
            data_dict = {}
            word = word_arr[1]
            data_dict['number'] = word_arr[0]
            data_dict['valence_mean'] = word_arr[2]
            data_dict['valence_deviation'] = word_arr[3]
            data_dict['arousal_mean'] = word_arr[5]
            data_dict['arousal_deviation'] = word_arr[6]
            ret_dict[word] = data_dict
        return ret_dict

    def getWordList(self, data_dict = None):
        """
        Gets a list of words being used from an array
        :param data_dict: A dict of dicts from restructureData containing information about words being used in
        analysis.
        :return: An array of words
        """

        if data_dict == None:
            data_dict = self.data_dict
        ret_data = []
        for word in data_dict:
            ret_data.append(word)
        return ret_data

    def getSentimentData(self, _filename = None):
        if _filename == None:
            _filename = self.filename
        else:
            self.filename = _filename
        raw_data = self.readLineData(_filename)
        struct_data = self.restructureData(raw_data)

        self.data_dict = struct_data
        self.word_list = self.getWordList(self.data_dict)
        return self

    def containsEntry(self, entry):
        if (self.word_list == None):
            return False
        return entry.lower() in self.word_list

    def getEntry(self, entry):
        if not self.containsEntry(entry):
            return None
        else:
            return self.data_dict[entry]
