create_env:
	@conda create --name ml_pinguins_env  python=3.9
	@echo "Saisir dans la console : conda activate ml_pinguins_env"

install_requirements:
	@conda install pip
	@pip install -r app/requirements.txt

maj_requirements:
	@pip freeze > app/requirements.txt
