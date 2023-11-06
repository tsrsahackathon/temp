
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://shriteqhackathon:5F5RZ96CiqZY4jzM@hackathon.vs7oa0j.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Define the list of file names to be uploaded
    file_names = ['PUNC_transcript.txt',
                  'summary.txt', 'keywords.txt', 'quiz.txt']

    # Create a new collection in MongoDB
    # Replace 'your_database_name' with your actual database name
    db = client['Inscribd']
    # Replace 'your_collection_name' with your actual collection name
    collection = db['Files']

    # Iterate through the file names and insert their contents into MongoDB
    for file_name in file_names:
        with open(file_name, 'r') as file:
            file_content = file.read()
            result = collection.insert_one(
                {'file_content': file_content, 'file_name': file_name})
            print(
                f"Inserted document with _id: {result.inserted_id} for {file_name}")

except Exception as e:
    print(e)
