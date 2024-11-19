import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        return None

# Filtrer les patients ayant un label donné
def filter_by_label(data, label):
    return data[data['Label'] == label]

# Afficher un graphique des âges des patients ayant un label spécifique
def plot_ages(filtered_data):
    plt.bar(filtered_data['Name'], filtered_data['Age'])
    plt.xlabel("Nom des patients")
    plt.ylabel("Âge")
    plt.title("Âge des patients avec label 4")
    plt.show()

if __name__ == "__main__":
    # Charger le fichier CSV
    filepath = "data_analysis/patients.csv"
    data = load_data(filepath)

    if data is not None:
        # Filtrer les patients avec le label 4
        filtered_data = filter_by_label(data, 4)
        print("Patients avec label 4 :")
        print(filtered_data)

        # Afficher le graphique des âges
        plot_ages(filtered_data)
