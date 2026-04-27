# write_slum.py
# This script prints out the SLURM job submission script

job_name = "blast_job"
number_of_hours = 2
queue_name = "cloud72"
email = "slraache@uark.edu"

print("#!/bin/bash")
print(f"#SBATCH --job_name={job_name}")
print(f"#SBATCH --time={number_of_hours}:00:00")
print(f"#SBATCH -p {queue_name}")
print(f"#SBATCH -N 1")
print("#SBATCH -n 1")
print("#SBATCH -c 1")
print("#SBATCH --qos=cloud")
print(f"#SBATCH --mail_user={email}")
print("#SBATCH --mail_type=END, FAIL")

print("")
print("echo Job started on $(03/16/2026)")
print("")
print("load modules on here")
print("")
print("echo Job finished on $(03/16/2026)")