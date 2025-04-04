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

`esc env set pulumi-esc/den-env api-key <value>`

After this we can easily use this value set in any project. For doing this, I used Pulumi.<stack>.yaml file to use the specified environment. 

<pre>```environment:
  - pulumi-esc/dev-env
  - pulumi-localstack/config-env
config:
  aws:region: us-east-1```</pre>


