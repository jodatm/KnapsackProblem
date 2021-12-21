  
import random
from item import Item
import networkx as nx

##########################################################################################
# KnapsackProblem source code taken from: https://github.com/edmilsonrobson 
##########################################################################################
# 

ITEMS = [Item(random.randint(0,30),random.randint(0,30)) for x in range (0,30)]

CAPACITY = 10*len(ITEMS)

POP_SIZE = 50

GEN_MAX = 200

START_POP_WITH_ZEROES = False

rewiring = 0.3

G = nx.generators.random_graphs.watts_strogatz_graph(POP_SIZE,3,rewiring)

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
    
    mutation_chance = 0.08
        
    for i in range(0,len(pop)):
        
        candidato = pop[i]
        vecinos=[]
        for k in G[i]:            
            vecinos.append(k)
            
        if(len(vecinos)>0):        
            mejor_vecino = 0
            puntaje_mejor_vecino = 0
            
            for k in G[i]:
                
                fitness_vecino = fitness(pop[k])                
                if(fitness_vecino>puntaje_mejor_vecino):
                    puntaje_mejor_vecino = fitness_vecino
                    mejor_vecino = k        
            
            pareja = pop[mejor_vecino]
            child = []
            half = len(candidato)/2
            child = candidato[:half] + pareja[half:] # from start to half from father, from half to end from mother
            if mutation_chance > random.random():
                mutate(child)
            if fitness(child)>fitness(candidato):
                pop[i]=child
                G.add_edge(i,mejor_vecino)
            return pop

def updateG():
    for j in range(0, POP_SIZE):            
        aristas = G.adj[j]        
        
        vecinos=[]
        for k in aristas:            
            vecinos.append(k)
                
        for i in range(0,len(vecinos)):
            if random.random() < rewiring:                
                random_index = int(random.random()*POP_SIZE)                
                G.remove_edge(j, vecinos[i])                
                G.add_edge(j,random_index)
    
def main():
    generation = 0
    population = spawn_starting_population(POP_SIZE)
    fitness_generations = []
    
    for g in range(0,GEN_MAX):
        population = evolve_population(population)
        updateG()
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
        #print(promedios[i])
        print(promedios[i]),
        
