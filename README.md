# 🧭 Custom Shortest Path Finder

An interactive **Python Streamlit app** to build your own graph, visualize it, and find the **shortest path** between nodes in real-time.

---

## 📌 Features

- **Graph Builder**: Add nodes and edges with custom distances.
- **Interactive Visualization**: Graph displayed using NetworkX & Matplotlib.
- **Shortest Path Finder**: Compute shortest distance and path between any two nodes.
- **Edge Highlighting**: Shortest path is highlighted in red on the graph.
- **Reset Graph**: Clear the current graph to start fresh.
- **Two-Column Layout**: 
  - Left: Build & visualize graph 🧭  
  - Right: Shortest path finder 🎯

---

## 🛠️ Technologies Used

- Python 3.x
- [Streamlit](https://streamlit.io/) – for interactive web app
- [NetworkX](https://networkx.org/) – graph data structure & algorithms
- [Matplotlib](https://matplotlib.org/) – graph visualization

---

## 🚀 How to Run

1. **Clone the repository** (or download the `app.py`):

```bash
git clone https://github.com/AlwaysUday006/shortest_path_algorithm.git

```
2. **Install dependencies:**

```bash
pip install streamlit networkx matplotlib
```
3. **Run the app:**
```bash
streamlit run app.py
```
4. **Open in browser:**
The app will open automatically, or visit http://localhost:8501.

## 📝 Usage Instructions

1. Build Graph (Left Panel):
	- Enter From Node and To Node names.
	- Enter the Distance between them.
	- Click Add Edge.
	- Repeat to add more edges and nodes (nodes are created automatically).
2. Visualize Graph:
	- The graph is displayed below the form.
	- Nodes are blue; edges display their distances.
3. Find Shortest Path (Right Panel):
	- Enter Start Node and Target Node.
	- Click Find Shortest Path.
	- The shortest path will be highlighted in red, with distance displayed.
4. Reset Graph:
	- Click Reset Graph to clear all nodes and edges.

## ⚡ Notes

- Node positions are currently managed by NetworkX’s layout algorithm and may change on each update.
- Only undirected edges are supported (distance is symmetric).
- Node names are case-insensitive but stored in uppercase.