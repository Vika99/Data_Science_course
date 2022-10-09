from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

import pandas as pd
import numpy as np

# ********************************************

class some_transformer (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
        
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            # Remove original fields
            pass
        
        return X
    
# **********************************************************
class T_O_T (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
        X['Type of Travel'] = X['Type of Travel'].map({'Business travel':0, 'Personal Travel':1})
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            pass
        
            # Remove original fields
           # X.drop(['Type of Travel'],axis = 1, inplace = True)
        
        return X
    
    
# **************************************************************8

class C_T(BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X['Customer Type'] = X['Customer Type'].map({'Loyal Customer': 0, 'disloyal Customer': 1})
        
        if self.remove_origin:
            # Remove original fields
            pass
        
        return X
    
    
# **************************************************************

class Gnd (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X['Gender'] = X['Gender'].map({'Female': 0, 'Male':1}) # inplace = True - чтобы изменения сразу сохранялись без присваивания
        
        if self.remove_origin:
            pass
            # Remove original fields
        
        return X
    
    
    
# ********************************************************************
class Imp_class (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X['Class'] = X['Class'].map({'Eco': 0, 'Eco Plus': 1, 'Business': 2})
        
        if self.remove_origin:
            pass
            # Remove original fields
        
        return X
    
    
# ***************************************************************************


class sat (BaseEstimator, TransformerMixin): 
     
    def __init__(self, remove_origin = False): 
        self.remove_origin = remove_origin 
     
    def fit(self, X, y = None): 
        return self 
     
    def transform(self, X, y = None): 
        # Transformation 
        X['satisfaction'] = X['satisfaction'].map({'neutral or dissatisfied': 0, 'satisfied': 1}) 
         
        if self.remove_origin: 
            pass 
         
        return X
    
    
# *************************************************************************************


#  мы закончили с определнием классов и переходим к контейнеру!!!!!!!!!

myPipe = Pipeline ([('some_transformer',some_transformer()),
                    ('T_O_T',T_O_T()), 
                    ('Imp_class',Imp_class()), 
                    ('C_T',C_T()),
                    ('Gnd',Gnd()),
                    ('sat',sat())])



