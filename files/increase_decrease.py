from charles.charles import Population
from charles.selection import rank
from charles.mutation import swap_mutation
from charles.crossover import single_point_co

# fixed values
fixed = {0:5,1:3,4:7,9:6,12:1,13:9,14:5,19:9,20:8,25:6,27:8,31:6,35:3,36:4,39:8,41:3,44:1,45:7,49:2,53:6,55:6,60:2,61:8,66:4,67:1,68:9,71:5,76:8,79:7,80:9}

# run 35 each algorithm  
for _ in range(35):    
    
    pop = Population(
        size=120,
        optim="max",
        fixed_vals=fixed,
        filename=f"\inc_dec_file",
        folder=r"files\inc_dec"
    )

    pop.evolve(
        gens=150,
        select=rank,
        crossover=single_point_co,
        mutate=swap_mutation,
        co_p=0.9,
        mu_p=0.4,
        elitism=True,
        log=True
        )
