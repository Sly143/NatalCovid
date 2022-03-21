
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

nSenhoraApresentacao = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'norte',					# Zona ao qual o bairro pertence
	'tamPop': 103110,					# Tamanho da população
	'tamFisico': 1024.8,				# Área do bairro em Hectare
	'densidadeDemografica': 100.62,		# Densidade demografica (Hab/km²)
	'numDomicilio': 22723,				# Numero de domicilios
	'domicilio': {'casa': 95.79, 'apartamento': 0.11, 'comodo':0.02, 'casa de vila ou condominio': 4.08,  'outro': 0},
	'idade': [13710, 19427, 19864, 15425, 18164, 8860, 4663, 1849, 1150],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [3.81, 10.56, 28.46, 33.72, 16.5, 2.68, 1.22, 0.32, 0.68, 2.39, 0.17], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 47.87, 'naoExiste': 52.13},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',			# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',				# Numero de leitos dos hospitais
	'uti': 'vazio',					# Número de UTIS do bairro
	'doencasCronicas': 'vazio',		# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':10, 'estadual': 1, 'particular': 14},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal': 7122, 'estadual': 1387, 'particular': 3168},	# Número de escolas	# Média de Alunos por escolas
}
