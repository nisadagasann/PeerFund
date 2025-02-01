class User:
    def __init__(self, user_id, name, email, password, user_type, registration_date, segment_group=None, ai_cluster_id=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type  # Kullanıcı türü (örneğin: Admin, Borrower, Investor)
        self.registration_date = registration_date  # Tarih bilgisi
        self.segment_group = segment_group  # Opsiyonel alan
        self.ai_cluster_id = ai_cluster_id  # Opsiyonel alan

    def __repr__(self):
        return f"<User {self.name}, Type: {self.user_type}>"
