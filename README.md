ATTENTION : la reproductibilité a été testé sur des PC en local et sur le Onyxia (SSPCloud) du groupe GENES
Un seul problème est parfois apparu : un service VSCode-Python de Onyxia peut avoir des problèmes à ouvrir des .ipynb
    Dans ce cas, utiliser un service Jupyter-python fonctionne (on a testé).


La présentation est sous forme de site Quarto.
Vous pouvez exécuter les commandes suivantes pour créer l'environnement et installer toutes les librairies nécessaires et lancer le site :
    cd ./PYDS
    py -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt

Puis, déployez le site Quarto
    quarto preview
Et naviguer à l'adresse indiquée par le terminal.
Vous pourrez ensuite naviguer vers la page "Projet" avec la navbar.

Toute l'étude est contenue dans un notebook : /website/code/index.ipynb
Tous les autres fichiers sont soit des fichiers de quarto soit des fichiers brouillons de travail.

Bonne lecture !

Nathan de Joannès, Dany Thai, Alexandre Pésenti