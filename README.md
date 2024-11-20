# Question 4 TP2 - Concepts en Python et Analyse de Données

**Cours :** 8INF957 – Programmation Objet Avancée  
**Session :** Automne 2024  
**Remis par :** Antonin Claudel  
**Code Permanent :** CLAA04020300  
**Groupe :** 01  
**Enseignant :** Hamid Mcheick  

---

## Description du projet

Ce projet est divisé en deux parties principales :  

1. **Exploration des concepts avancés de la programmation orientée objet (POO) :**
   - Polymorphisme
   - Surcharge des méthodes
   - Redéfinition des méthodes
   - Généricité
   - Modularité

   Chaque concept est illustré avec des exemples clairs et exécutables. Ces démonstrations sont regroupées dans le dossier `concepts/`.

2. **Analyse de données avec Python :**
   - Utilisation des bibliothèques **pandas** et **matplotlib**.
   - Étude de cas basée sur un fichier CSV contenant des données fictives de patients.
   - Filtrage des patients avec un label spécifique (ex. label 4) et visualisation de leurs âges sous forme de graphique.

---

## Structure du projet

```
tp2_question4/
├── README.md               # Ce fichier
├── main.py                 # Script principal pour exécuter les concepts de la POO
├── concepts/               # Dossier contenant les démonstrations des concepts de la POO
│   ├── __init__.py
│   ├── generics.py
│   ├── modularity.py
│   ├── overloading.py
│   ├── overriding.py
│   ├── polymorphism.py
├── data_analysis/          # Dossier contenant les scripts et données pour l'analyse
│   ├── analysis.py         # Script Python pour l'analyse des données
│   ├── patients.csv        # Fichier CSV contenant les données de test
└── results/                # Dossier contenant les résultats générés (graphiques)
```

---

## Instructions d'exécution

### Concepts de la POO

1. Naviguez dans le répertoire racine du projet.
2. Exécutez le fichier `main.py` pour tester tous les concepts :
   ```bash
   python main.py
   ```

### Analyse de données

1. Naviguez dans le répertoire racine du projet.
2. Exécutez le fichier `analysis.py` pour effectuer l'analyse :
   ```bash
   python data_analysis/analysis.py
   ```
3. Les résultats incluent :
   - Une sortie textuelle des patients avec un label spécifique.
   - Un graphique enregistré dans le répertoire `results/` (par exemple, `ages_label4.png`).

---

## Remarque supplémentaire

- Le fichier `.gitignore` a été configuré pour exclure les fichiers inutiles comme `__pycache__` ou les résultats temporaires.

---

**Date de remise :** 19 novembre 2024  
