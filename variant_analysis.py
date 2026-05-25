import pandas as pd
import matplotlib.pyplot as plt

# Load VCF data
vcf = pd.read_csv(
    "filtered_variants.vcf",
    comment='#',
    sep='\t',
    header=None
)

# Assign column names
vcf.columns = [
    "CHROM",
    "POS",
    "ID",
    "REF",
    "ALT",
    "QUAL",
    "FILTER",
    "INFO"
]

# Variant classification
vcf["Variant_Type"] = vcf.apply(
    lambda x: "SNP"
    if len(x["REF"]) == 1 and len(x["ALT"]) == 1
    else "INDEL",
    axis=1
)

# Visualization
vcf["Variant_Type"].value_counts().plot(kind="bar")

plt.title("Variant Type Distribution")
plt.xlabel("Variant Type")
plt.ylabel("Count")

plt.savefig("variant_distribution.png")

# Export report
vcf.to_csv("variant_report.csv", index=False)

print("Variant analysis completed successfully.")
