

class Arbitrage(object):

    HAS_CYCLE = False

    def shortestPath(self, vertexList, edgeList, startVertex):

        startVertex.minDistance = 0

        for i in range(0, len(vertexList)-1):
            for edge in edgeList:

                u = edge.startVertex
                v = edge.targetvertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u;

        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected")
                Arbitrage.HAS_CYCLE = True
            return
        return
