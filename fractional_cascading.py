import bisect
from fractional_cascading_node import FractionalCascadingNode

INT_MIN, INT_MAX = -2147483648, 2147483647


class FractionalCascading:
    def __init__(self, input_arrs):
        self.input_arrs = input_arrs
        self.arrs = []
        self.h = len(input_arrs)  # number of sorted arrays
        self.n = len(input_arrs[0])  # number of elements in each sorted arrays

    def _merge(self, arr1, arr2):
        p1, p2 = 0, 0
        _answer = []

        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1].value <= arr2[p2].value:
                _answer.append(FractionalCascadingNode(arr1[p1].value, -1, -1))
                p1 += 1
            else:
                _answer.append(FractionalCascadingNode(arr2[p2].value, -1, -1))
                p2 += 1
        _answer += arr1[p1:] + arr2[p2:]
        return _answer

    def merge_input_arrs(self):
        self.arrs.insert(
            0, [FractionalCascadingNode(value, -1, -1) for value in self.input_arrs[-1]]
        )
        for i in range(self.h - 2, -1, -1):
            self.arrs.insert(
                0,
                self._merge(
                    [
                        FractionalCascadingNode(node.value, -1, -1)
                        for j, node in enumerate(self.arrs[0])
                        if j % 2
                    ],
                    list(
                        map(
                            lambda value: FractionalCascadingNode(value, -1, -1),
                            self.input_arrs[i],
                        )
                    ),
                ),
            )
        for arr in self.arrs:
            arr.insert(0, FractionalCascadingNode(INT_MIN, -1, -1))
            arr.append(FractionalCascadingNode(INT_MAX, -1, -1))

    def calculate_pointers(self):
        for i, arr in enumerate(self.arrs):
            for j, node in enumerate(arr):
                node.right = bisect.bisect_left(self.input_arrs[i], node.value)
                node.down = (
                    0
                    if i == len(self.arrs) - 1
                    else bisect.bisect_left(
                        list(map(lambda node: node.value, self.arrs[i + 1])), node.value
                    )
                )

    def find(self, query_key):
        index = bisect.bisect_left(
            list(map(lambda node: node.value, self.arrs[0])), query_key
        )
        right = self.arrs[0][index].right

        _answers = []
        _answers.append(self.input_arrs[0][right])  # first value

        down = self.arrs[0][index].down
        for i in range(1, len(self.arrs)):
            if self.arrs[i][down - 1].value >= query_key:
                # back
                right = self.arrs[i][down - 1].right
                down = self.arrs[i][down - 1].down
            else:
                right = self.arrs[i][down].right
                down = self.arrs[i][down].down
            _answers.append(self.input_arrs[i][right])  # value

        return _answers
