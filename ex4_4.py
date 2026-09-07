#!/usr/bin/env python3

from abc import ABC, abstractmethod
import pandas as pd
import os
import errno
from jsonschema import validate, ValidationError
from pandas_schema import Column, Schema
from pandas_schema.validation import DateFormatValidation, InRangeValidation, LeadingWhitespaceValidation
import json

class PowerSystemDataSource(ABC):
    """Provides access to power system data from varying sources."""

    @abstractmethod
    def read_measurements(self) -> pd.DataFrame:
        """Read raw measurements and return a normalized DataFrame."""
        pass


class ScadaCsvAdapter(PowerSystemDataSource):
    """Ingest and process CSV files from SCADA systems."""

    def __init__(self, file_path: str):
        if os.path.isfile(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)

        self._csv_schema = Schema([
            Column('timestamp', [
                DateFormatValidation('%Y-%m-%dT%H:%M'),
                LeadingWhitespaceValidation()
            ]),
            Column('bus_id', [InRangeValidation(1, 999)]),
            Column('voltage_pu', [InRangeValidation(0.9, 1.1)]),
            Column('power_mw', [InRangeValidation(-1000, 1000)])
        ])

    @property
    def csv_schema(self) -> Schema:
        return self._csv_schema

    def read_measurements(self) -> pd.DataFrame:
        incoming = pd.read_csv(self.file_path)
        errors = self.csv_schema.validate(incoming)

        if len(errors) != 0:
            for error in errors:
                print(error)
            raise ValueError("Validation errors encountered in incoming data")

        return incoming

class Iec61850JsonAdapter(PowerSystemDataSource):
    """Ingest and process JSON data from IEC 61850 sources."""

    def __init__(self, file_path: str):
        if os.path.isfile(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)

        self._json_schema = {
            "type": "object",
            "properties": {
                "measurements": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "timestamp": {"type": "string", "format": "date-time"},
                            "busId": {"type": "integer"},
                            "voltage": {"type": "number"},
                            "power": {"type": "number"}
                        },
                        "required": ["timestamp", "busId", "voltage", "power"]
                    }
                }
            },
            "required": ["measurements"]
        }

    @property
    def json_schema(self) -> object:
        return self._json_schema

    def read_measurements(self) -> pd.DataFrame:
        with open(self.file_path, "r") as file:
            incoming = json.load(file)

            try:
                validate(instance=incoming, schema=self.json_schema)
            except ValidationError as e:
                print(e)
                raise ValueError("Validation errors encountered in incoming data")
            
            df = pd.DataFrame(incoming["measurements"])
            df.rename(columns={
                "busId": "bus_id", 
                "voltage": "voltage_pu", 
                "power": "power_mw"
            }, inplace=True)
            return df

def ingest_data(source: PowerSystemDataSource) -> pd.DataFrame:
    df: pd.DataFrame = source.read_measurements()

    return df

if __name__ == "__main__":

    scada = ScadaCsvAdapter("./scada_incoming.csv")
    df_scada = scada.read_measurements()
    print("Incoming SCADA data converted to normalized dataframe:")
    print(df_scada.to_string())

    iec61850 = Iec61850JsonAdapter("./iec61850_incoming.json")
    df_iec61850 = iec61850.read_measurements()
    print("Incoming Iec61850 data converted to normalized dataframe:")
    print(df_iec61850.to_string())
