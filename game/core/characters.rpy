# Character Images

image quixote = "images/quixote_fue_ostamara.png"
image furique = "images/furique_vallitu.png"
image torrez = "images/torrez_fue_léon.png"
image aurgenbia = "images/aurgenbia_panzarre.png"
image gaucho = "images/gaucho_fue_léon.png"
image cervanzian = "images/cervanzian_mulocco.png"
image isine = "images/Isine_fue_Tholedo.png"
image charristo = "images/Charristo_fue_Tholedo.png"
image mate = "images/Maté_fue_Tholedo.png"
image calitz = "images/Cálitz_fue_Tholedo.png"
image sicill = "images/Sicill fue Tholedo.png"
image robertz = "images/Robertz_fue_Tholedo.png"
image solene = "images/Solène_Lapis.png"

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
    "Isine fue Tholedo"
)

define charristo = Character(
    "Charristo fue Tholedo"
)

define mate = Character(
    "Maté fue Tholedo"
)

define calitz = Character(
    "Cálitz fue Tholedo"
)

define sicill = Character(
    "Sicill fue Tholedo"
)

define robertz = Character(
    "Robertz fue Tholedo"
)

define solene = Character(
    "Queen Solène Lapis"
)
