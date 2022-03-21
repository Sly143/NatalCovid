# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

felipeCamarao = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 57628,					# Tamanho da população
	'tamFisico': 654.4,					# Área do bairro em Hectare
	'densidadeDemografica': 8806.23,		# Densidade demografica (Hab/km²)
	'numDomicilio': 14392,				# Numero de domicilios
	'domicilio': {'casa': 92.66, 'apartamento': 1.25, 'comodo': 0.08, 'casa de vila ou condominio': 6.01,  'outro': 0},
	'idade': [7534, 10769, 11758, 9397, 9131, 4384, 2525, 1324, 806],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [3.61, 10.85, 30.59, 35.15, 13.2, 2.04, 0.97, 0.32, 0.11, 3.11, 0.03], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 86.16, 'naoExiste': 13.84},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':9, 'estadual': 5, 'federal': 0,'particular': 8},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':3847, 'estadual': 2511, 'federal': 0,'particular': 2475},	# Número de escolas	# Média de Alunos por escolas
}
