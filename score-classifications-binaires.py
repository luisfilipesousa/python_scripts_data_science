# Scores pour un algorithme de classification binaire (1 ou 0)

# Selection des valeurs test et prédites
y_test =
y_pred =

# matrice de confusion
# True Negatives , False Negatives
# False Positives , True Positives
M = metrics.confusion_matrix(y_test, y_pred)

# recall : taux de vrai positifs sur le nombre de positifs total
recall = M[1][1]/(M[1][1]+M[0][1])

# precision : taux de vrai positif sur le nombre de positifs déclarés
precision = M[1][1]/(M[1][1]+M[1][0])

# f_mesure : moyenne harmonique du recall et de la precision
f_mesure = (2*precision*recall)/(precision + recall)

# specificity : taux de vrai négatifs sur le nombre de négatifs total
specificity = M[0][0]/(M[1][0]+M[0][0])
