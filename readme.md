# Delivery Cost Calculator - Software Testing & Quality Assurance Project

This project implements a delivery cost calculation system with comprehensive test coverage for the Software Testing & Quality Assurance course (INT3117 1).

## 📋 Project Description

The project contains a delivery cost calculation function that computes shipping costs based on package weight and delivery distance. The system includes input validation and comprehensive unit tests to ensure code quality and reliability.

## 🚀 Features

- **Delivery Cost Calculation**: Calculate shipping costs based on weight and distance
- **Input Validation**: Validate weight (0.5-100 kg) and distance (1-500 km) parameters
- **Comprehensive Testing**: Multiple test suites covering various scenarios
- **Error Handling**: Proper error messages for invalid inputs

## 📦 Installation

Install the necessary packages using the following command:

```bash
pip install -r requirements.txt
```

## 🛠️ Usage

### Running the Main Application

```python
from main import tinh_chi_phi_giao_hang

# Calculate delivery cost
cost = tinh_chi_phi_giao_hang(weight, distance)
```

### Function Parameters

- `weight` (float): Package weight in kilograms (0.5 ≤ weight ≤ 100)
- `distance` (float): Delivery distance in kilometers (1 ≤ distance ≤ 500)

### Function Returns

- **Valid inputs**: Returns the calculated delivery cost (float)
- **Invalid inputs**: Returns "Đầu vào không hợp lệ" (Invalid input)

### Cost Formula

```
Cost = 10 + (Weight × 0.5) + (Distance × 0.2)
```

## 🧪 Testing

The project includes comprehensive test suites to ensure code quality:

### Running Test Suite C2

```bash
python test_C2.py
```

This test suite covers:
- Valid input scenarios
- Invalid weight validation
- Invalid distance validation

### Running All Uses Test Suite

```bash
python test_all_uses.py
```

This test suite covers:
- Boundary value testing
- Multiple test scenarios
- Edge case validation

## 📁 Project Structure

```
├── main.py              # Main delivery cost calculation function
├── test_C2.py           # Test suite C2 with validation tests
├── test_all_uses.py     # Comprehensive test suite for all use cases
├── requirements.txt      # Python dependencies
└── readme.md           # Project documentation
```

## 🎯 Test Coverage

The project includes tests for:
- ✅ Valid input scenarios
- ✅ Invalid weight handling (out of range)
- ✅ Invalid distance handling (out of range)
- ✅ Boundary value testing
- ✅ Multiple test scenarios

## 📚 Dependencies

- `unittest`: Python's built-in testing framework

## 👨‍💻 Author

This project was created as part of the Software Testing & Quality Assurance course (INT3117 1).

## 📄 License

This project is created for educational purposes as part of the Software Testing & Quality Assurance coursework.