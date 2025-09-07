import pandas as pd

# Path to Lab 2 dataset
CSV_PATH = "/Users/vinodkumarreddy/Desktop/cs-202/cs202-lab/outputs/diff_analysis.csv"

# Load dataset
bugfix_df = pd.read_csv(CSV_PATH)
bugfix_df.columns = bugfix_df.columns.str.strip()  # Clean column names

# ---------------- Baseline Statistics ----------------
num_commits = bugfix_df["Hash"].nunique()  # Total unique commits
num_files = bugfix_df["Filename"].nunique()  # Total unique files
avg_files_per_commit = bugfix_df.groupby("Hash")["Filename"].nunique().mean()  # Average files per commit

llm_fix_distribution = bugfix_df["LLM Inference (fix type)"].value_counts()  # Distribution of LLM fix types
top_files = bugfix_df["Filename"].value_counts().head(10)  # Top 10 modified files

# Extract file extensions and count top 10
bugfix_df["File_Extension"] = bugfix_df["Filename"].str.split(".").str[-1]
top_extensions = bugfix_df["File_Extension"].value_counts().head(10)

# ---------------- Report ----------------
print("=== Baseline Descriptive Statistics ===")
print(f"Total commits: {num_commits}")
print(f"Total files: {num_files}")
print(f"Average modified files per commit: {avg_files_per_commit:.2f}\n")

print("Distribution of LLM fix types:")
print(llm_fix_distribution, "\n")

print("Top 10 most frequently modified files:")
print(top_files, "\n")

print("Top 10 most frequently modified file extensions:")
print(top_extensions)

