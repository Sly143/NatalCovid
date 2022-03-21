
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

pontaNegra = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'sul',				# Zona ao qual o bairro pertence
	'tamPop': 25262,					# Tamanho da população
	'tamFisico': 1382.0,				# Área do bairro em Hectare
	'densidadeDemografica': 18.28,		# Densidade demografica (Hab/km²)
	'numDomicilio': 7928,				# Numero de domicilios
	'domicilio': {'casa': 56.8, 'apartamento': 20.83, 'comodo': 0.49, 'casa de vila ou condominio': 3.49,  'outro': 0},
	'idade': [2300, 2660, 5709, 3933, 3518, 3454, 2227, 1007, 453],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.53, 3.36, 10.33, 18.1, 20.56, 11.79, 14, 13.05, 5.9, 2.37, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 6.25, 'naoExiste': 93.75},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':4, 'estadual': 2, 'federal': 0,'particular': 6},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1191, 'estadual': 1688,'federal': 0, 'particular': 709},	# Número de escolas	# Média de Alunos por escolas
}
