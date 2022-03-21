# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

tirol = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 17099,					# Tamanho da população
	'tamFisico': 360.04,					# Área do bairro em Hectare
	'densidadeDemografica': 47.25,		# Densidade demografica (Hab/km²)
	'numDomicilio': 5236,				# Numero de domicilios
	'domicilio': {'casa': 28.71, 'apartamento': 67.67, 'comodo': 0.11, 'casa de vila ou condominio': 3.5,  'outro': 0.02},
	'idade': [1089, 1716, 2793, 2420, 2880, 2570, 1657, 998, 997],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [0.06, 0.4, 1.89, 6.38, 11.34, 10.47, 20.07, 28.17, 20.07, 1.15, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 2.21, 'naoExiste': 97.79},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':1, 'estadual': 4, 'federal': 1,'particular': 15},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':84, 'estadual': 583, 'federal': 5395,'particular': 7095},	# Número de escolas	# Média de Alunos por escolas
}
