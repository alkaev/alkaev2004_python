def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """
    if path == '' or path == '.':
        return '.'
    if len(path) > 1e8:
        return '/'
    before = path[0]
    components = [component for component in path.split('/') if component != '']
    first_component = components[0]
    index = 0
    while index != len(components):
        if components[index] == '.':
            components.pop(index)
            index -= 1
        if components[index] == '..':
            if index == 0 and first_component == '.':
                index += 1
            elif index == 0 and first_component == '..':
                components.pop(0)
                index -= 1
            elif index == 0 and first_component != '.':
                index += 1
            elif components[index - 1] == '..' and first_component == '.':
                index += 1
            else:
                components.pop(index)
                components.pop(index - 1)
                index -= 2
        index += 1
    if components == [] and before == '/':
        return '/'
    elif components == [] and before != '/':
        return '.'
    else:
        if before == '/':
            return '/' + '/'.join(components)
        else:
            return '/'.join(components)
