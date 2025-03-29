#!/bin/bash
#SBATCH --job-name=swAgent
#SBATCH --output=swAgent
#SBATCH --gres=gpu:2


python homework1/ideaGenerate_agent.py