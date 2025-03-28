import unittest
from credit_rating import calculate_credit_rating

class TestCreditRating(unittest.TestCase):
    def test_high_credit_score(self):
        mortgages = [
            {
                "credit_score": 750, 
                "loan_amount": 200000, 
                "property_value": 250000, 
                "annual_income": 60000, 
                "debt_amount": 20000, 
                "loan_type": "fixed", 
                "property_type": "single_family"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")
    
    def test_low_credit_score(self):
        mortgages = [
            {
                "credit_score": 600, 
                "loan_amount": 200000, 
                "property_value": 220000, 
                "annual_income": 40000, 
                "debt_amount": 25000, 
                "loan_type": "adjustable", 
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")
    
    def test_mixed_credit_scores(self):
        mortgages = [
            {
                "credit_score": 750, 
                "loan_amount": 200000, 
                "property_value": 250000, 
                "annual_income": 60000,
                "debt_amount": 20000, 
                "loan_type": "fixed", 
                "property_type": "single_family"
            },
            {
                "credit_score": 680, 
                "loan_amount": 150000, 
                "property_value": 175000, 
                "annual_income": 45000, 
                "debt_amount": 10000, 
                "loan_type": "adjustable", 
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")
    
    def test_edge_case_ltv_dti(self):
        mortgages = [
            {
                "credit_score": 680, 
                "loan_amount": 180000, 
                "property_value": 200000, 
                "annual_income": 50000, 
                "debt_amount": 25000, 
                "loan_type": "adjustable", 
                "property_type": "single_family"
            }
        ]
        print
        self.assertEqual(calculate_credit_rating(mortgages), "BBB")
    
    def test_average_credit_score_adjustment(self):
        mortgages = [
            {
                "credit_score": 640,
                "loan_amount": 150000, 
                "property_value": 180000, 
                "annual_income": 45000, 
                "debt_amount": 20000, 
                "loan_type": "adjustable", 
                "property_type": "condo"
            },
            {
                "credit_score": 630, 
                "loan_amount": 180000, 
                "property_value": 200000, 
                "annual_income": 50000, 
                "debt_amount": 25000, 
                "loan_type": "fixed", 
                "property_type": "single_family"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")

if __name__ == "__main__":
    unittest.main()
