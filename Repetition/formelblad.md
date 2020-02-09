
Syntax                      Memo
<name> = <value>            Tilldelning av värde till variabel
<listname>.append(<value>)  Tilldelning av värde till en lista

<value> <operator> <value>  Beräkningssats, där operator kan vara + - * /

= , += , -= , *= , /=       Tilldelningsoperatorer. För att spara nytt värde, addera ett värde, subtrahera,
                            multiplicera ett värde, dela ett värde

> < <= >= ==                Jämförelseoperatorer. För att jämföra två värden

float, int, str, list       Vanligt förekommande datatyper

<typename>(<value>)         Typkonvertering, för att kovertera datatypen på value till typen som angivs i typename


if (<vilkor>):              Vilkorssats som körs en gång om vilkor är True
    <commands>
elif (<vilkor>):            Vilkorsats som körs en gång om tidigare vilkor är False, och nuvarande är True
    <commands>
else:                       Else-sats som körs en gång om tidigare vilkor är False 
    <commands>

while (<vilkor>):           Vilkorssats som körs flera gånger så länge som vilkor är True
    <commands>

for (<value> in <list>):    List-iterator. Körs en gång för varje värde i listan. Där varje värde placeras i value
    <commands>

def <funcname>(<param>):    Funktionsdefinition. Definerar kommandon som körs för funktionen.
    <commands>              in-data till funktionen defineras i param
    [return <value>]        optional. funktionens resultat returneras.

<funcname>(<param>)         Funktionsanrop. Kör den angivna funktionen, med angivna parametrar.

class <classname>():        Klassdefinition.
    <datamedlemmar>:<type>  Definition av datamedlem, och dess typ     

    def __init__(self):     standardfunktion för klasser.
        <commands>

    def __str__(self):      standardfunktion för klasser.
        <commands>
        return <stringvalue>

<objectname> = <classname>()    Skapande av ett objekt från en klass.



