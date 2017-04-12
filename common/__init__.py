import logging
logging.basicConfig(format='%(asctime)s %(name)s:%(levelname)s:%(message)s')
root = logging.getLogger()
root.setLevel(logging.INFO)
logging.getLogger(__name__).debug("hello logger")
