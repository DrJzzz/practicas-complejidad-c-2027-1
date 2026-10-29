#!/usr/bin/env python3
import sys
import graph_parse as gp

def vertex_cover_to_dominating_set(vertices, edges, k):
    # 1. Se comienza con la gráfica original G.
    # 2. Para cada arista (v, w) de G se agrega un nuevo vértice vw.
    new_vertices = []
    for v, w in edges:
        vw = str(v) + str(w)
        new_vertices.append(vw)
    vertices.extend(new_vertices)
    # 3. El nuevo vértice vw se conecta con los dos extremos de la arista original mediante
    #   las aristas (v, vw) y (w,vw).
    # - Para cada arista (v, w) de G se agrega un nuevo vértice vw.
    # - El valor de k se conserva en el ejemplar resultante.
    new_edges = []
    for vw in new_vertices:
        v, w = vw[0], vw[1]
        new_edges.append((v, vw))
        new_edges.append((w, vw))

    edges.extend(new_edges)
    return vertices, edges, k, new_edges, new_vertices

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        sys.exit(1)
    try:
        k, vertices, edges = gp.read_graph(sys.argv[1])
        print("El ejemplar de vertex cover es:")
        print(gp.format_graph(vertices, edges, k))
        vertices, edges, k, new_edges, new_vertices = vertex_cover_to_dominating_set(vertices, edges, k)
        print("El ejemplar de dominating set es:")
        print(gp.format_graph(vertices, edges, k))
        print("Nuevos vértices agregados:")
        print(new_vertices)
        print("Nuevas aristas agregadas:")
        print(new_edges)
    except FileNotFoundError:
        print(f"Error: file not found: {sys.argv[1]}")
        sys.exit(1)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
