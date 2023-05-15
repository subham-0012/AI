def unify(x, y, theta):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.startswith('?'):
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.startswith('?'):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for xi, yi in zip(x, y):
            theta = unify(xi, yi, theta)
            if theta is None:
                return None
        return theta
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def resolve(c1, c2):
    resolvents = []
    for l1 in c1:
        for l2 in c2:
            if l1[0] == 'not' and l2[0] != 'not' and l1[1] == l2:
                resolvent = c1 + c2
                resolvent.remove(l1)
                resolvent.remove(l2)
                resolvents.append(resolvent)
            elif l1[0] != 'not' and l2[0] == 'not' and l1 == l2[1]:
                resolvent = c1 + c2
                resolvent.remove(l1)
                resolvent.remove(l2)
                resolvents.append(resolvent)
    return resolvents

# Example usage:
theta = {'?e': 'apple', '?y': 'banana'}
print(unify('?x', '?y', theta))

clause1 = [['not', 'p'], 'q']
clause2 = [['not', 'q'], 'r']
print(resolve(clause1, clause2))
