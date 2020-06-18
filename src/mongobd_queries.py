from pymongo import MongoClient

# connecting a client to default port
client = MongoClient()

# creating a database
db = client['ST_tasks']

# create some documents
first_task = {'course': 'ST',
		'author': 'sergei',
		'task description': 'stdio pipes',
		'status': 'done'}

second_task = {'course': 'ST',
		'author': 'sergei',
		'task description': 'orientDB',
		'status': 'done'}

third_task = {'course': 'ST',
		'author': 'sergei',
		'task description': 'mongoDB',
		'status': 'in progress'}

# getting a collection
sergei_collection = db.sergei

# inserting a documents
first_id = sergei_collection.insert_one(first_task).inserted_id
second_id = sergei_collection.insert_one(second_task).inserted_id
third_id = sergei_collection.insert_one(third_task).inserted_id

print(f'Inserted docs ids {first_id}, {second_id}, {third_id}')

# getting a single document
print('Task in progress', sergei_collection.find_one({'status': 'in progress'}))

# get a document by its id
print(f'Here is the document with {second_id} id', sergei_collection.find_one({'_id': second_id}))


# let's get the list of documents by query
for task in sergei_collection.find({'status': 'done'}):
	print(task)
