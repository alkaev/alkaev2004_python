import typing as tp


def convert_to_common_type(data: list[tp.Any]) -> tp.Any:
    """
    Takes list of multiple types' elements and convert each elements to common type according to given rules
    :param data: list of multiple types' elements
    :return: list with elements converted to common type
    """

    array_of_answer: list[tp.Any] = []
    first_type: tp.Any = None
    this_is_list: bool = False

    for elements in data:
        element_type: tp.Any = type(elements)

        if element_type == bool:
            first_type = bool
        elif element_type == float:
            first_type = float
        elif element_type == int and not first_type:
            first_type = int
        elif element_type == str and elements != '' and not first_type:
            first_type = str

        if element_type in (tuple, list):
            this_is_list = True
            for element in elements:
                elem_type: tp.Any = type(element)
                if elem_type == bool and not first_type:
                    first_type = bool
                elif elem_type == int and not first_type:
                    first_type = int
                elif elem_type == str and not first_type:
                    first_type = str
                elif elem_type == float and not first_type:
                    first_type = float

    if this_is_list:
        if first_type == bool:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append([])
                elif isinstance(element, (list, tuple)):
                    array_of_answer.append(list(element))
                else:
                    array_of_answer.append([element])
        elif first_type == float:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append([0.0])
                else:
                    array_of_answer.append(list(element))
        elif first_type == int:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append([])
                elif isinstance(element, (list, tuple)):
                    array_of_answer.append(list(element))
                else:
                    array_of_answer.append(list([int(element)]))
        elif first_type == str:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append([])
                elif isinstance(element, (list, tuple)):
                    array_of_answer.append(list(element))
                else:
                    array_of_answer.append(list([str(element)]))
    else:
        if first_type == bool:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append(bool(element))
                else:
                    array_of_answer.append(bool(element))
        elif first_type == float:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append(0.0)
                else:
                    array_of_answer.append(float(element))
        elif first_type == int:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append(0)
                else:
                    array_of_answer.append(int(element))
        elif first_type == str:
            for element in data:
                if element == '' or element is None:
                    array_of_answer.append("")
                else:
                    array_of_answer.append(str(element))
        else:
            for i in range(len(data)):
                array_of_answer.append("")

    return array_of_answer
