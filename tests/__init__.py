from src import create_app

app, client = create_app(mongodb_host_name="localhost", mongodb_port=27018)
