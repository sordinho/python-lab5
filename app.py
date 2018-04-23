from flask import Flask, render_template, request
import taskDB

app = Flask(__name__)


@app.route('/')
def index():
	# welcome page index.html
	return render_template("index.html", tasks=taskDB.read_from_db())


@app.route('/insert-task', methods=['POST'])
def insert_new_task():
	# retrieve the task to insert in db
	task_to_insert = request.form['new_task']

	# print(task_to_insert)

	# insert into DB
	taskDB.insert_in_db(task_to_insert)

	# go back the the updated home
	return render_template("index.html", tasks=taskDB.read_from_db())

@app.route('/delete-task/<id>') #id will bw the parameter to pass at delete_task function
def delete_task(id):
	taskDB.remove_from_db(id)

	# go back the the updated home
	return render_template("index.html", tasks=taskDB.read_from_db())

if __name__ == '__main__':
	app.run()
