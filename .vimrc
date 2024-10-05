" *********************************************************************************
" *                               VIM MAPPINGS REFERENCE                          *
" *********************************************************************************
" Mapping    Use Case
" \cm        Comment selected lines in C++.
" \uc        Uncomment selected lines in C++.
" \ff        Format the entire file for proper indentation.
" \rw        Remove trailing whitespace in the file.
" \r         Compile and run the current Python file.
" \cr        Compile and run the current C++ file without debug mode.
" \cd        Compile and run the current C++ file with debug mode.
" \sh        Switch from header (.hpp) to source (.cpp) file.
" \sc        Switch from source (.cpp) to header (.hpp) file.
" \nt        Toggle NERDTree file explorer.
" \wq        Save and quit.
" \w         Save the current file.
" \q         Quit without saving.
" \sp        Split window horizontally.
" \vs        Split window vertically.
" Ctrl+h/j/k/l    Move between split windows.
" \bl        List all open buffers.
" \bn        Move to the next buffer.
" \bp        Move to the previous buffer.
" \gg        Move to the top of the file.
" \G         Move to the bottom of the file.
" <Up>       Resize window vertically (increase height).
" <Down>     Resize window vertically (decrease height).
" <Left>     Resize window horizontally (decrease width).
" <Right>    Resize window horizontally (increase width).

" *********************************************************************************
" *                           BASIC VIM SETTINGS                                  *
" *********************************************************************************

syntax on                              " Enable syntax highlighting
filetype plugin indent on              " Enable file type detection, plugins, and indentation
set nocompatible                       " Disable Vi compatibility mode for enhanced Vim functionality

" Set leader key to '\' for custom shortcuts
let mapleader = "\\"                   " Leader key is '\'

" Disable confirmation for loading .ycm_extra_conf.py
let g:ycm_confirm_extra_conf = 0       " Automatically load .ycm_extra_conf.py without prompting

" *********************************************************************************
" *                            PLUGIN MANAGEMENT (Vundle)                         *
" *********************************************************************************

" Set the runtime path for Vundle (plugin manager)
set rtp+=~/.vim/bundle/Vundle.vim    

" Initialize Vundle plugin system
call vundle#begin()

" List of plugins to be managed by Vundle
Plugin 'VundleVim/Vundle.vim'          " Vundle plugin manager itself
Plugin 'ycm-core/YouCompleteMe'        " Autocompletion plugin for C++ and Python
Plugin 'dense-analysis/ale'            " Asynchronous linting and fixing for C++ and Python
Plugin 'vim-airline/vim-airline'       " Enhanced status line for Vim
Plugin 'preservim/nerdtree'            " File explorer for easy navigation
Plugin 'honza/vim-snippets'            " Snippets for faster coding
Plugin 'psf/black'                     " Black formatter for Python

" Finalize Vundle plugin setup
call vundle#end()

" Re-enable file type detection, plugins, and indentation after plugin loading
filetype plugin indent on

" *********************************************************************************
" *                           GENERAL VIM CONFIGURATIONS                          *
" *********************************************************************************

set number                             " Enable line numbers in the editor
set relativenumber                     " Enable relative line numbers for faster navigation
set showcmd                            " Show partial command in the last line of the screen
set cursorline                         " Highlight the current line
set tabstop=4                          " Number of spaces that a <Tab> in the file counts for
set shiftwidth=4                       " Number of spaces to use for each step of (auto)indent
set expandtab                          " Use spaces instead of tabs
set autoindent                         " Copy indent from the previous line automatically
set clipboard=unnamedplus              " Use system clipboard for copy/paste

" Map F3 to toggle search highlight on/off
nnoremap <silent> <F3> :set hlsearch!<CR> 

" *********************************************************************************
" *                               C++ SETTINGS                                    *
" *********************************************************************************

" === C++: Filetype Detection ===
autocmd BufRead,BufNewFile *.cpp set filetype=cpp        " Ensure Vim correctly sets filetype for C++ files

" === C++: Linting and Formatting ===
let g:ale_linters = {'cpp': ['clangtidy', 'cppcheck']}   " Use clang-tidy and cppcheck for linting C++ code
let g:ale_fixers = {'cpp': ['clang-format']}             " Use clang-format for fixing C++ code style

" === C++: Indentation and Numbering ===
autocmd FileType cpp setlocal tabstop=4 shiftwidth=4 expandtab        " Use 4 spaces for tabs and indentation in C++
autocmd FileType cpp setlocal number                                  " Enable line numbers for C++ files
autocmd FileType cpp setlocal relativenumber                          " Enable relative line numbers for C++ files
autocmd FileType cpp setlocal autoindent smartindent                  " Enable automatic indentation for C++ files

" === C++: Insert Template for New C++ Files ===
autocmd BufNewFile *.cpp 0r ~/.vim/templates/cpp_template.cpp         " Automatically insert a C++ template when creating new .cpp files

" === C++: Commenting and Uncommenting ===
" Comment selected lines in C++ with // (Visual Mode)
vnoremap <silent> <leader>cm :<C-u>'<,'>s/^/\/\//g<CR>

" Uncomment selected lines in C++ by removing // (Visual Mode)
vnoremap <silent> <leader>uc :<C-u>'<,'>s/^\/\///<CR>

" *********************************************************************************
" *                               PYTHON SETTINGS                                 *
" *********************************************************************************

" === Python: Linting and Formatting ===
let g:ale_linters = {'python': ['flake8']}               " Use flake8 for linting Python code
let g:ale_fixers = {'python': ['black']}                 " Use black for fixing Python code style

" === Python: Indentation and Numbering ===
autocmd FileType python setlocal tabstop=4 shiftwidth=4 expandtab      " Use 4 spaces for tabs and indentation in Python
autocmd FileType python setlocal number                                " Enable line numbers for Python files
autocmd FileType python setlocal relativenumber                        " Enable relative line numbers for Python files
autocmd FileType python setlocal autoindent smartindent                " Enable automatic indentation for Python files

" === Python: Insert Template for New Python Files ===
autocmd BufNewFile *.py 0r ~/.vim/templates/python_template.py         " Automatically insert a Python template when creating new .py files

" *********************************************************************************
" *                         CODE FORMATTING AND CLEANUP                          *
" *********************************************************************************

" Map leader + ff to format the entire file for proper indentation and spacing
vnoremap <leader>ff :normal gg=G<CR>  " Formats the entire file for C++ and Python

" Map leader + rw to remove trailing whitespaces in the entire file
nnoremap <leader>rw :%s/\s\+$//e<CR>  " Remove trailing whitespace in the entire file

" *********************************************************************************
" *                           COMPILING AND RUNNING CODE                         *
" *********************************************************************************

" Function to run Python code in a terminal with 30% width on the right side, 2-second limit
function! RunPython()
    exec "w" | exec "right resize 30 | term python3 %"
endfunction

" Function to compile and run C++ without debug mode with 30% width on the right side, 2-second limit
function! CompileCpp()
    exec "w" | exec "right resize 30 | term bash -c \"g++ -std=c++20 " . expand('%') . " -o " . expand('%<') . ".out  ./" . expand('%<') . ".out\""
endfunction

" Function to compile and run C++ with debug mode (-DLOCAL) with 30% width on the right side, 2-second limit
function! CompileCppDebug()
    exec "w" | exec "right resize 30 | term bash -c \"g++ -std=c++20 -DLOCAL " . expand('%') . " -o " . expand('%<') . ".out  ./" . expand('%<') . ".out\""
endfunction

" Map leader + r to compile and run Python code with 30% right-side split
nnoremap <leader>r :call RunPython()<CR>

" Map leader + cr to compile and run C++ without debug mode with 30% right-side split
nnoremap <leader>cr :call CompileCpp()<CR>

" Map leader + cd to compile and run C++ with debug mode with 30% right-side split
nnoremap <leader>cd :call CompileCppDebug()<CR>


" *********************************************************************************
" *                             QUICK NAVIGATION                                  *
" *********************************************************************************

" Map leader + sh to quickly switch to the corresponding .cpp file from a .hpp file
nnoremap <leader>sh :e %:r.cpp<CR>  

" Map leader + sc to quickly switch to the corresponding .hpp file from a .cpp file
nnoremap <leader>sc :e %:r.hpp<CR>  

" Map leader + nt to toggle NERDTree (file explorer)
nnoremap <leader>nt :NERDTreeToggle<CR> 

" *********************************************************************************
" *                             DAILY USE COMMANDS                                *
" *********************************************************************************

" Map leader + wq to save and quit
nnoremap <leader>wq :wq<CR>  

" Map leader + w to save the file
nnoremap <leader>w :w<CR>  

" Map leader + q to quit without saving
nnoremap <leader>q :q!<CR>  

" Map leader + sp to split the window horizontally
nnoremap <leader>sp :split<CR>

" Map leader + vs to split the window vertically
nnoremap <leader>vs :vsplit<CR>

" Move between split windows easily using Ctrl + h/j/k/l
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" Resize splits easily using leader + arrows
nnoremap <leader><Up> :resize +2<CR>
nnoremap <leader><Down> :resize -2<CR>
nnoremap <leader><Left> :vertical resize -2<CR>
nnoremap <leader><Right> :vertical resize +2<CR>

" Fast navigation to the start and end of a file
nnoremap <leader>gg :gg<CR>            " Move to the top of the file
nnoremap <leader>G :G<CR>              " Move to the bottom of the file

" Quick access to buffer list
nnoremap <leader>bl :ls<CR>            " List all open buffers
nnoremap <leader>bn :bnext<CR>         " Go to the next buffer
nnoremap <leader>bp :bprev<CR>         " Go to the previous buffer


