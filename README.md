# Credit Rating System for RMBS

## Overview
This project implements a **credit rating system** for **Residential Mortgage-Backed Securities (RMBS)**. The system evaluates mortgage risk using key financial metrics such as:
- **Loan-to-Value (LTV) Ratio**
- **Debt-to-Income (DTI) Ratio**
- **Borrower Credit Scores**
- **Loan Type** (Fixed or Adjustable)
- **Property Type** (Single Family or Condo)

Based on these factors, the system assigns a **credit rating** of `AAA`, `BBB`, or `C` to the RMBS.

## Project Structure
```
credit_rating_mock/
│
├── credit_rating.py          # Business logic for calculating credit rating
├── test_credit_rating.py     # Unit tests for validation
├── requirements.txt          # Required Python packages
└── README.md                 # Documentation
```

## Installation
1. Clone the repository:
    ```sh
   git clone git@github.com:yashsarjekar/rmbs-credit-evaluator.git .
   ```

   ```sh
   cd credit_rating_mock
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the **credit rating calculator** :
```sh
python credit_rating.py
```
Example JSON format:
```json
{
    "mortgages": [
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
}
```

## Running Tests
To run unit tests:
```sh
python -m unittest test_credit_rating.py
```


## Credit Rating Algorithm
### **1. Loan-to-Value (LTV) Ratio**
- `LTV > 90%` → Add `2` risk points
- `LTV > 80%` → Add `1` risk point

### **2. Debt-to-Income (DTI) Ratio**
- `DTI > 50%` → Add `2` risk points
- `DTI > 40%` → Add `1` risk point

### **3. Credit Score**
- `Credit Score >= 700` → Subtract `1` risk point
- `Credit Score < 650` → Add `1` risk point

### **4. Loan Type**
- `Fixed-rate` → Subtract `1` risk point
- `Adjustable-rate` → Add `1` risk point

### **5. Property Type**
- `Single-family home` → No change
- `Condo` → Add `1` risk point

### **6. Average Credit Score Adjustment**
- `Average Credit Score >= 700` → Subtract `1` risk point
- `Average Credit Score < 650` → Add `1` risk point

### **Final Credit Rating**
| Total Risk Score | Credit Rating |
|-----------------|--------------|
| `<= 2`         | AAA (Highly Secure) |
| `3 - 5`        | BBB (Medium Risk) |
| `> 5`          | C (High Risk) |

## Error Handling
- **Invalid JSON Structure** → Raises an error
- **Missing Fields** → Returns a validation error

## Future Enhancements
- Support for larger datasets
- Integration with a database
- Web API for real-time rating retrieval
- Implement logging and exception handling.

## Author
- Yash Sarjekar