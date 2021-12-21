  
import random
from item import Item

##########################################################################################
# KnapsackProblem source code taken from: https://github.com/edmilsonrobson 
##########################################################################################
# 

ITEMS = [Item(random.randint(0,30),random.randint(0,30)) for x in range (0,30)]

CAPACITY = 10*len(ITEMS)

POP_SIZE = 50

GEN_MAX = 200

START_POP_WITH_ZEROES = False

def fitness(target):    
    total_value = 0
    total_weight = 0
    index = 0
    for i in target:        
        if index >= len(ITEMS):
            break
        if (i == 1):
            total_value += ITEMS[index].value
            total_weight += ITEMS[index].weight
        index += 1
        
    
    if total_weight > CAPACITY:
        return 0
    else:
        return total_value

def spawn_starting_population(amount):
    return [spawn_individual() for x in range (0,amount)]

def spawn_individual():
    if START_POP_WITH_ZEROES:
        return [random.randint(0,0) for x in range (0,len(ITEMS))]
    else:
        return [random.randint(0,1) for x in range (0,len(ITEMS))]

def mutate(target):    
    r = random.randint(0,len(target)-1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1

def evolve_population(poblation):
    
    pop = poblation
    fitness_poblacion = []
    mutation_chance = 0.08
        
    for j in range(0, len(pop)):
        fitness_temporal = fitness(pop[j])
        fitness_poblacion.append(fitness_temporal)
    


    for i in range(0,len(pop)):        
        candidato = pop[i]
        posicion_pareja = 0
        no_encontro_pareja = True                
        while(no_encontro_pareja):
            max = sum(fitness_poblacion)        
            
            pick = random.uniform(0, max)
            
            current = 0
            
            for j in range (0,len(fitness_poblacion)):
                current += fitness_poblacion[j]
                if current > pick:
                    posicion_pareja = j
                    break
            if(posicion_pareja != i):
                no_encontro_pareja = False
                
        pareja = pop[posicion_pareja]
        child = []
        half = len(candidato)/2
        child = candidato[:half] + pareja[half:] 
        if mutation_chance > random.random():
            mutate(child)
        if fitness(child)>fitness(candidato):            
            pop[i]=child        
        return pop

def main():
    generation = 0
    population = spawn_starting_population(POP_SIZE)
    fitness_generations = []
    for g in range(0,GEN_MAX):
        population = evolve_population(population)
        fitness_mas_alto = 0
        
        for i in range (0,len(population)):
            if fitness(population[i])>fitness_mas_alto:
                fitness_mas_alto = fitness(population[i])
        
        fitness_generations.append(fitness_mas_alto)
        generation += 1
    return fitness_generations

if __name__ == "__main__":
    number_experiments = 100
    promedios = []
    experiments = []
    for i in range (0,number_experiments):
        experiments.append(main())        
    
    for i in range(0,GEN_MAX):
        sumatoria_temporal = 0
        for j in range(0,number_experiments):            
            sumatoria_temporal = sumatoria_temporal + experiments[j][i]
                
        promedio_temporal = sumatoria_temporal / number_experiments        
        promedios.append(promedio_temporal)
    
    print("\n")
    print("Promedios de las iteraciones")
    for i in range(0,GEN_MAX):
        print(promedios[i]),
        
