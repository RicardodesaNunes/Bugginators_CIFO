from charles.charles import Population
from charles.selection import fps, tournament, rank
from charles.mutation import swap_mutation, inversion_mutation, element_wise_mutation
from charles.crossover import cycle_co, single_point_co, arithmetic_co

# fixed values
fixed = {0:5,1:3,4:7,9:6,12:1,13:9,14:5,19:9,20:8,25:6,27:8,31:6,35:3,36:4,39:8,41:3,44:1,45:7,49:2,53:6,55:6,60:2,61:8,66:4,67:1,68:9,71:5,76:8,79:7,80:9}
# selection methods
selects = {'fps':fps, 'tournament':tournament, 'rank':rank}
# crossover methods
xos = {'cycle_co':cycle_co, 'single_point_co':single_point_co, 'arithmetic_co':arithmetic_co}
# mutation methods
muts = {'swap_mutation':swap_mutation, 'inversion_mutation':inversion_mutation, 'element_wise_mutation':element_wise_mutation}

# for each selection method
for sel in selects:
    # for each crossover method
    for xo in xos:
        # for each mutation method
        for mut in muts:
            # run 35 times each algorithm
            for _ in range(35):    
                
                pop = Population(
                    size=120,
                    optim="max",
                    fixed_vals=fixed,
                    filename=f"\{sel}_{xo}_{mut}",
                    folder=r"files\logs"
                )

                pop.evolve(
                    gens=150,
                    select=selects[sel],
                    crossover=xos[xo],
                    mutate=muts[mut],
                    co_p=0.6,
                    mu_p=0.2,
                    elitism=True,
                    log=True
                    )
