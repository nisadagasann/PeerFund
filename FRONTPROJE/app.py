from flask import Flask, render_template, request, redirect, url_for, flash
from services.risk_analysis import calculate_risk_score
from services.blockchain import connect_to_blockchain
from database.crud import (
    create_user, get_users, delete_user,
    create_borrower, get_borrowers, delete_borrower,
    create_investor, get_investors, delete_investor,
    get_connection, create_loan_request, get_loan_requests, delete_loan_request,create_loan , create_investment , update_borrower, 
)

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Flash mesajları için

# Ana sayfa
@app.route('/')
def home():
    return render_template('index.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    users = get_users()
    borrowers = get_borrowers()
    investors = get_investors()
    loans = get_loan_requests()
    return render_template('user_dashboard.html', users=users, borrowers=borrowers, investors=investors, loans=loans)

### Kullanıcı CRUD İşlemleri
@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':  # Kullanıcı ekleme işlemi
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('user_type')

        if not name or not email or not password or not user_type:
            flash("Lütfen tüm alanları doldurun!", "error")
        else:
            create_user(name, email, password, user_type)
            flash("Kullanıcı başarıyla eklendi!", "success")
        return redirect(url_for('manage_users'))

    # Kullanıcıları listeleme işlemi (GET isteği)
    users = get_users()
    return render_template('users.html', users=users)



@app.route('/users/delete/<int:user_id>')
def delete_user_route(user_id):
    delete_user(user_id)
    flash("Kullanıcı başarıyla silindi!")
    return redirect(url_for('manage_users'))

### Borçlu CRUD İşlemleri
@app.route('/borrowers', methods=['GET', 'POST'])
def manage_borrowers():
    if request.method == 'POST':
        user_id = request.form['user_id']
        credit_score = request.form['credit_score']
        risk_level = request.form['risk_level']
        create_borrower(user_id, credit_score, risk_level)
        flash("Borçlu başarıyla eklendi!")
    users = get_users()  # Kullanıcı listesini al
    borrowers = get_borrowers()  # Mevcut borçlu listesini al
    return render_template('borrowers.html', borrowers=borrowers, users=users)


@app.route('/borrowers/delete/<int:borrower_id>')
def delete_borrower_route(borrower_id):
    delete_borrower(borrower_id)
    flash("Borçlu başarıyla silindi!")
    return redirect(url_for('manage_borrowers'))

@app.route('/borrowers/update', methods=['POST'])
def update_borrower_route():
    borrower_id = request.form['borrower_id']
    credit_score = request.form['credit_score']
    risk_level = request.form['risk_level']
    update_borrower(borrower_id, credit_score, risk_level)
    flash("Borçlu başarıyla güncellendi!")
    return redirect(url_for('manage_borrowers'))


### Yatırımcı CRUD İşlemleri
@app.route('/investors', methods=['GET', 'POST'])
def manage_investors():
    if request.method == 'POST':
        user_id = request.form['user_id']
        investment_budget = request.form['investment_budget']
        result = create_investor(user_id, investment_budget)
        if result == "already_exists":
            flash("Bu kullanıcı zaten yatırımcı olarak eklenmiş!")
        else:
            flash("Yatırımcı başarıyla eklendi!")
    users = get_users()
    investors = get_investors()
    return render_template('investors.html', users=users, investors=investors)


@app.route('/investments', methods=['POST'])
def add_investment():
    investor_id = request.form['investor_id']
    loan_id = request.form['loan_id']
    amount_invested = request.form['amount_invested']
    return_rate = request.form['return_rate']
    create_investment(investor_id, loan_id, amount_invested, return_rate)
    return redirect(url_for('dashboard'))

def create_investor(user_id, investment_budget):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Zaten mevcutsa kontrol et
            check_query = "SELECT COUNT(*) FROM Investor WHERE user_id = ?"
            cursor.execute(check_query, (user_id,))
            if cursor.fetchone()[0] > 0:
                print("Bu kullanıcı zaten yatırımcı olarak eklenmiş.")
                return "already_exists"
            
            # Yeni yatırımcı ekle
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

def update_investor(investor_id, new_budget):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                UPDATE Investor
                SET investment_budget = ?
                WHERE id = ?
            """
            cursor.execute(query, (new_budget, investor_id))
            connection.commit()
            print("Yatırımcı başarıyla güncellendi!")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            connection.close()

@app.route('/investors/update', methods=['POST'])
def update_investor_route():
    investor_id = request.form['investor_id']
    new_budget = request.form['investment_budget']
    update_investor(investor_id, new_budget)
    flash("Yatırımcı başarıyla güncellendi!")
    return redirect(url_for('manage_investors'))


@app.route('/investors/delete/<int:investor_id>')
def delete_investor_route(investor_id):
    delete_investor(investor_id)
    flash("Yatırımcı başarıyla silindi!")
    return redirect(url_for('manage_investors'))

### Kredi Talebi CRUD İşlemleri
@app.route('/loans', methods=['GET', 'POST'])
def manage_loans():
    if request.method == 'POST':
        borrower_id = request.form['borrower_id']
        amount_requested = request.form['amount_requested']
        interest_rate = request.form['interest_rate']
        create_loan_request(borrower_id, amount_requested, interest_rate)
        flash("Kredi talebi başarıyla eklendi!")
    loans = get_loan_requests()
    return render_template('loans.html', loans=loans)

@app.route('/loans/delete/<int:loan_id>')
def delete_loan_route(loan_id):
    delete_loan_request(loan_id)
    flash("Kredi talebi başarıyla silindi!")
    return redirect(url_for('manage_loans'))

### Blockchain ve Risk Analizi
@app.route('/blockchain')
def blockchain_status():
    blockchain_connection = connect_to_blockchain()
    if blockchain_connection:
        flash("Blockchain ağına başarıyla bağlanıldı!")
    else:
        flash("Blockchain ağına bağlanılamadı!")
    return redirect(url_for('dashboard'))

@app.route('/risk_analysis', methods=['POST'])
def risk_analysis():
    credit_score = int(request.form['credit_score'])
    active_loans = int(request.form['active_loans'])
    investment_budget = float(request.form['investment_budget'])
    risk_score = calculate_risk_score(credit_score, active_loans, investment_budget)
    flash(f"Risk Skoru: {risk_score}")
    return redirect(url_for('dashboard'))

@app.route('/loans', methods=['POST'])
def add_loan():
    loan_request_id = request.form['loan_request_id']
    total_amount = request.form['total_amount']
    create_loan(loan_request_id, total_amount)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

