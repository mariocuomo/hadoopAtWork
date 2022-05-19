"""
questo script grafica gli andamenti dei tre job con mapreduce, hive, spark-core e spark-sql
"""

import matplotlib.pyplot as plt

job1 = {
	'mapReduce': [198,280,420,],
	'hive': [180,265,350],
	'spark-core': [305, 496, 786],
	'spark-SQL': [53, 122, 201]
}

job2 = {
	'mapReduce': [15, 23, 30],
	'hive': [123, 186, 201],
	'spark-core': [56, 92, 118],
	'spark-SQL': [61, 93, 110]
}

job3 = {
	'mapReduce': [246, 324, 387],
	'hive': [369, 490, 536],
	'spark-core': [183, 302, 364],
	'spark-SQL': [221, 320, 327]
}

jobs = [job1, job2, job3]
x=['N','2N','3N']
i=1

for job in jobs:
	for approccio in job.keys():
		y = job.get(approccio)
		y = sorted(y)
		plt.plot(x, y, label=approccio)

	plt.legend()
	plt.xlabel("DIMENSIONE FILE")
	plt.ylabel("TEMPO DI COMPUTAZIONE (s)")
	plt.title('job'+str(i))
	plt.savefig('../resources/job'+str(i))
	plt.clf()
	i=i+1



