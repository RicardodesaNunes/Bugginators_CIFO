from random import randint, sample, choice


def swap_mutation(individual, mu_p):
    # Get two mutation points
    mut_points = sample([i for i in range(81) if i not in individual.fixed_vals.keys()], 2)
    # Rename to shorten variable name
    i = individual

    i[mut_points[0]], i[mut_points[1]] = i[mut_points[1]], i[mut_points[0]]

    return i


def inversion_mutation(individual, mu_p):
    i = individual
    # Position of the start and end of substring
    mut_points = sample(range(len(i)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    vals = i[mut_points[0]:mut_points[1]]
    # Remove fixed values from list that will be inverted
    for index in list(i.fixed_vals.keys())[::-1]:
        if index >= mut_points[0] and index < mut_points[1]:
            vals.pop(index - mut_points[0])
    # Invert the list
    vals = vals[::-1]
    # Add fixed values in the correponding indexes
    for index in i.fixed_vals.keys():
        if index >= mut_points[0] and index < mut_points[1]:
            vals.insert(index - mut_points[0], i.fixed_vals[index]) 
    # Add inverted list to individual
    i[mut_points[0]:mut_points[1]] = vals

    return i


def element_wise_mutation(individual, mu_p):
    # Only select mutation points that are not fixed values
    not_fixed = [i for i in range(81) if i not in individual.fixed_vals.keys()]
    # Select the mutation points
    mut_points = sample(not_fixed, round(len(not_fixed) * mu_p))
    # Store the values of the mutation points
    vals = list(map(individual.__getitem__, mut_points))
    # Loop through mutation points to randomly mutate
    for i in mut_points:
        insert_val = choice(vals)
        vals.remove(insert_val)
        individual[i] = insert_val
    return individual

