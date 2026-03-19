# 📊 Normalverteilungs-Analyse Tool

Ein Projekt zur Demonstration von Normalverteilungen (Gaußsche Verteilung) mit umfassender Lizenz-Dokumentation.

## 🎯 Ziel

Dieses Projekt zeigt:
1. **Mathematische Konzepte**: Normalverteilung, Statistiken, Konfidenzintervalle
2. **Lizenzverwendung**: Wie man Lizenzen korrekt dokumentiert und verwendet
3. **Best Practices**: Professionelle Projektstruktur

## 📚 Was ist eine Normalverteilung?

Die **Normalverteilung** (auch Gaußsche Verteilung) ist:
- Eine kontinuierliche Wahrscheinlichkeitsverteilung
- Die häufigste Verteilung in der Natur und Gesellschaft
- Charakterisiert durch zwei Parameter: Mittelwert (μ) und Standardabweichung (σ)

**Beispiele:**
- Körpergröße von Menschen
- IQ-Werte
- Messfehler
- Produktqualität

### Die 68-95-99.7 Regel

- **68%** der Daten liegen innerhalb von ±1σ
- **95%** der Daten liegen innerhalb von ±2σ
- **99.7%** der Daten liegen innerhalb von ±3σ

## 🔧 Installation

### Voraussetzungen
- Python 3.7+
- pip (Python-Paketmanager)

### Schritt-für-Schritt

```bash
# 1. Repository klonen (if not already done)
git clone https://github.com/asistek95/190326_licence_uebung_asistek.git
cd 190326_licence_uebung_asistek

# 2. Virtual Environment erstellen (empfohlen)
python -m venv venv

# 3. Virtual Environment aktivieren
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Abhängigkeiten installieren
pip install -r requirements.txt
```

## 🚀 Verwendung

```bash
# Führe die Hauptanalyse durch
python normal_distribution.py
```

**Ergebnis:**
- Statistiken für verschiedene Normalverteilungen
- 3 Grafiken werden erstellt:
  - `nv_standard.png` - Standardverteilung
  - `nv_koerpergroesse.png` - Körpergröße-Beispiel
  - `nv_iq.png` - IQ-Test Beispiel

## 📖 Projektstruktur

```
190326_licence_uebung_asistek/
├── LICENSE                  ← MIT-Lizenz
├── README.md               ← Diese Datei
├── README_LIZENZEN.md      ← Detaillierte Lizenz-Dokumentation
├── requirements.txt        ← Python-Abhängigkeiten
└── normal_distribution.py  ← Hauptprogramm
```

## 📋 Lizenz

Dieses Projekt ist unter der **MIT-Lizenz** lizenziert - siehe [LICENSE](LICENSE) für Details.

### Abhängigkeiten:
| Paket | Lizenz | Zweck |
|-------|--------|-------|
| numpy | BSD-3-Clause | Numerische Berechnungen |
| scipy | BSD-3-Clause | Statistische Funktionen |
| matplotlib | PSF | Visualisierungen |

## 💡 Lizenz-Erklärung

**Warum sind Lizenzen wichtig?**
- ✅ Rechtliche Klarheit über Nutzungsrechte
- ✅ Schutz für Autoren und Nutzer
- ✅ Transparenz über Bedingungen
- ✅ Professionelle Darstellung

**MIT-Lizenz bedeutet:**
- ✅ Du darfst kommerziell nutzen
- ✅ Du darfst ändern
- ✅ Du darfst weitergeben
- ⚠️ Du musst die Lizenz erwähnen
- ❌ Keine Haftung

➡️ **Siehe [README_LIZENZEN.md](README_LIZENZEN.md) für detaillierte Erklärungen!**

## 📊 Code-Beispiele

### Beispiel 1: Standardnormalverteilung erstellen

```python
from normal_distribution import NormalDistribution

# Erstelle eine Normalverteilung mit μ=0, σ=1
dist = NormalDistribution(mean=0, std_dev=1)

# Berechne Wahrscheinlichkeitsdichte am Punkt x=0
pdf_value = dist.pdf(0)  # 0.3989

# Berechne kumulierte Wahrscheinlichkeit P(X ≤ 1)
cdf_value = dist.cdf(1)  # 0.8413
```

### Beispiel 2: Stichproben generieren

```python
# Generiere 1000 Stichproben
samples = dist.generate_samples(size=1000)

# Berechne Konfidenzintervall (1σ)
lower, upper, prob = dist.calculate_interval(sigma=1)
print(f"1σ Intervall: [{lower:.2f}, {upper:.2f}] - {prob*100:.1f}% Wahrscheinlichkeit")
```

### Beispiel 3: IQ-Verteilung analysieren

```python
iq_dist = NormalDistribution(mean=100, std_dev=15)

# Wie viel % der Population hat IQ > 130?
p_hochbegabt = 1 - iq_dist.cdf(130)
print(f"Hochbegabt (IQ > 130): {p_hochbegabt*100:.2f}%")
```

## 🧮 Mathematische Formeln

### PDF (Wahrscheinlichkeitsdichte)
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### CDF (Verteilungsfunktion)
$$F(x) = \frac{1}{2}\left(1 + \text{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right)$$

## 🔗 Externe Ressourcen

- **Wikipedia Normalverteilung:** https://de.wikipedia.org/wiki/Normalverteilung
- **NumPy Dokumentation:** https://numpy.org/
- **SciPy Statistik:** https://docs.scipy.org/doc/scipy/reference/stats.html
- **Matplotlib Galerie:** https://matplotlib.org/gallery.html

## ⚠️ Fehlerbehebung

### Problem: "ModuleNotFoundError: No module named 'numpy'"

**Lösung:**
```bash
pip install numpy scipy matplotlib
```

### Problem: Grafiken werden nicht angezeigt

**Lösung:**
Grafiken werden als PNG-Dateien gespeichert. Überprüfe das aktuelle Verzeichnis.

## 👨‍💻 Autor

Projekt zur Übung: Lizenzverwendung und mathematische Modelle

## 📝 Verbesserungsmöglichkeiten

- [ ] Weitere Verteilungen (t-Verteilung, Chi-Quadrat)
- [ ] Hypothesentests implementieren
- [ ] Web-Interface (Flask/Streamlit)
- [ ] Mehr Beispieldatensätze
- [ ] Performancer-Optimierungen für große Stichproben

## 📞 Support

Bei Fragen: siehe [README_LIZENZEN.md](README_LIZENZEN.md) für Lizenz-Spezifika

---

**Letzte Aktualisierung:** 19. März 2026
