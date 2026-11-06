# Publicación del proyecto en GitHub

El repositorio público `Jamarma12/IBEX35-CAPM-Research` tenía originalmente un ZIP, una licencia GPL-3.0 y un README mínimo. **El ZIP no sustituye a publicar su contenido:** GitHub no puede navegar ni renderizar un notebook que queda dentro de un archivo comprimido.

## Subida desde la web (sin usar Git)

1. Descarga el paquete actualizado y **descomprímelo** en tu ordenador.
2. Entra en [el repositorio](https://github.com/Jamarma12/IBEX35-CAPM-Research).
3. Si deseas conservar una copia del estado anterior, utiliza **Code → Download ZIP** antes de modificar nada.
4. Pulsa **Add file → Upload files** y arrastra **el contenido de la carpeta `IBEX35-CAPM-Research/`**, no la carpeta contenedora ni el ZIP.
5. Comprueba que la vista previa muestra `README.md`, `notebooks/`, `data/`, `docs/`, `scripts/`, `tests/`, `requirements.txt` y `.github/` en la raíz. Los archivos ocultos como `.gitignore`, `.gitattributes` y `.github/` requieren activar su visualización en el explorador del sistema.
6. En la vista de carga de GitHub, confirma los cambios, preferiblemente creando una rama y una pull request si la interfaz ofrece esa posibilidad.
7. Comprueba el renderizado del notebook desde GitHub y ejecuta la validación local o revisa la acción **Actions → Validate repository**.
8. El antiguo `IBEX35-CAPM-Research_GitHub.zip` en la raíz será **redundante** tras subir sus componentes. Puedes borrarlo manualmente desde la interfaz para dejar una portada limpia.

> Atención: la interfaz web de GitHub puede no aceptar arrastrar carpetas completas o archivos ocultos según el navegador. Si se pierden directorios, usa el procedimiento con Git indicado a continuación.

## Subida más fiable con Git

Clona el repositorio actual y copia **los contenidos** del directorio descomprimido en su raíz, sin borrar `.git/`:

```bash
git clone https://github.com/Jamarma12/IBEX35-CAPM-Research.git
cd IBEX35-CAPM-Research
# Copia aquí el contenido del paquete descomprimido.
git checkout -b docs/github-publication
git add README.md LICENSE requirements.txt CITATION.cff .gitignore .gitattributes .github notebooks data docs scripts tests
git status
git commit -m "Publish CAPM research notebook, dataset and documentation"
git push -u origin docs/github-publication
```

A continuación, crea una **pull request** hacia `main` desde GitHub. Este procedimiento mantiene intactos los archivos originales del historial hasta que apruebes los cambios. Si decides eliminar el ZIP antiguo, hazlo en un commit separado.

## Revisión antes de compartir

- [ ] Notebook accesible desde `notebooks/` (no únicamente dentro del ZIP).
- [ ] CSV accesible desde `data/`, y permisos de redistribución comprobados.
- [ ] README con enlaces internos que funcionan.
- [ ] Licencia GPL-3.0 coherente con la existente.
- [ ] Validación offline en verde; la validación online se documenta por separado.
- [ ] No se publican figuras, alphas, betas o conclusiones sin una ejecución real validada.
- [ ] Sin tokens, contraseñas, archivos temporales ni resultados locales sensibles.

## Nota sobre derechos de datos

El CSV del IBEX 35 Total Return procede de un tercero. Antes de subirlo a un repositorio público, revisa si el proveedor permite redistribuir el archivo. Si no es así, **no subas el CSV** y describe cómo obtenerlo legítimamente; los tests y rutas deberán ajustarse a esa modalidad de distribución.
