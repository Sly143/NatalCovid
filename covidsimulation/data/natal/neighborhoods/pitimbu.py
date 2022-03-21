
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

pitimbu = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'sul',				# Zona ao qual o bairro pertence
	'tamPop': 25635,					# Tamanho da população
	'tamFisico': 744.6,				# Área do bairro em Hectare
	'densidadeDemografica': 34.43,		# Densidade demografica (Hab/km²)
	'numDomicilio': 7077,				# Numero de domicilios
	'domicilio': {'casa': 84.22, 'apartamento': 14.48, 'comodo': 0.08, 'casa de vila ou condominio': 1.22,  'outro': 0},
	'idade': [1533, 1892, 6611, 3214, 3203, 4952, 2250, 1301, 681],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.08, 0.69, 4.3, 15.3, 29.86, 18.84, 18.24, 9.61, 1.88, 1.2, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 0.88, 'naoExiste': 99.12},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':5, 'estadual': 4, 'federal': 0,'particular': 11},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1858, 'estadual': 2017,'federal': 0, 'particular': 2475},	# Número de escolas	# Média de Alunos por escolas
}
