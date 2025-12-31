import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

def train_model():
    X = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv')
    Y = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv')['Class'].to_numpy()
    
    X = StandardScaler().fit_transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
    
    tree = DecisionTreeClassifier()
    params = {'criterion': ['gini', 'entropy'], 'max_depth': [4, 6, 8]}
    grid = GridSearchCV(tree, params, cv=10).fit(X_train, Y_train)
    
    print(f"Test Accuracy: {grid.score(X_test, Y_test):.4f}")

if __name__ == "__main__":
    train_model()