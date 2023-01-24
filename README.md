# dpll-sat-solver
A SAT-solver using the David-Putnam-Logemann-Loveland algorithm to solve the Boolean satisfiability problem.

A recursive Python function that takes in the 2 arguments (clause set and partial assignment) and solves the satisfiability of the clause set by applying unit propagation and pure literal elimination before branching on the two truth assignments for a given variable. If the clause set is satisfiable under the partial assignment it should output a satisfying assignment. When run with an empty partial assignment it should act as a SAT-solver.

Sample input files are given in the .txt files. 
