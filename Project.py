import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ('Ari', 'Sadaf'),
    ('Ari', 'Sina'),
    ('Sadaf', 'Bita'),
    ('Bita', 'Asal'),
    ('Asal', 'Maral'),
    ('Ari', 'Inaz'),
    ('Inaz', 'Taha'),
    ('Taha', 'Sina'),
    ('Sina', 'Ali'),
    ('Sina', 'Salar'),
    ('Salar', 'Amirali'),
    ('Ali', 'Amirali'),
    ('Ari' , 'Bita'),
    ('Maral' , 'Inaz')
]

G = nx.Graph()
G.add_edges_from(edges)


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
density = nx.density(G)
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Density: {density:.2f}")

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

print("Degree Centrality:", degree_centrality)
print("Betweenness Centrality:", betweenness_centrality)
print("Closeness Centrality:", closeness_centrality)

communities = list(nx.community.girvan_newman(G))
print("Communities:", communities[0])

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 7))

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx_edges(G, pos)

nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

most_influential = max(degree_centrality, key=degree_centrality.get)
nx.draw_networkx_nodes(G, pos, nodelist=[most_influential], node_color='r', node_size=800)

plt.title("Social Network Analysis")
plt.show()

plt.figure(figsize=(10, 7))
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for i, community in enumerate(communities[0]):
    nx.draw_networkx_nodes(G, pos, nodelist=list(community), node_color=colors[i % len(colors)], node_size=700)

nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
plt.title("Community Detection in Social Network")
plt.show()
