from website import create_app
from website.models import *

app = create_app()

if __name__ == '__main__': #Only runs this code if this file is run directly
    app.run(debug=True)