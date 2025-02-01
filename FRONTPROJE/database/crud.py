from database.connection import get_connection

# Kullanıcı İşlemleri
def create_user(name, email, password, user_type):
    print("Eklenecek veriler:", name, email, password, user_type)  # Debug için
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO [User] (name, email, password, user_type)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (name, email, password, user_type))
            connection.commit()
            print("Kullanıcı başarıyla oluşturuldu!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def get_users():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM [User]"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def get_users_with_details():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                SELECT u.id, u.name, u.email, t.type_name
                FROM [User] u
                JOIN UserType t ON u.user_type = t.id
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()


def update_user(user_id, name, email, password):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                UPDATE [User]
                SET name = ?, email = ?, password = ?
                WHERE id = ?
            """
            cursor.execute(query, (name, email, password, user_id))
            connection.commit()
            print("Kullanıcı başarıyla güncellendi!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def delete_user(user_id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM [User] WHERE id = ?"
            cursor.execute(query, (user_id,))
            connection.commit()
            print("Kullanıcı başarıyla silindi!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

# Borçlu İşlemleri
def create_borrower(user_id, credit_score, risk_level):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Borrower (user_id, credit_score, risk_level)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (user_id, credit_score, risk_level))
            connection.commit()
            print("Borçlu başarıyla oluşturuldu!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def get_borrowers():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Borrower"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def update_borrower(borrower_id, credit_score, risk_level):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                UPDATE Borrower
                SET credit_score = ?, risk_level = ?
                WHERE id = ?
            """
            cursor.execute(query, (credit_score, risk_level, borrower_id))
            connection.commit()
            print("Borçlu başarıyla güncellendi!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()


def delete_borrower(borrower_id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM Borrower WHERE id = ?"
            cursor.execute(query, (borrower_id,))
            connection.commit()
            print("Borçlu başarıyla silindi!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()


# Yatırımcı İşlemleri
def create_investor(user_id, investment_budget):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Investor (user_id, investment_budget)
                VALUES (?, ?)
            """
            cursor.execute(query, (user_id, investment_budget))
            connection.commit()
            print("Yatırımcı başarıyla oluşturuldu!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def get_investors():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Investor"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()
def delete_investor(investor_id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM Investor WHERE id = ?"
            cursor.execute(query, (investor_id,))
            connection.commit()
            print("Yatırımcı başarıyla silindi!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()




# Kredi Talebi İşlemleri
def create_loan_request(borrower_id, amount_requested, interest_rate):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO LoanRequest (borrower_id, amount_requested, interest_rate)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (borrower_id, amount_requested, interest_rate))
            connection.commit()
            print("Kredi talebi başarıyla oluşturuldu!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def get_loan_requests():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM LoanRequest"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()



def delete_loan_request(loan_request_id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM LoanRequest WHERE id = ?"
            cursor.execute(query, (loan_request_id,))
            connection.commit()
            print("Kredi talebi başarıyla silindi!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()


# Kredi İşlemleri
def create_loan(loan_request_id, total_amount):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Loan (loan_request_id, total_amount)
                VALUES (?, ?)
            """
            cursor.execute(query, (loan_request_id, total_amount))
            connection.commit()
            print("Kredi başarıyla oluşturuldu!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def get_loans():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Loan"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

# Yatırım İşlemleri
def create_investment(investor_id, loan_id, amount_invested):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Investment (investor_id, loan_id, amount_invested)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (investor_id, loan_id, amount_invested))
            connection.commit()
            print("Yatırım başarıyla oluşturuldu!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def get_investments():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Investment"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

def create_borrower(user_id, credit_score, risk_level):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Borrower (user_id, credit_score, risk_level)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (user_id, credit_score, risk_level))
            connection.commit()
        except Exception as e:
            print("Hata:", e)
        finally:
            connection.close()