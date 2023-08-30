
import faker
import polars as pl

def generate_fake_data():
    print('Generating fake data...')
    fake = faker.Faker()
    num_rows = 1000000
    fake_data = pl.DataFrame({'name': [fake.name() for i in range(num_rows)],
                                'age': [fake.random_int(18, 60) for i in range(num_rows)],
                                'job': [fake.job() for i in range(num_rows)],
                                'company': [fake.company() for i in range(num_rows)],
                                'address': [fake.address() for i in range(num_rows)],
                                'email': [fake.email() for i in range(num_rows)],
                                'phone_number': [fake.phone_number() for i in range(num_rows)],
                                'website': [fake.url() for i in range(num_rows)],
                                'blood_group': [fake.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')) for i in range(num_rows)],
                                'residence': [fake.city() for i in range(num_rows)],
                                'current_location': [fake.city() for i in range(num_rows)],
                                'favorite_food': [fake.random_element(elements=('Pizza', 'Hamburger', 'Hot Dog', 'Pasta', 'Sushi', 'Steak', 'Tacos', 'Burritos', 'Salad', 'Soup')) for i in range(num_rows)],
                                'favorite_color': [fake.color_name() for i in range(num_rows)],
                                'favorite_language': [fake.random_element(elements=('Python', 'R', 'Java', 'C++', 'C#', 'Javascript', 'Typescript', 'PHP', 'Go', 'Swift', 'Kotlin', 'Ruby', 'Perl', 'Scala', 'Julia', 'Haskell', 'Rust', 'Dart', 'Elixir', 'Clojure', 'Groovy', 'Lua', 'Matlab', 'Objective-C', 'Visual Basic', 'Assembly', 'Delphi', 'PowerShell', 'F#', 'CoffeeScript', 'VBA', 'COBOL', 'Ada', 'Fortran', 'Lisp', 'Scheme', 'Prolog', 'ABAP', 'Apex', 'Bash', 'Erlang', 'Forth', 'Hack', 'LabVIEW', 'Objective-J', 'OCaml', 'OpenEdge ABL', 'PL/SQL', 'RPG', 'Scratch', 'Smalltalk', 'Verilog')) for i in range(num_rows)],
                                'dog_or_cat': [fake.random_element(elements=('Dog', 'Cat')) for i in range(num_rows)],
                                'salary': [fake.random_int(1000, 10000) for i in range(num_rows)],
                                'weight': [fake.random_int(40, 100) for i in range(num_rows)],
                                'height': [fake.random_int(140, 200) for i in range(num_rows)],
                                'eye_color': [fake.random_element(elements=('Brown', 'Blue', 'Green', 'Gray')) for i in range(num_rows)],
                                'children': [fake.random_int(0, 5) for i in range(num_rows)],
                                'has_a_car': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_graduated': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_a_degree': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_company': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_pet': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_a_bike': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_a_motorcycle': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_a_truck': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
                                'has_a_car': [fake.random_element(elements=(True, False)) for i in range(num_rows)],
    })
    print('Fake data generated')
    print('Writing fake data to files...')
    fake_data.write_csv('data/fake_data.csv')
    fake_data.write_parquet('data/fake_data.parquet')
    fake_data.write_json('data/fake_data.json')
    fake_data.write_excel('data/fake_data.xlsx')
    print('Fake data written to files')
