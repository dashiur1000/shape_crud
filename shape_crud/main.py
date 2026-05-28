import logging
from shape_manager import ShapeManager


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


def choice_from_user(name_of_choice):
    """
    Asks for input from the user

    return selection
    """
    choice = input(f"enter your {name_of_choice}: ")
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
        raise ValueError("Incorrect choice!")

    elif valid_type == "1-3 number":
        if choice in ["1", "2", "3"]:
            return choice
        raise ValueError("Incorrect choice!")

    elif valid_type.lower() == "shapes":
        if choice in ["circle", "rectangle", "square"]:
            return choice
        raise ValueError("Incorrect choice!")

    elif valid_type == "size":
        try:
            float(choice)
            if float(choice) > 0:
                return choice
            else:
                raise ValueError("Incorrect size input!")
        except ValueError:
            raise ValueError("Incorrect size input!")

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



def main():
    program = True
    logger = create_logger()
    logger.info("The program has been activated!")
    logger.info("Loading the json file")
    logger.info("Displays a menu to the user")
    manager = ShapeManager()
    while program == True:
        menu()
        try:
            choice = choice_from_user("choice")
            logger.info("Asks for a choice from the user")
            if valid_your_choice(choice, "1-5 number") == choice:
                logger.debug("Checks the correctness of the selection")
                if choice == "1":
                    print("Choose the shape:\n"
                          "Square.....1\n"
                          "Rectangle..2\n"
                          "Circle.....3")
                    choice = choice_from_user("shape")
                    if valid_your_choice(choice, "1-3 number") == choice:
                        if choice == "1":
                            size = (choice_from_user("length of the side"))
                            if valid_your_choice(size, "size") == size:
                                manager.create_shape(1, side=float(size))

                        elif choice == "2":
                            width = (choice_from_user("width of the rectangle"))
                            if valid_your_choice(width, "size") == width:
                                height = (choice_from_user("height of the rectangle"))
                                if valid_your_choice(height, "size"):
                                    manager.create_shape(2, width=float(width), height=float(height))

                        elif choice == "3":
                            radius = (choice_from_user("length of the radius"))
                            if valid_your_choice(radius, "size") == radius:
                                manager.create_shape(3, radius=float(radius))

                elif choice == "2":
                    manager.get_all_shapes()

                elif choice == "3":
                    shape_id = choice_from_user("shape id")
                    if valid_your_choice(shape_id, "size") == shape_id:
                        found = manager.find_id(shape_id)
                        if found:
                            if found.shape_type == "rectangle":
                                width = choice_from_user("width")
                                if valid_your_choice(width, "size"):
                                    height = choice_from_user("height")
                                    if valid_your_choice(height, "size"):
                                        manager.update_shape(shape_id, width=float(width), height=float(height))
                            else:
                                value = choice_from_user("other value")
                                if valid_your_choice(value, "size"):
                                    values = "radius" if found.shape_type == "circle" else "side"
                                    manager.update_shape(shape_id, **{values: float(value)})
                        else:
                            print("Error: No shape found with this ID.")
                    else:
                        print("the shape id is not valid")


                elif choice == "4":
                    shape_id = choice_from_user("shape id")
                    if valid_your_choice(shape_id, "size") == shape_id:
                        found = manager.find_id(shape_id)
                        if found:
                            manager.delete_shape(int(shape_id))

                elif choice == "5":
                    print("exit from program")
                    program = False

        except ValueError as e:
            print(f"Error: {e} please try again!")


if __name__ == "__main__":
    main()
