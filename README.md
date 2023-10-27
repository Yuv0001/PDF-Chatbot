# PDF-Chatbot
1. **Repository Structure**:

   Organize your GitHub repository as follows:

   ```
   /pdf-chatbot
     ├── app.py
     ├── requirements.txt
     ├── README.md

   - `app.py`: Contain main script for building the PDF-Chatbot.
   - `requirements.txt`: List of required Python libraries.
   - `README.md`: Documentation for your project, including setup instructions.

2. **Steps**:

   1. Clone the repository:

      ```bash
      git clone https://github.com/yourusername/pdf-chatbot.git
      ```

   2. Navigate to the project directory:

      ```bash
      cd pdf-chatbot
      ```

   3. Install the required libraries using pip:

      ```bash
      pip install -r requirement.txt
      ```

   ## Running the App

   1. Start the app by running:

      ```bash
      python app.py
      streamlit run app.py
      ```

   2. Open a web browser and go to `http://localhost:8501`.

   ## Usage

   - Upload a PDF file.
   - Ask questions about the PDF content.
   - Get answers from the chatbot.

3. **Documentations**

    You can find the model I used, "bert-large-uncased-whole-word-masking-finetuned-squad," on the Hugging Face Model Hub. Here's the link to the model's documentation:[Documentation for "bert-large-uncased-whole-word-masking-finetuned-squad](https://huggingface.co/transformers/model_doc/bert.html#bertforquestionanswering)

   This documentation provides information about the model, its capabilities, and how to use it for question-answering tasks.
      
   For more information about the Hugging Face Transformers library and other pre-trained models, you can visit the Hugging Face Model Hub: [Hugging Face Model Hub](https://huggingface.co/models)

   You can explore various NLP models and find the one that best fits your needs for your PDF chat app or other natural language processing tasks
  

