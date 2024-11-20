import os
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
def load_data(filepath):
    """
    Charge les données depuis un fichier CSV.

    Args:
        filepath (str): Chemin vers le fichier CSV.

    Returns:
        pandas.DataFrame: Données chargées sous forme de DataFrame, ou None en cas d'erreur.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None

# Filtrer les patients ayant un label donné
def filter_by_label(data, label):
    """
    Filtre les données pour ne conserver que les patients ayant un label donné.

    Args:
        data (pandas.DataFrame): Données chargées.
        label (int): Label à filtrer.

    Returns:
        pandas.DataFrame: Données filtrées.
    """
    return data[data['Label'] == label]

# Afficher un graphique des âges des patients ayant un label spécifique
def plot_ages(filtered_data, label):
    """
    Génère un graphique des âges des patients ayant un label donné.

    Args:
        filtered_data (pandas.DataFrame): Données filtrées.
        label (int): Label utilisé pour filtrer.
    """
    plt.bar(filtered_data['Name'], filtered_data['Age'])
    plt.xlabel("Nom des patients")
    plt.ylabel("Âge")
    plt.title(f"Âge des patients avec label {label}")
    os.makedirs("results", exist_ok=True)
    plt.savefig(f"results/ages_label{label}.png")
    plt.show()

if __name__ == "__main__":
    # Charger le fichier CSV
    filepath = "data_analysis/patients.csv"
    data = load_data(filepath)

    if data is not None:
        # Saisir le label à analyser
        try:
            label = int(input("Entrez le label à filtrer : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier pour le label.")
            exit(1)

        # Filtrer les patients
        filtered_data = filter_by_label(data, label)
        if filtered_data.empty:
            print(f"Aucun patient trouvé avec le label {label}.")
        else:
            print(f"Patients avec label {label} :")
            print(filtered_data)

            # Afficher le graphique des âges
            plot_ages(filtered_data, label)
