##Este programa serve para calcular a média salarial nos últimos 3 meses trabalhados;
mes1=0;
mes2=0;
mes3=0;
Mediasal=0;
mes1=int(input("Digite o valor do primeiro salário:"));
mes2=int(input("Digite o valor do segundo salário:"));
mes3=int(input("Digite o valor do terceiro salário:"));
Mediasal=int((mes1+mes2+mes3)/3);
print("A Media Salarial é:%i"%Mediasal);
