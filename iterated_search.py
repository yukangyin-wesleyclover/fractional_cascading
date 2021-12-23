from iterated_search_node import IteratedSearchNode
import bisect

INT_MAX = 2147483647


class IteratedSearch:
    def __init__(self, input_arrs):
        self.input_arrs = input_arrs
        self.arrs = []
        self.merged_arrs = []
        self.values_in_merged_arrs = []
        self.h = len(input_arrs)  # number of sorted arrays
        self.n = len(input_arrs[0])  # number of elements in each sorted arrays

        # initialize pointers arrays
        for i, arr in enumerate(input_arrs):
            self.arrs.append([])
            for value in arr:
                self.arrs[i].append(IteratedSearchNode(value, i, [INT_MAX] * self.h))

    def _merge(self, arr1, arr2):
        p1, p2 = 0, 0
        _answer = []

        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1].value <= arr2[p2].value:
                _answer.append(
                    IteratedSearchNode(
                        arr1[p1].value, arr1[p1].origin, arr1[p1].pointers
                    )
                )
                p1 += 1
            else:
                _answer.append(
                    IteratedSearchNode(
                        arr2[p2].value, arr2[p2].origin, arr2[p2].pointers
                    )
                )
                p2 += 1
        _answer += arr1[p1:] + arr2[p2:]
        return _answer

    def calculate_pointers(self):
        auxiliary_array = [INT_MAX] * self.h

        for i in range(self.n * self.h - 1, -1, -1):
            auxiliary_array = auxiliary_array.copy()
            auxiliary_array[self.merged_arrs[i].origin] = self.merged_arrs[i].value
            self.merged_arrs[i].pointers = auxiliary_array

    def merge_input_arrs(self):
        self.merged_arrs = self.arrs.copy()
        while len(self.merged_arrs) > 1:
            _temp_merged_arrs = []
            for index in range(0, len(self.merged_arrs), 2):
                result = (
                    self.merged_arrs[index]
                    if index + 1 == len(self.merged_arrs)
                    else self._merge(
                        self.merged_arrs[index], self.merged_arrs[index + 1]
                    )
                )
                _temp_merged_arrs.append(result)
            self.merged_arrs = _temp_merged_arrs
        self.merged_arrs = self.merged_arrs[0]

        # map node in merged_arrs to pure numbers
        self.values_in_merged_arrs = list(
            map(lambda node: node.value, self.merged_arrs)
        )

    def find(self, query_key):
        # locate query key
        index = bisect.bisect_left(self.values_in_merged_arrs, query_key)

        # directly read off the answers
        return self.merged_arrs[index].pointers
