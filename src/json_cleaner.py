import json
from pathlib import Path


def clear_benchmarks() -> dict:
    file_path = Path(__file__).parent.parent / 'benchmark_results.json'
    with open(file_path, "r") as f:
        data = json.load(f)

    filtered_benchmarks = []
    for benchmark in data["benchmarks"]:
        filtered_benchmarks.append(
            {
                "name": benchmark["name"],
                "min": benchmark["stats"]["min"],
                "max": benchmark["stats"]["max"],
                "mean": benchmark["stats"]["mean"],
            }
        )

    filtered_data = {"benchmarks": filtered_benchmarks}

    return filtered_data
