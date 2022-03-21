# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

dixSeptoRosado = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'oeste',					# Zona ao qual o bairro pertence
	'tamPop': 15494,					# Tamanho da população
	'tamFisico': 109.64,					# Área do bairro em Hectare
	'densidadeDemografica': 14131.7,		# Densidade demografica (Hab/km²)
	'numDomicilio': 4605,				# Numero de domicilios
	'domicilio': {'casa': 77.05, 'apartamento': 7.51, 'comodo': 0.09, 'casa de vila ou condominio': 15.35,  'outro': 0},
	'idade': [1614, 2208, 3077, 2360, 2668, 1525, 1173, 543, 324],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [1.35, 6.19, 22.11, 36.09, 21.98, 5.21, 3.15, 1.04, 0.15, 2.74, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 74.5, 'naoExiste': 25.5},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':3, 'estadual': 5, 'federal': 0,'particular': 2},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':775, 'estadual': 3463, 'federal': 0,'particular': 187},	# Número de escolas	# Média de Alunos por escolas
}
