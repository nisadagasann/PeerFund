class Investment:
    def __init__(self, investment_id, investor_id, loan_id, amount_invested, return_rate, investment_date):
        self.investment_id = investment_id
        self.investor_id = investor_id
        self.loan_id = loan_id
        self.amount_invested = float(amount_invested)  # Finansal veri, float
        self.return_rate = float(return_rate)          # Yüzdesel oran, float
        self.investment_date = investment_date         # Tarih

    def calculate_return(self):
        """
        Yatırımın geri dönüş tutarını hesaplar.
        Return = Amount Invested * (1 + Return Rate)
        """
        return self.amount_invested * (1 + self.return_rate / 100)

    def __repr__(self):
        """
        Sınıfın okunabilir bir temsilini döndürür.
        """
        return (
            f"<Investment: ID={self.investment_id}, Investor={self.investor_id}, "
            f"Loan={self.loan_id}, Amount={self.amount_invested:.2f}, "
            f"ReturnRate={self.return_rate}%, Date={self.investment_date}>"
        )
