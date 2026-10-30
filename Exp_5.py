def generate_report_card(name, math, science, english):
    total = math + science + english
    percentage = (total / 300) * 100
    
    print("-" * 30)
    print(f"REPORT CARD: {name}")
    print("-" * 30)
    print(f"Math:    {math}")
    print(f"Science: {science}")
    print(f"English: {english}")
    print("-" * 30)
    print(f"Total: {total}/300")
    print(f"Percentage: {percentage:.2f}%")
    print("-" * 30)

generate_report_card("John Doe", 88, 92, 79)