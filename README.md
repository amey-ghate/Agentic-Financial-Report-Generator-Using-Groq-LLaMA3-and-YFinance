📊 Agentic Financial Report Generator
=====================================

This project is an **Agentic Financial Report Generator**, designed to create professional, markdown-formatted fundamental and valuation reports for publicly listed companies using AI. Powered by **Groq's LLaMA3 model**, the agent combines real-time financial data and reasoning capabilities to deliver insightful, structured outputs.

Features
--------

*   **Agentic Execution**: Uses the agno.agent framework to create a self-contained intelligent agent.
    
*   **Groq LLaMA3 Model**: Leverages the high-speed performance of Groq’s LLaMA 3 (70B) model.
    
*   **YFinance Integration**: Fetches real-time data such as:
    
    1.  Stock price and changes
        
    2.  Analyst recommendations
        
    3.  Company fundamentals
        
    4.  Recent financial news
        
*   **Reasoning Tools**: Adds logical breakdown and intermediate steps behind the analysis.
    
*   **Structured Output**: Generates markdown tables with only the report content.
    
*   **Streamed Reasoning**: Intermediate thoughts and processing are streamed for transparency.
    

Prerequisites
-------------

Before getting started, ensure the following are installed:

*   Python 3.8 or later
    
*   An active Groq API key
    
*   Required Python libraries (listed in requirements.txt)
    

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/agentic-financial-report-generator.gi
   cd agentic-financial-report-generator
    ```   
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
    ```   
3. Create a .env file in the root directory and add your Groq API key:
    ```bash
   GROQ_API_KEY=your_groq_api_key_here
    ```  
---
    

Usage
-----

Run the Python script:
```bash
   python main.py
```


The agent will:

*   Connect to Groq
    
*   Use YFinance to fetch data on the company (e.g., Apple)
    
*   Output a valuation and fundamentals report in markdown
    
*   Stream intermediate reasoning steps
    

To modify the company being analyzed, change the prompt in the message argument:
```bash
   message="Write a fundamental & valuation report on MICROSOFT"
```

File Structure
--------------

*   main.py: Main script to launch the agent and generate the report.
    
*   requirements.txt: Python dependencies.
    
*   .env: Environment file to store Groq API key.
    
*   README.md: Documentation.
    

Example Output
--------------

### Input:
```bash
   message="Write a fundamental & valuation report on APPLE"
```

### Output:

*   Markdown-formatted financial report
    
*   Includes stock summary, key metrics, analyst insights, and recent headlines
    
*   Shows streamed intermediate reasoning from the agent
    

Customization
-------------

*   **Model Temperature**: Adjust creativity by changing the temperature parameter in the Groq model.
    
*   **Prompt Instructions**: Update the instructions section to tweak formatting or analysis style.
    
*   **Data Sources**: Extend the toolset to include additional APIs for more financial data.
    

Contributing
------------

Contributions are welcome! Please fork the repo and submit a pull request if you'd like to add new features or improvements.
