from charles.charles import Individual
from random import randint, uniform



def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1)-2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return Individual(representation = offspring1, fixed_vals = p1.fixed_vals), Individual(representation = offspring2, fixed_vals = p2.fixed_vals)
    

def cycle_co(p1, p2):
    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)
    # Dictionary with the positions of each value
    repeated = {i:[j for j, x in enumerate(p1) if x == i] for i in range(1,10)}
    index = offspring1.index(None)
    val1 = p1[index]
    val2 = p2[index]
    # Cycle to obtain a cycle of indexes
    while repeated[val1] != []:
        offspring1[index] = p1[index]
        offspring2[index] = p2[index]
        # Remove used index
        repeated[val1].pop(0)
        if repeated[val2] == []:
            pass
        else:
            index = repeated[val2][0]
            val1 = p1[index]
            val2 = p2[index]
    # Fill values outside the cycle
    none_indexes = [i for i, x in enumerate(offspring1) if x is None]
    for i in none_indexes:
        offspring1[i] = p2[i]
        offspring2[i] = p1[i]

    return Individual(representation = offspring1, fixed_vals = p1.fixed_vals), Individual(representation = offspring2, fixed_vals = p2.fixed_vals)


def arithmetic_co(p1, p2):
    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)
    # Set a value for alpha between 0 and 1
    alpha = uniform(0,1)
    # Take weighted sum of two parents, invert alpha for second offspring
    for i in range(len(p1)):
        offspring1[i] = round(p1[i] * alpha + (1 - alpha) * p2[i])
        offspring2[i] = round(p2[i] * alpha + (1 - alpha) * p1[i])

    return Individual(representation = offspring1, fixed_vals = p1.fixed_vals), Individual(representation = offspring2, fixed_vals = p2.fixed_vals)