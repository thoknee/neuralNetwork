from graphviz import Digraph
from micrograd.engine import Value


def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._pre:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_graph(root, format='svg', rankdir='LR'):
    assert rankdir in ['LR', 'TB']
    nodes, edges = trace(root)
    gr = Digraph(format=format, graph_attr={'rankdir': rankdir})
    
    for n in nodes:
        gr.node(name=str(id(n)), label = "{ Val %.4f | Chng %.4f }" % (n.data, n.chng), shape='record')
        
        if n._op:
            gr.node(name=str(id(n)) + n._op, label=n._op)
            gr.edge(str(id(n)) + n._op, str(id(n)))
    
    for x, y in edges:
        gr.edge(str(id(x)), str(id(y)) + y._op)
    
    return gr