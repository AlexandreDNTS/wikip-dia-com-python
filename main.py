import wikipedia as wiki
wiki.set_lang('pt')
titulo = input('tirulo: ')
pag = int(input('número de páginas: '))
print(wiki.summary(titulo,pag))