
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

neopolis = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'sul',				# Zona ao qual o bairro pertence
	'tamPop': 22994,					# Tamanho da população
	'tamFisico': 322.1,				# Área do bairro em Hectare
	'densidadeDemografica': 71.38,		# Densidade demografica (Hab/km²)
	'numDomicilio': 6763,				# Numero de domicilios
	'domicilio': {'casa': 75.19, 'apartamento': 20.83, 'comodo': 0.49, 'casa de vila ou condominio': 3.49,  'outro': 0},
	'idade': [1618, 2039, 5292, 3089, 2790, 3638, 2775, 982, 772],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.41, 1.2, 7.01, 20.66, 28.94, 16.12, 14.39, 7.87, 1.51, 1.91, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 6.96, 'naoExiste': 93.04},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':6, 'estadual': 5, 'federal': 0,'particular': 6},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1260, 'estadual': 2496, 'federal': 0,'particular': 1208},	# Número de escolas	# Média de Alunos por escolas
}
