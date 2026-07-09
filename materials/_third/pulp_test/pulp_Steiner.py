import networkx as nx
import matplotlib.pyplot as plt
import random
import pulp
import csv


G = nx.Graph()

Terminal = []


csv_file = 'terminal.csv'

with open(csv_file, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        # 空行をスキップ
        if not row:
            continue

        Terminal.append(int(row[0]))

csv_graph = 'graph.csv'


with open(csv_graph, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
    # 空行をスキップ
        if not row:
            continue

        u = int(row[0])
        v = int(row[1])
        weight = float(row[2])

        G.add_edge(u, v)
        G[u][v]["weight"] = weight

print(G.number_of_edges())




print(Terminal)

root = Terminal[0]

problem = pulp.LpProblem("SteinerTree", pulp.LpMinimize)

# 変数
x = {}
f = {}

for (i, j) in G.edges():
    x[i, j] = pulp.LpVariable(f"x_{i}_{j}", cat="Binary")

    for k in Terminal[1:]:
        f[i, j, k] = pulp.LpVariable(f"f_{i}_{j}_{k}", lowBound=0)
        f[j, i, k] = pulp.LpVariable(f"f_{j}_{i}_{k}", lowBound=0)

# フロー保存則
for k in Terminal[1:]:
    for i in G.nodes():

        outflow = pulp.lpSum(f[i, j, k] for j in G[i])
        inflow = pulp.lpSum(f[j, i, k] for j in G[i])

        if i == root:
            problem += outflow - inflow == 1

        elif i == k:
            problem += outflow - inflow == -1

        else:
            problem += outflow - inflow == 0

# xとの対応
for (i, j) in G.edges():
    for k in Terminal[1:]:
        problem += f[i, j, k] + f[j, i, k] <= x[i, j]

# 目的関数
problem += pulp.lpSum(
    G[i][j]["weight"] * x[i, j]
    for (i, j) in G.edges()
)

solver = pulp.PULP_CBC_CMD(timeLimit=7200, options=['presolve off'])

problem.solve(solver)

# 結果の表示
print("Status:", pulp.LpStatus[problem.status])

if problem.status in (
    pulp.LpStatusOptimal,
    pulp.LpStatusNotSolved,
):
    print("Objective =", pulp.value(problem.objective))