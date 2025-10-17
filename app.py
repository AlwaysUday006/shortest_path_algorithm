import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# --- Streamlit Page Config ---
st.set_page_config(page_title="Custom Shortest Path Finder", page_icon="🧭", layout="wide")

# --- Page Title ---
st.markdown(
    """
    <h1 style='text-align: center;'>🧭 Custom Shortest Path Finder</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>
        Build your own graph, visualize it, and find the shortest path interactively!
    </p>
    """,
    unsafe_allow_html=True,
)

# --- Initialize Session State ---
if "graph" not in st.session_state:
    st.session_state.graph = {}

# --- Shortest Path Algorithm ---
def shortest_path(graph, start, target=''):
    if start not in graph:
        return None, None

    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                paths[node] = paths[current] + [node]
        unvisited.remove(current)

    return distances, paths

# --- Draw Graph Function ---
def draw_graph(graph, path=None):
    if not graph:
        st.warning("⚠️ Graph is empty! Add some nodes first.")
        return

    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(7, 5))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1200)
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    if path and len(path) > 1:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')

    st.pyplot(plt)

# --- Function to Add Edge ---
def add_edge(node1, node2, distance):
    graph = st.session_state.graph
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append((node2, distance))
    graph[node2].append((node1, distance))

# --- Split Page Layout ---
left_col, right_col = st.columns(2, gap="large")

# -------------------------------------------------------------
# 🧭 LEFT SIDE: GRAPH BUILDER + VISUALIZER
# -------------------------------------------------------------
with left_col:
    st.subheader("🧭 Build & Visualize Graph")

    with st.form("add_edge_form"):
        col1, col2, col3 = st.columns(3)
        node1 = col1.text_input("From Node:", placeholder="e.g., A").strip().upper()
        node2 = col2.text_input("To Node:", placeholder="e.g., B").strip().upper()
        distance = col3.number_input("Distance", min_value=1, step=1)

        submitted = st.form_submit_button("Add Edge")
        if submitted:
            if not node1 or not node2:
                st.error("⚠️ Please enter both node names.")
            elif node1 == node2:
                st.error("⚠️ Start and End nodes must be different.")
            else:
                add_edge(node1, node2, distance)
                st.success(f"✅ Added edge: {node1} ↔ {node2} (Distance: {distance})")

    if st.session_state.graph:
        st.markdown("### 🗺️ Current Graph Data")
        for node, edges in st.session_state.graph.items():
            st.write(f"**{node}** → {edges}")

        draw_graph(st.session_state.graph)
    else:
        st.info("Add some edges above to start building your graph.")

    if st.button("🧹 Reset Graph"):
        st.session_state.graph = {}
        st.success("Graph cleared successfully!")

# -------------------------------------------------------------
# 🎯 RIGHT SIDE: SHORTEST PATH FINDER
# -------------------------------------------------------------
with right_col:
    st.subheader("🎯 Find Shortest Path")

    start = st.text_input("Enter Start Node:", placeholder="e.g., A").strip().upper()
    target = st.text_input("Enter Target Node:", placeholder="e.g., D").strip().upper()

    if st.button("Find Shortest Path"):
        if not st.session_state.graph:
            st.error("⚠️ Please build a graph first!")
        elif not start or not target:
            st.error("⚠️ Please enter both start and target nodes.")
        elif start not in st.session_state.graph or target not in st.session_state.graph:
            st.error("⚠️ Invalid nodes! Make sure both exist in the graph.")
        else:
            distances, paths = shortest_path(st.session_state.graph, start, target)
            if not paths or not paths[target]:
                st.error("❌ No path found between the given nodes.")
            else:
                st.success(f"**Shortest Distance from {start} → {target}:** {distances[target]}")
                st.info(f"**Path:** {' → '.join(paths[target])}")
                draw_graph(st.session_state.graph, paths[target])
