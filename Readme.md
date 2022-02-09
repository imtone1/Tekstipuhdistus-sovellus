Tämän harjoitustyön ohjelma mahdollistaa poistaa tekstitiedostoista merkit/sanat/lauseet.

Tiedostojen luku
Ohjelma kysyy ensin tiedostopolut, se mistä poistetaan ja se mihin kirjoitetaan.
Ohjelma tarkistaa tässä vaiheessa onko kyseiset tiedostot olemassa ja tarkistaa, ettei kyseessä olisi sama tiedosto.

Poistettavan tiedon tallentaminen
Tiedosto kysyy loopissa mitä haluaa tekstitiedostosta poistaa, x:lla poistuu. Ohjelma ottaa huomioon niin isolla kuin pienellä kirjoitettu vastaus (x). 
Ohjelma tarjoaa myös mahdollisuuden muokata poistettava lista.
Ohjelma ottaa huomioon jos on kirjoitettu monta sanaa välilyönnillä erotettuna ja lisää nämäkin listalle.

Poistetaan annettu tieto tekstitiedostosta
Avataan tiedostot ja käydään tekstitiedoston rivi riviltä, poistetaan delete_listalla esiintyviä sanoja. Puhdistettu teksti kirjoitetaan toiseen tiedostoon.

Tiedoston tulostaminen
Ohjelma antaa mahdollisuuden avata tiedosto ohjelmassa. (Ei suositella isojen tiedostojen kohdalla!)
Tarjotaan myös mahdollisuuden aloittaa ohjelma uudelleen.

Ohjelma sisältää 5 metodia + main() metodin.
Ohjelmassa on käytetty os kirjastoa tarkistaessa tiedostojen olemassaolon.