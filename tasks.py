TASKS = [
    {
        "id": "easy",
        "code": "def add(a,b):return a+b",
        "expected": {
            "bug": False,
            "issue": "formatting"
        }
    },
    {
        "id": "medium",
        "code": "def divide(a,b): return a/0",
        "expected": {
            "bug": True
        }
    },
    {
        "id": "hard",
        "code": "def fetch(): pass",
        "expected": {
            "bug": False,
            "suggestion": "implement function"
        }
    }
]