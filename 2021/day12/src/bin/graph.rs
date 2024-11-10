use std::{collections::HashSet, fmt};


#[derive(Clone)]
pub struct Graph {
    pub nodes: HashSet<String>,
    pub edges: HashSet<(String, String)>
}

impl Graph {
    pub fn neighbors(self, node: String) -> Vec<String>{
        let mut neighbors = Vec::new();
        for edge in self.edges {
            if edge.0 == node {
                neighbors.push(edge.1);
            }
        }
        neighbors
    }
}

impl fmt::Debug for Graph {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        // write!(f, "Graph")
        write!(f, "Graph(nodes={:?}, edges={:?})", self.nodes, self.edges)
    }
}
