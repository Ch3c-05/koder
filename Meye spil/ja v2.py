from scipy.stats import binom
import matplotlib.pyplot as plt

# Meyer Rangliste (værdier højere end 53)
meyer_rangliste = [
    "21", "31", "66", "55", "44", "33", "22", "11",
    "65", "64", "63", "62", "61",
    "54", "53", "52", "51",
    "43", "42", "41", "32"
]

# Brugerinput
slag = input("Hvad slog modstanderen? (f.eks. '53'): ")
try:
    forsøg = int(input("Hvor mange gange vil du slå?: "))
    if forsøg <= 0:
        raise ValueError("Antallet af forsøg skal være et positivt heltal.")
except ValueError as e:
    print(f"Ugyldigt input: {e}")
    exit()

# Beregn sandsynligheden for at slå højere end slag
if slag in meyer_rangliste:
    index = meyer_rangliste.index(slag)
    p = (len(meyer_rangliste) - index - 1) / len(meyer_rangliste)
else:
    print("Ugyldig Meyer-værdi")
    exit()

# Udskriv sandsynligheden for at slå højere end slag
print(f"\nSandsynlighed for at slå højere end {slag} = {p:.3f}")

# Beregn sandsynligheden for mindst én succes i de forsøg
p_at_least_one_success = 1 - (1 - p)**forsøg

# Udskriv sandsynligheden for mindst én succes i forsøg
print(f"Sandsynlighed for at slå højere end {slag} mindst én gang i {forsøg} forsøg: {p_at_least_one_success:.3f}")

# Binomialfordeling - sandsynlighed for præcise succeser
print("\nSucceser | Sandsynlighed")
for k in range(forsøg + 1):
    prob = binom.pmf(k, forsøg, p)
    print(f"{k:9} | {prob:.4f}")

# Binomialfordeling Plot
X = range(forsøg + 1)
binom_pd = binom.pmf(X, forsøg, p)

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, binom_pd, 'bo', ms=8, label='Binomial pmf')
plt.ylabel("Sandsynlighed", fontsize="18")
plt.xlabel("X - Antal Succeser", fontsize="18")
plt.title(f"Binomialfordeling - Antal Succeser vs Sandsynlighed for {forsøg} Forsøg", fontsize="18")
ax.vlines(X, 0, binom_pd, colors='b', lw=5, alpha=0.5)

plt.legend()
plt.show()
