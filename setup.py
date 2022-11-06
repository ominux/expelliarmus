from setuptools import Extension, setup
import os

setup(
        name="potter",
        author="Fabrizio Ottati", 
        author_email="fabriziottati@gmail.com", 
        maintainer="Fabrizio Ottati",
        maintainer_email="fabriziottati@gmail.com", 
        py_modules=["decoders"],
        license="GPL V2",
        include_dirs=["potter/src"],
        ext_modules=[
            Extension(
                name="potter", 
                sources=[os.path.join("potter", "src", "potter.c")],
                language="c",
                ), 
            ]
        )
