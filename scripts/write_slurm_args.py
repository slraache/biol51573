#!/usr/bin/env python3

# write_slum.py
# This script prints out the SLURM job submission script

import argparse

###------------accept and parse command line arguments
# create an argument parser object
parser=argparse.ArgumentParser(description="This script prints out the SLURM job submission script")

# add a positional argument, in this case, the name of the job
parser.add_argument("job_name", help="Name of the job")

# add a positional argument, in this case, the number of hours
parser.add_argument("number_of_hours", help="Number of hours")

# add a positional argument, in this case, the queue name
parser.add_argument("queue_name", help="Name of the queue")

# add a positional argument, in this case, your email
parser.add_argument("email", help="Your email")

# parse the arguments
args = parser.parse_args()


print("#!/bin/bash")
print(f"#SBATCH --job_name=" + args.job_name)
print(f"#SBATCH --time=" + args.number_of_hours)
print(f"#SBATCH -p =" + args.queue_name)
print(f"#SBATCH -N 1")
print("#SBATCH -n 1")
print("#SBATCH -c 1")
print("#SBATCH --qos=cloud")
print(f"#SBATCH --mail_user=" + args.email)
print("#SBATCH --mail_type=END, FAIL")

print("")
print("echo Job started on $(03/30/2026)")
print("")
print("load modules on here")
print("")
print("echo Job finished on $(03/30/2026)")