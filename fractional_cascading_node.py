class FractionalCascadingNode:
    def __init__(self, value, right, down):
        self.value = value
        self.right = right  # right pointer index
        self.down = down  # down pointer index

    def __str__(self):
        return "value={value} right={right} down={down}".format(
            value=self.value, right=self.right, down=self.down
        )
