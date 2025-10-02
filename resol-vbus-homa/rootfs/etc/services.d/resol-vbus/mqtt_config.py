"""Module providing the MQTT configuration for the service."""

import os
import sys
import bashio_logging  # provides logging output like bashio, must be imported before logging #pylint: disable=unused-import
import logging  # pylint: disable=wrong-import-order

host = os.getenv('MQTT_HOST', "")
port = int(os.getenv("MQTT_PORT", "1883"))
user = os.getenv("MQTT_USER")
pwd = os.getenv("MQTT_PASSWORD")
ca_certs = os.getenv("MQTT_CA_CERTS")  # not used with port 1883

if host == "":
    logging.error("No MQTT broker configured. Exiting.")
    sys.exit(1)
