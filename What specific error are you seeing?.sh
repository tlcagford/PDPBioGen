python3 -c "
import sys
print('Python:', sys.version)
try:
    import pdpbiogen
    print('PDPBioGen: OK')
except Exception as e:
    print('PDPBioGen Error:', e)
try:
    import graphviz
    dot = graphviz.Digraph()
    dot.node('test')
    print('Graphviz: OK')
except Exception as e:
    print('Graphviz Error:', e)
"
