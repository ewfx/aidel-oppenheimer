# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

Note
We uploaded the dataset we used for getting the outputs for low risk, moderate risk and high risk
The OPEN AI API key works for only 2 days. The latest we generated was on 26th March. If any error comes when trying to send data kindly contact us. 
Rajahrushikesh.Swamy@wellsfargo.com
Tanvi.Singh@wellsfargo.com
dwaarakesh.ramesh@wellsfargo.com


## 🎯 Introduction
Our project aims to build an AI-driven system to automate and enhance the analysis of transaction data, addressing the problem of identifying and assessing entities involved in financial transactions. This solution is designed to reduce manual effort, improve accuracy, and provide actionable insights for analysts.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
The project is inspired by the need to automate and enhance the manual process of analyzing financial transactions for potential fraud and risk. Analysts often face challenges such as:
Unstructured data: Extracting meaningful insights from inconsistent or incomplete transaction details.
Complex risk factors: Evaluating multiple dimensions like entity reputation, transaction patterns, and geographic risks.
Time constraints: Manually assessing large volumes of data is time-consuming and prone to errors.
This system leverages OpenAI's GPT model to provide a structured, scalable, and intelligent solution for these challenges.

## ⚙️ What It Does
1. Risk Scoring Framework: A detailed scoring system evaluates transactions across five categories (e.g., Entity Reputation, Transaction Amount, etc.) and calculates a total risk score.
2. Data Enrichment: Incorporates external data (e.g., geographic details from IP addresses) to enhance analysis.
3. Structured Outputs: Provides JSON-formatted results for easy integration with other systems.
4. Customizable Analysis: Allows for additional categories and insights based on transaction details.

## 🛠️ How We Built It
This system was built using OpenAI's GPT API to automate financial transaction risk analysis. It processes transaction data, applies a predefined scoring framework (Entity Reputation, Transaction Amount, Geographic Risk, etc.), and calculates a Total Risk Score. Key features include:

1. Data Processing: Reads and processes structured (CSV) or unstructured data.
2. AI Analysis: Sends data to GPT for detailed scoring and reasoning.
3. Output Structuring: Extracts and formats results into JSON for easy integration.
4. Customizable Framework: Allows dynamic scoring and additional categories.

The system reduces manual effort, enhances accuracy, and provides actionable insights for analysts.

## 🚧 Challenges We Faced
1. OpenAI API Integration: Managing prompt engineering for consistent and accurate outputs while handling rate limits and response formatting.
2. Data Processing: Handling diverse input formats (CSV, text) and ensuring compatibility with the AI model.
3. Output Structuring: Parsing AI responses into structured JSON while managing incomplete or unexpected outputs.
4. Error Handling: Addressing issues like JSONDecodeError and ensuring graceful handling of invalid inputs.
5. Scoring Framework: Designing a balanced, comprehensive risk scoring system and aligning AI outputs with it.
6. External Data Enrichment: Incorporating external sources (e.g., IP geolocation) for enhanced analysis.
7. Scalability: Ensuring the system handles large datasets efficiently while remaining modular and extensible.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/aidel-oppenheimer.git
   ```
2. Install dependencies  
   ```sh
   pip install openai
   pip install -r requirements.txt
   ```
3. Run the project  
   ```sh
   python3 app.py
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: Flask
- 🔹 Backend: python
- 🔹 Other: OpenAI API

## 👥 Team
- **Raja Swamy** - [GitHub](#) | [LinkedIn](#)
- **Tanvi Singh** - [GitHub](#) | [LinkedIn](#)
- **Dwaarakesh Ramesh** - [GitHub](#) | [LinkedIn](#)
