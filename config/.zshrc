export TYPEWRITTEN_PROMPT_LAYOUT="singleline_verbose"
export TYPEWRITTEN_SYMBOL="$"
export TYPEWRITTEN_CURSOR="block"
export TYPEWRITTEN_DISABLE_RETURN_CODE="true"

fpath+=$HOME/.zsh/typewritten
autoload -U promptinit; promptinit
prompt typewritten

PATH=$HOME/.local/bin:$HOME/.cargo/bin:/opt/swift/usr/bin:$PATH

alias top=ytop
alias cat=bat
alias ls=exa

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
