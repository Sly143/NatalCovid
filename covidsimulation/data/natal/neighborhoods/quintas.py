# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

quintas = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 24754,					# Tamanho da população
	'tamFisico': 248.54,					# Área do bairro em Hectare
	'densidadeDemografica': 9959.77,		# Densidade demografica (Hab/km²)
	'numDomicilio': 7929,				# Numero de domicilios
	'domicilio': {'casa': 86.22, 'apartamento': 0.92, 'comodo': 0.29, 'casa de vila ou condominio': 12.57,  'outro': 0},
	'idade': [2671, 3879, 4465, 3450, 4069, 2594, 1905, 1004, 718],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [1.82, 7.79, 22.54, 35.07, 21.71, 4.22, 2.41, 0.64, 0.1, 3.61, 0.09], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 34.94, 'naoExiste': 65.06},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':7, 'estadual': 4, 'federal': 0,'particular': 7},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1905, 'estadual': 976, 'federal': 0,'particular': 980},	# Número de escolas	# Média de Alunos por escolas
}
