import logging
import shape_manager

def menu():
    """
    Menu displayed to the user
    """
    print("Welcome to the shape creation program!")
    print("Please select your choice:")
    print("Add shape........1\n"
          "Show all shapes..2\n"
          "Update shape.....3\n"
          "Delete shape.....4\n"
          "Exit.............5")


def choice_from_user():
    """
    Asks for input from the user

    return selection
    """
    choice = input("enter your choice: ")
    return choice


def valid_your_choice(choice, valid_type):
    """
    Tests the input entered by the user.

    Requests: Input entered
    Requests: Test type
    If input is valid:
    Returns the input
    """
    if valid_type == "number":
        if choice.isdigit():
            return choice

    elif valid_type == "1-5 number":
        if choice in ["1", "2", "3", "4", "5"]:
            return choice

    elif valid_type.lower() == "shapes":
        if choice in ["circle", "rectangle", "square"]:
            return choice

    else:
        pass

def create_logger():
    """
    Creating and configuring loggers
    """
    logging.basicConfig(level=logging.DEBUG,
                            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s ",
                        filename = "logs_file.log", encoding="utf-8")
    logger = logging.getLogger(__name__)
    return logger


def open_json(filename, opening_type):
    """
    Opening the Jason file

    Receiver: File name
    Receiver: File opening type
    Opens the file as required
    """
    with open(filename, opening_type, encoding="utf-8") as file:
        pass


def main():
    program = True
    logger = create_logger()
    while program == True:
        logger.info("The program has been activated!")
        data = open_json("shapes.json", "r+")
        logger.info("Loading the json file")
        menu()
        logger.info("Displays a menu to the user")
        choice = choice_from_user()
        logger.info("Asks for a choice from the user")
        if valid_your_choice(choice, "1-5 number") == choice:
            logger.debug("Checks the correctness of the selection")
            print("kukuriku!")


if __name__ == "__main__":
    main()
