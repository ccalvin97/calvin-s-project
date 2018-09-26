# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn import model_selection, metrics
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
import warnings
warnings.filterwarnings('ignore')
import  tensorflow as tf
from pandas.core.frame import DataFrame
import JA_house as ja
from sklearn.decomposition import PCA 

def getpcareduction(eig_vecs,order):
    redmatrix_w = eig_vecs[:,0:order]    
    print('reduction W:\n', redmatrix_w)
    return redmatrix_w 




def getpca(X_std,orifeature):
    mean_vec = np.mean(X_std, axis=0)
    cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)    
    
    cor_mat1 = np.corrcoef(X_std.T)
    eig_vals, eig_vecs = np.linalg.eig(cor_mat1)
    print('Correlation \n%s' %cor_mat1)
    print('Eigenvectors \n%s' %eig_vecs)
    print('\nEigenvalues \n%s' %eig_vals)  

    # Make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    
    # Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    
    # Visually confirm that the list is correctly sorted by decreasing eigenvalues
    print('Eigenvalues in descending order:')
    for i in eig_pairs:
        print(i[0])    

    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    plt.figure(5)
#    with plt.style.context('seaborn-whitegrid'):
#       
#        plt.figure(figsize=(6, orifeature))
#    
#        plt.bar(range(orifeature), var_exp, alpha=0.5, align='center',
#                label='individual explained variance')
#        plt.step(range(orifeature), cum_var_exp, where='mid',
#                 label='cumulative explained variance')
#        plt.ylabel('Explained variance ratio')
#        plt.xlabel('Principal components')
#        plt.legend(loc='best')
#        plt.tight_layout()

    matrix_w = eig_pairs
    eig_vec_sort = np.zeros([orifeature,orifeature])

    for i1 in range(orifeature):
        eig_vec_sort[:,i1] = eig_pairs[i1][1]
      
    print('eig_vec_sort W:\n', eig_vec_sort)
    
    #print('Matrix W:\n', matrix_w)
    
    return cor_mat1, eig_vec_sort, eig_vals, matrix_w






train = pd.read_csv('house_price_train.csv')
test = pd.read_csv('house_price_test.csv')
all_data = pd.concat([train, test], ignore_index = True)

feature=list(train.columns)
label="SalePrice"
feature.remove("SalePrice")

#將label 換到第一行
SalePrice=all_data.pop("SalePrice")
all_data.insert(0,"SalePrice",SalePrice)

#完成初始設定-------------------------------------------------------------------
#data cleaning ----------------------------------------------------------

 
            
# print出label對於其他所有變數的相關係數
ja.Plot_Corr_Label(label, all_data)

#檢查缺值以及缺值的比例並刪除某些變數很少的丟失值
all_data=ja.Checkdelete_Na(feature,label, all_data)   

cols1 = ["PoolQC" , "MiscFeature", "Alley", "Fence", "FireplaceQu", "GarageQual", "GarageCond", "GarageFinish", "GarageYrBlt", "GarageType", "BsmtExposure", "BsmtCond", "BsmtQual", "BsmtFinType2", "BsmtFinType1", "MasVnrType"]
for col in cols1:
    all_data[col].fillna("None", inplace=True)
    
cols=["MasVnrArea", "BsmtUnfSF", "TotalBsmtSF", "GarageCars", "BsmtFinSF2", "BsmtFinSF1", "GarageArea"]
for col in cols:
    all_data[col].fillna(0, inplace=True)
all_data['LotFrontage']=all_data.groupby(['LotArea','Neighborhood'])['LotFrontage'].transform(lambda x: x.fillna(x.median()))

mean=np.mean(all_data["LotFrontage"])
all_data["LotFrontage"]=all_data["LotFrontage"].fillna(mean)

#檢查缺失值以及缺失值比例
ja.Checkde_Na(feature, all_data)

# feature engineering----------------------------------------------------------

all_data=pd.get_dummies(all_data)
#ja.Plot_Corr_01(all_data)
ja.Plot_Corr_Matrix(all_data)
#feature2=list(all_data.columns)
#for i in feature2:
#    ja.outlier(i,label,all_data)



# 建模start
#------------------------------------------------------------------------------
#A linear regression learning algorithm example using TensorFlow library.
#from __future__ import print_function




# 調整data，準備開始建模
train=all_data[all_data[label].notnull()]
test=all_data[all_data[label].isnull()].drop(label,axis=1)
train_y=train[label]
train_x=train.drop([label],axis=1)
train_x, valid_x, train_y, valid_y = train_test_split(train_x, train_y, test_size=0.1)

#training set
train_x=train_x.values
train_y=train_y.values
train_y=train_y.reshape(-1,1)
valid_x=valid_x.values
valid_y=valid_y.values
valid_y=valid_y.reshape(-1,1)

#PCA
pca=PCA(n_components=260)
newData=pca.fit_transform(train_x)

#testing set


#建模code
rng = np.random

# Parameters
learning_rate = 0.000001
training_epochs = 20
display_step = 2

n_samples = train_x.shape[0]

# tf Graph Input
X = tf.placeholder("float64",[None, 290],name="my_x")
Y = tf.placeholder("float64",name="my_y")

# Set model weights
W=tf.Variable(tf.random_normal([290, 1]),name="weight" )
W=tf.cast(W, tf.float64)
#W = tf.Variable(rng.randn(), name="weight")
#b = tf.Variable(tf.random_uniform([train_x.shape,1],dtype=tf.float64 ), name="bias")
#b = tf.Variable(tf.ones([1,1]))
#b=tf.Variable(np.random.normal(0,0.05,train_x.shape),name="bias")
#b=tf.cast(b, tf.float64)

# Construct a linear model
a=tf.matmul( X,W )
pred=tf.cast(a, tf.float64)
#pred = tf.add(a, b)


# Mean squared error
#cost = tf.reduce_mean(tf.reduce_sum(tf.square(Y - pred), 
#                     reduction_indices=[1]))

cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(n_samples)
#hypothesis = tf.sigmoid(tf.multiply(X, W) + b)
#cost=tf.reduce_mean(Y *( tf.log(cost + 1e-4)) + (1 - Y) * (tf.log(1 - cost+1e-4))) 
# Gradient descent
#  Note, minimize() knows to modify W and b because Variable objects are trainable=True by default
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()


cost_history = np.empty(shape=[1],dtype=float)

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_x, train_y):
            x = x.reshape(x.shape[0],1)
            x=np.transpose(x)
            y = y.reshape(y.shape[0],1)
            sess.run(optimizer, feed_dict={X: x, Y: y})
#            cost_history = np.append(cost_history,sess.run(cost,feed_dict={X:x,Y:y}))

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_x, Y:train_y})
            cost_history = np.append(cost_history,sess.run(cost,feed_dict={X:train_x,Y:train_y}))
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_x, Y: train_y})
    print("Training cost=", training_cost, "W=", sess.run(W), '\n')


    plt.plot(range(len(cost_history)),cost_history)
    plt.axis([0,training_epochs,0,np.max(cost_history)])
    plt.pause(0.1)
    plt.show()

    pred_y = sess.run(a, feed_dict={X: valid_x})
    mse = tf.reduce_mean(tf.square(pred_y - valid_y))
    print("MSE: %.4f" % sess.run(mse)) 
    
    fig, ax = plt.subplots()
    ax.scatter(valid_y, pred_y)
    ax.plot([valid_y.min(), valid_y.max()], [valid_y.min(), valid_y.max()], 'k--', lw=3)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()

    
        # Graphic display
#    plt.plot(train_x, train_y, 'ro', label='Original data')
#    cost_plot=np.dot( train_x,sess.run(W) )
#    plt.plot(train_x, cost_plot, label='Fitted line')
#    plt.legend()
#    plt.pause(0.1)
#    plt.show()





    traininputx = np.array([train_x[:,4],train_x[:,1],train_x[:,2],train_x[:,3]])
    X_std=traininputx.T
    
    meanCC = np.mean(X_std,axis=0)
    stdCC = np.std(X_std, axis=0)
    solderstd = X_std - meanCC
    solderstd = solderstd/stdCC    
    X_std=solderstd
    mean_vec = np.mean(X_std, axis=0)
    cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)    
    
    
    
    cor_mat1 = np.corrcoef(X_std.T)
    eig_vals, eig_vecs = np.linalg.eig(cor_mat1)
    print('Correlation \n%s' %cor_mat1)
    print('Eigenvectors \n%s' %eig_vecs)
    print('\nEigenvalues \n%s' %eig_vals)  
    
    # Make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    
    # Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    
    # Visually confirm that the list is correctly sorted by decreasing eigenvalues
    print('Eigenvalues in descending order:')
    for i in eig_pairs:
        print(i[0])    

    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    matrix_w = eig_pairs
    eig_vec_sort = np.zeros([4,4])

    for i1 in range(4):
        eig_vec_sort[:,i1] = eig_pairs[i1][1]
      
    print('eig_vec_sort W:\n', eig_vec_sort)    

    redmatrix_w = eig_vec_sort[:,0:2]    
    print('reduction W:\n', redmatrix_w)
    getpcamatix = X_std.dot(redmatrix_w) # obtain PCA data
    
    plt.figure()
    plt.scatter(getpcamatix[:,0],getpcamatix[:,1])






