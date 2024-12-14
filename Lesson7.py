class IWG:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield item


if __name__ == "__main__":
    iterable = IWG([1, 2, 3, 4, 5])

    for value in iterable:
        print(value)
