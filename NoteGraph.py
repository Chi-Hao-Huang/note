# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:40:56 2023

@author: gerar
"""


# 給定路徑
path = [[1, 7], [1, 3], [1, 2], [2, 3], [5, 6], [6, 8]]


# 使用 defaultdict 建立無向圖
from collections import defaultdict

def build_graph(paths):
    graph = defaultdict(list)
    
    for edge in paths:
        node1, node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)  # 因為是無向圖，所以要加上這一行

    return graph


# 使用 dict 建立無向圖
def build_undirected_graph(paths):
    graph = {}

    for edge in paths:
        node1, node2 = edge

        # 將 node2 加入 node1 的相鄰節點列表
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]

        # 將 node1 加入 node2 的相鄰節點列表
        if node2 in graph:
            graph[node2].append(node1)
        else:
            graph[node2] = [node1]

    return graph



# 圖形性質
def calculate_graph_properties(graph):
    num_nodes = len(graph)
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2  # 除以2是因為無向圖的邊是雙向的

    return num_nodes, num_edges


# 獨立分支數量
def count_connected_components(graph):
    visited = set()
    components = 0

    def dfs(node):
        # 將變量visited的作用域提升到最近的封閉範圍count_connected_components
        # 使得在嵌套函數中可以修改外層函數的變量
        nonlocal visited
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            components += 1
            dfs(node)

    return components


# 獨立的分支圖
def node_connected_graph(graph):
    visited = set()
    components = 0
    
    node_components = defaultdict(list)

    def dfs(node, components):
        # 將變量visited的作用域提升到最近的封閉範圍count_connected_components
        # 使得在嵌套函數中可以修改外層函數的變量
        nonlocal visited
        visited.add(node)
        node_components[components].append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, components)

    for node in graph:
        if node not in visited:
            components += 1
            dfs(node, components)

    return dict(node_components)


# 使用疊代方式，計算獨立分支數量及每個分支含有的節點數量
def node_connected_graph_stack(graph):
    visited = set()
    def dfs(node):
        stack = [node]
        visited.add(node)
        branch_size = 1  # 紀錄分支大小
    
        while stack:
            current_node = stack.pop()
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    branch_size += 1
    
        return branch_size

    num_branches = 0
    nodes_in_branches = []

    # 遍歷所有節點，計算獨立分支和每個分支的節點數量
    for node in graph:
        if node not in visited:
            num_branches += 1
            nodes_in_branches.append(dfs(node))

    return num_branches, nodes_in_branches




# 建立無向圖
graph = build_undirected_graph(path)

# 計算圖的性質
num_nodes, num_edges = calculate_graph_properties(graph)

# 計算獨立分支數量
num_components = count_connected_components(graph)

node_components = node_connected_graph(graph)

# 輸出結果
print("Graph representation:", graph)
print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Number of connected components:", num_components)
print("Node of connected graph:", node_components)




path = [[0, 1], [2, 3], [0, 4]]
n = 5



def build_undirected_graph(paths):
    graph = {}

    for edge in paths:
        node1, node2 = edge

        # 將 node2 加入 node1 的相鄰節點列表
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]

        # 將 node1 加入 node2 的相鄰節點列表
        if node2 in graph:
            graph[node2].append(node1)
        else:
            graph[node2] = [node1]

    return graph



def node_connected_graph_stack(graph):
    visited = set()
    def dfs(node):
        stack = [node]
        visited.add(node)
        branch_size = 1  # 紀錄分支大小
    
        while stack:
            current_node = stack.pop()
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    branch_size += 1
    
        return branch_size

    num_branches = 0
    nodes_in_branches = []

    # 遍歷所有節點，計算獨立分支和每個分支的節點數量
    for node in graph:
        if node not in visited:
            num_branches += 1
            nodes_in_branches.append(dfs(node))

    return num_branches, nodes_in_branches



graph = build_undirected_graph(path)
nodes_comb = node_connected_graph_stack(graph)

















