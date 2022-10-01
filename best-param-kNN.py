# Calcul du meilleur paramètre k selon le score choisis pour optimiser un k-neirest-neighbors

# Bibliotèques nécéssaires
import numpy as np
from sklearn import model_selection, preprocessing, neighbors, metrics

# Sélectionner les données et la valeur à prédire
X = 
y =

# Transformation de la classe à prédire en valeur catégorielle 1 ou 0
# Remplire la condition la classification
condition =
y_class = np.where(condition, 1, 0)

# Séparer le dataset en données d'entrainement et données de test
# Remplire le test_size comme on le souhaite
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y_class, test_size=0.3)

# Recentrage des données
std_scale = preprocessing.StandardScaler().fit(X_train)
X_train_std = std_scale.transform(X_train)
X_test_std = std_scale.transform(X_test)

# Paramètres à tester
param_grid = {'n_neighbors':[3,5,7,9,11,13]}

# Score à optimiser
score=

# Implémentation du Grid Search
# Il effectue une validation croisée sur 'cv' folds pour chaque paramètres dans param_grid
clf = model_selection.GridSearchCV(
    neighbors.KNeighborsClassifier(),
    param_grid,
    cv=5,
    scoring=score)

# Fit les modèles pour chaque hyperparamère choisi et conserve le score de chaque
# clf conserve le fit du k-NN avec le meilleur score sur les données d'entrainement
clf.fit(X_train_std, y_train)

# Meilleurs paramètres pour le k-NN
clf.best_params_

# Afficher le(s) hyperparamètre(s) optimaux
print("Meilleur(s) hyperparamètre(s) sur le jeu d'entraînement:")
print(clf.best_params_)

# Afficher les performances correspondantes
print("Résultats de la validation croisée :")
for mean, std, params in zip(
        clf.cv_results_['mean_test_score'], # score moyen
        clf.cv_results_['std_test_score'],  # écart-type du score
        clf.cv_results_['params']           # valeur de l'hyperparamètre
    ):

    print("{} = {:.3f} (+/-{:.03f}) for {}".format(
        score,
        mean,
        std*2,
        params
    ) )

# Calcul des prédictions données par le k-NN
y_pred = clf.predict(X_test_std)

# Afficher le score de du modèle pour les données d'entrainement
print("\nSur le jeu de test : {:.3f}".format(metrics.accuracy_score(y_test, y_pred)))

