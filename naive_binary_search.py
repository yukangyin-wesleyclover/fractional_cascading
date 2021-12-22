import bisect


class NaiveBinarySearch:
    def __init__(self, input_arrs):
        self.input_arrs = input_arrs
        self.arrs = input_arrs

    def find(self, query_key):
        _answers = []
        for arr in self.arrs:
            index = bisect.bisect_left(arr, query_key)
            _answers.append(arr[index])
        return _answers
