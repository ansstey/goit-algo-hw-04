def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-9') as file:
            salaries = []
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f'Error in line {line.strip()}')
            if not salaries:
                return 0, 0
            total = sum(salaries)
            average = total/len(salaries)
            return total, average
    except FileNotFoundError:
        print(f"File {path} wasn't found")
        return 0, 0
    except Exception:
        print(f"Error {Exception}")
        return 0, 0
