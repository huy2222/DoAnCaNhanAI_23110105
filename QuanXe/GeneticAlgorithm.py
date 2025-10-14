import random
import globals
def Fitness(individual):
    hx = 0
    for i in range(len(globals.target_solution)):
        if i > len(individual) - 1:
            hx += globals.target_solution[i]
        else:
            hx += abs(individual[i] - globals.target_solution[i])
    return hx
def GeneticAlgorithm(Fitness_fn, gene_pool, target_solution, generations, size_population):
    best = ()
    all_state = []
    step = 0
    print("Mục tiêu: ", target_solution)
    population = random.sample(gene_pool, size_population)
    for resident in population:
        if resident == target_solution:
            print("tim ra roi")
            return resident, None, None
    for gen in range(generations):
        scored = []
        for individual in population:
            scored.append((individual, Fitness_fn(individual)))
        scored.sort(key=lambda x: x[1], reverse=False)
        best = scored[0]
        print(f"Gen {gen}: {best}")
        step = gen
        all_state.extend([f"Gen {gen}: {best}"])
        if best[0] == target_solution:
            break
        parents = [ind for ind, score in scored[:size_population // 2]]
        # lai ghep
        children = []
        while len(children) < size_population:
            p1, p2 = random.sample(parents, 2)
            cut = random.randint(1, len(p1) - 1)
            child = p1[:cut] + p2[cut:]
            children.append(child)
            # dot bien
            for i in range(int(len(children) * 0.1)):
                child = random.choice(children)
                children.remove(child)
                for i in range(len(child)):
                    for j in range(random.randint(2, 8)):
                        if child[i] == len(child) - 1:
                            child[i] = 0
                        else:
                            child[i] = child[i] + 1
                children.append(child)
                if child == target_solution:
                    return child
        population = children
    return best[0], all_state, step