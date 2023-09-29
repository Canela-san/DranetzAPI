Para utilizar a API basta importala e chamar os métodos collect_data ou collect_data_Loop

Collect_data:
    - Recebe um dicionário com as seguintes informações
    {
        address = endereço IP do Dranetz (servidor modbus).
        port_number = Porta de do serviço Modbus no Dranetz, o padrão é (502).
        device_id = caso aja mais de uma conexão simultanea, atualmente pode ser apenas (1).
        sample_count = Quantas vezes a função será executada para a caleta.
        sample_delay = O tempo de espera entre cada coleta.
        code = A posição na memória do dranetz para coleta, veja o arquivo de documentação para se informar dos códigos.
        quant_reg = quantidade de posições na memória do Dranetz que será coletada, obrigatório ser um número par, pois cada registro ocupa 2 posições de memória.
    }
    collect_data_loop:
    {
        address = endereço IP do Dranetz (servidor modbus).
        port_number = Porta de do serviço Modbus no Dranetz, o padrão é (502).
        device_id = caso aja mais de uma conexão simultanea, atualmente pode ser apenas (1).
        sample_delay = O tempo de espera entre cada coleta.
        code = é um dicionário que tem as informações de título para exibição e código que representa a posição na memória do dranetz para coleta, veja o arquivo de documentação para se informar dos códigos.
        quant_reg = quantidade de posições na memória do Dranetz que será coletada, obrigatório ser um número par, pois cada registro ocupa 2 posições de memória.
    }