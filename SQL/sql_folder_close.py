def close(dbConnection):
    # Check if the connection exists, then close it
    if dbConnection:
        dbConnection.close()
        print("Connection closed")