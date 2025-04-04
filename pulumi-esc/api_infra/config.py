import pulumi

# Import the configuration values
config = pulumi.Config()

# Retrieve the values of "api-key" and "city"
endpoint_url = config.get("endpoint_url")
api_key = config.get("api-key")
city = config.get("city")
