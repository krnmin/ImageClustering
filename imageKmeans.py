import pandas as pd
import numpy as np
data = pd.read_csv('imageTestData.txt', header=None)		# reads the data which the model will base off. no header provided so we need to turn stat that lest pandas reads first column as a header
#print(data.head())
k = 10		# using 10 for the sake of miner
centroids = data.sample(k,replace = False)		# obtaining a random sample of k samples from dataset
#print(centroids)
temp = pd.DataFrame()		
clusters = pd.DataFrame()
while not temp.equals(centroids):
	#using Euclidean Distance
	cluster_count = 1		# iterating through the clusters
	for idx, mean in centroids.iterrows():		# 
		clusters[cluster_count] = (data[centroids.columns] - np.array(mean)).pow(2).sum(1).pow(0.5)		# squareroot(squared + 1 ) 
		cluster_count += 1		# iterate through each cluster once again
	data['Cluster'] = clusters.idxmin(axis=1)		# placing the Cluster value into the table 
	temp = centroids		# store previous iteration values to be used in the next iteration
	centroids = pd.DataFrame()		#
	centroids_frame = data.groupby('Cluster').agg(np.mean)		# groups centroid frame grouped by value of cluster and taking the mean
	centroids[centroids_frame.columns] = centroids_frame[centroids_frame.columns]		# setting the values at each point
#result = data['Cluster'].to_csv(index=False)
#print(result)
f = open("outputImage.txt", 'w')		# printing out the clusters separated by newline
for v in data['Cluster']:
	f.write(str(v) + '\n')
f.close()								#closing file in case some weird error occurs
# used to plot graphs
import plotly.offline as plt
import plotly.graph_objs as go
#plotting
ctr=1

data_graph = [go.Scatter(
              x=data[0],
              y=data[1].where(data['Cluster'] == ctr+1),
              mode='markers',
              name='Cluster: ' + str(ctr+1)
              ) for ctr in range(k)]

data_graph.append(
    go.Scatter(
        x=centroids[0],
        y=centroids[1],
        mode='markers',
        marker=dict(
            size=10,
            color='#000000',
        ),
        name='Centroids of Clusters'
    )
)
plt.plot(data_graph, filename='cluster.html')

print("success")	#statement to show that the program finished running

	