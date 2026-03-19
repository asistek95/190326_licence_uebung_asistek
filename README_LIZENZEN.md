# Lizenzverwendung und Erklärungen

## 📋 Übersicht

Dieses Projekt demonstriert die richtige Verwendung und Dokumentation von Lizenzen in einem Python-Projekt zur Normalverteilungsanalyse.

---

## 🎯 Warum sind Lizenzen wichtig?

### Rechtliche Gründe:
- **Schutz des Urheberrechts**: Klärt, wer Eigentümer des Codes ist
- **Klare Regeln**: Definiert, was andere mit deinem Code dürfen
- **Haftungsausschluss**: Schützt dich vor Haftung für Fehler
- **Rechtssicherheit**: Vermeidung von Streitigkeiten

### Praktische Gründe:
- **Transparenz**: Nutzer wissen genau, was sie dürfen
- **Vertrauen**: Zeigt professionelle Arbeit
- **Kompatibilität**: Klarheit beim Kombinieren verschiedener Komponenten
- **Open-Source-Kultur**: Ermöglicht Zusammenarbeit

---

## 📄 Lizenzen dieses Projekts

### 1. **MIT-Lizenz** (Hauptprojekt)
**Datei:** `LICENSE`

#### Was sie erlaubt:
✅ Kommerziell nutzen
✅ Modifizieren
✅ Weitergeben
✅ Privat nutzen

#### Was sie verlangt:
⚠️ Urheberrechtshinweis und Lizenztext einfügen
⚠️ Änderungen dokumentieren

#### Was verboten ist:
❌ Haftung übernehmen
❌ Marke/Markenname verwenden

**Beispiel:** Du kannst diesen Code nehmen, ändern, weiterverkaufen - musst aber die Original-Lizenz und Urheberrechtsangabe mitteilen.

---

## 🔗 Abhängigkeiten und deren Lizenzen

### NumPy - `BSD 3-Clause License`
```
import numpy as np
```
**Lizenz:** BSD-3-Clause
**Link:** https://github.com/numpy/numpy/blob/main/LICENSE.txt

**Was bedeutet das?**
- Kostenlos nutzbar
- Muss Lizenz beigelegt werden, aber nicht dieser Quellcode
- Verwendung: Mathematische und wissenschaftliche Berechnungen

### SciPy - `BSD License`
```
from scipy import stats
```
**Lizenz:** BSD-3-Clause
**Link:** https://github.com/scipy/scipy/blob/main/LICENSE.txt

**Was bedeutet das?**
- Ähnlich NumPy - BSD-Lizenz
- Verwendung: Statistische Funktionen und Verteilungen

### Matplotlib - `PSF (Python Software Foundation License)`
```
import matplotlib.pyplot as plt
```
**Lizenz:** PSF License
**Link:** https://github.com/matplotlib/matplotlib/blob/main/LICENSE/LICENSE

**Was bedeutet das?**
- Python-kompatible Lizenz
- Kostenlos nutzbar
- Verwendung: Grafiken und Visualisierungen erstellen

---

## ✅ So dokumentierst du Lizenzen richtig

### 1. Im Root-Verzeichnis
```
PROJECT/
├── LICENSE           ← Hauptlizenz deines Projekts
├── README.md
├── requirements.txt
└── src/
```

### 2. In der README.md
```markdown
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Third-party Libraries
- numpy: MIT License
- scipy: BSD License
- matplotlib: PSF License
```

### 3. Im Code (Dateiheader)
```python
"""
Dieses Modul steht unter MIT-Lizenz.
Siehe LICENSE für Details.

Abhängigkeiten:
- numpy: BSD-Lizenz
- scipy: BSD-Lizenz
"""
```

### 4. In requirements.txt
```
numpy>=1.20.0  # BSD-3-Clause License
scipy>=1.6.0   # BSD-3-Clause License
matplotlib>=3.3.0  # PSF License
```

---

## 📊 Lizenz Vergleich-Tabelle

| Lizenz | Kommerziell | Ändern | Teilen | Lizenz mitgeben | Haftung |
|--------|:-----------:|:-------:|:------:|:---------------:|:--------:|
| **MIT** | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **BSD-3** | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **GPL** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Apache 2.0** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Proprietary** | ❌ | ❌ | ❌ | N/A | Variabel |

---

## 🔍 Wann brauchst du welche Lizenz?

### MIT-Lizenz verwenden, wenn...
- Du willst maximale Freiheit für Nutzer
- Es dir egal ist, ob Code kommerzielle genutzt wird
- Du wenig Haftungsschutz brauchst
- Du einfaches, kurzes Lizenztext willst
**Beispiele:** Dieses Projekt, Bootstrap, jQuery

### GPL verwenden, wenn...
- Abgeleitete Werke auch Open-Source sein sollen („Copyleft")
- Du willst, dass Änderungen zurück fließen
- Du starke Gemeinschaft aufbauen willst
**Beispiele:** Linux, WordPress Kern

### Apache 2.0 verwenden, wenn...
- Du Patentschutz brauchst
- Du will klare Regeln für Markennutzung
- Professionelle Projekte
**Beispiele:** Android, Kubernetes

### Proprietär verwenden, wenn...
- Maximaler Kontrolle nötig
- Nur bestimmte Partner dürfen nutzen
- Kommerzielle Sensibilität
**Beispiele:** Microsoft Office, Adobe

---

## 🚀 Praktische Anleitung

### Schritt 1: README-Datei erstellen
```markdown
# Mein Projekt

## Installation
```

### Schritt 2: LICENSE-Datei hinzufügen
- Gehe zu https://choosealicense.com/
- Wähle Lizenz (z.B. MIT)
- Kopiere Text in `LICENSE` Datei

### Schritt 3: Abhängigkeiten dokumentieren
```bash
pip list > requirements.txt
# Dann manuell Lizenzen recherchieren
```

### Schritt 4: Im Code dokumentieren
```python
# Top des Hauptmoduls
"""
This project is licensed under MIT License.
External dependencies use BSD-3-Clause and PSF licenses.
"""
```

### Schritt 5: Zur Versionskontrolle hinzufügen
```bash
git add LICENSE README_LIZENZEN.md
git commit -m "Add license documentation"
```

---

## 📚 Zusätzliche Ressourcen

- **Choose a License:** https://choosealicense.com/
- **SPDX Lizenzliste:** https://spdx.org/licenses/
- **Kompatibilität Check:** https://www.synopsys.com/blogs/software-security/top-open-source-licenses/
- **GitHub Guide:** https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

---

## 💡 Zusammenfassung

| Was | Warum | Wie |
|-----|-------|-----|
| **Lizenz wählen** | Rechtliche Klarheit | choosealicense.com |
| **LICENSE-Datei** | Nennung der Lizenz | Im Root-Verzeichnis |
| **README** | Nutzer informieren | Sektion mit Links |
| **Code-Header** | Dokumentation | Docstring am Anfang |
| **requirements.txt** | Abhängigkeiten tracen | Mit Lizenzanmerkungen |

---

**Tipp:** Lizenzen sind nicht kompliziert - sie schützen dich und andere! 🛡️

