#!/usr/bin/env python

import argparse
import sys
import os
import yaml
import zipfile
#!/usr/bin/env python

import argparse
import sys
import os
import yaml
import zipfile

def db4pkg():
    with open("manifest.yml") as stream:
        try:
            db_manifest = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return db_manifest
