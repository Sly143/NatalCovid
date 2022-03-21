# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

alecrim = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 25957,					# Tamanho da população
	'tamFisico': 344.73,					# Área do bairro em Hectare
	'densidadeDemografica': 76.03,		# Densidade demografica (Hab/km²)
	'numDomicilio': 8646,				# Numero de domicilios
	'domicilio': {'casa': 77.4, 'apartamento': 7.01, 'comodo': 0.51, 'casa de vila ou condominio': 15.1,  'outro': 0},
	'idade': [2028, 2941, 5433, 3710, 4161, 3409, 2004, 1205, 1067],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.51, 3.84, 15.63, 31.7, 27.52, 9.36, 5.68, 2.52, 0.68, 2.39, 0.17], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 36.8, 'naoExiste': 63.2},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':7, 'estadual': 9, 'federal': 0,'particular': 11},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1877, 'estadual': 4190, 'federal': 0,'particular': 6198},	# Número de escolas	# Média de Alunos por escolas
}
