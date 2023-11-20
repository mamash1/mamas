import azure.functions as func
from weather import we


app = func.FunctionApp()

app.register_functions(we)
