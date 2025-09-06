def load_config(path='config.txt'):
    config = {}
    with open(path, 'r') as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            key, value = line.strip().split('=', 1)
            config[key] = value
    return config

config = load_config()
