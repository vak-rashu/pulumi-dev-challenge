import boto3
import json
import requests
from api_infra.config import api_key, city, endpoint_url

endpoint_url = endpoint_url
api_key = api_key
city_val = city

#set up SSM client
ssm_client = boto3.client("ssm",
            endpoint_url = endpoint_url,
            aws_access_key_id = 'test', 
            aws_secret_access_key = 'test',
            region_name = 'us-east-1',  
)

def handler(event, context):
        try:
            #getting value from the url
            base_url = f"https://api.weatherstack.com/current?access_key={api_key}&query={city_val}"
            response = requests.get(base_url)
            body = response.json()
            temperature = body["current"]["temperature"]

            #describing parameters
            parameter_name = "/weather/temperature_value"
            parameter_value = temperature

            #using ssm client to put the paratmets 
            response = ssm_client.put_parameter(
            Name=parameter_name,
            Value=parameter_value,
            Type="String",  
            Overwrite=True 
        )
            body = json.dumps({
                "message": "value added successfully"
            })

        except Exception as e:
            body = json.dumps({
                "error": e
            })
        return body
