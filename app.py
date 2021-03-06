#!/Users/andresleal/.local/share/virtualenvs/PersonalityInsights-_jrMTAdN/bin/python3
from flask import Flask, render_template, request
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

import credentials

app = Flask(__name__, template_folder="./templates")


# make this POST method to accept the text
@app.route("/")
def hello_world():
	return render_template("index.html")
	# return render_template("detailView.html")


@app.route("/analyze", methods=['POST'])
def analyze():
	text = request.form["textToAnalyze"]

	apiKey = APIKEY
	url = URL

	authenticator = IAMAuthenticator(apiKey)
	service = PersonalityInsightsV3(
		version='2017-10-13',
		authenticator=authenticator
	)

	service.set_service_url(url)
	profile = service.profile(text, accept="application/json", consumption_preferences=True).get_result()

	# warnings = len(profile['warnings'])

	# print(f"Warnings: {warnings}")

	print(json.dumps(profile, indent=4))
	return json.dumps(profile)

@app.route("/detail")
def detailView():
	return render_template("detailView.html")