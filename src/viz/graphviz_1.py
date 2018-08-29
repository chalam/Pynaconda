from graphviz import Digraph



def main():
    dot = Digraph(comment='The Round Table')
    print(dot)

    dot.node('A', 'King Arthur')
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')

    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='false')

    print(dot.source)
    # The Round Table
    # digraph {
    #     A [label="King Arthur"]
    #     B [label="Sir Bedevere the Wise"]
    #     L [label="Sir Lancelot the Brave"]
    #     A -> B
    #     A -> L
    #     B -> L [constraint=false]
    # }

    dot.render('test-output/round-table.gv', view=True)
    # 'test-output/round-table.gv.pdf'

if __name__ == '__main__':
    main()
