import pytest

from src.string_concat_benchmark import StringConcatBenchmark


string_list_sizes = [10**3, 10**5, 10**6]


@pytest.mark.parametrize("size", string_list_sizes)
def test_string_concat_with_plus(benchmark, size):
    strings = ["a" * 10] * size  # Генерируем список строк
    benchmark(StringConcatBenchmark.concat_with_plus, strings)


@pytest.mark.parametrize("size", string_list_sizes)
def test_string_concat_with_join(benchmark, size):
    strings = ["a" * 10] * size  # Генерируем список строк
    benchmark(StringConcatBenchmark.concat_with_join, strings)
