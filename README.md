# DranetzAPI

A DranetzAPI é uma API desenvolvida em Python para a transferência de dados utilizando o protocolo ModBus. Esta API é projetada para facilitar a comunicação com o Analisador de Qualidade de Energia Dranetz.

## Uso da API

Para utilizar a API, basta importá-la e chamar os métodos `collect_data` ou `collect_data_loop`.

### `collect_data`

- **address**: Endereço IP do Dranetz (servidor ModBus).
- **port_number**: Porta do serviço ModBus no Dranetz. O padrão é **502**.
- **device_id**: Identificador do dispositivo. Caso haja mais de uma conexão simultânea, atualmente é permitido apenas o valor **1**.
- **sample_count**: Número de vezes que a função será executada para a coleta de dados.
- **sample_delay**: Tempo de espera entre cada coleta.
- **code**: Posição na memória do Dranetz para a coleta. Consulte o arquivo de documentação para obter informações sobre os códigos.
- **quant_reg**: Quantidade de posições na memória do Dranetz que serão coletadas. É obrigatório que seja um número par, pois cada registro ocupa 2 posições de memória.

### `collect_data_loop`

- **address**: Endereço IP do Dranetz (servidor ModBus).
- **port_number**: Porta do serviço ModBus no Dranetz. O padrão é **502**.
- **device_id**: Identificador do dispositivo. Caso haja mais de uma conexão simultânea, atualmente é permitido apenas o valor **1**.
- **sample_delay**: Tempo de espera entre cada coleta.
- **code**: Um dicionário contendo informações de título para exibição e o código que representa a posição na memória do Dranetz para coleta. Consulte o arquivo de documentação para obter informações sobre os códigos.
- **quant_reg**: Quantidade de posições na memória do Dranetz que serão coletadas. É obrigatório que seja um número par, pois cada registro ocupa 2 posições de memória.

Para mais informações e exemplos de uso, consulte a documentação completa.