import pandas as pd

# ----------------------------
# CONFIG
# ----------------------------
INPUT_CSV = "/Users/vinodkumarreddy/Desktop/cs-202/ass3/classification_results.csv"  # Output from part (e)
OUTPUT_CSV = "/Users/vinodkumarreddy/Desktop/cs-202/ass3/lab3_final_table.csv"

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv(INPUT_CSV)
df.columns = df.columns.str.strip()

# ----------------------------
# FINAL TABLE STRUCTURE
# ----------------------------
final_columns = [
    "Hash",
    "Message",
    "Filename",
    "MI_Change",
    "CC_Change",
    "LOC_Change",
    "Semantic_Similarity",
    "Token_Similarity",
    "Semantic_class",
    "Token_class",
    "Classes_Agree"
]

# Keep only existing columns (safety check)
final_columns = [col for col in final_columns if col in df.columns]

final_df = df[final_columns]

# Save final table
final_df.to_csv(OUTPUT_CSV, index=False)
print(f"Final table saved to '{OUTPUT_CSV}'.")

