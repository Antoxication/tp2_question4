class Math:
    def add(self, *args):
        return sum(args)

def test_overloading():
    math = Math()
    return [math.add(1, 2), math.add(1, 2, 3)]
