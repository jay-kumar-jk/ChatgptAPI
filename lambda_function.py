import json
import openai

def lambda_handler(event, context):
    # TODO implement
    openai.api_key = "Enter your key"

    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = event['headers']['search']
    
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    response = completion.choices[0].text

    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
