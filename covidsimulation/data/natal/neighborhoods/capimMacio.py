
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

capimMacio = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'sul',				# Zona ao qual o bairro pertence
	'tamPop': 24100,					# Tamanho da população
	'tamFisico': 433.4,				# Área do bairro em Hectare
	'densidadeDemografica': 55.61,		# Densidade demografica (Hab/km²)
	'numDomicilio': 7360,				# Numero de domicilios
	'domicilio': {'casa': 44.52, 'apartamento': 49.31, 'comodo': 0.16, 'casa de vila ou condominio': 6.01,  'outro': 0},
	'idade': [1217, 1623, 5940, 2940, 2628, 4669, 3279, 1099, 705],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.1, 0.26, 1.82, 7.17, 17.49, 14.63, 23.02, 22.92, 10.37, 2.2, 0.03], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 0.68, 'naoExiste': 99.32},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':1, 'estadual': 1,'federal': 0, 'particular': 10},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':95, 'estadual': 763, 'federal': 0,'particular': 4947},	# Número de escolas	# Média de Alunos por escolas
}
