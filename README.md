<H1>Spam Projekt , IKT SS24, Irina Ukhanova</H1>

<p> <b>Klassifikation von Spam-Buchungsanfragen auf einem Immobilienportal</b></p>

<p> Das Ziel dieses Projekts ist es, die Sicherheit von Buchungsanfragen auf einem Immobilienportal zu erhöhen, indem anfällige und gefährliche Anfragen automatisch vom System erkannt und blockiert werden. Hierbei sollen ML-Techniken angewendet werden, um legitime Buchungsanfragen von Spam zu unterscheiden. Dies schützt sowohl das Unternehmen als auch die Nutzer vor potenziellen Betrugsversuchen und anderen schädlichen Aktivitäten.</p>
<p>
<p><b>Datensatz: </b> Ein unternehmensinterner Datensatz, der Spam-Buchungsanfragen enthält. Dieser Datensatz besteht aus Inhalt der Nachricht und Spam/nicht Spam Labels</p>
<p>
<p><b>ML-Instrumente: </b> 
<li> Logistische Regression</li>
<li> Cross Validation</li>
<li> Oversampling</li>
  <p>
<p> <b>Erkenntnisse </b><br>
Das Modell zeigt eine hohe Präzision und Genauigkeit und kann gut zwischen positiven und negativen Klassen unterscheiden. Es zeigt aber auch False Positives (3). Dies ist zwar eine sehr geringe Anzahl, aber für dieses Geschäftsmodell sind False Positives kritisch, da sie bedeuten, dass Nachrichten, die kein Spam sind, als Spam blockiert werden: zu viele False Positives können das Vertrauen der Benutzer in das System beeinträchtigen.
Da die Kreuzvalidierung sehr gute Ergebnisse zeigt und auch die allgemeinen Metriken nach dem Oversampling sehr gut sind, deuten die allgemeinen Ergebnisse nicht direkt auf Overfitting hin. Daher kann man weitere mögliche Schritte vornehmen:
<li>Entscheidungsschwellenwert für Logistische Regression anpassen um False Positives zu reduzieren (Nachteil - möglicherweise auf Kosten der Steigerung von False  Negatives)</li>
<li>Qualität der Datensatz erhöhen -  mit weiteren realen Daten erweitern, jetzt sind die Daten etwa verrauscht </li>
<li>ein komplexeres Modell ausprobieren (z.B. Random Forest)</li>
<p>
<p> <b>Wichtige Links</b><br>
<a href = "SpamKlassifikationPrasentation.pdf"> Präsentation des Projekts Juli 2024</a>  <br>
<a href = "Sprints_Projektbeschreibung.ipynb"> Sprints</a>  <br> 
<a href = "https://spamornotp4g.streamlit.app/"> Streamlit App </a>  <br> 

