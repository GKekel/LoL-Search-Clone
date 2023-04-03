import dotenv
import os
import pathlib

from flask import Flask, render_template, request
from api import fetch_summoner_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search-summoner', methods=['POST'])
def search_summoner():
    # Get the summoner name and region from the form
    summoner_name = request.form['summoner-name']
    region = request.form['region']

    # Fetch the summoner data from the API
    data = fetch_summoner_data(summoner_name, region)

    # Pass the summoner data to the template
    return render_template('search.html', data=data)


if __name__ == '__main__':
    app.run()


# #%%
# pathlib.Path('.env').exists()
# #%%
# dotenv.set_key('.env', '_TESTKEY', 'This is my test value')
# #%%
# pathlib.Path('.env').exists()
# #%%
# # we read the contents of the .env file
# pathlib.Path('.env').read_text()
# #%%
# # we test to see if the list of our current session's environment variables contain the env var of '_TESTKEY' - it doesn't
# print(os.getenv('_TESTKEY'))
# # %%
# # load the values from the .env file as environment variables for this session
# dotenv.load_dotenv()

# # %%
# # we test again to see if the list of our current session's environment variables contain the env var of '_TESTKEY' - now it does
# os.getenv('_TESTKEY')
# # %%
