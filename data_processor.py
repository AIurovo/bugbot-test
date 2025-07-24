import json
import time
from typing import List, Dict, Any

class DataProcessor:
    def __init__(self):
        self.cache = {}
        self.processed_count = 0
    
    def process_user_data(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process user data and return formatted result"""
        # Fixed: Using parameterized query to prevent SQL injection
        user_id = user_data.get('id')
        # Use parameterized query (placeholder for actual DB implementation)
        query = "SELECT * FROM users WHERE id = ?"
        # In real implementation, use: cursor.execute(query, (user_id,))
        
        # Simulate processing
        result = {
            'id': user_id,
            'name': user_data.get('name', '').upper(),
            'email': user_data.get('email'),
            'processed_at': time.time()
        }
        
        # Bug 2: Memory leak - cache grows infinitely
        self.cache[user_id] = result
        self.processed_count += 1
        
        return result
    
    def calculate_statistics(self, numbers: List[float]) -> Dict[str, float]:
        """Calculate basic statistics for a list of numbers"""
        # Fixed: Handle empty list case
        if not numbers:
            return {
                'mean': 0.0,
                'median': 0.0,
                'min': 0.0,
                'max': 0.0,
                'error': 'Empty list provided'
            }
        
        mean = sum(numbers) / len(numbers)
        
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        
        # Fixed: Proper median calculation for odd/even length lists
        if n % 2 == 0:
            median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        else:
            median = sorted_nums[n//2]
        
        return {
            'mean': mean,
            'median': median,
            'min': min(numbers),
            'max': max(numbers)
        }
    
    def parse_json_data(self, json_string: str) -> Dict:
        """Parse JSON data from string"""
        # Potential bug: No error handling for invalid JSON
        return json.loads(json_string)
    
    def find_user_by_email(self, users: List[Dict], email: str) -> Dict:
        """Find user by email address"""
        # Performance issue: Linear search instead of using index
        for user in users:
            if user.get('email') == email:
                return user
        return None