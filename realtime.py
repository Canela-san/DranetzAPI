from API import DranetzAPI as dranetz
import pandas as pd
import os
import time
# Exemplo de uso:
try:
    address = "192.168.0.30"
    port_number = 502
    device_id = 1
    sample_delay = 0.5 # update dalay time
    code = {"Potência Aparente": 2038,"Potência Ativa": 2000,"Potência Fundamental Reativa": 2028}
    quant_reg = 6 

    # print realizado dentro da própria função.
    dranetz.collect_data_Loop(address, port_number, device_id, sample_delay, code, quant_reg)

except Exception as e:
    print(f"Erro: {e}")
