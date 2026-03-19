"""
Normalverteilungs-Analyse Tool
==============================

Dieses Modul implementiert Funktionen zur Analyse und Visualisierung 
von Normalverteilungen (Gaußsche Verteilung).

Lizenzierung:
- Dieses Projekt steht unter der MIT-Lizenz (siehe LICENSE-Datei)
- Externe Abhängigkeiten:
  * numpy: BSD-Lizenz
  * scipy: BSD-Lizenz
  * matplotlib: PSF-Lizenz

Lizenzverwendung erklärt:
- MIT-Lizenz: Ermöglicht freie Nutzung, Modifikation und Weitergabe
  des Codes unter bestimmten Bedingungen
- Diese Libraries dürfen verwendet werden, solange ihre Lizenzen 
  respektiert werden
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


class NormalDistribution:
    """
    Klasse zur Verwaltung und Analyse von Normalverteilungen.
    
    Die Normalverteilung (Gauß-Verteilung) ist eine kontinuierliche 
    Wahrscheinlichkeitsverteilung, die in der Statistik sehr häufig auftritt.
    """
    
    def __init__(self, mean=0, std_dev=1):
        """
        Initialisiert eine Normalverteilung.
        
        Args:
            mean: Mittelwert (μ) der Verteilung
            std_dev: Standardabweichung (σ) der Verteilung
        """
        self.mean = mean
        self.std_dev = std_dev
        self.distribution = stats.norm(loc=mean, scale=std_dev)
    
    def pdf(self, x):
        """
        Probability Density Function (PDF) - Wahrscheinlichkeitsdichte
        
        Gibt die Wahrscheinlichkeitsdichte an Position x zurück.
        """
        return self.distribution.pdf(x)
    
    def cdf(self, x):
        """
        Cumulative Distribution Function (CDF) - Verteilungsfunktion
        
        Gibt die Wahrscheinlichkeit P(X ≤ x) zurück.
        """
        return self.distribution.cdf(x)
    
    def ppf(self, p):
        """
        Percent Point Function (PPF) - Quantilfunktion
        
        Gibt den Wert x zurück, für den P(X ≤ x) = p.
        """
        return self.distribution.ppf(p)
    
    def generate_samples(self, size=1000):
        """
        Generiert Stichproben aus der Normalverteilung.
        
        Args:
            size: Anzahl der zu generierenden Stichproben
            
        Returns:
            numpy array mit Stichproben
        """
        return np.random.normal(self.mean, self.std_dev, size)
    
    def calculate_interval(self, sigma=1):
        """
        Berechnet das Konfidenzintervall.
        
        Args:
            sigma: Anzahl der Standardabweichungen (1σ, 2σ, 3σ)
            
        Returns:
            Tupel (untere_grenze, obere_grenze)
        """
        lower = self.mean - sigma * self.std_dev
        upper = self.mean + sigma * self.std_dev
        probability = self.cdf(upper) - self.cdf(lower)
        return (lower, upper, probability)
    
    def print_statistics(self):
        """Gibt Statistiken der Verteilung aus."""
        print(f"\n=== Normalverteilung Statistik ===")
        print(f"Mittelwert (μ): {self.mean}")
        print(f"Standardabweichung (σ): {self.std_dev}")
        print(f"Varianz (σ²): {self.std_dev**2}")
        
        # 68-95-99.7 Regel
        print(f"\n68-95-99.7 Regel:")
        for sigma in [1, 2, 3]:
            lower, upper, prob = self.calculate_interval(sigma)
            print(f"{sigma}σ Intervall [{lower:.2f}, {upper:.2f}]: "
                  f"{prob*100:.2f}% der Daten")


def plot_distribution(mean=0, std_dev=1, samples=5000, filename="normalverteilung.png"):
    """
    Erstellt eine Visualisierung der Normalverteilung.
    
    Uses matplotlib (PSF-Lizenz) - siehe README_LIZENZEN.md
    
    Args:
        mean: Mittelwert
        std_dev: Standardabweichung
        samples: Anzahl der Zufallsstichproben
        filename: Dateiname für das Ausgabebild
    """
    dist = NormalDistribution(mean, std_dev)
    
    # Generiere Stichproben
    data = dist.generate_samples(samples)
    
    # Erstelle Figure mit zwei Subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Subplot 1: Histogram und PDF
    ax1.hist(data, bins=50, density=True, alpha=0.7, color='blue', 
             label='Stichproben Histogram', edgecolor='black')
    
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = dist.pdf(x)
    ax1.plot(x, y, 'r-', linewidth=2, label='Wahrscheinlichkeitsdichte (PDF)')
    
    # Markiere 68-95-99.7 Regel
    colors = ['green', 'orange', 'red']
    alphas = [0.3, 0.2, 0.1]
    for sigma, color, alpha in zip([1, 2, 3], colors, alphas):
        lower, upper, _ = dist.calculate_interval(sigma)
        ax1.axvline(lower, color=color, linestyle='--', alpha=0.7)
        ax1.axvline(upper, color=color, linestyle='--', alpha=0.7)
    
    ax1.set_xlabel('Wert')
    ax1.set_ylabel('Häufigkeit')
    ax1.set_title(f'Normalverteilung N(μ={mean}, σ={std_dev})')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Kumulative Verteilungsfunktion (CDF)
    ax2.plot(x, dist.cdf(x), 'b-', linewidth=2, label='CDF')
    ax2.axhline(0.5, color='red', linestyle='--', alpha=0.7, label='Median (50%)')
    ax2.fill_between(x, 0, dist.cdf(x), alpha=0.3)
    ax2.set_xlabel('Wert')
    ax2.set_ylabel('Kumulierte Wahrscheinlichkeit')
    ax2.set_title('Kumulative Verteilungsfunktion (CDF)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\n✓ Grafik gespeichert als: {filename}")
    plt.close()


def main():
    """Hauptfunktion - Beispiele für Normalverteilungsanalyse."""
    
    print("=" * 60)
    print("NORMALVERTEILUNGS-ANALYSE TOOL")
    print("=" * 60)
    print("\n📚 Lizenzinformation:")
    print("-" * 60)
    print("Dieses Projekt verwendet:")
    print("• MIT-Lizenz (Hauptprojekt) - Erlaubt kommerzielle Nutzung")
    print("• numpy (BSD-Lizenz) - Wissenschaftliche Berechnungen")
    print("• scipy (BSD-Lizenz) - Statistische Funktionen")
    print("• matplotlib (PSF) - Visualisierung")
    print("\nWARUM Lizenzen wichtig sind:")
    print("✓ Rechtliche Klarheit über Nutzungsrechte")
    print("✓ Schutz für Autor und Nutzer")
    print("✓ Transparenz über Bedingungen")
    print("-" * 60)
    
    # Beispiel 1: Standardnormalverteilung
    print("\n\n1️⃣  STANDARDNORMALVERTEILUNG (μ=0, σ=1)")
    print("-" * 60)
    normal = NormalDistribution(mean=0, std_dev=1)
    normal.print_statistics()
    
    # Beispiel 2: Körpergrößen-Verteilung
    print("\n\n2️⃣  KÖRPERGRÖSSEN-VERTEILUNG (realistische Daten)")
    print("-" * 60)
    heights = NormalDistribution(mean=170, std_dev=10)  # cm
    heights.print_statistics()
    
    print(f"\nWahrscheinlichkeit einer Person zwischen 160-180 cm:")
    p = heights.cdf(180) - heights.cdf(160)
    print(f"P(160 < X < 180) = {p*100:.2f}%")
    
    # Beispiel 3: IQ-Verteilung
    print("\n\n3️⃣  IQ-VERTEILUNG")
    print("-" * 60)
    iq = NormalDistribution(mean=100, std_dev=15)  # Standard IQ-Test
    iq.print_statistics()
    
    print(f"\nIQ-Klassifikation:")
    print(f"Minderbegabt (IQ < 70): {iq.cdf(70)*100:.2f}%")
    print(f"Durchschnitt (85-115): {(iq.cdf(115)-iq.cdf(85))*100:.2f}%")
    print(f"Hochbegabt (IQ > 130): {(1-iq.cdf(130))*100:.2f}%")
    
    # Visualisierungen erstellen
    print("\n\n4️⃣  VISUALISIERUNGEN ERSTELLEN")
    print("-" * 60)
    plot_distribution(mean=0, std_dev=1, filename="nv_standard.png")
    plot_distribution(mean=170, std_dev=10, filename="nv_koerpergroesse.png")
    plot_distribution(mean=100, std_dev=15, filename="nv_iq.png")
    
    print("\n" + "=" * 60)
    print("✓ Analyse abgeschlossen!")
    print("=" * 60)


if __name__ == "__main__":
    main()
