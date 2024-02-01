from typing import List

from utils.graph import Graph


def main() -> None:
    vertexes: int = 0
    graph: List[List[int]] = []
    try:
        with open("data/input.txt", "r", encoding="utf-8") as file:
            vertexes = int(file.readline())
            for _ in range(vertexes):
                row = list(map(int, file.readline().split()))
                graph.append(row)

        gr = Graph(graph)
        print("Исходный граф:")
        print(gr)

        gr.show_graph()

    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()
