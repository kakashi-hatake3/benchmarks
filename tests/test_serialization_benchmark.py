import pytest

from src.serialization_benchmark import SerializationBenchmark


data_sizes_kb = [1, 1024, 10240]


@pytest.mark.parametrize("size_kb", data_sizes_kb)
def test_serialize_pickle(benchmark, size_kb):
    sb = SerializationBenchmark(size_kb)
    benchmark(SerializationBenchmark.serialize_pickle, sb.data)

@pytest.mark.parametrize("size_kb", data_sizes_kb)
def test_deserialize_pickle(benchmark, size_kb):
    sb = SerializationBenchmark(size_kb)
    serialized_data = SerializationBenchmark.serialize_pickle(sb.data)
    benchmark(SerializationBenchmark.deserialize_pickle, serialized_data)

@pytest.mark.parametrize("size_kb", data_sizes_kb)
def test_serialize_json(benchmark, size_kb):
    sb = SerializationBenchmark(size_kb)
    benchmark(SerializationBenchmark.serialize_json, sb.data)

@pytest.mark.parametrize("size_kb", data_sizes_kb)
def test_deserialize_json(benchmark, size_kb):
    sb = SerializationBenchmark(size_kb)
    serialized_data = SerializationBenchmark.serialize_json(sb.data)
    benchmark(SerializationBenchmark.deserialize_json, serialized_data)

@pytest.mark.parametrize("size_kb", data_sizes_kb)
def test_serialize_msgpack(benchmark, size_kb):
    sb = SerializationBenchmark(size_kb)
    benchmark(SerializationBenchmark.serialize_msgpack, sb.data.encode())

@pytest.mark.parametrize("size_kb", data_sizes_kb)
def test_deserialize_msgpack(benchmark, size_kb):
    sb = SerializationBenchmark(size_kb)
    serialized_data = SerializationBenchmark.serialize_msgpack(sb.data.encode())
    benchmark(SerializationBenchmark.deserialize_msgpack, serialized_data)