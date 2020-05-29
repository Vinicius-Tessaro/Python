con_t = float (input ('Digite o valor do consumo total(em KWh): '))
qnt_f = int (input ('Digite a quantidade de fases do motor: '))
con_r = float

if qnt_f == 1:
    con_r = con_t-30

elif qnt_f == 2:
    con_r = con_t-50

else:
    con_r = con_t-100

con_rd = float (con_r/30)
hrs_sp = float (input ('digite Horas sol pico: '))
pps = con_rd/hrs_sp
wpp = float (input('Insira WPpainel: '))
np = float (pps/wpp)
temp_a = float (input('Digite a temperatura ambiente(em:°C) '))
temp_sm = float (temp_a+30)
c_temp = float (input('Digite o valor do coeficiente de temperatura: '))
pmm = float (con_t*(1+c_temp/100)*(temp_sm-temp_a))




print ('\n\nConsumo do cliente:\n Consumo total: {}KWh\n Tipo de ligação: {} fases\n **Consumo Real: {}KWp**\n **Consumo Real diário:{}KWp**\n\n'.format(con_t,qnt_f,con_r,con_rd))
print ('Potência do sistema:\n Horas Sol pico: {}h/d\n **Potência de pico do sistema: {}KWp**\n\n'.format(hrs_sp,pps))
print ('Dados dos paineis:\n WPpainel: {}KWp\n **Número de painéis: {} painéis**\n\n'.format(wpp,np))
print ('Temperatura nos módulos:\n Temperatura Ambiente: {}°C)\n **Temperatura na superfície do módulo {}°C**\n\n'.format(temp_a,temp_sm))
print ('Potência-Pico nos módulos: \n Coeficiente de temperatura: {}\n **Potência máxima nos módulos: {}KWp**\n\n'.format(c_temp,pmm))
print ('@Nota: Os valores que possuem **...** indicam que foi gerado pelo programa@\nDeveloped by V1nicius Tessaro\nFor Gustavo Shawn')

input()
