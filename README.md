# ETSM


This is the source code of ETSM model. Some parts of it can't be used directly. Due to the long time, it is difficult to supplement. Therefore, I explain the programming ideas for reference. The following explanations take the prediction of AKI 24 hours in advance as an example.

## Select the patients whose icu stay time is more than 24h

## Feature extraction

### Vital signs and laboratory results (marked as "status")

- There may be a large number of missing values in the patient's status value. Select the average value of the queue to supplement. (feature_extract/fill_status.py)

- For AKI positive patients, the status on the day of admission and the day before the onset were selected. For AKI negative patients, the status on the day of admission and the last day with data record were selected. (feature_extract/selectstatus_focusPatient.py)

- The selected two parts joint a one-dimensional feature vector. (feature_extract/feature.py)


### medication data (marked as "treatment")

- Change the medication data to a Boolean value. (featureextract/numlize.py)

- Medication data is organized in chronological order, so you only need to extract all the different rows in the data to get the "dictionary". (feature_extract/dictionary.py)

- Extract the medication data of the patient within the observation window. (featureextract/treatment.py)

- Each "word" in the "dictionary" (drug combination) is marked as a feature. Calculate the number of times each patient uses each drug combination. (This part of the code is missing, sorry)

- The TF-IDF method was applied to the whole cohort, and the one-dimensional drug combination faetures were obtained. (featureExtract/tf_idf.py)



### feature combination

The input is obtained by connecting the features of state and medication combination. (featureextract/X.py)



## Model training

Using xgboost model for training. (model/xgboost.py)
