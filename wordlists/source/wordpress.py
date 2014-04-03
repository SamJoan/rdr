import sys
sys.path.append("../../")

from bs4 import BeautifulSoup
from lib.util import out, err
import re
import requests

try:
    total_nb = int(sys.argv[1])
except IndexError:
    err("Usage: %s total_nb" % sys.argv[0])
    sys.exit()

if total_nb % 100 != 0:
    err("total_nb needs to be a multiple of 100")
    sys.exit()

