#!/bin/bash

echo "Starting NGS Variant Calling Pipeline"

# Install bioinformatics tools
apt-get install -y bwa samtools bcftools

# Index reference genome
bwa index chr22.fa

# Align sequencing reads
bwa mem chr22.fa sample_trimmed.fastq > aligned.sam

# Convert SAM to BAM
samtools view -Sb aligned.sam > aligned.bam

# Sort BAM file
samtools sort aligned.bam -o aligned_sorted.bam

# Index BAM file
samtools index aligned_sorted.bam

# Variant Calling
bcftools call -mv raw_variants.vcf -Ov -o variants.vcf

echo "Pipeline Completed Successfully"
