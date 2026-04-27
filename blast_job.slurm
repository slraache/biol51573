#!/bin/bash
#SBATCH --job_name=blast_job
#SBATCH --time=2:00:00
#SBATCH -p cloud72
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --qos=cloud
#SBATCH --mail_user=slraache@uark.edu
#SBATCH --mail_type=END, FAIL

echo Job started on $(03/16/2026)

module load blast 
blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn

echo Job finished on $(03/16/2026)
