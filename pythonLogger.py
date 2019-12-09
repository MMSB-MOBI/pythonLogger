import logging
import coloredlogs


def init_logger(name, level = "classic"):
    level_dic = { "classic" : logging.INFO, "debug" : logging.DEBUG
    }   

    if level not in ["classic", "debug"]:
        raise Exception('pythonLogger init_looger() : level is not classic or debug')

    logger = logging.getLogger(name)

    coloredlogs.install(level='DEBUG', logger = logger, fmt ='%(levelname)s : %(message)s')

    logger.setLevel(logging.DEBUG)

    #ch = logging.StreamHandler()
    #ch.setLevel(level_dic[level])

    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #formatter = logging.Formatter('%(levelname)s : %(message)s')

    #ch.setFormatter(formatter)

    #logger.addHandler(ch)

    return logger