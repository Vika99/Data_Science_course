from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

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



class Months (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
        X['Month'] = X['Month'].map({'January':0, 'February':1, 'March':2,'April':3, 'May':4, 'June':5,'July':6, 'Augusth':7})
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            pass
        
            # Remove original fields
           # X.drop(['Type of Travel'],axis = 1, inplace = True)
        
        return X
    
    
# *************************************************************************************





class CreditScore (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
        X['CreditScore'] = X['CreditScore'].map({'Standard':0, 'Good':0,'Poor':1})
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            pass
        
            # Remove original fields
           # X.drop(['Type of Travel'],axis = 1, inplace = True)
        
        return X
    
    
    
# *******************************************************************************************************




class CreditMix (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
        X['CreditMix'] = X['CreditMix'].map({'Standard':0, 'Good':1, 'Bad':2})
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            pass
        
            # Remove original fields
           # X.drop(['Type of Travel'],axis = 1, inplace = True)
        
        return X
    
    
    
# *************************************************************************************************************


class PaymentofMinAmount (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
        X['PaymentofMinAmount'] = X['PaymentofMinAmount'].map({'Yes':0, 'No':1})
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            pass
        
            # Remove original fields
           # X.drop(['Type of Travel'],axis = 1, inplace = True)
        
        return X
    
    
    
    
# **************************************************************************************************



class Occupation (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
    
        X = pd.get_dummies(X,columns=['Occupation'])
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            pass
        
            # Remove original fields
           # X.drop(['Type of Travel'],axis = 1, inplace = True)
        
        return X
    
    
    
    
    
# ********************************************************************************************************

class PaymentBehaviour (BaseEstimator, TransformerMixin):
    
    def __init__(self, remove_origin = False):
        self.remove_origin = remove_origin
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        # Transformation
        X.fillna(0,inplace = True)
    
        oh = OneHotEncoder()
        h_cat_en, h_categories = X['PaymentBehaviour'].factorize()
        coded = oh.fit_transform(h_cat_en.reshape(-1,1))
        proxy = pd.DataFrame(coded.toarray(), index = X.index, columns = ['1','2','3','4','5','6','7'])
        X = pd.concat([X, proxy], axis = 1)
       # X = df.drop(['PaymentBehaviour','CustomerID','ID','Name','CreditScore','TypeofLoan','SSN','CreditHistoryYears_Range','MonthlyBalance_Range'], axis = 1)
       # X = pd.concat([X, proxy], axis = 1)
        
# СЮДА МОЖНО ЗАСУНУТЬ ВСЕ ДАМНИС, ХОТТЕР И ТОГДА ПОЛУЧИТСЯ ВСЕ.

        if self.remove_origin:
            pass
        
            # Remove original fields
           # X.drop(['Type of Travel'],axis = 1, inplace = True)
        
        return X
    
    
    
    
    
 # ***********************************************************************************************


#  мы закончили с определнием классов и переходим к контейнеру!!!!!!!!!


myPipe = Pipeline ([('some_transformer',some_transformer()),
                    ('Months',Months()), 
                    ('CreditScore',CreditScore()), 
                    ('CreditMix',CreditMix()),
                    ('PaymentofMinAmount',PaymentofMinAmount()),
                    ('Occupation',Occupation()),
                    ('PaymentBehaviour',PaymentBehaviour())
                   
                   ])