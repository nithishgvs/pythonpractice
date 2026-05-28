from typing import List


class Employee:
    def __init__(self, emp_id: int, importance: int, subordinates: List[int]):
        self.id = emp_id
        self.importance = importance
        self.subordinates = subordinates





class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        return self.dfs(id, emp_map)

    def dfs(self, emp_id, emp_map):
        employee = emp_map[emp_id]
        return employee.importance + sum(self.dfs(sub, emp_map) for sub in employee.subordinates)


def make_employee(emp_id, importance, subordinates):
    # Helper so tests are easier to read (like a factory method in Java)
    return Employee(emp_id, importance, subordinates)


def run_tests():
    sol = Solution()

    # Test 1: Basic - manager with two subordinates
    # Tree:  1(5) -> [2(3), 3(4)]
    # Total = 5 + 3 + 4 = 12
    employees = [
        make_employee(1, 5, [2, 3]),
        make_employee(2, 3, []),
        make_employee(3, 4, []),
    ]
    result = sol.getImportance(employees, 1)
    print(f"Test 1: {result} (expected 12) -> {'PASS' if result == 12 else 'FAIL'}")

    # Test 2: Start from a subordinate, not the root
    # Same tree but query from emp 2 (no subordinates)
    # Total = 3
    employees = [
        make_employee(1, 5, [2, 3]),
        make_employee(2, 3, []),
        make_employee(3, 4, []),
    ]
    result = sol.getImportance(employees, 2)
    print(f"Test 2: {result} (expected 3) -> {'PASS' if result == 3 else 'FAIL'}")

    # Test 3: Only one employee, no subordinates
    employees = [make_employee(1, 7, [])]
    result = sol.getImportance(employees, 1)
    print(f"Test 3: {result} (expected 7) -> {'PASS' if result == 7 else 'FAIL'}")

    # Test 4: Chain - 1 -> 2 -> 3 (three levels deep)
    # Total from root = 10 + 5 + 2 = 17
    employees = [
        make_employee(1, 10, [2]),
        make_employee(2, 5, [3]),
        make_employee(3, 2, []),
    ]
    result = sol.getImportance(employees, 1)
    print(f"Test 4: {result} (expected 17) -> {'PASS' if result == 17 else 'FAIL'}")

    # Test 5: Query from middle of chain (emp 2)
    # Total = 5 + 2 = 7
    result = sol.getImportance(employees, 2)
    print(f"Test 5: {result} (expected 7) -> {'PASS' if result == 7 else 'FAIL'}")


if __name__ == "__main__":
    run_tests()

