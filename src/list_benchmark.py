import numpy as np

class ListCreationBenchmark:
    @staticmethod
    def list_comprehension(size: int):
        return [i for i in range(size)]

    @staticmethod
    def for_loop(size: int):
        result = []
        for i in range(size):
            result.append(i)
        return result

    @staticmethod
    def numpy_array(size: int):
        return np.arange(size).tolist()
