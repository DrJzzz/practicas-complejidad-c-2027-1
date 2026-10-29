import sys


def read_graph(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        raise ValueError("Input file is empty.")

    try:
        k = int(lines[0])
    except ValueError as exc:
        raise ValueError(f"Invalid k value: {lines[0]!r}") from exc

    vertices = []
    edges = []

    if len(lines) >= 2:
        vertex_tokens = lines[1].replace(",", " ").split()
        vertices = [str(v) for v in vertex_tokens]

    for line in lines[2:]:
        edge_tokens = line.replace(",", " ").split()
        if len(edge_tokens) < 2:
            continue
        u, v = str(edge_tokens[0]), str(edge_tokens[1])
        edges.append((u, v))

    return k, vertices, edges


def format_graph(vertices, edges, k):
    vertex_str = ",".join(str(v) for v in vertices)
    edge_str = ",".join(f"({u},{v})" for u, v in edges)
    return f"G=(V={{{vertex_str}}}, E={{{edge_str}}}), k={k}"