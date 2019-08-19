# Project List:
Update     
2018/5/12 v1  
2019/7/11 v2  
2019/8/18 v3  


1. Named Entity Recognition    
•	Compared with different NN structures, incl. Bi-LSTM, CRF – F1 score 83.2% and 96%   
•	Utilised different embedding function, incl. Glove and Tensorflow Elmo  

2. NLP Personality System(Production Level) - Oleeo UK    
•	Model 1 - Glove + Global & Soft Attention + Bi-LSTM, 31d multi-labels - RMSE 0.83  
•	Model 2 - XLNet Fine Tune + Downstream, 31d multi-labels regression - RMSE 0.80  
•	Model 3 - XLNet Fine Tune + Downstream,  1d single label regression - RMSE 0.5    

![image](https://github.com/ccalvin97/calvin-s-project/blob/master/dissertation_model_1/Untitled%20Diagram%20(1).png)![image](https://github.com/ccalvin97/calvin-s-project/blob/master/dissertation_model_1/Untitled%20Diagram%20(2).png)

3. Sentiment Classification NLP  
•	Compared with different structures, incl. Bi-LSTM + Global Soft Attention and SVM – Acc 0.771  
![image](https://github.com/ccalvin97/kaggle2/blob/master/NLP_sentiment%20classification/poster.gif)

4. Speech Recognition Industrial Project  
•	Utilised Bi-LSTM to create language speech recognition system transforming audio data to text  
•	Audio → MFCC → NN → Target: CTC Loss (Beam Search, Edit Distance)  

5. Kaggle - House Prices: Advanced Regression Techniques   
•	Achieved top 6% and accuracy of 0.11 for the RMSE  
•	DNN, Linear Regression & Stacking Model (Lasso, Elastic Net, SVR, Kernel Ridge, Bayesian Ridge, Ridge)   

6. Kaggle - Histopathologic Cancer Detection  
•	Two CNN structures, incl. Fastai DenseNet 201 & NASNet + global max/average pooling – Acc 95.9%  

7. Machine Learning Mobile Application – Second Hand Car Selling  
•	Model 1: Utilised NN to create a price prediction system  
•	Model 2: Utilised Latent Dirichlet Allocation to create a topic system  
•	Model 3: Utilised Google Cloud Vision API to create an image recognition system  
•	Workflow: Created ML models (Python) → Imported 3 models to API → Created a mobile application  

8. Machine Learning Startup Project – Crime Warning System   
•	Market Demand: Theft offences occurred at a rate of 45.8 per 1,000 population in 2017 in London   
•	Workflow: Dimension Reduction → ARIMA & LSTM → Validation → Output Prediction  
•	Function: Once users walks on a road at a specific time, they will be reminded if the time is dangerous  

9. Kaggle – Titanic Machine Learning from Disaster   
•	Achieved top 2% and accuracy of 83.7% for the prediction of the data  
•	Utilised 2 methods to predict labels respectively, incl. DNN & Random Forest  
