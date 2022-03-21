
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

candelaria = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'sul',				# Zona ao qual o bairro pertence
	'tamPop': 25302,					# Tamanho da população
	'tamFisico': 761.4,				# Área do bairro em Hectare
	'densidadeDemografica': 33.23,		# Densidade demografica (Hab/km²)
	'numDomicilio': 6871,				# Numero de domicilios
	'domicilio': {'casa': 52.8, 'apartamento': 40.07, 'comodo': 0.04, 'casa de vila ou condominio': 7.09,  'outro': 0},
	'idade': [1641, 2182, 5716, 3699, 3297, 3640, 3146, 1193, 786],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.23, 0.68, 3.57, 10.61, 17.93, 14, 20.46, 19.43, 9.33, 3.73, 0.03], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 2.66, 'naoExiste': 97.34},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':1, 'estadual': 3, 'federal':0,'particular': 3},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':92, 'estadual': 1298, 'federal': 0, 'particular': 1399},	# Número de escolas	# Média de Alunos por escolas
}
