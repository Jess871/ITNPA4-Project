### Deployment (Question 2.3)

This folder has the Streamlit app for Question 2. It classifies a research abstract as AI or classical research using the tuned Linear SVM model from Question 2.

Files:
- `Q2.3_app.py` <- the app
- `best_model.joblib` <- the saved model from Question 2

### How to run

1. Open a terminal in this folder.
2. Install the packages:
    
   python -m pip install streamlit scikit-learn nltk joblib

4. Run the app:

   python -m streamlit run Q2.3_app.py

5. The app opens in your browser. Paste an abstract and click **Classify Abstract**.
