## Overview
This project is a submission of **Pulumi Deploy and Document Challenge** - *Shhh, It's a secret!*
## About the Project
This project configures a Lambda Code to run and fetch value from [weatherstack.com](https://weatherstack.com/) and would store the temperature in SSM under the parameter name /weather/temperature_value.
## How I used Pulumi ESC in my Project
I used Pulumi ESC to store the API key. It was really easy to setup the whole thing.
##### -Creating the environment
`esc env init <project-name/<environment-name>`
##### -Setting the value of API in esc
`esc env set <project-name>/<environment-name> <key> <value>`

For Example

`esc env set pulumi-esc/dev-env api-key <value>`

To use the values, first we have to set the config in the env file. We can edit the env file by using the following command:-

`esc env edit pulumi-esc/dev-env`

<pre>
  values:
  pulumiConfig:
    api-key: (value)
    city: New%20York
</pre> 

Now we can easily use this value in any project. For doing this, I configured Pulumi.(stack).yaml file to use the specified environment. 

<pre>environment:
  - pulumi-esc/dev-env
config:
  aws:region: us-east-1</pre>

Now I can use the configuration values, as I did in **config.py**, to be use in my code like the following:-

`config.py`<pre>
  import pulumi
  
  #Import the configuration values
  config = pulumi.Config()

  #Retrieve the values of "api-key" and "city"
  endpoint_url = config.get("endpoint_url")
  api_key = config.get("api-key")
  city = config.get("city")
</pre>

