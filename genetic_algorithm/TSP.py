import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

# klasa tworząca miasta czy też śmietniki
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

# fitness function,
# inverse of route distance
# we want to minimize distance so the larger the fitness the better
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None    
                if i + 1 < len(self.route):         #  for returning to point 0?   
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

# creating one individual - single route from city to city (trash to trash)
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

# creating initial population of given size
def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population

# ranking fitness of given route, output is ordered list with route id and its fitness score
def rankRoutes(population):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)

# selecting "mating pool"
# we are using here "Firness proportionate selection", its fitness-weighted probability of being selected
# moreover we are using elitism to ensure that the best of the best will preserve

def selection(popRanked, eliteSize):
    selectionResults = []
    # roulette wheel
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, eliteSize): # elitism
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize): # comparing randomly drawn number to weights for selection for mating pool
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults # returns list of route IDs

# creating mating pool from list of routes IDs from "selection"
def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

# creating new generation
# ordered crossover bc we need to include all locations exactly one time
# randomly selecting a subset of the first parent string and then filling the remainder of route 
# with genes from the second parent in the order in which they appear, without duplicating any genes from the first parent
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene): # ordered crossover
        childP1.append(parent1[i])
        
    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

# creating whole offspring population
def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))
    
    # using elitism to retain best genes (routes)
    for i in range(0,eliteSize): 
        children.append(matingpool[i])
    
    # filling rest generation
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

# using swap mutation
# with specified low prob we swap two cities in route
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

# extending mutate function to run through new pop
def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

# creating new generation 
def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen) # rank routes in current gen
    selectionResults = selection(popRanked, eliteSize) # determining potential parents
    matingpool = matingPool(currentGen, selectionResults) # creating mating pool
    children = breedPopulation(matingpool, eliteSize) # creating new gen
    nextGeneration = mutatePopulation(children, mutationRate) # applying mutation to new gen
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
    
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute

# tutaj ma być lista kordów potencjalnych śmietników z drzewa decyzyjnego

cityList = []

for i in range(0,25):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=1000)




# plotting the progress

def geneticAlgorithmPlot(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    progress = []
    progress.append(1 / rankRoutes(pop)[0][1])
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])
    
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()


# geneticAlgorithmPlot(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=1000)