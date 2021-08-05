#Basics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Display
from IPython.core.display import HTML
from IPython.core.display import display

#System
import sys

#Sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

from ml_pinguins_pkg.pinguins_ml import Pinguins_ml


class Pinguins_model(Pinguins_ml):
    
    def __init__(self,df, target):
         #--------------------------------------------------------
        """ • Initialise with Data_ml
            • Params = df, target
            • Return None """
        #---------------------------------------------------------
        super().__init__(df, target)
        
            
    def del_null(self, data):
        #---------------------------------------------------------
        """ • drop NA from dataset rows
            • Return dataset without Na"""
        #---------------------------------------------------------  
        data = data.dropna().reset_index().drop('index', axis = 1)
        return data
    
    
    def transform_null(self, df):
        #---------------------------------------------------------
        """ • include function del_null in a transformer and 
            modify df, X and y
            • Return None"""
        #---------------------------------------------------------  
        transformer = FunctionTransformer(self.del_null)
        df = pd.DataFrame(transformer.fit_transform(df))
        
        self.X = df.drop(self.target, axis = 1)
        self.y = df[self.target]
    
    
    def split(self, X,y):
        #---------------------------------------------------------
        """ • Spit Dataset in Train and test sets
            • Return None"""
        #---------------------------------------------------------  
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,y, random_state=42, stratify=y)
    
    
    def preprocessing(self, X):
        #---------------------------------------------------------
        """ • Shows 5 first lines of Dataset
            • Return transformer """
        #---------------------------------------------------------
        num = X.select_dtypes(include = [np.number]).columns
        cat = X.select_dtypes(exclude = [np.number]).columns
        
        return make_column_transformer((OneHotEncoder(handle_unknown='ignore'), cat),(StandardScaler(),num))
    
    
    def create_model_pipe(self, preprocess, model):
        #---------------------------------------------------------
        """ • Create Pileline with model and preprocess
            • Return pipe model"""
        #---------------------------------------------------------  
        return make_pipeline(preprocess, model)  
    
    
    def train_model(self, model, X, y):
        #---------------------------------------------------------
        """ • Train model
            • Return fit model"""
        #---------------------------------------------------------  
        return model.fit(X,y)
    
    
    def predict_model(self, model, X_test):
        #---------------------------------------------------------
        """ • Predict with fit model
            • Return array of prediction"""
        #---------------------------------------------------------  
        return model.predict(X_test)
    
    
    def show_classification_scores(self, y_test, y_pred):
         #---------------------------------------------------------
        """ • Shows basics infos from dataset
            • Return string """
        #---------------------------------------------------------
        string = [f'accuracy : {accuracy_score(y_test, y_pred)}',
        f'precision : {precision_score(y_test, y_pred, average = None)}',
        f'recall : {recall_score(y_test, y_pred, average = None)}',
        f'f1 : {f1_score(y_test, y_pred, average = None)}']
        
        return string
    
    
    def matrix_plot(self, model, X_test, y_test):
        #---------------------------------------------------------
        """ • Create fig for matrix_confusion
            • Return fig"""
        #---------------------------------------------------------  
        
        listing = list(y_test.unique())
        listing.sort()
        
        fig, ax = plt.subplots(figsize=(8,6))
        disp = plot_confusion_matrix(model, X_test, y_test, 
                                     display_labels=listing, 
                                     cmap=plt.cm.Blues, normalize=None,
                                     ax = ax)

        fig.suptitle('Decision Tree Confusion matrix, without normalization', fontweight='bold', fontsize=20);
        return fig

    
    def evaluate_model(self, send_model):
        #---------------------------------------------------------
        """ • Create Pileline with model and preprocess
            • Return pipe model"""
        #---------------------------------------------------------  
    
        #del_NA
        self.transform_null(self.df)
        
        #split
        self.split(self.X, self.y)
        
        #preprocessing creation
        self.preprocess = self.preprocessing(self.X)
        
        #pipeline model creation
        model = self.create_model_pipe(self.preprocess, send_model)
        
        #training model
        model = self.train_model(model, self.X_train, self.y_train)   
        
        #predict model
        pred_simple = self.predict_model(model, self.X_test)
        
        #show scores
        display(self.show_classification_scores(self.y_test, pred_simple))
        
        #plot confusion matrix
        self.matrix_plot(model, self.X_test, self.y_test)
        
        
    def prepare_model(self, send_model):
        #---------------------------------------------------------
        """ • Create self.model fitted
            • Return None"""
        #---------------------------------------------------------  

        #del_NA
        self.transform_null(self.df)

        #preprocessing creation
        self.preprocess = self.preprocessing(self.X)

        #pipeline model creation
        model = self.create_model_pipe(self.preprocess, send_model)

        #training model
        self.model = self.train_model(model, self.X, self.y)   