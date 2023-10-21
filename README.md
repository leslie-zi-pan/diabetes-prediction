# T2 Diabetes Prediction

## Frame The Problem

| Problem | Solution | 
|---|---|
| Business Objective | Ability to infer if a patient has diabetes given a set of symptoms provided |
| How will the solution be used | Puporse is intended for educational purposes and should not be used as a diagnostic tool |
| Current Solutions | Fulfillment of criteria as outlined by [WHO](https://www.diabetes.org.uk/professionals/position-statements-reports/diagnosis-ongoing-management-monitoring/new_diagnostic_criteria_for_diabetes) recommendations |
| How should performance be measured | We should be using standard classfication metrics. |
| Minimum Performance Needed For Business Objective | The 2016 [UK GOV prevalence model](https://assets.publishing.service.gov.uk/media/5a82c07340f0b6230269c82d/Diabetesprevalencemodelbriefing.pdf) states "940,000 people with diabetes that are undiagnosed" out of 3.8 million (diagnosed and undiagnosed) - giving us an approximate rate of 0.753. We should be striving to hit and surpass this baseline for our recall (this is not entirely scientifically correct as UK GOV websites are assumed to be undiagnosed and not misdiagnosed. However, this is a good baseline to aim for our purposes). |
| Comparable Problems | - |
| Is human expertise available | Domain knowledge would ideally be required, but self-research will suffice for this project | 
| Assumptions | Business Performance  recall objective based on undiagnosed estimate not misdiagnosed. |

UK Population in 2016 as outlines by [Office of National Statistics](<https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2019estimates#:~:text=the%20number%20of%20children%20(those,by%2022.9%25%20to%2012.4%20million>)


<div style="text-align:center">
    <img src="reports\figures\uk_population_2016.png" alt="UK Population 2016" />
</div>
<br />
<div style="text-align:center">
    <img src="reports\figures\diabetic_prevalence_2016_uk.png" alt="UK Diabetic Prevalence 2016" />
</div>



## Dataset 

| Source Information | Information | 
|---|---|
| Source | https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset |
| Owner | Mohammed Mustafa |
| About | The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes. |
| File Information | The diabetes_prediction_dataset.csv file contains medical and demographic data of patients along with their diabetes status, whether positive or negative. It consists of various features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. The Dataset can be utilized to construct machine learning models that can predict the likelihood of diabetes in patients based on their medical history and demographic details. |
| Provenance Sources | Electronic Health Records (EHRs) are the primary source of data for the Diabetes Prediction dataset. EHRs are digital versions of patient health records that contain information about their medical history, diagnosis, treatment, and outcomes. The data in EHRs is collected and stored by healthcare providers, such as hospitals and clinics, as part of their routine clinical practice. <br/><br/> To create the Diabetes Prediction dataset, EHRs were collected from multiple healthcare providers and aggregated into a single dataset. The data was then cleaned and preprocessed to ensure consistency and remove any irrelevant or incomplete information.<br/><br/> The use of EHRs as a data source for the Diabetes Prediction dataset has several advantages. First, EHRs contain a large amount of patient data, including demographic and clinical information, which can be used to develop accurate machine learning models. Second, EHRs provide a longitudinal view of a patient's health over time, which can be used to identify patterns and trends in their health status. Finally, EHRs are widely used in clinical practice, making the Diabetes Prediction dataset relevant to real-world healthcare settings. |
| Provenance Collection Methodology | The collection methodology for the diabetes prediction dataset involves gathering medical and demographic data from patients who have been diagnosed with or are at risk of developing diabetes. The data is typically collected through surveys, medical records, and laboratory tests. The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. The data is then processed and cleaned to remove any errors or inconsistencies. The dataset can also be used for research purposes to identify potential risk factors for diabetes and to develop effective prevention and treatment strategies. |


| EDA Investigations | Information | 
|---|---|
| Data Shape | `(100000, 9)` |
| Data Columns | ```['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level', 'diabetes']``` |
| Train Test Split Distribution Stratified By Label - Diabetes | ![strat_diab](reports\train_test_split\split_strat_by_diabetes.png) |
| Train Test Split Distribution Stratified By Gender | ![strat_gender](reports\train_test_split\split_strat_by_gender.png) |
