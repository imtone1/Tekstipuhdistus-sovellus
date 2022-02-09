Tämän tekstipuhdistus- ohjelma mahdollistaa poistaa tekstitiedostoista merkit/sanat/lauseet.

Tiedostojen luku<br>
Ohjelma kysyy ensin tiedostopolut, se mistä poistetaan ja se mihin kirjoitetaan.<br>
Ohjelma tarkistaa tässä vaiheessa onko kyseiset tiedostot olemassa ja tarkistaa, ettei kyseessä olisi sama tiedosto.<br>

Poistettavan tiedon tallentaminen<br>
Tiedosto kysyy loopissa mitä haluaa tekstitiedostosta poistaa, x:lla poistuu. Ohjelma ottaa huomioon niin isolla kuin pienellä kirjoitettu vastaus (x). <br>
Ohjelma tarjoaa myös mahdollisuuden muokata poistettava lista.<br>
Ohjelma ottaa huomioon jos on kirjoitettu monta sanaa välilyönnillä erotettuna ja lisää nämäkin listalle.<br>

Poistetaan annettu tieto tekstitiedostosta<br>
Avataan tiedostot ja käydään tekstitiedoston rivi riviltä, poistetaan delete_listalla esiintyviä sanoja. Puhdistettu teksti kirjoitetaan toiseen tiedostoon.<br>

Tiedoston tulostaminen<br>
Ohjelma antaa mahdollisuuden avata tiedosto ohjelmassa. (Ei suositella isojen tiedostojen kohdalla!)<br>
Tarjotaan myös mahdollisuuden aloittaa ohjelma uudelleen.<br>

Ohjelma sisältää 5 metodia + main() metodin.<br>
Ohjelmassa on käytetty os kirjastoa tarkistaessa tiedostojen olemassaolon.
