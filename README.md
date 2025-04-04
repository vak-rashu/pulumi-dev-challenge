## Overview
This project is submitted as part of the **Pulumi Deploy and Document Challenge** – *"Shhh, It's a secret!"*  
It demonstrates how to securely store and access secrets using **Pulumi ESC** and integrate them into an AWS Lambda function.

## About the Project
The project deploys an AWS Lambda function that fetches weather data from [weatherstack.com](https://weatherstack.com/) and stores the current temperature in AWS Systems Manager (SSM) under the parameter path:  
`/weather/temperature_value`

## How I used Pulumi ESC in my Project
I used Pulumi ESC to store the API key. Pulumi ESC made it extremely easy to manage secrets like API keys without hardcoding them or using environment variables. The integration into Pulumi's configuration system was seamless and secure.It was really easy to setup the whole thing.

##### -Creating the environment
`esc env init <project-name/<environment-name>`

##### -Setting Secrets (API Keys)
`esc env set <project-name>/<environment-name> <key> <value>`

For Example

`esc env set pulumi-esc/dev-env api-key <value>`

##### -Editing the Environment
Using `esc env edit`, I configured the Pulumi values:

`esc env edit pulumi-esc/dev-env`
<pre>
  values:
  pulumiConfig:
    api-key: (value)
    city: New%20York
</pre> 

##### -Linking Environment in Pulumi.(stack).yaml
<pre>environment:
  - pulumi-esc/dev-env
config:
  aws:region: us-east-1</pre>

Inside my `config.py` file, I retrieved the configuration like this:-

<pre>
  import pulumi
  
  #Import the configuration values
  config = pulumi.Config()

  #Retrieve the values of "api-key" and "city"
  endpoint_url = config.get("endpoint_url")
  api_key = config.get("api-key")
  city = config.get("city")
</pre>

