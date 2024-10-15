#### 10/14/2024: Update to remove unnecessary files, modify code in Home.py to remove errors
#### 10/15/2024: Created an all-in-one app as well as an app.py with crew.py. removed all other files
####             pdf and txt files of results are written to the project and named appropriately
####             updated streamlit page, removing tushar's personal information except for his original
####             copywrite statement.. much of his work has been removed and modified, but his work was still
####             the inspiration and initial backbone for this project.


# BloggerCrew - Current Topic Blogs Writer with Llama3 via Ollama, Groq and CrewAI
## Overview

BloggerCrew is an innovative tool designed to streamline the process of writing topical blog content using advanced AI technologies. By leveraging Llama3 through platforms like Ollama, Groq, and CrewAI, BloggerCrew offers a seamless experience in generating high-quality blog posts efficiently.

## Features

- **AI-Powered Content Creation**: Utilizes Llama3's capabilities to generate relevant and engaging blog content.
- **Integration with Ollama and Groq**: Offers local deployment and enhanced performance with Groq's powerful processing capabilities.
- **Collaborative AI Agents**: Employs CrewAI's multi-agent framework for optimized task execution.

## Installation

To set up BloggerCrew on your local machine, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/Tina-Sterite/Blogger_Crew
   cd bloggercrew
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```
   Note: I have not tested this installation, I was not successful setting up a new environment so I used a previously created environment from the stock-analysis-agents project and added what came up as missing while attempting execution. 
   pip install -r requirements.txt
   ```

3. **Setup Ollama**:
   Download and install Ollama to run Llama3 locally:
   ```
   ollama run llama3
   ```

4. **Configure Groq (Optional)**:
   For enhanced performance, configure Groq by obtaining an API key and setting it up in your environment.

## Usage

To start generating content, execute the following command:
```
streamlit run app.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of Llama3, Ollama, Groq, and CrewAI for their incredible tools that make this project possible.
- Special thanks to all contributors who have helped enhance BloggerCrew.
- And to this project's forked project creator: Tushar Aggarwal.




