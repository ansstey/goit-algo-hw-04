def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({
                        'id': cat_id,
                        'name': name,
                        'age': age
                    })
                except ValueError:
                    print(f'Error in {line.strip()}')
            return cats
    except FileNotFoundError:
        print(f"File {path} wasn't found")
        return []
    except Exception:
        print(f"Error {Exception}")
        return []
