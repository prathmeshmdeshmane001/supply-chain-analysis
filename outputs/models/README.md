# Trained Models Directory

The trained machine learning model (`random_forest_model.joblib`, ~527 MB) exceeds GitHub's 100 MB per-file upload limit without Git LFS.

To generate or regenerate the model artifact locally:
```bash
python run_analysis.py
```
The script will train the Random Forest classifier on balanced SMOTE data and save the serialized model here.
