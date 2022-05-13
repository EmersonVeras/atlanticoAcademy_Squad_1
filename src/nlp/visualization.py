import networkx as nx
from mycolorpy import colorlist as mcp
import matplotlib.pyplot as plt

# Cada ponto central será um dos 5 termos de maior TF-IDF.
# As conexões são as palavras próximas obtidas em 4.5.

words_and_connections = {"fruit": {"weight": 4, "neighbors": ["apple", "orange", "banana"]},
                         "city": {"weight": 2, "neighbors": ["São Paulo", "Paris", "Rome"]},
                         "language": {"weight": 10, "neighbors": ["Python", "Java", "C#", "Ruby"]}}

egdes = []

g = nx.Graph()
colors = color1 = mcp.gen_color(cmap="Set1", n=len(words_and_connections))
#print(colors)

for word, color in zip(words_and_connections, colors):
    for n in words_and_connections[word]["neighbors"]:
        g.add_edge(word, n, weight=1)
        g.nodes[n]['weight'] = 300
        g.nodes[n]['color'] = color
    g.nodes[word]['weight'] = words_and_connections[word]['weight']*300
    g.nodes[word]['color'] = color

node_colors = [g.nodes[word]['color'] for word in g.nodes]


plt.figure(figsize=(10, 10))

edge_weight = list(nx.get_edge_attributes(g, 'weight').values())
node_weight = list(nx.get_node_attributes(g, 'weight').values())

nx.draw_networkx(g, width=edge_weight, node_size=node_weight, edge_color='#b5b1b0', node_color=node_colors, font_family = 'Ubuntu')

# Se necessario, instalar o Tk:
# UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
# sudo apt-get install python3-tk
plt.savefig("graph.png")
plt.show()
