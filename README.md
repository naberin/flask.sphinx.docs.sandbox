# Documentation with Sphinx

## Getting Started
To add new Sphinx source files using the autodoc extension
```bash
# output to <source>
sphinx-apidoc -o source/ ../backend/
```

To build / rebuild the documentation
```bash
# without make
sphinx-build source/ build/

# with make
make clean build
```

## Tips
To prevent autodoc from running your Flask application, put
your global initializations inside
```python
if __name__ == "__main__":
    someRandomGlobalOrSingleton = someRandomGlobalOrSingleton()
```

## The Code
The backend code built with Flask [[go]](./backend/README.md)

## Getting more help
- [Official Sphinx Documentation](https://www.sphinx-doc.org/en/master/contents.html)
- [Markdown Support with MyST](https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html#)

