def dpll_sat_solve(clause_set, partial_assignment):
    def make_list_of_variable(clause_set):
        set_of_variable = set()
        for lists in clause_set:
            for literal in lists:
                if literal < 0:
                    x = literal*-1
                    set_of_variable.add(x)
                else:
                    set_of_variable.add(literal)
        list_of_variable = list(set_of_variable)
        return list_of_variable
        
    def unit_propagate_advance(clause_set):
        removed = []
        while 1 in [len(x) for x in clause_set]:
            i = [len(x) for x in clause_set].index(1)
            x = clause_set[i][0]
            removed.append(x)

            clause_set = [clause for clause in clause_set if x not in clause]
            x = x*-1
            for i in range(len(clause_set)):
                clause_set[i] = [item for item in clause_set[i] if item != x]
            
        return clause_set, set(removed)
    
    def pure_literal_eliminate_advance(clause_set):
        removed_pure = set()
        def find_pure(clause_set):
            set_of_variable = set()
            for lists in clause_set:
                for literal in lists:
                    set_of_variable.add(literal)
            list_of_variable = list(set_of_variable)
            
            pure_list =[]
            for variable in list_of_variable:
                x = int(variable*-1)
                if x not in list_of_variable:
                    pure_list.append(variable)
                    removed_pure.add(variable)
            return pure_list
        
        while find_pure(clause_set):
            pure_list = find_pure(clause_set)
            clause_set = [clause for clause in clause_set if not bool(set(clause).intersection(set(pure_list)))]

        return clause_set, removed_pure

    def solve(clause_set, partial_assignment):

        up_clause_set, removed_up = unit_propagate_advance(clause_set)
        pl_clause_set, removed_pl = pure_literal_eliminate_advance(up_clause_set)

        if removed_up:
            partial_assignment.append(removed_up)

        for item in removed_pl:
            empty = []
            empty.append(item)
            pl_clause_set.append(empty)
        
        if pl_clause_set == []:
            return True, partial_assignment

        if [] in pl_clause_set:
            if partial_assignment:
                partial_assignment.pop()
            return False

        list_of_v = make_list_of_variable(pl_clause_set)
        x = list_of_v[0]
        y = x*-1
        listedx = [[x]]
        listedy = [[y]]

        new_clause_set = pl_clause_set + listedx
        new_clause_set2 = pl_clause_set + listedy 

        if solve(new_clause_set, partial_assignment):
            return True, partial_assignment
        
        elif solve(new_clause_set2, partial_assignment):
            return True, partial_assignment

        else:
            if partial_assignment:
                partial_assignment.pop()
            return False


    result = solve(clause_set, [])
    if result == False:
        return "unsat"

    else:
        list_of_assignments = result[1]
        flat_list = [item for sublist in list_of_assignments for item in sublist]
        flat_list.sort()
        return flat_list
    

def dimacs_load(filename):
    clause_set=[]
    raw_file = open(str(filename), "r")

    stripped = [s.strip() for s in raw_file.readlines()]

    stripped = stripped[1:]

    for clauses in stripped:
        clauses = clauses.split()
        clauses = [int(i) for i in clauses]
        clauses = clauses[:-1]
        clause_set.append(clauses)
        
    return clause_set


#load text file here
clause_sett = dimacs_load('8queens.txt')
print(dpll_sat_solve(clause_sett,[]))

  