# 📧 Cold Mail Generator

## Overview

The Cold Mail Generator is a tool designed for services companies to streamline their cold emailing process. Using Groq, LangChain, and Streamlit, the tool enables users to input the URL of a company's careers page. It extracts job listings from the page and generates personalized cold emails tailored to the job descriptions. The emails also include relevant portfolio links from a vector database, making the outreach more effective.

### Scenario

A Job Seeker is an emerging talent in the tech industry with expertise in Python, SQL, data analysis using Power BI, machine learning, and web development. He is interested in exploring job opportunities at Nike, a leading company known for its innovation and excellence. His aims to connect with Nike’s hiring manager to discuss potential roles that align with his skills and qualifications. By leveraging the Cold Mail Generator, He can craft a personalized cold email that highlights his capabilities and enthusiasm for contributing to Nike’s team.

![Architecture Diagram]([Architecture Diagram.png](https://github.com/VEDAANT711/Cold-Email-Generator-Tool/blob/main/Architecture%20Diagram.png?raw=true)

## Features

- **URL-Based Job Listing Extraction**: Input a URL and extract job listings for email personalization.
- **Personalized Cold Emails**: Generate tailored cold emails based on job descriptions.
- **Portfolio Integration**: Include relevant portfolio links sourced from a vector database.
- **User-Friendly Interface**: Utilize a Streamlit-based web interface for easy interaction.

## Setup

### Prerequisites

1. **Get API Key**
   - Obtain an API key from [Groq Console](https://console.groq.com/keys).

2. **Environment Setup**
   - Create a `.env` file in the `app/` directory and add your API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/VEDAANT711/Cold-Email-Generator-Tool.git

2. **Navigate to the Project Directory**

    ```bash
    cd Cold-Email-Generator-Tool

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt

 4. **Run the Streamlit App**

    ```bash
    streamlit run app/main.py
   
### Usage

1. **Start the Application**

    *Run the Streamlit app as described in the setup instructions.*

2. **Input URL**

    *Enter the URL of a company's careers page into the app.*

3. **Generate Emails**

    *The tool will process the job listings and generate personalized  cold emails.* 

4. **Review and Send**

    *Review the generated emails, make any necessary adjustments, and  send them.*


### Contributing

1. **Fork the Repository** 

`Click the "Fork" button on the top right of this repository page.`

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/yourusername/Cold-Email-Generator-Tool.git

3. **Create a New Branch**

   ```bash
   git checkout -b feature/your-feature-name

4. **Make Changes and Commit**
   ```bash
   git add .
   git commit -m "Add a descriptive commit message"

5. **Push Changes**

   ```bash
   git push origin feature/your-feature-name

6. **Create a Pull Request**

```Submit a pull request from your fork to the main repository.```



### License
This software is licensed under the MIT License. Commercial use is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.

### Contact
For questions or further information, please contact:

**Author: Vedant Gaikwad**       
**Email: gaikwadvedant2@gamil.com**  
**GitHub: VEDAANT711**
