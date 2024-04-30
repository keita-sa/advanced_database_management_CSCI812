import sys
import os

# Add the directory containing mongodb_connection to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/mongodb_connection')

from db_connection import MongoDBConnection
from data_manipulation.data_operations import DataOperations
from gui_interface.gui import GUI

# Connect to MongoDB
mongo_connection = MongoDBConnection(host='localhost', port=27017, db_name='your_database')

# Initialize data operations
data_ops = DataOperations(mongo_connection)

# Launch GUI
app = GUI(mongo_connection)
