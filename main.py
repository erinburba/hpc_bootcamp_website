
import datetime
from flask import Flask, request, jsonify, render_template
import sys
# import logging
import time
from chatbot import Chatbot

app = Flask(__name__)

@app.route('/')
def root_default():
	# For the sake of example, use static information to inflate the template.
	# This will be replaced with real information in later steps.
	dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
				   datetime.datetime(2018, 1, 2, 10, 30, 0),
				   datetime.datetime(2018, 1, 3, 11, 0, 0),
				   ]
	
	# images = [get_signed_gcs_download_url("eyebot-exams", "blastoise.png"), get_signed_gcs_download_url("eyebot-exams", "howdy/ANMP0023.jpg"),]

	return render_template('index.html', times=dummy_times)#, images=images)


@app.route('/<version>/echo', methods=['POST'])
def echo_default(version):
	"""Simple echo service."""
	message = request.get_json().get('message', '')
	return jsonify({'message': message})

@app.route('/query_chatbots', methods=['POST'])
def query_chatbots():

	print('printing')
	app.logger.info('testing info log')
	# query = request.
	query = request.form['query']
	print(f"in query_chatbots ... got query {query}", file=sys.stderr)

	try:
		chatbot_a = Chatbot("pickle_a.pkl")

		a_start = time.time()
		answer_a = chatbot_a.query(query).formatted_answer
		# answer_a = " ".join(str(chatbot_a.query(query)).split("\n")[1:])
		a_end = time.time()
		print(f"in query_chatbots ... A answered {answer_a}", file=sys.stderr)
		chatbot_a = None

		chatbot_b = Chatbot("pickle_b.pkl")
		b_start = time.time()
		answer_b = chatbot_b.query(query).formatted_answer
		# answer_b = " ".join(str(chatbot_b.query(query)).split("\n")[1:])
		b_end = time.time()
		print(f"in query_chatbots ... B answered {answer_b}", file=sys.stderr)
		chatbot_b = None
		# answer_a = "YAY A"
		# answer_b = "YAY B"
	except Exception as e:
		return jsonify({'group_a': "error", 'group_b': str(e)})

	# return jsonify({'group_a': answer_a, 'group_b': answer_a, 'group_a_time':  f"Took {(a_end-a_start):.2f} seconds to generate",  'group_b_time':  f"Took {(a_end-a_start):.2f} seconds to generate"})

	return jsonify({'group_a': answer_a, 'group_b': answer_b, 'group_a_time':  f"Took {(a_end-a_start):.2f} seconds to generate",  'group_b_time':  f"Took {(b_end-b_start):.2f} seconds to generate"})


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)