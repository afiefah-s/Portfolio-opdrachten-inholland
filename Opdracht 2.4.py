x = 320
stap = 0

while x >= 4.5:
    stap = stap + 1
    x = x / 2

    verdunningsfactor = 2 ** stap

    print("Stap:", stap)
    print("Concentratie:", x)
    print("Totale verdunningsfactor:", verdunningsfactor)
    print()

