## I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20230030/w2051533
from graphics import *
#variables for counting different progression outcomes
progress_count = 0
progress_moduler_trailer = 0
module_retriever = 0
Exclude = 0

input_data = []

terminate = False

def get_credit_input(prompt):
    while True:
        try:
            credit_input = input(prompt)
            credit = int(credit_input)
            if credit not in range(0, 121, 20):
                print("Out of range.")
                print()
                continue
                
            return credit
        except ValueError:
            print("Integer Required")
            print()

def save_data_to_file(file_path, data):
    with open(file_path, 'a') as file:
        for student_data in data:
            file.write(','.join(map(str, student_data)) + '\n')

def load_data_from_file(file_path):
    loaded_data = []
    with open(file_path, 'r') as file:
        for line in file:
            credits = list(map(int, line.strip().split(',')))
            loaded_data.append(credits)
    return loaded_data

# Specify the text file extension ('data.txt')
file_path = 'progression_data.txt'
#loop to enter student data
while not terminate:
    pass_credit = get_credit_input("Enter your credit at pass: ")
    defer_credit = get_credit_input("Enter your credit at defer: ")
    fail_credit = get_credit_input("Enter your credit at fail: ")

    if (pass_credit + defer_credit + fail_credit) != 120:
        print("Total incorrect")
        print()
        continue

    if pass_credit == 120 and defer_credit == 0:
        print("Progress")
        progress_count += 1
    elif pass_credit == 100:
        print("Progress (module trailer)")
        progress_moduler_trailer += 1
    elif pass_credit <= 80 and fail_credit <= 60:
        print("Do not progress- module retriever")
        module_retriever += 1
    elif pass_credit <= 40 and fail_credit >= 80:
        print("Exclude")
        Exclude += 1

    # Add data to the list
    input_data.append([pass_credit, defer_credit, fail_credit])

    # Save data to file
    save_data_to_file(file_path, input_data)

    # Ask the user if they want to enter another set of data
    print()
    print("Would you like to enter another set of data?")
    role = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print()

    if role.lower() == 'y':
        continue

    while role.lower() != 'y' and role.lower() != 'q':
        role = input("Enter 'y' for yes or 'q' to quit and view results: ")
        print()
        continue
# if user quits then load the data from file and display the results
    if role.lower() == 'q':
        # Load data from file
        loaded_data = load_data_from_file(file_path)

        print("\nPart 2:")
        for student_data in loaded_data:
            if student_data[0] == 120 and student_data[1] == 0:
                print("Progress -", student_data[0],  student_data[1],  student_data[2])
            elif student_data[0] == 100:
                print("Progress(module trailer) -",  student_data[0],  student_data[1],  student_data[2])
            elif student_data[0] <= 80 and student_data[2] <= 60:
                print("Module retriever -", student_data[0],  student_data[1],  student_data[2])
            elif student_data[0] <= 40 and student_data[2] >= 80:
                print("Exclude -", student_data[0],  student_data[1],  student_data[2])

        break

def draw_bar(win, x, height, color, label, value):
    # Draw rectangular
    bar = Rectangle(Point(x, 550), Point(x + 50, 549 - height))
    bar.setFill(color)
    bar.setOutline(color_rgb(224, 250, 252))
    bar.draw(win)

    # Add label under each rectangle
    bar_text = Text(Point(x + 25, 570), label)
    bar_text.setSize(14)
    bar_text.draw(win)

    # Add value on each rectangle
    value_text = Text(Point(x + 25, 555 - height - 20), str(value))
    value_text.setSize(12)
    value_text.setStyle("bold")
    value_text.draw(win)
    
def histogram():
    win = GraphWin("Histogram", 1080, 720)
    win.setBackground("white")
    
    # Title
    title_of_bargraph = Text(Point(540, 30), "Histogram Results")
    title_of_bargraph.setSize(20)
    title_of_bargraph.setStyle("bold")
    title_of_bargraph.draw(win)

    # Bar 1= progress
    draw_bar(win, 100, 40 * progress_count, "yellow", "Progress", progress_count)

    # Bar 2 = trailer
    draw_bar(win, 300, 40 * progress_moduler_trailer, "pink", "Trailer", progress_moduler_trailer)

    # Bar 3 = retriever
    draw_bar(win, 500, 40 * module_retriever, "red", "Retriever", module_retriever)

    # Bar 4 = excluded
    draw_bar(win, 700, 40 * Exclude, "green", "Excluded", Exclude)

    # horizontal line
    line = Line(Point(50, 600), Point(1030, 600))
    line.draw(win)

    # represent the total value
    horizontal_line_represent = Text(Point(540, 670), f"{progress_count + progress_moduler_trailer + module_retriever + Exclude} Outcomes in Total")
    horizontal_line_represent.setSize(15)
    horizontal_line_represent.setStyle("bold")
    horizontal_line_represent.draw(win)

   
    win.getMouse()
    win.close()

histogram()
