#!/usr/bin/python3
import sys
import os

### Author: Bilal Sharif

# checking if both input and ouput file is provided
if len(sys.argv) != 3:
    sys.exit(f"EUsage: {os.path.basename(sys.argv[0])} <probes_file> <probes_output>\n\n")

probes_file = sys.argv[1]
probes_output = sys.argv[2]


print(f"\tFiltering probe sequences for file...............{probes_file}\n\n", flush=True)
with open(probes_file, 'r') as f1, open(probes_output, 'w') as f2:
    for line in f1:
        if not line.startswith(">"):
            sys.exit(f"Error: The file {probes_file} is not in fasta format. Please provide a fasta file. the proble name should start with '>'. Exiting...")
        probe_name = line.strip()
        probe_seq = f1.readline().strip()
        probe_GC = (probe_seq.count("G") + probe_seq.count("C")) / len(probe_seq)
        if probe_GC > 0.4 and probe_GC < 0.6:
            f2.write(f"{probe_name}\n{probe_seq}\n")
        else:
            print(f"\t\tExcluding the {probe_name} probe with GC content of {probe_GC}", flush=True)
print(f"\n\n\tProbes with GC content between 0.4 and 0.6 have been written to {probes_output}\n\n", flush=True)

