from API import DranetzAPI as dranetz
import pandas as pd
import os
try:
    
    address = "192.168.0.30"
    port_number = 502
    device_id = 1
    # sample_count = 1 fixa em 1 para visualização em tempo real
    sample_delay = 0
    # code = 2000 // é escolhida de acordo com qual registro pegar 
    quant_reg = 6
    
    

    resposta = ''
    potenciaAtiva = (address, port_number, 2038, device_id, quant_reg, 1, sample_delay)
    collected_data = dranetz.collect_data(*potenciaAtiva)
    decoded_values = pd.DataFrame(dranetz.decode_data(collected_data)).to_string(index=False, header=False)
    resposta = "[Potência Aparente]\n" + decoded_values + "\n\n"
    
    potenciaAtiva = (address, port_number, 2000, device_id, quant_reg, 1, sample_delay)
    collected_data = dranetz.collect_data(*potenciaAtiva)
    decoded_values = pd.DataFrame(dranetz.decode_data(collected_data)).to_string(index=False, header=False)
    resposta += "[Potência Ativa]\n" + decoded_values + "\n\n"
    
    potenciaAtiva = (address, port_number, 2028, device_id, quant_reg, 1, sample_delay)
    collected_data = dranetz.collect_data(*potenciaAtiva)
    decoded_values = pd.DataFrame(dranetz.decode_data(collected_data)).to_string(index=False, header=False)
    resposta += "[Potência Fundamental Reativa]\n" + decoded_values + "\n\n"
    os.system('cls')
    print(resposta)

    
except Exception as e:
    print(f"Erro: {e}")