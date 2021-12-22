class IteratedSearchNode:
    def __init__(self, value, origin, pointers):
        self.value = value
        self.origin = origin  # which input array is this node from
        self.pointers = pointers

    def __str__(self):
        return "value={value} origin={origin} pointers={pointers}".format(
            value=self.value, origin=self.origin, pointers=self.pointers
        )
