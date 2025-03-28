import json

class CreditRatingService:

    def __init__(
        self, 
        loan_amount: int, 
        property_value: int,
        debt_amount: int,
        annual_income: int,
        credit_score: int,
        loan_type: str,
        property_type: str  
    ):
        """ 
            The Credit Rating Service helps in calculating 
            risk_score, loan to property value ratio and ratio of debt
            to income.


        Args:
            loan_amount (int): Loan amount
            property_value (int): Value of property
            debt_amount (int): Debt amount
            annual_income (int): Annual Income
            credit_score (int): credit score
            loan_type (str): Loan type
            property_type (str): type of property.
        """
        self.loan_amount = loan_amount
        self.property_value = property_value
        self.debt_amount = debt_amount
        self.annual_income = annual_income
        self.credit_score = credit_score
        self.loan_type = loan_type
        self.property_type = property_type

    def calculate_ltv(self) -> float:
        """ 
            This functionality helps in calculating loan to property value ratio.
        Returns:
            float: ratio of loan to property value.
        """
        return (self.loan_amount/ self.property_value) * 100

    def calculate_dti(self) -> float:
        """
            This functionality helps in calculating debt to annual income ratio.
        Returns:
            float: ratio of debt to annual income.
        """
        return (self.debt_amount / self.annual_income) * 100

    def calculate_risk_score(self) -> int:
        """
            This functionality helps in calculating risk score.
        Returns:
            int: risk score.
        """
        risk_score = 0
        
        # Loan-to-Value (LTV) Ratio
        ltv = self.calculate_ltv()
        if ltv > 90:
            risk_score += 2
        elif ltv > 80:
            risk_score += 1
        
        # Debt-to-Income (DTI) Ratio
        dti = self.calculate_dti()
        if dti > 50:
            risk_score += 2
        elif dti > 40:
            risk_score += 1
  
        # Credit Score
        if self.credit_score >= 700:
            risk_score -= 1
        elif self.credit_score < 650:
            risk_score += 1
        
        # Loan Type
        if self.loan_type == "fixed":
            risk_score -= 1
        elif self.loan_type == "adjustable":
            risk_score += 1
        
        # Property Type
        if self.property_type == "condo":
            risk_score += 1
        
        return risk_score


def calculate_credit_rating(mortgages):
    """
       This method helps in finding credit rating.

    Args:
        mortgages (list): list of mortgages.

    Returns:
        str: credit rating.
    """
    total_risk_score = 0
    total_credit_score = 0
    num_mortgages = len(mortgages)
    
    for mortgage in mortgages:
        credit_rating_service = CreditRatingService(
            loan_amount=mortgage['loan_amount'],
            property_value=mortgage['property_value'],
            debt_amount=mortgage['debt_amount'],
            annual_income=mortgage['annual_income'],
            credit_score=mortgage['credit_score'],
            loan_type=mortgage['loan_type'],
            property_type=mortgage['property_type']
        )
        total_risk_score += credit_rating_service.calculate_risk_score()
        total_credit_score += mortgage["credit_score"]
    
    avg_credit_score = total_credit_score / num_mortgages
    
    # Adjust risk score based on average credit score
    if avg_credit_score >= 700:
        total_risk_score -= 1
    elif avg_credit_score < 650:
        total_risk_score += 1
    
    # Determine Credit Rating
    if total_risk_score <= 2:
        return "AAA"
    elif 3 <= total_risk_score <= 5:
        return "BBB"
    else:
        return "C"

def validate_mortgage(mortgage):
    """
        This method validate the input data.

    Args:
        mortgage (dict): single mortgage

    Returns:
        boolean: valid/invalid input.
    """
    required_fields = ["credit_score", "loan_amount", "property_value", "annual_income", "debt_amount", "loan_type", "property_type"]

    # Check if all required fields exist
    for field in required_fields:
        if field not in mortgage:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate types and ranges
    if not isinstance(mortgage["credit_score"], int) or not (300 <= mortgage["credit_score"] <= 850):
        raise ValueError("Invalid credit_score. Must be an integer between 300 and 850.")
    
    if not isinstance(mortgage["loan_amount"], (int, float)) or mortgage["loan_amount"] <= 0:
        raise ValueError("Invalid loan_amount. Must be a positive number.")
    
    if not isinstance(mortgage["property_value"], (int, float)) or mortgage["property_value"] <= 0:
        raise ValueError("Invalid property_value. Must be a positive number.")
    
    if not isinstance(mortgage["annual_income"], (int, float)) or mortgage["annual_income"] <= 0:
        raise ValueError("Invalid annual_income. Must be a positive number.")
    
    if not isinstance(mortgage["debt_amount"], (int, float)) or mortgage["debt_amount"] < 0:
        raise ValueError("Invalid debt_amount. Must be a non-negative number.")
    
    if mortgage["loan_type"] not in ["fixed", "adjustable"] or not isinstance(mortgage["loan_type"], str):
        raise ValueError("Invalid loan_type. Must be 'fixed' or 'adjustable'.")
    
    if mortgage["property_type"] not in ["single_family", "condo"] or not isinstance(mortgage["property_type"], str):
        raise ValueError("Invalid property_type. Must be 'single_family' or 'condo'.")

    return True



# Example usage
if __name__ == "__main__":
    input_json = '''{
        "mortgages": [
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
    }'''
    try:
        data = json.loads(input_json)
        if "mortgages" not in data or not isinstance(data["mortgages"], list):
            raise ValueError("Invalid JSON structure: 'mortgages' must be a list.")
        
        for mortgage in data["mortgages"]:
            validate_mortgage(mortgage)

        rating = calculate_credit_rating(data["mortgages"])
        print(f"Credit Rating: {rating}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")