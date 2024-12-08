import pickle
import json
import msgpack
import random
import string


class SerializationBenchmark:
    def __init__(self, size_kb: int):
        self.data = self.generate_data(size_kb)

    @staticmethod
    def generate_data(size_kb: int) -> str:
        size_bytes = size_kb * 1024
        return "".join(
            random.choices(string.ascii_letters + string.digits, k=size_bytes)
        )

    @staticmethod
    def serialize_pickle(data) -> bytes:
        return pickle.dumps(data)

    @staticmethod
    def deserialize_pickle(serialized_data) -> object:
        return pickle.loads(serialized_data)

    @staticmethod
    def serialize_json(data) -> str:
        return json.dumps(data)

    @staticmethod
    def deserialize_json(serialized_data) -> object:
        return json.loads(serialized_data)

    @staticmethod
    def serialize_msgpack(data) -> bytes:
        return msgpack.packb(data)

    @staticmethod
    def deserialize_msgpack(serialized_data) -> object:
        return msgpack.unpackb(serialized_data)
