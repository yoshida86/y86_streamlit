import pulp

##問題設定
problem = pulp.LpProblem(
	"production",
	pulp.LpMaximize)

##変数定義
x = pulp.LpVariable(
	"A",
	lowBound=0
)

y = pulp.LpVariable(
	"B",
	lowBound = 0
)

##目的関数
problem += 3*x + 5*y

##制約設定
problem += 2*x + y <= 100

problem += x + 3*y <= 90

problem.solve()

print("Status:", pulp.LpStatus[problem.status])

print("A =" ,x.value())
print("B =" ,y.value())

print(
	"profit =",
	pulp.value(problem.objective))