# Corrigé TP-1, Intelligence artificielle, GI  Corrigé TP-1, Intelligence artificielle, GI

# Initiation à python
# Exercice 1 :
# En utilisant la structure de contrôle if, comparer deux nombres. Si 3>2 alors afficher un texte, sinon
# afficher un autre texte

print("Saisir un nombre")
nbre = input()
nbre = int(nbre)
if nbre>5:
 print("Superieur")
else:
 print("Inferieur")


# Exercice 2 :
# En utilisant la fonction input, écrire un programme qui propose de saisir un nom et renvoie "Bonjour
# nom !".
# Ajouter au programme précédant la prise en compte du genre et renvoyer "Bonjour genre Nom"
# Limiter le choix du genre en proposant de choisir 0 pour madame ou 1 pour monsieur.

print("Saisir votre nom")
nom = input()
print("Bonjour %s"%nom)
print("Saisir votre genre 0 pour femme--------1 pour homme")
genre = int(input())
while genre!=0 and genre!=1:
 print("Re-saisir votre genre 0 pour femme--------1 pour homme")
 genre = int(input())
if genre==0:
 print("Bonjour Madame %s"% nom)
else:
 print("Bonjour Monsieur %s" % nom)


# Exercice 3 :
# Définir une variable int
# Vérifier s’elle est supérieure à 100 ou inférieure à 10. Si vrai afficher un message sinon traiter le cas
# échéant

variable = 30
if variable>100:
 print("Variable superieur a 100")
elif variable<10:
 print("Variable inferieur a 10")
else:
 print("Variable entre 10 et 100")

# Vérifier si un élément est pair, alors le retourner sinon lui ajouter 1
def parite(entier):
 if entier%2:
 return entier + 1
 else:
 return entier
print("Saisir un entier")
entier = int(input())
print(parite(entier))


# Exercice 4 :
# Ecrire un programme qui renvoi la liste des nombres premiers inférieurs à n.
# On pourra utiliser :
# 1. deux boucles for
# 2. la fonction Range
# . %
# 4. Break
# 5. Append pour remplir la liste

fin=input('nombre limite : ')
premiers=[]
for n in range(2, int(fin)):
 for x in range(2, n):
 if n % x == 0:
 break
 else:
 premiers.append(n)
print(premiers)


# La programmation orientée objets
# Exercice 1 :
# 1. Implémenter la méthode modifier_age(self, nouveau)
# 2. Implémenter la méthode saluer(self, autre_personne)

class Personne(object):
 def __init__(self, nom, prenom, age):
 self.nom = nom
 self.prenom = prenom
 self.age = age
 def afficher(self):
 print("Je m'appelle %s %s et j'ai %d" % (self.nom, self.prenom, self.age))
 def modifier_age(self,nouveau):
 self.age = nouveau
 def saluer(self, autre):
 print("Bonjour " + autre.nom)
personne1 = Personne('dupond', 'david', 30)
personne2 = Personne('thomas', 'pierre', 34)
personne1.afficher()
personne2.modifier_age(35)
personne1.saluer(personne2)


# 3. modifier l’attribut âge par date de naissance de type date et implémenter la méthode calculAge() qui
# calcule l’âge d’une personne

from datetime import date
class Personne(object):
 def __init__(self, nom, prenom, y, m, j):
 self.nom = nom
 self.prenom = prenom
 self.daten = date(y,m,j)
 def afficher(self):
 print("Je m'appelle %s %s et je suis né le %s"% (self.nom, self.prenom,
str(self.daten)))
 def saluer(self, autre):
 print("Bonjour " + autre.nom)
 def calculerAge(self):
 today = date.today()
 anniversaire = self.daten.replace(year=today.year)
 if anniversaire > today:
 return today.year - self.daten.year - 1
 else:
 return today.year - self.daten.year
personne1 = Personne('dupond', 'david', 2000, 5, 4)
personne1.afficher()
print("votre age est %s"%personne1.calculerAge())





 



# Corrigé : TP-2, Agents Intelligents, GI  Corrigé : TP-2, Agents Intelligents, GI Corrigé : TP-2, Agents Intelligents, GI

# Exercice 1 :
# Soit un environnement contenant deux agent A et B :
# Ecrire le code de la classe Agent_A ou l’agent A demande à l’agent B de changer sa position
# Ecrire le code de la classe Agent_B qui calcule sa décision en utilisant l’équation x
# 2 + log(y3), ou x et y sont l’abscisse et l’ordonné de l’agent (rendus d’une manière aléatoire), et lui répond selon la parité du résultat (OK ! si pair, NO ! sinon)
# Ecrire le code la classe Environnement qu’utilise la planification simultanée des agents
# Lancer votre environnement
# Corrigé:

import random
import mesa
import numpy as np
class Agent_A(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 def step(self):
 # autre = self.model.plan.agents[1]
 autre = self.random.choice(self.model.plan.agents)
 while autre.unique_id != 1:
 autre = self.random.choice(self.model.plan.agents)
 print("Merci de changer votre position")
class Agent_B(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 self.x = random.randint(1, 10)
 self.y = random.randint(1, 10)
 def step(self):
 self.x = random.randint(1, 10)
 self.y = random.randint(1, 10)
 resultat = pow(self.x, 2) + np.log(pow(self.y, 3))
 if int(resultat) % 2:
 print("Ok!")
 else:
 print("NO!")
class Environnement(mesa.Model):
 def __init__(self):
 super().__init__()
 A = Agent_A(0, self)
 B = Agent_B(1, self)
 self.plan = mesa.time.BaseScheduler(self)
 self.plan.add(A)
 self.plan.add(B)
 def step(self):
 self.plan.step()
model = Environnement()
while True:
 model.step()


# Exercice 2 :
# Soit un environnement contenant deux agents rationnels, chacun a un durée de fonctionnement d'une manière
# séquentielle (le 1er agent entre et fait son travail et sort pour céder le reste du travaille au 2
# eme agent). Le 1 er agent travaille pour 8 heures et effectue un calcul (incrémente une variable i par 1)
# Le 2eme agent fonctionne pour une durée de 9 heures et incrémente la dernière valeur calculée, par
# l'agent, par 1
# Corrigé:

import mesa
class Agent_A(mesa.Agent):
 def __init__(self,ID,model):
 super().__init__(ID,model)
 def step(self):
 self.model.i += 1
class Agent_B(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 def step(self):
 self.model.i += 2
class Environnement(mesa.Model):
 def __init__(self):
 super().__init__()
 self.i = 0
 self.A = Agent_A(0,self)
 self.B = Agent_B(1,self)
 self.plan = mesa.time.BaseScheduler(self)
 self.plan.add(self.A)
 self.count = 0
 def step(self):
 self.count += 1
 self.plan.step()
 if self.count==8:
 self.plan.remove(self.A)
 self.plan.add(self.B)
 if self.count == 17:
 self.plan.remove(self.B)
 print(self.i)
model = Environnement()
for j in range(17):
 model.step()








# TP-3, Algorithmes de recherche non-informée # TP-3, Algorithmes de recherche non-informée # TP-3, Algorithmes de recherche non-informée
# Exercice 1 :
La séquence des nœuds visités en utilisant l’algorithme : largeur d’abord (BFS)
{b, a, d, e, c g, f, h}
La séquence des nœuds visités en utilisant l’algorithme : profondeur d’abord (DFS)
{b, a, c, d, e, g, h}

# Exercice 2 :
# L’implémentation en python de l’algorithme BFS
visited = []
queue = []
def bfs(visited, graph, node):
 visited.append(node)
 queue.append(node)
 while queue:
 m = queue.pop(0)
 print (m, est = " ")
 for neighbour in graph[m]:
 if neighbour not in visited:
 visited.append(neighbour)

# Ecrire l'implémentation en python de l’algorithme DFS
visited = set()
def dfs(visited, graph, node):
 if node not in visited:
 print (node)
 visited.add(node)
 for neighbour in graph[node]:
 dfs(visited, graph, neighbour)


# Exercice 3 :
# Ecrire le code pour comparer 2 agents, en termes de complexité de temps, où le 1er agent
# utilise l’algorithme BFS et le 2eme agent déploie le DFS.
# Le graphe a utilisé :
# graphe = {'5' : ['3','7'], '3' : ['2', '4'], '7' : ['8'], '2' : [], '4' : ['8'], '8' : []}
import time
import mesa
class Agent_A(mesa.Agent):
 def __init__(self,ID,model):
 super().__init__(ID,model)
 self.graph = self.model.graphe
 self.node = self.model.start
 self.goal = self.model.end
 def BFS(self,graphe,node,goal):
 visited = []
 file = []
 file.append(node)
 visited.append(node)
 while file:
 m = file.pop(0)
 print(m)
 if m == goal:
 return 1
 for n in graphe[m]:
 if n not in visited:
 file.append(n)
visited.append(n)
 return 0
 def step(self):
 start_time = time.perf_counter()
 self.BFS(self.graph,self.node,self.goal)
 end_time = time.perf_counter()
 execution_time = end_time - start_time
 print(f" BFS est {execution_time}")
class Agent_B(mesa.Agent):
 def __init__(self, ID, model):
 super().__init__(ID, model)
 self.graph = self.model.graphe
 self.node = self.model.start
 self.goal = self.model.end
 self.visited = set()
 self.end_time = 0
 def DFS(self, graphe, node, goal,visited):
 if node not in visited:
 visited.add(node)
 if node==goal:
 self.end_time = time.perf_counter()
 for n in graphe[node]:
 self.DFS(graphe, n, goal, visited)
 def step(self):
 start_time = time.perf_counter()
 self.DFS(self.graph, self.node, self.goal,self.visited)
 execution_time = self.end_time - start_time
 print(f" DFS est {execution_time}")
class Environnement(mesa.Model):
 def __init__(self):
 super().__init__()
 self.graphe = {'5' : ['3','7'],
 '3' : ['2', '4'],
 '7' : ['8'],
 '2' : [],
'4' : ['8'],
 '8' : []}
 self.start = '5'
 self.end = '8'
 self.A = Agent_A(0,self)
 self.B = Agent_B(1,self)
 self.plan = mesa.time.SimultaneousActivation(self)
 self.plan.add(self.A)
 self.plan.add(self.B)
 def step(self):
 self.plan.step()
model = Environnement()
model.step()











# Corrigé TP-4, Algorithmes de recherche informée # Corrigé TP-4, Algorithmes de recherche informée # Corrigé TP-4, Algorithmes de recherche informée

# Exercice 1 :

# Dans quel ordre les nœuds sont développés pour chacun des algorithmes ?
# • Meilleur d’abord glouton
# • A*

Meilleur d’abord glouton : {A, B, E, D, C, G}
A* :
f(B) = g(B) + h(B) = 1 + 2 = 3
f(C) = g(C) + h(C) = 4 + 10 = 14
f(D) = g(D) + h(D) = 3 + 1 + 7 = 11
f(E) = g(E) + h(E) = 2 + 1 + 3 = 6
f(F) = g(F) + h(F) = 4 + 2 + 5 = 11
f(H) = g(H) + h(H) = 1 + 2 + 1 + 11 = 15
f(I) = g(I) + h(I) = 4 + 2 + 7 + 9 = 22
La séquence : {A, B, E, D, C, G}


# Exercice 2 :
# En utilisant les algorithmes, Meilleur d’abord glouton et A*, chercher le nœud 8.

nombre_noeuds = 6
graphe = [[] for i in range(nombre_noeuds)]
def fct(x,y,cout):
 graphe[x].append((y,cout))
 graphe[y].append((x, cout))
fct(0,1,7)
fct(0,2,2)
fct(1,3,4)
fct(1,4,3)
fct(2,5,0)
fct(4,5,0)
print(graphe)
from queue import PriorityQueue
liste = [5,3,7,2,4,8]
def best_first(graphe,node,goal,n):
 visited = [False]*n
 visited[node] = True
 p_queue = PriorityQueue()
 p_queue.put((0,node))
 while p_queue.empty() == False:
 m = p_queue.get()[1]
 print(liste[m])
 if m == goal:
 return 1
 for n,c in graphe[m]:
 if visited[n] == False:
 visited[n] = True
 p_queue.put((c,n))
 return 0
print("%d"%best_first(graphe,0,5,6))


# 
A* : Il faut modifier les couts avec les nouveaux couts calculer avec la fonction f(n) = g(n) +
h(n)
f(3) = g(3) + h(3) = 7 + 2 = 9
f(7) = g(7) + h(7) = 4 + 2 = 6
f(2) = g(2) + h(2) = 3 + 4 + 2 = 9
f(4) = g(4) + h(4) = 2 + 2 + 3 = 7
Donc les instructions à modifier sont :
5
3 7
2 4 8
2
4
1
3 2
5
h = 7 h = 2
h = 4 h = 3 h = 0
h = 10
fct(0,1,9)
fct(0,2,6)
fct(1,3,9)
fct(1,4,7)
fct(2,5,0)
fct(4,5,0)