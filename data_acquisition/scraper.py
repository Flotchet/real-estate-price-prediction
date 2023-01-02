import itertools 
import requests
import functools
import warnings
import os
import re

from multiprocessing import Process

import numpy as np
import pandas as pd

from requests import Session
from bs4 import BeautifulSoup