class StringConcatBenchmark:
    @staticmethod
    def concat_with_plus(strings):
        result = ""
        for s in strings:
            result += s
        return result

    @staticmethod
    def concat_with_join(strings):
        return "".join(strings)
