#El entorno virtual se hace por los problemas de versión pertinentes que hagan falta para cada proyecto

#python -m venv VirtualEnv  (De esta manera crearemos la carpeta del entorno virtual)
#VirtualEnv\Scripts\activate.bat        (Sino se activa activar de esta manera, suele aparecer el entorno abajo a la izquierda)
#Si no ejecutaba esta línea no podía permitir los scripts Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process     (Pendiente de buscar una manera más segura)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot


#Recomendado!
#Con conda sería algo así (https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv?page=2&tab=votes#tab-top)
#conda search "^python$"
#conda create -n yourenvname python=x.y.z(versión)
#conda activate yourenvname (Para desactivar conda deactivate)
#(Para borrar) conda remove -n yourenvname --all
#Para instalar librerías conda install -n <env_name> <package> (https://stackoverflow.com/questions/33680946/how-to-add-package-to-conda-environment-without-pip)