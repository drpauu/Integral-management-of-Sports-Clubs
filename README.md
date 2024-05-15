# Gestió de clubs esportius
Una associació esportiva local vol desenvolupar un sistema de base de dades per gestionar de manera eficient tota la informació relacionada amb els seus membres, equips, i competicions. El sistema ha de gestionar els membres del club, els equips formats per aquests membres, i les competicions en les quals participen els equips.
La informació que es guarda dels membres inclou el seu nom complet, número de soci, data de naixement, sexe, i adreça de correu electrònic; només pot haver-hi un compte associat a una adreça de correu i a un número de soci, sent aquest últim el que identifica a cada membre. Dels equips es guarda un nom (que identifica l'equip), categoria (juvenil, sènior...), i esport (que serà identificat pel seu nom), a més dels membres que en formen part, juntament amb la data d’inclusió a l’equip. La informació sobre les competicions inclou el nom de la competició (que l'identifica), esport, categoria, i any de celebració, així com els equips que hi participen i la data en la que han participat. Un equip pot participar en diverses competicions, però dins d'una mateixa competició, un membre no pot formar part de més d'un equip.

Els membres no podran pertànyer a diversos equips encara que siguin d’esports i categories diferents. A més, per a gestionar millor les estadístiques, cada membre tindrà registrades les seves estadístiques personals per cada competició en la qual participa. Tindrem 3 casos en els que guardarem informació addicional. A les estadístiques de bàsquet guardarem punts anotats, assistències i rebots. Pel que fa al futbol s’emmagatzemeran els gols, les assistències i les targetes grogues. Per últim, es guardaran els gols anotats, assistències i parades de l’esport handbol.

L'associació també vol poder gestionar les quotes anuals dels socis, guardant les dades de pagament i la data de realització. L’identificador de la quota serà la data i el número de soci. Així mateix, és necessari tenir un control sobre els entrenaments de cada equip, registrant la data, hora, lloc, esport, categoria i els membres que han assistit a cada sessió d'entrenament. Sent la data, esport i categoria l’identificador de cada entrenament. De l’assistència s’ha de conèixer la hora d’arribada, la durada de l’entrenament i hi ha d’haver la possibilitat d’afegir comentaris.

Finalment, el sistema ha de permetre la creació de paquets de patrocinis (cadascún amb un identificador numèric únic) per als equips, on cada paquet contindrà un o més patrocinadors, i oferirà beneficis específics com equipament esportiu o suport financer. Els patrocinadors estaran identificats per un nom i proporcionaran una descripció dels beneficis que ofereixen. Un paquet de patrocinis podrà estar associat a múltiples equips i múltiples patrocinadors, a més a més un patrocinador pot estar present en diferents paquets de patrocini simultàniament. El sistema no permetrà l'eliminació de patrocinadors que estiguin associats a algun paquet actiu.
Perquè un acord entre patrocinador i paquet de patrocini sigui vàlid, s’hauran de guardar, la data de l’acord, la durada i les condicions.

# Glossari

Membre del Club: Persona inscrita a l'associació esportiva, la informació del qual inclou nom complet, número de soci, data de naixement, sexe, i adreça de correu electrònic. El número de soci és únic i identifica a cada membre. En el context d’aquesta pràctica 'soci' i 'membre' són sinònims

Equip: Grup format per membres del club. Inclou informació com el nom (identificador de l'equip), categoria (per exemple, juvenil, sènior), i esport practicat (com futbol, bàsquet, handbol).

Competició: Esdeveniment esportiu en el qual participen els equips. Inclou el nom (que l'identifica), esport, categoria, i any de celebració.

Estadístiques personals: Dades individuals d'un membre per cada competició en la qual participa, com ara punts anotats, assistències, i rebots, varien segons l'esport.

Quota anual del soci: Import que els membres han de pagar anualment per la seva afiliació al club. El sistema registra si s'ha pagat i quan.

Sessió d'entrenament: Pràctica programada per als membres dels equips. Registra data, hora, lloc, i assistència dels membres.

Paquet de patrocini: Conjunt d'acords entre l'associació i una o més empreses patrocinadores, que ofereixen beneficis com equipament esportiu o suport financer als equips. Cada paquet inclou els noms dels patrocinadors i una descripció dels beneficis oferts.

Patrocinador: Empresa o individu que dona suport financer o en espècie a l'associació o als seus equips, identificat per un nom i que proporciona una descripció dels beneficis que ofereix.

Esport: Disciplina esportiva practicada pels membres del club. Identificada per un nom, l'esport és una activitat central dins les competicions i entrenaments, dictant les normes i les característiques de cada esdeveniment i sessió.
