# Vector met concentraties
v = [10, 20, 30, 40, 49, 51, 60, 70,80]

# Drempelwaarde
drempel = 50

# Lege lijst voor hoge waarden
te_hoge_waarden = []

# For-loop:
# voor elke waarde in de lijst
for waarde in v:

    # If-statement:
    # controleer of de waarde groter is dan 50
    if waarde > drempel:
        # Print alleen de te hoge waarden
        print("Waarde te hoog:", waarde)

        # Voeg de waarde toe aan nieuwe lijst
        te_hoge_waarden.append(waarde)

# Nieuwe lijst tonen
print("Waarden voor heranalyse:", te_hoge_waarden)