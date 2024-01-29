from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment='Asset Tracking Process')

# Add nodes representing different stages of the asset tracking process
dot.node('A', 'Procurement')
dot.node('B', 'Receiving')
dot.node('C', 'Tagging & Recording')
dot.node('D', 'Assignment to Departments')
dot.node('E', 'Maintenance & Upkeep')
dot.node('F', 'Audit & Verification')
dot.node('G', 'Disposal/Retirement')

# Add edges to represent the flow of the process
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])
dot.edge('F', 'C', label='Updates')  # Representing feedback loop for updates
dot.edge('E', 'G', label='End of Life')  # Representing disposal at end of life

# Print the source code for the graph
print(dot.source)

# Render the graph to a file (e.g., in PNG format)
dot.render('asset-tracking-process.gv', format='png', view=True)
