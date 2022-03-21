
# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

lagoaAzul = {
	# =============================================================
	# Dados Demográficos - Dados de 2010-2017
	'regiao': 'norte',					# Zona ao qual o bairro pertence
	'tamPop': 69258,					# Tamanho da população
	'tamFisico': 1167.5,				# Área do bairro em Hectare
	'densidadeDemografica': 59.32,		# Densidade demografica (Hab/km²)
	'numDomicilio': 17281,				# Numero de domicilios
	'domicilio': {'casa': 96.82, 'apartamento': 0.06, 'comodo':0.05, 'casa de vila ou condominio': 3.07,  'outro': 0},
	'idade': [8871, 11573, 14521, 10380, 10188, 7447, 3898, 1495, 885],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [2.91, 9.94, 28.06, 35.94, 16.01, 2.53, 0.96, 0.28, 0.06, 3.29, 0.02], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 57.72, 'naoExiste': 42.28},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',			# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',				# Numero de leitos dos hospitais
	'uti': 'vazio',					# Número de UTIS do bairro
	'doencasCronicas': 'vazio',		# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares - Dados de 2018
	'escolas': {'municipal':12, 'estadual': 8, 'particular': 12},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':4343, 'estadual': 5676, 'particular': 2586},	# Número de escolas	# Média de Alunos por escolas
}
