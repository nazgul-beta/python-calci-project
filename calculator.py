
class Calculator:
    def add(self, a, b):
        # No type checking or validation
        return a + b

    def subtract(self, a, b):
        # Could use better error handling
        return a - b

    def multiply(self, a, b):
        # Missing docstring and input validation
        return a * b

    def divide(self, a, b):
        # Basic division without proper error handling
        return a / b

# Global instance - potential improvement area
calculator = Calculator()
