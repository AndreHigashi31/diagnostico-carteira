import time

conservador = [62.5, 0.0, 20.0, 10.0, 5.0, 0.0, 0.0, 2.5, 0.0]
moderado = [42.5, 0.0, 20.0, 15.0, 15.0, 2.5, 0.0, 5.0, 0.0]
sofisticado = [25.0, 0.0, 15.0, 15.0, 25.0, 10.0, 5.0, 5.0, 0.0]

print('=' * 100)
print(' ' * 40 + 'Seja Bem Vindo')
print(' ' * 35 + 'DIAGNÓSTICO DE CARTEIRA')
print('=' * 100)

print('Primeiro vamos definir seu perfil de investimentos!')
print('\n [1] - Conservador'
      '\n [2] - Moderado'
      '\n [3] - Sofisticado')
perfil = int(input('\nQual perfil você se identifica: '))

print('=' * 100)

print('Agora vamos mapear seus investimentos:')
print('Orientações:'
      '\nCaso você não tenha aplicação em alguma classe de ativo, preencha com "0"'
      '\nSe você tiver em Fundo de Investimento em Renda Fixa, ele será computado como Renda Fixa  + seu Indexador')
print('=' * 100)

rfpos = float(input('Valor aplicado em Renda Fixa Pós Fixada: R$ '))
rfpre = float(input('Valor aplicado em Renda Fixa Prefixado: R$ '))
rfinf = float(input('Valor aplicado em Renda Fixa Inflação: R$ '))
mult = float(input('Valor aplicado em Fundos Multimercado: R$ '))
rvbr = float(input('Valor aplicado em Ações BR: R$ '))
rvint = float(input('Valor aplicado em ativos Internacionais: R$ '))
alt = float(input('Valor aplicado em ativos alternativos: R$ '))
fiis = float(input('Valor aplicado em Fundos Imobiliários: R$ '))
coes = float(input('Valor aplicado em Certificado de Operação Estruturada (COE): R$ '))

total = rfinf + rfpre + rfpos + mult + rvbr + rvint + alt + fiis + coes
rendaFixa = (rfpos + rfpre + rfinf) / total * 100
rendaVariavel = (mult + rvbr + rvint + alt + fiis + coes) / total * 100
percRFpos = rfpos / total * 100
perRFpre = rfpre / total * 100
percRFinf = rfinf / total * 100
percMult = mult / total * 100
percRvBr = rvbr / total * 100
percRvInt = rvint / total * 100
percAlt = alt / total * 100
percFii = fiis / total * 100
percCoes = coes / total * 100

print('=' * 100)
print('Aguarde um momento...')
print('=' * 100)
time.sleep(3)
print(f'\nVocê tem R$ {total :.2f} investido')
print('Sua carteira está dividida em:'
      f'\n {rendaFixa :.1f} % em ativos de Renda Fixa'
      f'\n {rendaVariavel :.1f} % em ativos que possuem mais volatilidade')
print('=' * 100)
time.sleep(3)
print('A distribuição da sua carteira de investimente está da seguinte forma:')
print(f'\n{percRFpos :.1f} % em Renda Fixa Pós Fixado')
print(f'\n{perRFpre :.1f} % em Renda Fixa Prefixado')
print(f'\n{percRFinf :.1f} % em Renda Fixa Inflação')
print(f'\n{percMult :.1f} % em Fundos Multimercado')
print(f'\n{percRvBr :.1f} % em Ações')
print(f'\n{percRvInt :.1f} % em ativos Internacionais')
print(f'\n{percAlt :.1f} % em ativos Alternativos')
print(f'\n{percFii :.1f} % em Fundos Imobiliários')
print(f'\n{percCoes :.1f} % em Certificado de Operação Estruturada (COE)')
print('=' * 100)
time.sleep(5)
print('Para o seu perfil de investidor, o recomendado seria ter uma carteira diversificada da seguinte forma:')
time.sleep(1)
if perfil == 1:
    print(f'\n{conservador[0]} % em Renda Fixa Pós Fixado')
    print(f'\n{conservador[1]} % em Renda Fixa Prefixado')
    print(f'\n{conservador[2]} % em Renda Fixa Inflação')
    print(f'\n{conservador[3]} % em Fundos Multimercado')
    print(f'\n{conservador[4]} % em Ações')
    print(f'\n{conservador[5]} % em ativos Internacionais')
    print(f'\n{conservador[6]} % em ativos Alternativos')
    print(f'\n{conservador[7]} % em Fundos Imobiliários')
    print(f'\n{conservador[8]} % em Certificado de Operação Estruturada (COE)')

elif perfil == 2:
    print(f'\n{moderado[0]} % em Renda Fixa Pós Fixado')
    print(f'\n{moderado[1]} % em Renda Fixa Prefixado')
    print(f'\n{moderado[2]} % em Renda Fixa Inflação')
    print(f'\n{moderado[3]} % em Fundos Multimercado')
    print(f'\n{moderado[4]} % em Ações')
    print(f'\n{moderado[5]} % em ativos Internacionais')
    print(f'\n{moderado[6]} % em ativos Alternativos')
    print(f'\n{moderado[7]} % em Fundos Imobiliários')
    print(f'\n{moderado[8]} % em Certificado de Operação Estruturada (COE)')

else:
    print(f'\n{sofisticado[0]} % em Renda Fixa Pós Fixado')
    print(f'\n{sofisticado[1]} % em Renda Fixa Prefixado')
    print(f'\n{sofisticado[2]} % em Renda Fixa Inflação')
    print(f'\n{sofisticado[3]} % em Fundos Multimercado')
    print(f'\n{sofisticado[4]} % em Ações')
    print(f'\n{sofisticado[5]} % em ativos Internacionais')
    print(f'\n{sofisticado[6]} % em ativos Alternativos')
    print(f'\n{sofisticado[7]} % em Fundos Imobiliários')
    print(f'\n{sofisticado[8]} % em Certificado de Operação Estruturada (COE)')