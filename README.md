Graph theory based approach to identify phase transitions in condensed matter
==============

This repository contains the implementation of key algorithms, computed results, and Python scripts for visualizing all figures from the article "Graph theory based approach to identify phase transitions in condensed matter".

The related article is published in Physical Review B (PRB) and can be accessed at https://journals.aps.org/prb/abstract/10.1103/PhysRevB.111.054116.

Algorithm Implementation
-----------------

Due to space constraints, the [PRB article](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.111.054116) only outlines the core idea of the algorithm and does not delve into every detail. The detailed implementation of the cut distance algorithm can be found in [Algorithm.pdf](Algorithm.pdf) in this repository.

Please note that its content is consistent with [Algorithm.md](Algorithm.md), but since GitHub does not support rendering LaTeX formulas in markdown files, the markdown version may not display correctly.

Implementation of Cut Distance (All Languages)
-----------------

The Implementation of Cut Distance in pure C, C++, Java, Python, Fortran, Matlab, and Mathematica (including both imperative and functional programming).

See repo https://github.com/anwanguow/cut_dist_all_languages.

Computation and Testing of Cut Distance (Python)
-----------------

See "cut_dist" directory.

Molecular Dynamics (MD) Simulation
-----------------

See "MD_simulation" directory for the LAMMPS scripts.

Graph Construction:
Fully connected graphs with edge weights representing the spatial distances of particles.

Figures
-----------------

The generation of Fig.6 requires the complete trajectory data from the KA system simulation. This data has been uploaded to Baidu Netdisk at the following link: https://pan.baidu.com/s/13V_jR030NeefVrGKnXca4Q and the access code is: f9ud. For readers who do not have access to Baidu Netdisk, please contact me directly if you need this data. My email is amturing@outlook.com.


All python scripts in "Plot" directory reproduces the computed figures in the article, including Fig.2b), Fig.2c), Fig.3a), Fig.3b), Fig.4a), Fig.4b), Fig.5b), Fig.5c), Fig.8a) and Fig.8b). Besides, the generated figures are saved in "Figure" directory, demonstrated as follow:


Fig.2b)

<img src="./fig/Fig_2b.png" alt="Fig_2b" title="Fig_2b" width="300">

Fig.2c)

<img src="./fig/Fig_2c.png" alt="Fig_2c" title="Fig_2c" width="300">

Fig.3a)

<img src="./fig/Fig_3a.png" alt="Fig_3a" title="Fig_3a" width="300">

Fig.3b)

<img src="./fig/Fig_3b.png" alt="Fig_3b" title="Fig_3b" width="300">

Fig.4a)

<img src="./fig/Fig_4a.png" alt="Fig_4a" title="Fig_4a" width="300">

Fig.4b)

<img src="./fig/Fig_4b.png" alt="Fig_4b" title="Fig_4b" width="300">

Fig.5b)

<img src="./fig/Fig_5b.png" alt="Fig_5b" title="Fig_5b" width="450">

Fig.5c)

<img src="./fig/Fig_5c.png" alt="Fig_5c" title="Fig_5c" width="450">

Fig.8a)

<img src="./fig/Fig_8a.png" alt="Fig_8a" title="Fig_8a" width="450">

Fig.8b)

<img src="./fig/Fig_8b.png" alt="Fig_8b" title="Fig_8b" width="450">

Reference
-----------------

Please consider adding the following citation if you use this work in your research.

```bibtex
@article{PhysRevB.111.054116,
  title = {Graph theory based approach to identify phase transitions in condensed matter},
  author = {Wang, An and Sosso, Gabriele C.},
  journal = {Phys. Rev. B},
  volume = {111},
  issue = {5},
  pages = {054116},
  numpages = {10},
  year = {2025},
  month = {Feb},
  publisher = {American Physical Society},
  doi = {10.1103/PhysRevB.111.054116},
  url = {https://link.aps.org/doi/10.1103/PhysRevB.111.054116}
}
```

Contact:
-----------------
An Wang: amturing@outlook.com
