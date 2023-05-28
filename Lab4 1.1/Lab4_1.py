import pandas as pd

def get_upper_approximation(decision_system):
    n, m = decision_system.shape
    attributes = set(range(m - 1))
    upper_approximation = set(range(m - 1))
    while attributes:
        attr = attributes.pop()
        new_upper_approximation = upper_approximation - {attr}
        rows = decision_system.iloc[:, list(new_upper_approximation)]
        unique_rows = rows.drop_duplicates()
        if len(unique_rows) == n:
            upper_approximation = new_upper_approximation
        else:
            attributes -= {attr}
    return upper_approximation

def get_rules(decision_system, reduct):
    unique_rows = decision_system.iloc[:, list(reduct) + [-1]].drop_duplicates()
    rules = []
    for _, row in unique_rows.iterrows():
        conditions = [f"{col} = {row[col]}" for col in reduct]
        rule = f"Jeśli {' i '.join(conditions)}, to dec = {row['dec']}"
        rules.append(rule)
    return rules


decision_system2 = pd.DataFrame({
    'a1': ['wysoka', 'wysoka', 'wysoka', 'więcej niż średnia', 'więcej niż średnia', 'więcej niż średnia', 'wysoka', 'więcej niż średnia', 'więcej niż średnia'],
    'a2': ['bliski', 'bliski', 'bliski', 'daleki', 'daleki', 'daleki', 'bliski', 'daleki', 'daleki'],
    'a3': ['średni', 'średni', 'średni', 'silny', 'silny', 'lekki', 'średni', 'lekki', 'lekki'],
    'dec': ['tak', 'tak', 'tak', 'nie pewne', 'nie', 'nie', 'tak', 'nie', 'tak']
})

# Zadanie 4
print("\nZadanie 4")
reduct2 = get_upper_approximation(decision_system2)
print(f"Redukt decyzyjny dla Fig. 2: {reduct2}")

rules2 = get_rules(decision_system2, reduct2)
print("Reguły wygenerowane z otrzymanego reduktu decyzyjnego dla Fig. 2:")
for rule in rules2:
    print(rule)
