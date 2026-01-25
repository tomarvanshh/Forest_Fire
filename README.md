# Forest Fire Prediction - FWI (Forest Weather Index) Prediction System

## 📋 Project Overview

This is an end-to-end machine learning project that predicts the **Forest Weather Index (FWI)** for Algerian forest fires. The project encompasses data cleaning, preprocessing, feature scaling, model training with cross-validation, and deployment on AWS Beanstalk with a CI/CD pipeline.

The FWI is a critical metric used to assess fire weather conditions and predict the potential for forest fires. This application provides real-time predictions based on weather and fire weather indices.

---

## 🎯 Project Workflow

### 1. **Data Analysis & Exploration**

- Analyzed the Algerian forest fires dataset
- Performed Exploratory Data Analysis (EDA)
- Identified patterns, correlations, and anomalies in weather and fire index data
- Notebook: `notebooks/Algerain_EDA_FE.ipynb`

### 2. **Data Preprocessing & Feature Engineering**

- Cleaned missing values and outliers
- Handled categorical variables
- Feature engineering for improved model performance
- Notebook: `notebooks/Model_training.ipynb`

### 3. **Feature Scaling**

- Applied StandardScaler for normalization
- Ensured features are on the same scale for better model performance
- Scaler model saved for prediction pipeline

### 4. **Model Training & Selection**

- Trained three regression models with cross-validation:
  - **RidgeCV** - L2 regularization
  - **LassoCV** - L1 regularization
  - **ElasticNetCV** - Combined L1 and L2 regularization

- **Selected Model**: **RidgeCV** (Best accuracy and generalization)
- Cross-validation ensures robust model performance
- Model saved as pickle file for deployment

### 5. **Deployment**

- Deployed on **AWS Elastic Beanstalk**
- CI/CD pipeline set up with **AWS CodePipeline**
- Source: GitHub repository with automatic deployment
- Framework: Flask with Gunicorn WSGI server

---

## 📁 Project Structure

```
Project-Algerian_Fire_End-To-End/
│
├── application.py                  # Flask application entry point
├── requirements.txt                # Python dependencies
├── Procfile                        # AWS Beanstalk configuration
├── README.md                       # This file
│
├── models/                         # Trained models directory
│   ├── ridgecv.pkl                # RidgeCV model (selected)
│   └── scaler.pkl                 # StandardScaler for preprocessing
│
├── notebooks/                      # Jupyter notebooks for analysis
│   ├── Algerain_EDA_FE.ipynb      # Exploratory Data Analysis & Feature Engineering
│   ├── Model_training.ipynb        # Model training and evaluation
│   ├── Algerain_forest_fires_cleaned_dataset.csv
│   └── Algerian_forest_fires_dataset_UPDATE.csv
│
└── templates/                      # HTML templates
    ├── home.html                   # Main prediction interface
    └── index.html                  # Additional page
```

---

## 🔧 Features

### Input Parameters for Prediction:

1. **Temperature** - Temperature in Celsius
2. **Rh** - Relative Humidity (%)
3. **Ws** - Wind Speed (km/h)
4. **Rain** - Rainfall (mm)
5. **FFMC** - Fine Fuel Moisture Code
6. **DMC** - Duff Moisture Code
7. **ISI** - Initial Spread Index
8. **Classes** - Fire weather classes
9. **Region** - Geographic region code

### Output:

- **FWI (Forest Weather Index)** - Predicted fire weather index value

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip package manager
- Git for version control

### Local Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd Project-Algerian_Fire_End-To-End
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python application.py
   ```

   The application will be available at `http://localhost:5000`

---

## 📦 Dependencies

```
flask              # Web framework
numpy              # Numerical computing
pandas             # Data manipulation
scikit-learn       # Machine learning library
gunicorn           # WSGI HTTP server for production
```

---

## ☁️ AWS Beanstalk Deployment

### Architecture

- **Platform**: AWS Elastic Beanstalk (Python 3.9 runtime)
- **Server**: Gunicorn WSGI server
- **CI/CD**: AWS CodePipeline
- **Repository**: GitHub

### Deployment Configuration

The `Procfile` configures Gunicorn to run the Flask application:

```
web: gunicorn application:app
```

### Deployment Steps

1. **Push to GitHub**

   ```bash
   git add .
   git commit -m "Deploy to AWS"
   git push origin main
   ```

2. **AWS CodePipeline Triggers**
   - Automatically detects changes in GitHub repository
   - Builds the application
   - Deploys to AWS Elastic Beanstalk

3. **Access Application**
   - Once deployed, access via the Beanstalk environment URL

---

## 🤖 Machine Learning Models

### Model Comparison

| Model        | Regularization | Status          |
| ------------ | -------------- | --------------- |
| RidgeCV      | L2             | ✅ **Selected** |
| LassoCV      | L1             | Evaluated       |
| ElasticNetCV | L1 + L2        | Evaluated       |

### Why RidgeCV?

- Best cross-validation score
- Superior generalization performance
- Handles multicollinearity well
- Robust predictions on unseen data

---

## 📊 Model Performance

- **Training Approach**: K-Fold Cross-Validation
- **Metrics**: Mean Squared Error (MSE), R² Score
- **Preprocessing**: StandardScaler normalization
- **Optimization**: Hyperparameter tuning with cross-validation

---

## 🎨 User Interface

The web interface provides a simple form-based input system where users can enter weather parameters and receive real-time FWI predictions.

**Key Features:**

- Clean, user-friendly HTML form
- Real-time prediction results
- Input validation
- Responsive design

---

## 📝 Usage Example

1. Navigate to the web application
2. Fill in the weather parameters:
   - Temperature: 25°C
   - Relative Humidity: 60%
   - Wind Speed: 15 km/h
   - Rain: 0 mm
   - FFMC: 85
   - DMC: 50
   - ISI: 10
   - Classes: 2
   - Region: 1

3. Click "Predict" button
4. View the predicted FWI value

---

## 🔍 Data Files

### Datasets Used:

- **Algerain_forest_fires_cleaned_dataset.csv** - Cleaned dataset
- **Algerian_forest_fires_dataset_UPDATE.csv** - Updated dataset with additional features

### Data Source:

Algerian Forest Fires Dataset - Contains weather indices and forest fire data from Algerian regions.

---

## 🛠️ Development & Maintenance

### For Model Retraining:

1. Update dataset in `notebooks/` folder
2. Run `Model_training.ipynb` notebook
3. Re-pickle and save models to `models/` directory
4. Update `application.py` if feature changes occur
5. Push changes to trigger automatic deployment

### Logging & Monitoring:

- AWS Beanstalk CloudWatch logs for application monitoring
- Track prediction accuracy over time
- Monitor API response times

---

## 📈 Future Enhancements

- [ ] Add additional regression models (Gradient Boosting, Random Forest)
- [ ] Implement real-time fire detection integration
- [ ] Add historical prediction analytics dashboard
- [ ] Enhance UI with visualization of FWI trends
- [ ] Implement API documentation with Swagger/OpenAPI
- [ ] Add model performance tracking and versioning
- [ ] Deploy prediction caching for frequently occurring inputs

---

## 🐛 Troubleshooting

### Common Issues:

**1. Model Loading Error**

- Ensure `ridgecv.pkl` and `scaler.pkl` exist in `models/` directory
- Check file paths in `application.py`

**2. AWS Beanstalk Deployment Failure**

- Verify `Procfile` is correctly formatted
- Check `requirements.txt` has all dependencies
- Review AWS CodePipeline logs

**3. Prediction Errors**

- Ensure input values are numeric
- Check input ranges match training data
- Verify feature order matches training sequence

---

## 📧 Contact & Support

For issues or questions regarding this project:

- Review the Jupyter notebooks for detailed analysis
- Check AWS CloudWatch logs for deployment issues
- Verify GitHub repository for latest updates

---

## 📄 License

This project is provided as-is for educational and research purposes.

---

## ✅ Checklist for Deployment

- [x] Data cleaned and preprocessed
- [x] Features scaled with StandardScaler
- [x] Multiple models trained with cross-validation
- [x] Best model (RidgeCV) selected and serialized
- [x] Flask application configured
- [x] HTML templates created
- [x] Requirements.txt updated
- [x] Procfile configured for Beanstalk
- [x] CodePipeline setup for CI/CD
- [x] GitHub repository connected
- [x] Application deployed on AWS Beanstalk
- [x] README documentation completed

---

## 🎓 Learning Outcomes

Through this project, you've learned:

- End-to-end machine learning workflow
- Data preprocessing and feature engineering
- Model comparison and selection with cross-validation
- Scikit-learn machine learning pipeline
- Flask web application development
- Cloud deployment with AWS Beanstalk
- CI/CD automation with CodePipeline

---

**Last Updated**: January 2026  
**Status**: ✅ Active & Deployed
