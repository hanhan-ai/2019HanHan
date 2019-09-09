# ======================================================================================================================
# =========================================Population & Select Part=====================================================
# ======================================================================================================================


from GApart.Brain import *
import pickle
import operator

class Population:
    def __init__(self, population_num):
        self.size_population = population_num
        self.biont = []
        self.generation = 1

    def initPopulation(self, net_in, net_h1, net_h2, net_out):
        for i in range(self.size_population):
            self.biont.append(Network(net_in, net_h1, net_h2, net_out))

    def selectParents(self):

        total_score = 0
        add_rate = 0
        father = Network()
        mother = Network()

        for i in range(self.size_population):
            total_score += self.biont[i].evaluate_score

        for i in range(self.size_population):
            self.biont[i].chosen_rate = self.biont[i].evaluate_score/total_score
            add_rate += self.biont[i].chosen_rate
            self.biont[i].accumulative_rate = add_rate

        sort_key = operator.attrgetter('evaluate_score')
        self.biont.sort(key=sort_key, reverse=True)

        father = self.biont[0]
        mother = self.biont[1]

        print("**************the chosen father's score is ", father.evaluate_score, " **************")
        print("**************the chosen mother's score is ", mother.evaluate_score, " **************")

        return father, mother

    def breed(self, father, mother):

        for i in range(self.size_population):
            self.biont[i] = mutate(cross(father, mother))

        self.biont[0] = father
        self.biont[1] = mother

        father.generation += 1
        mother.generation += 1

    def saveNet(self, generation):
        pickle_file = open('../saved_bionts/'+str(generation), 'wb')
        pickle.dump(self.biont, pickle_file)
        pickle_file.close()

    def loadNet(self, generation):
        pickle_file = open('../saved_bionts/'+str(generation), 'rb')
        bionts = pickle.load(pickle_file)
        pickle_file.close()
        return bionts


