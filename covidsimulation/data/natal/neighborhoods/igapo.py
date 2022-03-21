
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

igapo = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'norte',					# Zona ao qual o bairro pertence
	'tamPop': 30516,					# Tamanho da população
	'tamFisico': 220.2,					# Área do bairro em Hectare
	'densidadeDemografica': 138.61,		# Densidade demografica (Hab/Ha)
	'numDomicilio': 8500,				# Numero de domicilios
	'domicilio': {'casa': 82.52, 'apartamento': 0.58, 'comodo':0, 'casa de vila ou condominio': 16.91,  'outro': 0},
	'idade': [3445, 4765, 6384, 4717, 5047, 3048, 1751, 777, 580],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [1.82, 7.18, 23.81, 37.38, 20.61, 3.79, 2.08, 0.48, 0.08, 2.76, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 45.38, 'naoExiste': 54.62},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',			# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',				# Numero de leitos dos hospitais
	'uti': 'vazio',					# Número de UTIS do bairro
	'doencasCronicas': 'vazio',		# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':7, 'estadual': 1, 'particular': 6},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':3477, 'estadual': 195, 'particular': 2762},	# Número de escolas	# Média de Alunos por escolas
}
