#!/usr/bin/env python3
"""DPLL SAT solver — backtracking with unit propagation."""

def dpll(clauses, assignment=None):
    if assignment is None: assignment = {}
    clauses = [c for c in clauses if not any(assignment.get(abs(l)) == (l > 0) for l in c)]
    clauses = [frozenset(l for l in c if abs(l) not in assignment) for c in clauses]
    if not clauses: return assignment
    if frozenset() in clauses: return None
    # Unit propagation
    for c in clauses:
        if len(c) == 1:
            l = next(iter(c)); a = dict(assignment); a[abs(l)] = l > 0
            return dpll(clauses, a)
    # Pure literal
    lits = set(); [lits.update(c) for c in clauses]
    for l in list(lits):
        if -l not in lits:
            a = dict(assignment); a[abs(l)] = l > 0
            return dpll(clauses, a)
    # Branch
    v = abs(next(iter(next(iter(clauses)))))
    for val in [True, False]:
        a = dict(assignment); a[v] = val
        r = dpll(clauses, a)
        if r is not None: return r
    return None

def main():
    clauses = [{1,2},{-1,3},{-2,-3},{1,-2}]
    print(f"SAT: {dpll(clauses)}")

if __name__ == "__main__": main()
