from openai import OpenAI
import json
import re
client = OpenAI(
    api_key="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"
)

system_message={"role":"system",
                "content": """Act as a financial data analyst and assess transactions for potential fraud risks using the following framework. Ensure you analyze every aspect thoroughly, even seemingly minor details, and extract all meaningful insights.

### Scoring System (Total Risk Score: 0-100):

1. Entity Reputation (20 pts):
   - 0-5: Clean history
   - 6-10: Minor disputes
   - 11-15: Legal issues
   - 16-20: Sanctions or fugitive status

2. Transaction Amount (15 pts):
   - 0-5: Normal amount
   - 6-10: Unusual amount
   - 11-15: Extremely high or low

3. Geographic Risk (15 pts):
   - 0-5: Low-risk (USA/EU)
   - 6-10: Moderate-risk
   - 11-15: High-risk (FATF blacklist)

4. Transaction Pattern (20 pts):
   - 0-5: Normal pattern
   - 6-10: Irregular timing
   - 11-15: Structured payments
   - 16-20: No logical purpose

5. External Data (30 pts):
   - 0-10: No red flags
   - 11-20: Negative news
   - 21-30: Sanctions/legal actions

### Approach:
- Perform detailed sub-scoring for each category, ensuring you evaluate each aspect fully.If it involves multiple reason, assign score to every reason within that category and then take an average of all reasons to decide final sub score for that particular category. and then sum up all category score to get final risk score. Pay attention to potentially minor details such as transaction dates, which may hold relevance to the entity involved.
- Extract relevant entities efficiently and make note of any indicators that might suggest risks, even those that initially seem trivial.
- give proper reasoning
-for proper separating of data give heading as category score
-the above mentioned 5 catogories shall be seperated by ### 
-if there is any other important data that does not lie in the above category then show that other data by creating category yourself.
-if ip address is present in the data then using this link https://tools.keycdn.com/geo?host=2001%3A4860%3A7%3A405%3A%3A69 or any other link find the geo location and related detail
-always give total risk score as a seperate heading (seperated by ###) and in this format ..sample->Total Risk Score Calculation
Now let's sum up these category scores to reach a total risk score:
- Entity Reputation: 8
- Transaction Amount: 10
- Geographic Risk: 10
- Transaction Pattern: 20
- External Data: 20

Total Risk Score = 8 + 10 + 10 + 20 + 20 = 78
-GIVE THE TOTAL RISK SCORE CALCULATION WITH PROPER SUB CATEGORY SCORES ALWAYS"""}

def responseFetcher(data):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            system_message,
            {
                "role": "user",
                "content": f"Here is the transaction detail for you to analyse:'{data}'"
            }
        ]
    )

    output_message = completion.choices[0].message.content

    # Check if it's JSON format and print it properly
    try:
        parsed_output = json.loads(output_message)
        print(json.dumps(parsed_output, indent=4))  # Pretty-print JSON output
    except json.JSONDecodeError:
        print("lets go")
        #print(output_message)
    return output_message

def read_file(file_content, file_extension):
    if file_extension == 'csv':
        # Convert CSV content to a string
        df = pd.read_csv(io.StringIO(file_content))
        content = df.to_string()  # You could also process this to a more specific format
    else:
        content = file_content  # If it's just plain text or a txt file, we can directly use it
    return content

def handle_file_and_get_response(content):
   
    
    # Step 2: Send the content to OpenAI and get the response
    output_message = responseFetcher(content)
    processed_output = process_output(output_message)
    for heading, content in processed_output.items():
        
        print(heading)
        processed_output[heading]=content
        print(processed_output[heading])
        print("\n")
    # Step 3: Return or display the response
    return processed_output

def process_output(output):
    # Remove ** and * characters
    output = re.sub(r'[\*\*|\*]', '', output)
    
    # Split the message by ### and filter out empty sections
    sections = [section.strip() for section in output.split('###') if section.strip()]
    
    # Create a dictionary to map each heading to its content
    heading_dict = {}
    for section in sections:
        heading, *content = section.split("\n", 1)
        heading = heading.strip()
        content = content[0].strip() if content else ""
        # Keep line breaks in content intact
        heading_dict[heading] = content.strip()
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {
            "role": "system",
            "content": """The user will give a dictionary. Extract the value for the key-(total risk score calculation only). convert those sub score values and total value to json AND JUST GIVE ME only THE JSON (do not put it under '''json ''' like that)  , DO NOT GIVE ANY EXPLAINATION OR THEORIATICAL REPLY.convert in json format to structure as shown =>{
  "Entity Reputation": 5,
  "Transaction Amount": 5,
  "Geographic Risk": 10,
  "Transaction Pattern": 10,
  "External Data": 10,
  "Total Risk Score":40}"""
        },
        
        {
            "role": "user",
            "content": f"Dictionary=>'{str(heading_dict)}'"
        },

    ]
    )

    output_message = completion.choices[0].message.content
    heading_dict["pie_score"]=output_message

    

    return heading_dict