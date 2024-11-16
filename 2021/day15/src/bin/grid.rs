use std::fmt;

#[derive(Clone)]
pub struct Grid<T> {
    pub rows: Vec<Vec<T>>,
}

impl Grid<u32> {
    pub fn nof_rows(&self) -> usize {
        self.rows.len()
    }

    pub fn nof_cols(&self) -> usize {
        self.rows[0].len()
    }

    pub fn from_txt(text: &str) -> Grid<u32> {
        let rows: Vec<Vec<u32>> = text
            .lines()
            .map(|line| line.chars().map(|c| c.to_digit(10).unwrap()).collect())
            .collect();
        Grid { rows }
    }

    // pub fn diagonal_neighbors(&self, coordinate: (usize, usize)) -> Vec<(usize, usize)> {
    //     let mut neighbors: Vec<(usize, usize)> = Vec::new();

    //     let drs: Vec<isize> = [-1, 0, 1].to_vec();

    //     for dr in drs {
    //         let dcs: Vec<isize> = [-1, 0, 1].to_vec();
    //         for dc in dcs {
    //             if (coordinate.0 as isize + dr) >= 0
    //                 && ((coordinate.0 as isize + dr) as usize) < self.nof_rows()
    //                 && (coordinate.1 as isize + dc) >= 0
    //                 && ((coordinate.1 as isize + dc) as usize) < self.nof_cols()
    //             {
    //                 neighbors.push((
    //                     usize::try_from(coordinate.0 as isize + dr).unwrap(),
    //                     usize::try_from(coordinate.1 as isize + dc).unwrap(),
    //                 ))
    //             }
    //         }
    //     }
    //     neighbors
    // }

    pub fn manhattan_neighbors(&self, coordinate: (usize, usize)) -> Vec<(usize, usize)> {
        let mut neighbors: Vec<(usize, usize)> = Vec::new();

        let ds: Vec<(isize, isize)> = [(1, 0), (0, 1), (-1, 0), (0, -1)].to_vec();

        for d in ds {
            if (coordinate.0 as isize + d.0) >= 0
                && ((coordinate.0 as isize + d.0) as usize) < self.nof_rows()
                && (coordinate.1 as isize + d.1) >= 0
                && ((coordinate.1 as isize + d.1) as usize) < self.nof_cols()
            {
                neighbors.push((
                    usize::try_from(coordinate.0 as isize + d.0).unwrap(),
                    usize::try_from(coordinate.1 as isize + d.1).unwrap(),
                ))
            }
        }
        neighbors
    }
}

impl fmt::Debug for Grid<u32> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let grid_str: String = self
            .rows
            .clone()
            .into_iter()
            .map(|r| {
                r.into_iter()
                    .map(|v| v.to_string())
                    .collect::<Vec<String>>()
                    .join("")
            })
            .collect::<Vec<String>>()
            .join("\n");

        let nof_rows = self.nof_rows();
        let nof_cols = self.nof_cols();
        write!(f, "Grid [{}x{}]\n\n{}\n", nof_rows, nof_cols, grid_str)
    }
}

impl IntoIterator for Grid<u32> {
    type Item = Vec<u32>;
    type IntoIter = std::vec::IntoIter<Self::Item>;

    fn into_iter(self) -> Self::IntoIter {
        self.rows.into_iter()
    }
}
