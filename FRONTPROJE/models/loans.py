class Loan:
    def __init__(self, loan_id, loan_request_id, approval_date, total_amount):
        self.loan_id = loan_id
        self.loan_request_id = loan_request_id
        self.approval_date = approval_date  # Tarih bilgisi
        self.total_amount = float(total_amount)  # Finansal veri, float

    def calculate_monthly_payment(self, months, interest_rate):
        """
        Aylık ödeme tutarını hesaplar.
        Formül: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
        P: Ana para (total_amount)
        r: Aylık faiz oranı (yıllık faiz oranı / 12)
        n: Toplam ay sayısı
        """
        monthly_rate = interest_rate / 12 / 100  # Aylık faiz oranı
        if monthly_rate == 0:  # Faiz oranı sıfırsa
            return self.total_amount / months
        numerator = self.total_amount * monthly_rate * ((1 + monthly_rate) ** months)
        denominator = ((1 + monthly_rate) ** months) - 1
        return numerator / denominator

    def __repr__(self):
        """
        Sınıfın okunabilir bir temsilini döndürür.
        """
        return (
            f"<Loan ID: {self.loan_id}, Request ID: {self.loan_request_id}, "
            f"Amount: {self.total_amount:.2f}, Approval Date: {self.approval_date}>"
        )
