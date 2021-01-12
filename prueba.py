import sys
import argparse
import os
import datetime
import schedule
import time


def job():
    print(3)

schedule.every(10).seconds.do(job)

if __name__ == "__main__":
    args = my_parser.parse_args()

    while args.es_programado:
            schedule.run_pending()
            time.sleep(1)
    
    print(args.es_programado, args.fecha_desde, args.fecha_hasta)