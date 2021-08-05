#Basics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Display
from IPython.core.display import HTML
from IPython.core.display import display

from ml_pinguins_pkg.pinguins_ml import Pinguins_ml

class Pinguins_viz(Pinguins_ml):
    
    def __init__(self,df, target):
         #--------------------------------------------------------
        """ • Initialise with Data_ml
            • Params = df, target
            • Return None """
        #---------------------------------------------------------
        super().__init__(df, target)
        
    
    def data_head(self):
        #---------------------------------------------------------
        """ • Shows 5 first lines of Dataset
            • Return dataset """
        #---------------------------------------------------------       
        return self.df.head()
    
    
    def data_shape(self):
        #---------------------------------------------------------
        """ • Shows basics infos from dataset
            • Return string """
        #---------------------------------------------------------
        string = [f"Nombre de lignes : {self.df.shape[0]} lignes",
        f"Nombre de colonnes : {self.df.shape[1]} colonnes",
        f"Nombre total de celulles non nulles : {self.df.notna().sum().sum()}",
        f"Nombre total de cellules nulles : {self.df.isna().sum().sum()}"]
        
        return string
    
    
    def data_sample(self):
        #---------------------------------------------------------
        """ • Shows samples of features from dataset
            • Return dataset """
        #---------------------------------------------------------
        samples = []
        for i in self.df.columns:
            samples.append(str(list(self.df[i].head(5))))

        obs = pd.DataFrame({
            'name' : self.df.columns,
            'type':self.df.dtypes,
            'sample':samples,
            '% nulls':round((self.df.isnull().sum()/len(self.df))*100)   
            })

        return obs
        
    
    def infos(self):
        #---------------------------------------------------------
        """ • Shows infos on self.df(lines, cilumns, nulls) 
            and make sample of features
            • Return dataset """
        #---------------------------------------------------------             
        print('')
        display(HTML('<h2>INFOS DATASET</h2>'))
        
        display(HTML('<h3>Head dataset</h3>'))
        display(self.data_head())
        
        display(HTML('<h3>Shape dataset</h3>'))
        display(self.data_shape())

        display(HTML('<h3>Sample dataset</h3>'))
        display(self.data_sample())   
    
    
    def look(self, target):
        #---------------------------------------------------------
        """ • Shows infos on self.df(lines, cilumns, nulls) 
            and make sample of features
            • Return dataset """
        #---------------------------------------------------------       
        display(HTML(f'<h3>Analysis of feature : "{target}"</h3>'))
        display(self.df[target].describe())
        
        fig, ax = plt.subplots(figsize=(8,6))
        plot = sns.histplot(data=self.df, x=target, hue=self.target, kde=True, ax=ax)
        fig.suptitle(f'Distribution of {target}')
        return fig
        
    
    def korr(self, target):
        #---------------------------------------------------------
        """ • Shows infos correlation between numeric targets
            • Return plot """
        #---------------------------------------------------------            
        temp_df = self.df.copy()
        
        if target in list(self.df.select_dtypes(exclude=[np.number]).columns):

            listing = temp_df[target].unique()
            replacing = list(range(1, len(listing)+1))
            temp_df[target] = temp_df[target].replace(listing,replacing)
            
            df_corr = temp_df.corr()
        else:
            df_corr = self.df.corr()
                    
        corr_target = df_corr.sort_values(target, ascending=False)
        
        fig, ax = plt.subplots(figsize=(8,6))
        plot = sns.barplot(x=corr_target[target], y=corr_target.index, ax=ax)
        fig.suptitle(f'Correlation des features vis à vis de {target}')
        return fig

    
    def kompare(self, x, y):
        #---------------------------------------------------------
        """ • Scatterplot with regression line between numeric targets
            • Return plot """
        #---------------------------------------------------------    
        
        new_df = self.df.copy()
        
        if (x in list(self.df.select_dtypes(exclude=[np.number]).columns)):
            listing = new_df[x].unique()
            replacing = list(range(1, len(listing)+1))
            new_df[x] = new_df[x].replace(listing,replacing)
            
        if (y in list(self.df.select_dtypes(exclude=[np.number]).columns)):
            listing = new_df[y].unique()
            replacing = list(range(1, len(listing)+1))
            new_df[y] = new_df[y].replace(listing,replacing)
        
        fig, ax = plt.subplots(figsize=(8,6))
        #plot = sns.lmplot(x=x, y=y, data=new_df, height=5, aspect=2)
        plot = sns.regplot(x=x, y=y, data=new_df, ax=ax)
        fig.suptitle(f'Comparaison de {x} en fonction de {y}');
        return fig