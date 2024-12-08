class StringConcatBenchmark:
    @staticmethod
    def concat_with_plus(strings) -> str:
        result = ""
        for s in strings:
            result += s
        return result

    @staticmethod
    def concat_with_join(strings) -> str:
        return "".join(strings)
