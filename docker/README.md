# Complete docker setup to speed up experimentation

## Build image
```
docker build -t niching -f docker/Dockerfile .
```


## Run experiments
```
cd docker
bash run_experiment.sh <num_runs> <experiment_name> <algo> '<parameters>'
```
* num_runs: Number of runs (competition default is 50)
* experiment_name: Will be the name of the output folder and analysis. Should be unique
* algo: The name of the script that will execute the algorithm.
	* random_search
* parameters: passed to the algorithm directly, which are available depend on the algorithm. See algorithm readmes


Example:
```
bash run_experiment.sh 2 test random_search '--budget_multiplier 0.01'
```
