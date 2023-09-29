# DranetzAPI
é uma API para acessar os dados do dranetz utilizando o protocolo ModBus da linguagem python

Para utilizar a API basta importala e chamar os métodos collect_data ou collect_data_Loop
<div>
<t2>Collect_data:</t2>    
        <ul>
        <li>address = endereço IP do Dranetz (servidor modbus).</li>
        <li>port_number = Porta de do serviço Modbus no Dranetz, o padrão é (502).</li>
        <li>device_id = caso aja mais de uma conexão simultanea, atualmente pode ser apenas (1).</li>
        <li>sample_count = Quantas vezes a função será executada para a caleta.</li>
        <li>sample_delay = O tempo de espera entre cada coleta.</li>
        <li>code = A posição na memória do dranetz para coleta, veja o arquivo de documentação para se informar dos códigos.</li>
        <li>quant_reg = quantidade de posições na memória do Dranetz que será coletada, obrigatório ser um número par, pois cada registro ocupa 2 posições de memória.</li>
        </ul>
</div>
<div>
<t2>collect_data_loop:</t2>
        <ul>
        <li>address = endereço IP do Dranetz (servidor modbus).</li>
        <li>port_number = Porta de do serviço Modbus no Dranetz, o padrão é (502).</li>
        <li>device_id = caso aja mais de uma conexão simultanea, atualmente pode ser apenas (1).</li>
        <li>sample_delay = O tempo de espera entre cada coleta.</li>
        <li>code = é um dicionário que tem as informações de título para exibição e código que representa a posição na memória do dranetz para coleta, veja o arquivo de documentação para se informar dos códigos.
        <li>quant_reg = quantidade de posições na memória do Dranetz que será coletada, obrigatório ser um número par, pois cada registro ocupa 2 posições de memória.</li>
        </ul>
</div>
