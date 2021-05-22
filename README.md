The project files are inside the 'files' folder.  
We will explain what each file and folder contains.

- 'charles' folder contains the python files with the selection, crossover, and mutation methods. It also includes the implementation of Individual and Population in the 'charles.py' file;

- 'sudoky.py' is the python file where we experimented whith different combinations of selection, crossover, and mutation methods. Each combination has 35 runs of 150 generations. The fitness values of each generation of each run of each combination are stored in a csv file in the 'logs' folder. The name of each file is the combination of used methods;

- 'param_finetune.py' is the python file where we experimented with different values for the crossover and mutation probabilities on the two best algorithms retrieved by 'sudoky.py'. Again, each probabilities combination has 35 runs of 150 generations. The fitness values of each generation of each run of each combination are stored in a csv file in the 'finetune' folder. The name of each file is the combination of probabilities and reference to which of the two best algorithms was used;

- 'increase_decrease.py' is the python file where we experimented with decreasing the crossover probability and increasing the mutation probability over generations. We applied this to 35 runs of 150 generations. The fitness values are stored in a csv file in the 'inc_dec' folder;

- 'Statistical_analysis.ipynb' is the jupyter notebook where we did the statistical analysis of the fitness values in the 'logs', 'finetune', and 'inc_dec' folders to select the best algorithm;

- 'attempts.py' is the python file where we applied the best algorithm founded in 'Statistical_analysis.ipynb' to three sudoku problems with different levels of difficulty (easy, medium, and hard). The fitness values were stored in csv files in the 'attempts' folder. Also in this folder, there are csv files containing the representation of the best individual in each run of each level of difficulty. The 'Display_attempts.ipynb' is the jupyter notebook where we show the individual with the best fitness value among all runs of each level of difficulty in a regular sudoky 9x9 grid.
