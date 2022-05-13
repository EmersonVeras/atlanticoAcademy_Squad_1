import networkx as nx
from mycolorpy import colorlist as mcp
import matplotlib.pyplot as plt

# Cada ponto central será um dos 5 termos de maior TF-IDF. 
# As conexões são as palavras próximas obtidas em 4.5. 

words_and_connections = {"fruit": {"weight": 4, "neighbors": ["apple", "orange", "banana"]}, \
    "city": {"weight": 2, "neighbors": ["São Paulo", "Paris", "Rome"]}, \
    "language": {"weight": 10, "neighbors": ["Python", "Java", "C#", "Ruby"]}}
nodes = []
egdes = []

g = nx.Graph()
colors = color1=mcp.gen_color(cmap="winter",n=len(words_and_connections))
for word, color in zip(words_and_connections, colors):
    #nodes.append(word)
    for n in words_and_connections[word]["neighbors"]:
        #nodes.append(n)
        g.add_edge(word, n, weight=1)
        g.nodes[n]['weight'] = 300
        g.nodes[n]['corlo'] = color
    g.nodes[word]['weight'] = words_and_connections[word]['weight']*300

plt.figure(figsize=(10,10))

edge_weight = list(nx.get_edge_attributes(g,'weight').values())
node_weight = list(nx.get_node_attributes(g,'weight').values())

nx.draw_networkx(g, width=edge_weight, node_size=node_weight)


#g.add_nodes_from(nodes)

#subax1 = plt.subplot(121)
#nx.draw(g, with_labels=True, font_weight='bold')
#subax2 = plt.subplot(122)
#nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

# Se necessario, instalar o Tk:
# UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
# sudo apt-get install python3-tk
plt.savefig("graph.png")
plt.show()
