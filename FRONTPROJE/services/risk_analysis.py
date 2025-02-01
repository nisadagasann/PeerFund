def calculate_risk_score(credit_score, active_loans, investment_budget):
    """
    Basit bir risk analizi algoritması:
    - Kredi skoru: 0-100 arasında
    - Aktif kredi sayısı: 0 veya üstü
    - Yatırım bütçesi: Pozitif bir sayı
    """
    base_score = credit_score
    if active_loans > 3:
        base_score -= active_loans * 2
    if investment_budget < 5000:
        base_score -= 10
    return max(0, base_score)  # Skor asla negatif olamaz
