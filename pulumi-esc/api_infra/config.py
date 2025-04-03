import pulumi

# Import the configuration values
config = pulumi.Config()

# Retrieve the values of "api-key" and "city"
api_key = config.get("api-key")
city = config.get("city")
