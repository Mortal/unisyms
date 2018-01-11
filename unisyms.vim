py3 <<EOF
def uniname(ch):
    import unicodedata
    try:
        return '\\N{%s}' % unicodedata.name(ch)
    except ValueError:
        return repr(ch)[1:-1]
EOF
command! -range Uniname <line1>,<line2>py3do import re; return re.sub(r'[^\x20-\x7f]', lambda mo: uniname(mo.group()), line)

"" Unicode magic
function! Unisyminputcomplete(ArgLead, CmdLine, CursorPos)
py3 import unisyms
return py3eval('unisyms.search(' . json_encode(a:CmdLine) . '[:' . a:CursorPos . '])')
endfunction
let g:unisyminputlast = ''
function! Unisyminput()
    let g:unisyminputlast = input('', '', 'customlist,Unisyminputcomplete')
    py3 import unisyms
    return py3eval('unisyms.try_lookup(' . json_encode(g:unisyminputlast) . ')')
endfunction
inoremap <C-b> <C-r>=Unisyminput()<CR>

function! Unisyminput2()
    cmap <Space> <CR>
    try
	return Unisyminput()
    finally
	cunmap <Space>
    endtry
endfunction
autocmd FileType text inoremap <buffer> \ <C-r>=Unisyminput2()<CR>
