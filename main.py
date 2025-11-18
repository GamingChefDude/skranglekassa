from db.functions import *
from AI.AIBackend import *
from db.dataBase import *

print(get_user_by_email("eskil@epost"))

print(app)
print(app.template_folder)

if __name__ == "__main__":
    app.run(debug=True)
