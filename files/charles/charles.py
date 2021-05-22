from random import shuffle, choice, sample, random
from operator import  attrgetter
from copy import deepcopy
import csv
from pathlib import Path


class Individual:
    def __init__(
        self,
        representation=None,
        size=81,
        valid_set=[i for i in range(1,10)],
        fixed_vals=None
        ):   

        self.fixed_vals = fixed_vals
        self.size = size

        if representation is None:
            self.representation = self.get_representation()
        else:
            self.representation = representation
        
        self.fitness = self.evaluate()


    def get_representation(self):
        # Create list to store the available values to fill the sudoku
        bag_of_vals = [i for i in range(1,10) for j in range(9)]
        
        # Remove fixed values from the list
        for i in self.fixed_vals.values():
            bag_of_vals.remove(i)
        
        representation = []
        
        for i in range(self.size):
            if i not in self.fixed_vals.keys():
                selected = choice(bag_of_vals)
                representation.append(selected)
                bag_of_vals.remove(selected)
            else:
                representation.append(self.fixed_vals[i])
        
        return representation


    def display(self):
        print()
        for i in range(81):
            if i in [0, 27, 54]:
                print('--------+-------+--------')
            if i in [0, 9, 18, 27, 36, 45, 54, 63, 72]:
                print ('|', end=' ')
            print(self.representation[i], end=' ')
            if (i+1) % 3 == 0:
                print ('|', end=' ')
            if i in [8, 17, 26, 35, 44, 53, 62, 71, 80]:
                print ()
            if i == 80:
                print('--------+-------+--------')
        print()


    def evaluate_rows(self):
        fitness = 0
        for first in [0, 9, 18, 27, 36, 45, 54, 63, 72]:
            fitness += len(set(self.representation[first : first + 9]))
        return fitness


    def evaluate_cols(self):
        fitness = 0
        indexes = [0, 9, 18, 27, 36, 45, 54, 63, 72]
        for plus in range(9):
            cols = [i + plus for i in indexes]
            fitness += len(set(map(self.representation.__getitem__, cols)))
        return fitness


    def evaluate_squares(self):
        fitness = 0
        indexes = [0, 1, 2, 9, 10, 11, 18, 19, 20]
        for plus_col in range(3):
            for plus_row in range(3):
                square = [i + 3* plus_row + 27 * plus_col for i in indexes]
                fitness += len(set(map(self.representation.__getitem__, square)))
        return fitness


    def evaluate(self):
        """A simple objective function to calculate distances
        for the TSP problem.

        Returns:
            int: the total distance of the path
        """
        return self.evaluate_rows() + self.evaluate_cols() + self.evaluate_squares()


    def index(self, value):
        return self.representation.index(value)

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Fitness: {self.fitness}"


class Population:
    def __init__(self, size, optim, filename=None, folder=None **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.gen = 1
        self.filename = filename
        self.folder = folder
        for _ in range(size):
            self.individuals.append(
                Individual(
                    fixed_vals=kwargs["fixed_vals"]
                )
            )
    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism, log=False):
        super_elite = deepcopy(self.individuals[0])
        for gen in range(gens):
            new_pop = []
 
            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))
            
            if elite.evaluate() > super_elite.evaluate():
                super_elite = deepcopy(elite)
 
            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1, mu_p)
                if random() < mu_p:
                    offspring2 = mutate(offspring2, mu_p)
 
                new_pop.append(offspring1)
                if len(new_pop) < self.size:
                    new_pop.append(offspring2)
 
            if elitism == True:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))
                new_pop.pop(new_pop.index(least))
                new_pop.append(elite)

            self.individuals = new_pop
            if log:
                self.log(gens)
            self.gen += 1
 
            # if self.optim == "max":
            #     print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
            # elif self.optim == "min":
            #     print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')

        # This code was used to show the solutions for the sudoku problems of different levels
        # with open(fr"{self.folder}{self.filename}_display.csv", 'a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerow([super_elite.representation])

    def log(self, num_gens):
        best_indiv = max(self, key=attrgetter("fitness"))
        i=0
        my_file = Path(fr"{self.folder}{self.filename}.csv")
        # Counting the number of lines if the file exists
        if my_file.is_file():
            with open(fr"{self.folder}{self.filename}.csv") as f:
                for i, l in enumerate(f):
                    pass
        # Check if first generation is yet to complete
        if i < num_gens - 1:
            with open(fr"{self.folder}{self.filename}.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.gen, best_indiv.fitness])
        # if first generation is complete, then add new fitness value to the end of the line
        else:
            with open(fr"{self.folder}{self.filename}.csv", 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.split(',')[0] == f"{self.gen}":
                        lines[i] = lines[i].strip() + f",{best_indiv.fitness}\n"
                f.seek(0)
                for line in lines:
                    f.write(line)


    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"
