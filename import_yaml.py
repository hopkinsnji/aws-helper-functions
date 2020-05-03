def _load_yaml(file_path):
    '''
    Loads a .yml file from provided path.
    '''
    if not os.path.isfile(file_path):
        os.system('pwd')
        raise FileNotFoundError(f"File {file_path} does not exist")

    try:
        with open(file_path) as f:
            contents = yaml.safe_load(f)
        return contents
    except yaml.YAMLError as e:
        raise ValidationError("file format error")