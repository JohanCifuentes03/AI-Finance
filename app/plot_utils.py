import matplotlib.pyplot as plt
import numpy as np

def plot_normal_distribution(data):
    """
    Genera un histograma y una curva de distribución normal basada en los precios de cierre.
    """
    prices = data['Close']
    mean = prices.mean()
    std_dev = prices.std()

    plt.figure(figsize=(10, 6))
    plt.hist(prices, bins=30, density=True, alpha=0.6, color='blue', label="Precios de cierre")
    x = np.linspace(prices.min(), prices.max(), 100)
    y = (1 / (np.sqrt(2 * np.pi) * std_dev)) * np.exp(-0.5 * ((x - mean) / std_dev)**2)
    plt.plot(x, y, color='red', label="Distribución Normal")
    plt.title("Distribución Normal de los Precios de Cierre")
    plt.xlabel("Precio de cierre")
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig("normal_distribution.png")
    plt.close()
    return "normal_distribution.png"
