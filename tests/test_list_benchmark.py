import pytest

from src.list_benchmark import ListCreationBenchmark


list_sizes = [10**3, 10**5, 10**6]


@pytest.mark.parametrize("size", list_sizes)
def test_list_creation_comprehension(benchmark, size):
    benchmark(ListCreationBenchmark.list_comprehension, size)

@pytest.mark.parametrize("size", list_sizes)
def test_list_creation_for_loop(benchmark, size):
    benchmark(ListCreationBenchmark.for_loop, size)

@pytest.mark.parametrize("size", list_sizes)
def test_list_creation_numpy(benchmark, size):
    benchmark(ListCreationBenchmark.numpy_array, size)
