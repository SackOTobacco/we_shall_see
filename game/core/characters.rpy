# Character Images

image quixote = Transform("images/quixote_fue_ostamara.png", yoffset=-5)
image furique = Transform("images/furique_vallitu.png", yoffset=-5)
image torrez = Transform("images/torrez_fue_léon.png", yoffset=-5)
image aurgenbia = Transform("images/aurgenbia_panzarre.png", yoffset=-5)
image gaucho = Transform("images/gaucho_fue_léon.png", yoffset=-5)
image cervanzian = Transform("images/cervanzian_mulocco.png", yoffset=-5)
image isine = Transform("images/Isine_fue_Tholedo.png", yoffset=-5)
image charristo = Transform("images/Charristo_fue_Tholedo.png", yoffset=-5)
image mate = Transform("images/Maté_fue_Tholedo.png", yoffset=-5)
image calitz = Transform("images/Cálitz_fue_Tholedo.png", yoffset=-5)
image sicill = Transform("images/Sicill fue Tholedo.png", yoffset=-5)
image robertz = Transform("images/Robertz_fue_Tholedo.png", yoffset=-5)
image solene = Transform("images/Solène_Lapis.png", yoffset=-5)

# Narrator

init python:

    class CodexNarrator(ADVCharacter):
        """Preserves narrator italics on codex hyperlinks."""

        def __call__(self, what, *args, **kwargs):
            if isinstance(what, str):
                what = narrator_codex_markup(what)

            return super(CodexNarrator, self).__call__(what, *args, **kwargs)


define n = CodexNarrator(
    None,
    what_italic=True
)

# Emperor

define p = Character(
    "Pherip IV"
)

# Castilles

define q = Character(
    "{a=codex_name:quixote}Quixote fue Ostamara{/a}"
)

define f = Character(
    "{a=codex_name:furique}Furique Vallitu{/a}"
)

define t = Character(
    "{a=codex_name:torrez}Torrez fue Léon{/a}"
)

define a = Character(
    "{a=codex_name:aurgenbia}Aurgenbia Panzarre{/a}"
)

define g = Character(
    "{a=codex_name:gaucho}Gaucho fue Léon{/a}"
)

# Side Characters to Council

define c = Character(
    "Cervanzian Mulocco"
)

# House Tholedo

define isine = Character(
    "{a=codex_name:isine_tholedo}Isine fue Tholedo{/a}"
)

define charristo = Character(
    "{a=codex_name:charristo_tholedo}Charristo fue Tholedo{/a}"
)

define mate = Character(
    "{a=codex_name:mate_tholedo}Maté fue Tholedo{/a}"
)

define calitz = Character(
    "{a=codex_name:calitz_tholedo}Cálitz fue Tholedo{/a}"
)

define sicill = Character(
    "{a=codex_name:sicill_tholedo}Sicill fue Tholedo{/a}"
)

define robertz = Character(
    "{a=codex_name:robertz_tholedo}Robertz fue Tholedo{/a}"
)

define solene = Character(
    "{a=codex_name:solene_lapis}Solène Lapis{/a}"
)
