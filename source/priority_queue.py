from point import Point


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item):
        self.elements.append(item)
        self.elements = sorted(self.elements, key=lambda x: x[0], reverse=True)

    def get(self) -> Point:
        return self.elements.pop(0)[1]