# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

barroVermelho = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 11399,					# Tamanho da população
	'tamFisico': 94.79,					# Área do bairro em Hectare
	'densidadeDemografica': 118.97,		# Densidade demografica (Hab/km²)
	'numDomicilio': 2883,				# Numero de domicilios
	'domicilio': {'casa': 49.81, 'apartamento': 47.87, 'comodo': 0, 'casa de vila ou condominio': 2.3,  'outro': 0},
	'idade': [737, 1054, 2367, 1782, 2028, 1540, 905, 546, 437],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.24, 0.83, 3.64, 10.54, 16.72, 12.94, 20.67, 22.89, 9.4, 2.08, 0.03], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 0.07, 'naoExiste': 99.93},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':1, 'estadual': 2, 'federal': 0,'particular': 4},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':141, 'estadual': 645, 'federal': 0,'particular': 1484},	# Número de escolas	# Média de Alunos por escolas
}
