import pickle
import json
import msgpack
import random
import string

class SerializationBenchmark:
    def __init__(self, size_kb: int):
        self.data = self.generate_data(size_kb)

    @staticmethod
    def generate_data(size_kb: int):
        size_bytes = size_kb * 1024
        return ''.join(random.choices(string.ascii_letters + string.digits, k=size_bytes))

    @staticmethod
    def serialize_pickle(data):
        return pickle.dumps(data)

    @staticmethod
    def deserialize_pickle(serialized_data):
        return pickle.loads(serialized_data)

    @staticmethod
    def serialize_json(data):
        return json.dumps(data)

    @staticmethod
    def deserialize_json(serialized_data):
        return json.loads(serialized_data)

    @staticmethod
    def serialize_msgpack(data):
        return msgpack.packb(data)

    @staticmethod
    def deserialize_msgpack(serialized_data):
        return msgpack.unpackb(serialized_data)
