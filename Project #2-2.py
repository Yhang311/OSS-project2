import pandas as pd

def sort_dataset(dataset_df):
    #TODO: Implement this function
    sort = dataset_df.sort_values(by='p_year',ascending=True)
    return sort

def split_dataset(dataset_df):
    #TODO: Implement this function
    labels = dataset_df['salary']*0.001
    
    train_df = dataset_df.iloc[:1718]
    test_df = dataset_df.iloc[1718:]
    
    X_train = train_df.drop('salary',axis =1)
    X_test = test_df.drop('salary',axis =1)
    
    Y_train = labels.iloc[:1718]
    Y_test = labels.iloc[1718:]
    
    return X_train, X_test, Y_train, Y_test
    
def extract_numerical_cols(dataset_df):
    #TODO: Implement this function
    type =  ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
    typedf = dataset_df[type]
    
    return typedf

def train_predict_decision_tree(X_train, Y_train, X_test):
    #TODO: Implement this function
    tree_model = DecisionTreeRegressor()
    tree_model.fit(X_train,Y_train)
    tree_pre = tree_model.predict(X_test)
    return tree_pre

def train_predict_random_forest(X_train, Y_train, X_test):
    #TODO: Implement this function
    rf_model = RandomForestRegressor()
    rf_model.fit(X_train,Y_train)
    rf_pre = rf_model.predict(X_test)
    return rf_pre

def train_predict_svm(X_train, Y_train, X_test):
    #TODO: Implement this function
    svm_model =make_pipeline(StandardScaler(), SVR())
    svm_model.fit(X_train, Y_train)
    svm_pre = svm_model.predict(X_test)
    return svm_pre

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
    RMSE = np.sqrt(mean_squared_error(labels,predictions))
    return RMSE
    
if __name__=='__main__':
#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

    sorted_df = sort_dataset(data_df)
    X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

    X_train = extract_numerical_cols(X_train)
    X_test = extract_numerical_cols(X_test)

    dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
    rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
    svm_predictions = train_predict_svm(X_train, Y_train, X_test)

    print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
    print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
    print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))