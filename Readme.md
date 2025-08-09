# mdot

[![PyPI version](https://img.shields.io/pypi/v/mdot.svg)](https://pypi.org/project/mdot/)

> *"Talk in dots and dashes like it’s 1844."*  
---

A lightweight **CLI tool** to encode and decode Morse code - because typing `.... . .-.. .-.. ---` is just cooler than typing “hello”.  

---

## Install

```bash
pip install mdot
````

---

## Usage

**Encode Text → Morse**

```bash
mdot --encode "HELLO WORLD"
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

**Decode Morse → Text**

```bash
mdot --decode ".... . .-.. .-.. ---"
# HELLO
```

---

## Features

* Encode text into Morse code
* Decode Morse code back into text
* No internet required - works entirely offline
* Simple & lightweight (less than 100 lines of code)

---

## Contributing

PRs are welcome!
If you’d like to add sound output, file support, or even ASCII flashing lights - go wild.

---

## License

[MIT License](LICENSE) - free to use, modify, and share.

---
