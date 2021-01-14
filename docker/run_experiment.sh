#!/bin/bash
#1: num_runs
#2: experiment_name
#3: algo
#4: parameters

for i in $(seq 1 $1)
do
    docker run --name $2-$3-$i -d -v $PWD/../python3/algorithms:/run/algorithms -v $PWD/../competition-analysis/submissions/:/analysis/submissions niching:latest bash -c "cd /run;
    python -u $3.py $4;ls -lt data"
done
