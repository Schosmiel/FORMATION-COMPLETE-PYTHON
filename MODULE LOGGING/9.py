import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug("Debogage")
logging.info("Information")
logging.warning("Avertissement")
logging.error("Erreur grave")
logging.critical("Erreur critique")