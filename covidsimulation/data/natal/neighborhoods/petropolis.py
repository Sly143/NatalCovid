# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

petropolis = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 5846,					# Tamanho da população
	'tamFisico': 78.43,					# Área do bairro em Hectare
	'densidadeDemografica': 74.16,		# Densidade demografica (Hab/km²)
	'numDomicilio': 1930,				# Numero de domicilios
	'domicilio': {'casa': 25.85, 'apartamento': 61.81, 'comodo': 0.1, 'casa de vila ou condominio': 2,  'outro': 10.21},
	'idade': [366, 403, 1005, 815, 900, 810, 747, 411, 389],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0, 0.75, 2.71, 6.81, 9.06, 8.77, 16.39, 30.24, 23.2, 2.02, 0.06], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 21.13, 'naoExiste': 78.87},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':1, 'estadual': 6, 'federal': 0,'particular': 3},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':666, 'estadual': 5522, 'federal': 0,'particular': 1015},	# Número de escolas	# Média de Alunos por escolas
}
