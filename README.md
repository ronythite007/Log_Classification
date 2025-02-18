# Log Classification With Hybrid Classification Aproach

## Overview
This project implements a **Hybrid Classification Aproach** for log classification using **BERT, Large Language Models (LLM), Regex-based approaches, Logistic Regression, and FastAPI for the backend**. The framework effectively classifies log messages by leveraging the strengths of machine learning, and rule-based techniques to achieve high accuracy and reliability.

## Classification Approaches

**Regular Expression (Regex)**

Regex-based classification is effective for structured and predictable log patterns. It works well when predefined rules can accurately capture log categories, making it a fast and lightweight approach for specific use cases.

**Sentence Transformer & Logistic Regression**

For complex log patterns where sufficient training data is available, Sentence Transformers are used to generate embeddings, which are then classified using a Logistic Regression model. This approach ensures accurate classification by leveraging machine learning techniques.

**Large Language Models (LLM)**

When labeled training data is insufficient, LLMs provide an alternative method for log classification. These models utilize their pre-trained knowledge to classify logs with contextual understanding, serving as a powerful complement to other approaches.

## Flowchart
Below is a flowchart illustrating the log classification process:

![Log Classification Flowchart](![Screenshot 2025-02-18 082231](https://github.com/user-attachments/assets/fa8f9ff7-e951-4bc9-865e-44eb66f27068))

## Features
- **BBERT-based log classification**: Embedding for classification using a pre-trained BERT model.
- **Large Language Models (LLMs)**: Incorporates LLMs for improved context-based classification(Used Groq).
- **Regex-based filtering**: Applies rule-based regex patterns for predefined log categories.
- **Logistic Regression Model**: Implements a machine learning-based classification approach for log messages.
- **FastAPI Backend**: Provides a RESTful API for log classification and model interaction.
- **HTML-based UI**: Simple and interactive frontend for log classification.
- **Hybrid approach**: Combines deep learning, machine learning, and regex techniques for enhanced classification accuracy.
- **Scalable and efficient**: Optimized for large-scale log processing.
  
## Technologies Used
- **Programming Languages:** Python
- **Frameworks & Libraries:** FastAPI (Backend API), TensorFlow/PyTorch (BERT implementation), Transformers (Hugging Face), Scikit-learn (Logistic Regression)
- **Frontend:** HTML, CSS
- **Data Processing:** Pandas, NumPy, Regex

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed along with the required dependencies.

### Steps to Install
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/log-classification.git
   cd log-classification
   ```
2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
### Running the FastAPI Backend
- Start the API server:
  ```bash
  uvicorn main:app --reload
  ```
  ## Demo 
Below is a Demo of Sever :

![Log Classification Demo](![Screenshot 2025-02-18 092609](https://github.com/user-attachments/assets/35eefcac-2b64-4a82-93ac-35ee76abc998)
)
![Log Classification Demo](![Screenshot 2025-02-18 092609](https://github.com/user-attachments/assets/4553c3e6-dca4-48dc-ae88-cee707777e16)
)
- **Upload a CSV file containing logs** to the FastAPI endpoint for classification. Ensure the file has the following columns:
  - `source`
  - `log_message`
  
  The output will be a CSV file with an additional column `target_label`, which represents the classified label for each log entry.
