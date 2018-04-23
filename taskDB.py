# Created by Davide Sordi in 23/04/2018 at 16.46

import pymysql


def read_from_db():
	"""
	Reading task list from a DB
	:return: a dictionary of tasks
	"""
	# prepare the query for reading from DB
	query = "SELECT * FROM tasks"

	# connectione to database
	connection = pymysql.connect(user="root", password="sysadmin", host="localhost", database="todolist")

	# get a cursor
	cursor = connection.cursor()

	# execute query
	cursor.execute(query)

	# fetch result from query
	results = cursor.fetchall()

	# close cursor and connection
	cursor.close()
	connection.close()

	return results


def remove_from_db(id_task_to_rem):
	"""
	function for deleting task from DB
	:param task: task to delete in DB
	"""
	# delete query
	query = "DELETE FROM tasks WHERE id_task=(%s)"

	# connection to database
	connection = pymysql.connect(user="root", password="sysadmin", host="localhost", database="todolist")
	# get a cursor
	cursor = connection.cursor()

	# execute query
	cursor.execute(query, (id_task_to_rem,))
	# commit on DB
	connection.commit()
	# close cursor and connection
	cursor.close()
	connection.close()


def insert_in_db(task):
	"""
	insert a new task in DB
	:param task: the task to insert
	"""
	# insert query
	query = "INSERT INTO tasks (todo) VALUES (%s)"
	# connection to database
	connection = pymysql.connect(user="root", password="sysadmin", host="localhost", database="todolist")
	# get a cursor
	cursor = connection.cursor()
	# execute query
	cursor.execute(query, (task,))
	# commit on DB
	connection.commit()
	# close cursor and connection
	cursor.close()
	connection.close()

print(read_from_db())