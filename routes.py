from config import app
from controller_functions import root, addDojo, addNinja

app.add_url_rule("/", view_func=root)
app.add_url_rule("/addDojo", view_func=addDojo, methods=["POST"])
app.add_url_rule("/addNinja", view_func=addNinja, methods=["POST"])
