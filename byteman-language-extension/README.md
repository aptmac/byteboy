# Byteman Language Extension

A Visual Studio Code Language Extension for Byteman.

## Installation

Byteboy currently requires manual installation, and it is an easy task. Once downloaded, this folder (byteman-language-plugin) must be copied into the vscode extensions folder located at : ``/home/<hostname>/.vscode/extensions``.

Here's a command to install the extension:  
``cp -r <path/to/byteman-language-plugin> ~/.vscode/extensions``

## Features
- VS Code should auto-recognize ``.btm`` files
- Byteman Language Support
- Basic Syntax Highlighting

## Contributing

When making changes on the source-code, the folder must be re-copied to the ``~/.vscode/extensions`` folder in order to apply the changes. Visual Studio Code will also need to be restarted.

To get started, in the grammar file at ``syntaxes/byteman.tmLanguage.json`` there are some useful documents included in a coment at the top. There is a link to the Byteman Language Syntax a found on the Byteman repo, a link to an existing language extension to get inspiration from, and a link to the manual for creating tmLanguage grammars as written by TextMate.

## Thinking Big (TODOs & Areas of Improvement)
- Add languge Snippets
- Add IntelliSense Support (auto-completion)
- Add a custom theme
- Add highlighting for incorrect syntaxes
- Add debugging support

## Release Notes

### 0.0.1

Current Release.
