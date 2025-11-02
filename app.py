from flask import Flask, render_template
from datetime import datetime

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def home_page():
    # Get the current time on the server
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Render the HTML template and pass data to it
    return render_template(
        'index.html', 
        page_title='My Simple Python App',
        message='Welcome to the Minimal Web Service!',
        server_time=current_time
    )

# Run the app
if __name__ == '__main__':
    # host='0.0.0.0' allows access from outside the container/localhost
    app.run(host='0.0.0.0', port=5000, debug=True)