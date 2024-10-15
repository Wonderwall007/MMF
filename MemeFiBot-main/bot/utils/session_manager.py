class SessionManager:
    def __init__(self):
        # This dictionary will store the query IDs
        self.sessions = {}

    def create_session(self, session_identifier, query_id):
        # This function will store the query ID with a corresponding identifier
        self.sessions[session_identifier] = query_id

    def get_query_id(self, session_identifier):
        # This function will retrieve the query ID for a given identifier
        return self.sessions.get(session_identifier)
