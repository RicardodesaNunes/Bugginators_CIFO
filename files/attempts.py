from charles.charles import Population
from charles.selection import rank
from charles.mutation import swap_mutation
from charles.crossover import single_point_co

easy = {0:2, 1:6, 5:3, 7:1, 8:5, 9:4, 10:7, 17:8, 18:5, 19:8, 20:1, 23:4, 24:7, 25:6, 26:3, 28:3, 30:4, 31:8, 32:9, 34:7, 38:6, 41:2, 42:8, 43:3, 47:8, 48:3, 49:1, 54:6, 55:9, 59:8, 62:7, 63:3, 67:9, 69:2, 73:1, 75:5, 79:9, 80:6}
medium = {0:8, 3:5, 5:4, 7:1, 8:3, 9:1, 15:6, 20:2, 22:1, 24:5, 25:7, 27:4, 29:7, 33:9, 35:5, 36:5, 39:4, 40:2, 49:5, 50:9, 51:4, 52:6, 55:8, 56:1, 59:2, 66:9, 67:7, 68:5, 69:1, 70:8, 71:2, 77:1}
hard = {0:6, 5:5, 12:3, 14:4, 16:5, 22:4, 25:6, 27:4, 29:3, 37:8, 39:7, 42:2, 50:1, 51:7, 58:9, 62:6, 65:5, 67:2, 69:8, 70:4, 71:9, 73:4, 77:3}
attempts = {'easy':easy, 'medium':medium, 'hard':hard}


for attempt in attempts:  
    for _ in range(35):    
        
        pop = Population(
            size=120,
            optim="max",
            fixed_vals=attempts[attempt],
            filename=f"{attempt}",
            folder=r"files\attempts\"
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