import pandas as pd
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

INPUT_FILE = "/Users/vinodkumarreddy/Desktop/cs-202/cs202-lab/outputs/diff_analysis.csv"
OUTPUT_FILE = "/Users/vinodkumarreddy/Desktop/cs-202/ass3/structural_metrics_sample100.csv"

# Load dataset
data = pd.read_csv(INPUT_FILE)
data.columns = data.columns.str.strip()
data = data.head(100)  # first 100 rows only


def extract_metrics(record):
    def safe_eval(code_snippet):
        if not isinstance(code_snippet, str) or code_snippet.strip() == "":
            return 0, 0, 0
        try:
            mi_val = mi_visit(code_snippet, True)
            cc_val = sum(obj.complexity for obj in cc_visit(code_snippet))
            loc_val = len(code_snippet.splitlines())
        except Exception:
            mi_val, cc_val, loc_val = 0, 0, 0
        return mi_val, cc_val, loc_val

    mi_before, cc_before, loc_before = safe_eval(record["Source Code (before)"])
    mi_after, cc_after, loc_after = safe_eval(record["Source Code (current)"])
    return mi_before, mi_after, cc_before, cc_after, loc_before, loc_after


if __name__ == "__main__":
    results = []
    with Pool(cpu_count()) as workers:
        for outcome in tqdm(workers.imap(extract_metrics, [row for _, row in data.iterrows()]),
                            total=len(data), desc="Analyzing Structural Metrics"):
            results.append(outcome)

    # Unpack results into dataframe
    (data["MI_Before"], data["MI_After"],
     data["CC_Before"], data["CC_After"],
     data["LOC_Before"], data["LOC_After"]) = zip(*results)

    # Calculate differences
    data["MI_Change"] = data["MI_After"] - data["MI_Before"]
    data["CC_Change"] = data["CC_After"] - data["CC_Before"]
    data["LOC_Change"] = data["LOC_After"] - data["LOC_Before"]

    # Save output
    data.to_csv(OUTPUT_FILE, index=False)
    print(f"Structural metrics (first 100 rows) saved to: {OUTPUT_FILE}")

