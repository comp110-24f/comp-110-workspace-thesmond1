"""This program calculates the numbers needed to plan a cozy tea party."""

# doc strings can be too long and cause a problem

__author__: str = "730700749"


def main_planner(guests: int) -> None:
    """Printed recipt."""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


# f string: prefix with f before open quotes, curly brackets


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags."""
    return people * 2  # 2 tea bags per person


# to multiply use the * symbol
# print(tea_bags(people=2))


def treats(people: int) -> int:
    """Calculate the number of treats."""
    return int(tea_bags(people=people) * 1.5)


# use tea_bags to get the number of tea bags then multiply by 1.5 for treats
# print(treats(people=2))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of tea and treats."""
    return tea_count * 0.5 + treat_count * 0.75


# print(cost(tea_count=2, treat_count=6))

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
