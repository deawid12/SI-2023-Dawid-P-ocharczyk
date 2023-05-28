import itertools


def sp(regul, decision_system):
    for reg in regul:
        for row in decision_system:
            if all(reg[attr] == row[attr] for attr in reg):
                if reg['d'] != row['d']:
                    return False
    return True


def f_regul(decision_system):
    attributes = len(decision_system[0]) - 1
    regul = []
    now_regul = True

    while now_regul:
        now_regul = False
        for row in decision_system:
            for length in range(1, attributes + 1):
                for combination in itertools.combinations([f'a{i+1}' for i in range(attributes)], length):
                    reg = {attr: row[attr] for attr in combination}
                    reg['d'] = row['d']
                    if sp([reg], decision_system):
                        regul.append(reg)
                        decision_system = [r for r in decision_system if not all(reg[attr] == r[attr] for attr in reg)]
                        now_regul = True
                        break
                if now_regul:
                    break
            if now_regul:
                break

    return regul


decision_system = [
    {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 1, 'a5': 3, 'a6': 1, 'd': 1},
    {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 1, 'a5': 3, 'a6': 2, 'd': 1},
    {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 3, 'a5': 2, 'a6': 1, 'd': 0},
    {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 3, 'a5': 3, 'a6': 2, 'd': 1},
    {'a1': 1, 'a2': 1, 'a3': 2, 'a4': 1, 'a5': 2, 'a6': 1, 'd': 0},
    {'a1': 1, 'a2': 1, 'a3': 2, 'a4': 1, 'a5': 2, 'a6': 2, 'd': 1},
    {'a1': 1, 'a2': 1, 'a3': 2, 'a4': 2, 'a5': 3, 'a6': 1, 'd': 0},
    {'a1': 1, 'a2': 1, 'a3': 2, 'a4': 2, 'a5': 4, 'a6': 1, 'd': 1},
]

regul = f_regul(decision_system)
print("Reguły:")
for reg in regul:
    conditions = [f"({attr} = {reg[attr]})" for attr in reg if attr != 'd']
    conclusion = f"(d = {reg['d']})"
    print(f"Reguła: {' ∧ '.join(conditions)} ⇒ {conclusion}")
