import struct
from pyModbusTCP.client import ModbusClient
import time
import os
import pandas as pd
def collect_data(slave_address:str, port:int, registerCode:int, unit_id:int, quant_reg:int, amostragem:int, delay:float) -> list:
    """
    Coleta dados da unidade remota usando o protocolo Modbus TCP.

    Args:
        slave_address (str): Endereço IP ou nome de host da unidade remota.
        port (int): Número da porta para conexão Modbus TCP.
        registerCode (int): Código para seleção de coleta de dados.
        unit_id (int): ID da unidade Modbus.
        amostragem (int): Número de amostras a serem coletadas (0-100), 0 para repetições sem limitação.
        delay (float): Tempo de atraso entre cada amostra em segundos.

    Returns:
        list: Uma lista contendo os registros de dados coletados.

    Exemplo de uso:
        import dranetzAPI as dranetz
        try:
            address = "192.168.0.30"
            port_number = 502
            device_id = 1
            sample_count = 2
            sample_delay = 0.1
            code = 40000
            quant_reg = 56

            collected_data = dranetz.collect_data(address, port_number, code, device_id, quant_reg, sample_count, sample_delay)
            decoded_values = pd.DataFrame(dranetz.decode_data(collected_data))

            print("Valores coletados:", collected_data)
            print("Valores decodificados:", decoded_values)
        except Exception as e:
            print(f"Erro: {e}")    
    """

    # if not (slave_address and port and registerCode and unit_id and quant_reg and amostragem and delay):
    #     raise Exception("Parametros invalidos")
        
    if not (0 <= port <= 65535):
        raise ValueError("Porta deve estar entre 0 e 65535")

    if not (registerCode >= 0):
        raise ValueError("O código de registro deve ser um inteiro positivo")

    if not (delay >= 0):
        raise ValueError("Deley deve ser um flutuante positivo, em segundos")

    if not (amostragem >= 0):
        raise ValueError("amostragem deve ser um inteiro positivo")
    
    data = []
    # Conectando ao servidor Modbus e definindo as configurações do dispositivo
    # Caso já tenha conexão não a fará novamente.
   
    modbus_client = ModbusClient(
        host=slave_address, port=port, unit_id=unit_id, auto_open=True
    )
    try:

        for _ in range(amostragem):
            regs = modbus_client.read_holding_registers(registerCode, quant_reg)
            if regs:
                data.append(regs)
            else:
                print("Dados vazios")
            time.sleep(delay)
            
    except Exception as e:
        print(f"Erro na coleta de dados: {e}")
    finally:
        modbus_client.close()
    return data


def collect_data_Loop(slave_address: str, port: int, unit_id: int, delay: float, registerCode: dict, quant_reg: int):
    """
    Coleta dados de dispositivos Modbus de forma contínua e exibe as informações no console.

    Esta função estabelece uma conexão Modbus com um dispositivo escravo, lê registros de
    acordo com os códigos de registro fornecidos e exibe os dados no console em um loop infinito.

    Args:
        slave_address (str): O endereço IP ou nome do host do dispositivo escravo Modbus.
        port (int): A porta TCP utilizada para a comunicação Modbus (geralmente 502).
        unit_id (int): O ID da unidade Modbus do dispositivo escravo (geralmente 1).
        delay (float): O intervalo de tempo (em segundos) entre cada leitura de dados.
        registerCode (dict): Um dicionário que mapeia títulos de registro para seus códigos de registro correspondentes.
                            Exemplo: {"Potência Aparente": 2038,"Potência Ativa": 2000,"Potência Fundamental Reativa": 2028}
        quant_reg (int): O número de registros a serem lidos em cada solicitação. número 2 para cada registro
            por exemplo:
                caso queria apenas um valor use o numero 2.and
                
                caso queira coletar mais valores seguidos, como por exemplo as potencias em nas 3 fazes, 
                utlize o código da primeira potencia, e no quant_reg utlize o número 6, isso é, 3 registros.

    Returns:
        None

    Note:
        Certifique-se de que a biblioteca ModbusClient estejam instaladas para o funcionamento adequado desta função.
            pip install pip install pyModbusTCP pandas
            

    Example:
        collect_data_Loop("192.168.1.1", 502, 1, 5.0, {"Potência Aparente": 2038}, 2)

    """
    data = []
    # conecta no servidor ModBus (Dranetz)
    modbus_client = ModbusClient(
        host=slave_address, port=port, unit_id=unit_id, auto_open=True
    )
    while True:
        resposta = ''
        for title, code in registerCode.items(): # coleta os dados a serem exibidos
            regs = modbus_client.read_holding_registers(code, quant_reg)
            if regs:
                data = []
                resposta += f"[{title}] {code}\n"
                data.append(regs)
                resposta += pd.DataFrame(decode_data(data)).to_string(index=False, header=False) + "\n\n"
        os.system('cls')  # Limpa a tela do console (funciona apenas no Windows)
        print(resposta)
        time.sleep(delay)
    modbus_client.close()


def decode_data(encoded_data: list) -> list:
    """
    Decodifica os valores brutos de dados em valores float.

    Args:
        data (list): Lista de registros de dados brutos.

    Returns:
        list: Lista de valores decodificados como floats.
    """
    decoded_data = []
    for data in encoded_data:
        decoded_values = []
        for i in range(0, len(data), 2):
            raw_data = data[i:i+2]
            combined_value = (raw_data[0] << 16) + raw_data[1]
            decoded_value = struct.unpack('f', struct.pack('I', combined_value))[0]
            decoded_values.append(decoded_value)
        decoded_data.append(decoded_values)
    return decoded_data