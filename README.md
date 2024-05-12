# BDA PROJECT (SPOTIFY)

# Group Members
- Shaban Hassan (22i-1927)
- Ahtezaz Ahsan (22i-2064)
  
# Data Collection and Preprocessing: 

Initially, the Free Music Archive (FMA) dataset comprising 106,574 tracks was utilized. This dataset included essential details such as title, artist, genres, tags, and play counts. The data underwent meticulous preprocessing, where missing values and outliers were addressed. Feature extraction techniques such as Mel-Frequency Cepstral Coefficients (MFCC), spectral centroid, and zero-crossing rate were applied to convert audio files into numerical and vector formats. Furthermore, normalization and standardization techniques were employed to ensure consistency and improve model performance. The preprocessed data was then stored in MongoDB for its scalability and accessibility, facilitating seamless integration with subsequent phases of the project.

# Model Training and Evaluation: 

Apache Spark's MLlib library was the cornerstone for training the music recommendation model. Leveraging the ALS (Alternating Least Squares) algorithm for collaborative filtering, the model was trained using the preprocessed data stored in MongoDB. A rigorous hyperparameter tuning process was conducted to optimize the model's performance, considering factors such as the number of iterations and regularization parameters. Evaluation metrics, including Root Mean Squared Error (RMSE), were extensively utilized to assess the effectiveness of the recommendation model. The model's ability to accurately predict user preferences and provide relevant music suggestions was meticulously evaluated, ensuring alignment with the project objectives and user expectations.

# Deployment: 

The culmination of the project involved deploying the trained recommendation model into a web application designed to deliver an immersive and interactive music streaming experience. Utilizing frameworks such as Flask or Django, the web application provided users with seamless access to a vast library of music tracks. The recommendation engine, powered by Apache Kafka, dynamically generated personalized music suggestions in real-time based on users' listening history and preferences. The absence of manual input for uploading audio files underscored the system's autonomy, with recommendations exclusively derived from user activity. The integration of Apache Kafka enabled efficient monitoring of user interactions and the generation of contextually relevant recommendations, thereby enhancing the overall user experience.

# Findings:

The comprehensive approach adopted in developing the music recommendation system yielded promising results, with the model demonstrating a high degree of accuracy in predicting user preferences.
Collaborative filtering, augmented by real-time recommendation generation using Apache Kafka, significantly enhanced user engagement by providing tailored music suggestions aligned with individual tastes and preferences.
The user-centric design of the web application interface facilitated seamless navigation and interaction, fostering an immersive music streaming experience devoid of cumbersome manual inputs.
# Conclusion:
The integration of cutting-edge technologies and methodologies in the development of the music recommendation system underscored its effectiveness in delivering personalized and engaging music recommendations to users. The iterative nature of the project, coupled with continuous evaluation and refinement, ensured the alignment of the recommendation model with user expectations and preferences. Moving forward, ongoing optimization and enhancement of the recommendation engine and web application interface will be critical in sustaining user satisfaction and fostering long-term engagement with the platform.
