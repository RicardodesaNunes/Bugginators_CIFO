from charles.charles import Population
from charles.selection import rank
from charles.mutation import swap_mutation
from charles.crossover import cycle_co, single_point_co

# x=Individual(fixed_vals={0:5,1:3,4:7,9:6,12:1,13:9,14:5,19:9,20:8,25:6,27:8,31:6,35:3,36:4,39:8,41:3,44:1,45:7,49:2,53:6,55:6,60:2,61:8,66:4,67:1,68:9,71:5,76:8,79:7,80:9})
# print(x)
# y=inversion_mutation(x)
# print(y)

fixed = {0:5,1:3,4:7,9:6,12:1,13:9,14:5,19:9,20:8,25:6,27:8,31:6,35:3,36:4,39:8,41:3,44:1,45:7,49:2,53:6,55:6,60:2,61:8,66:4,67:1,68:9,71:5,76:8,79:7,80:9}
xos = {'cycle_co':cycle_co, 'single_point_co':single_point_co}
xo_ps = {f"0.{i}":i/10 for i in range(1,10)}
mut_ps = {f"0.{i}":i/10 for i in range(1,10)}

for xo_p in xo_ps:
    for mut_p in mut_ps:
        for xo in xos:  
            for _ in range(35):    
                
                pop = Population(
                    size=120,
                    optim="max",
                    fixed_vals=fixed,
                    filename=f"\xo_p_{xo_p.split('.')[1]}_mut_p_{mut_p.split('.')[1]}_{xo}",
                    folder=r"files\finetune"
                )

                pop.evolve(
                    gens=150,
                    select=rank,
                    crossover=xos[xo],
                    mutate=swap_mutation,
                    co_p=xo_ps[xo_p],
                    mu_p=mut_ps[mut_p],
                    elitism=True,
                    log=True
                    )