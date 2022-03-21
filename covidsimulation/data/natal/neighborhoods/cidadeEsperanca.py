# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

cidadeEsperanca = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 18362,					# Tamanho da população
	'tamFisico': 182.87,					# Área do bairro em Hectare
	'densidadeDemografica': 10041.01,		# Densidade demografica (Hab/km²)
	'numDomicilio': 5346,				# Numero de domicilios
	'domicilio': {'casa': 90.14, 'apartamento': 4.58, 'comodo': 0.24, 'casa de vila ou condominio': 5.03,  'outro': 0},
	'idade': [1612, 2422, 3102, 2529, 3839, 1892, 1458, 883, 625],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.95, 3.91, 15.9, 31.48, 26.75, 8.81, 5.05, 3.57, 1.66, 1.91, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 9.43, 'naoExiste': 90.57},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':4, 'estadual': 4, 'federal': 0,'particular': 5},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':1858, 'estadual': 1256, 'federal': 0,'particular': 1736},	# Número de escolas	# Média de Alunos por escolas
}
