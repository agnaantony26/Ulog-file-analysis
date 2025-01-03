import json


def load_mission_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Analyze the original and translated code
def analyze_codes(data):
    original_code = data.get('original_code', '')
    translated_code = data.get('translated_code', '')

    print("==== Original Code ====")
    print(original_code)
    print("\n==== Translated Code ====")
    print(translated_code)

    # Extract simple insights from the original and translated code
    print("\n==== Analysis of Original Code ====")
    analyze_original_code(original_code)

    print("\n==== Analysis of Translated Code ====")
    analyze_translated_code(translated_code)

# Analyze the original code for basic structure and patterns
def analyze_original_code(code):
    # Simple analysis for function-like calls and conditionals
    functions = ['mu', 'md', 'mf', 'tu', 'tc']
    conditions = ['?x%2==0', '?x%2==1']
    
    print("\nDetected Function Calls:")
    for func in functions:
        if func in code:
            print(f"- {func}")
    
    print("\nDetected Conditions:")
    for cond in conditions:
        if cond in code:
            print(f"- {cond}")

# Analyze the translated code (Python code) for key sections like async functions, imports, etc.
def analyze_translated_code(code):
    lines = code.split('\n')
    async_functions = []
    imports = []
    control_statements = ['if', 'await', 'try', 'except']
    
    for line in lines:
        # Detect async functions
        if 'async def' in line:
            async_functions.append(line.strip())
        
        # Detect imports
        if 'import' in line or 'from' in line:
            imports.append(line.strip())
        
        # Detect control statements
        for statement in control_statements:
            if statement in line:
                print(f"Control Statement: {line.strip()}")
    
    print("\nDetected Async Functions:")
    for func in async_functions:
        print(f"- {func}")
    
    print("\nDetected Imports:")
    for imp in imports:
        print(f"- {imp}")

# Main function to load and analyze the mission file
def main(file_path):
    data = load_mission_file(file_path)
    analyze_codes(data)

# Provide the path to the mission.json file
if __name__ == "__main__":
    file_path = './mission_code.json'  
    main(file_path)
