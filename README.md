<H1>Spam Projekt , IKT SS24, Irina Ukhanova</H1>

<p> <b>Klassifikation von Spam-Buchungsanfragen auf einem Immobilienportal</b></p>

<p> Das Ziel dieses Projekts ist es, die Sicherheit von Buchungsanfragen auf einem Immobilienportal zu erhöhen, indem anfällige und gefährliche Anfragen automatisch vom System erkannt und blockiert werden. Hierbei sollen ML-Techniken angewendet werden, um legitime Buchungsanfragen von Spam zu unterscheiden. Dies schützt sowohl das Unternehmen als auch die Nutzer vor potenziellen Betrugsversuchen und anderen schädlichen Aktivitäten.</p>

<p><b>Datensatz: </b> Ein unternehmensinterner Datensatz, der Spam-Buchungsanfragen enthält. Dieser Datensatz besteht aus Inhalt der Nachricht und Spam/nicht Spam Labels</p>
<a href = "https://spamornotp4g.streamlit.app/"> Streamlit App </a>   

<p> <h2>Sprint 1: Problemdefinition und Prozessexploration</h2></p>
<p> <b>Ziel: </b><br></p>
Problem und Status Quo Prozesse im Unternehmen besser verstehen<br>
<p> <b>Aufgaben: </b></p>
<li>Status Quo Prozess von Spamerkennung von Nachrichten erkennen und beschreiben </li>
<li>Ziel des Projekt definieren - alle Spam-Nachrichten auffangen</li><br>
<p> <b>Ergebnis: </b><br></p>
<li>Flowchart von Prozessen</li>
<li>Problem ist klar dargestellt, Ziel definiert - alle Spam-Nachrichten auffangen</li>
<img src="img/SPAMprojekt.png" >

<p> <h2>Sprint 2: Datenvorbereitung und Exploration</h2></p>
<p> <b>Ziel: </b><br>
Datenaufbereitung und erste Explorative Datenanalysen. 
<p> <b>Aufgaben: </b>
<li>Datensammlung und -import: Die Daten wurden aus der Unternehmensdatenbank heruntergeladen. Der Datensatz ist mit 0 für Nicht-Spam und mit 1 für Spam gekennzeichnet.</li>
<li>Datenbereinigung</li>
<table>
  <tr>
    <th>Nicht Spam</th>
    <th>Spam</th>
  </tr>
  <tr>
    <td>5416</td>
    <td>68</td>
  </tr>
</table>

<p> Ergebnis: 
<li> Sauberer und explorierter <a href = "spam_nichtspam_datensatz.csv"> Datensatz </a>.   </li>

<p> <h2>Sprint 3: Evaluierung vom Datensatz als Baseline</h2></p>
<p> <b>Ziel:  </b><br>
Evaluieren des Datensatzes für Anwendung von jetzigen Spam-Filtern
<p> <b>Aufgaben:  </b>
<li>Ein Skript erstellen, um die Effektivität vom Spam-Filetr zu prüfen  </li>
<p> <b>Ergebnis: </b>
<li> <a href = "baseline_vs_model.py"> Skript </a></li>
<li> <table>
     <tr>
    <td> </td>
    <td>Spam-Filter</td>
    <td>Datensatz</td>
  </tr>
  <tr>
    <td> Anzahl von Spam-Nachrichten:</td>
    <td>38</td>
     <td>68</td>
  </tr>
  <tr>
    <td> Anzahl von Nicht-Spam-Nachrichten:</td>
    <td>5447</td>
     <td>5416</td>
  </tr>
</table>

<p> <h2>Sprint 4: Modellentwicklung und erste Evaluierung</h2></p>
<p> <b>Ziel: Erstellen und evaluieren eines ersten Machine Learning Modells.</b><br>
<p> <b>Aufgaben:  </b>
<li>Auswahl des Baseline-Modells -  sklearn.linear_model -> Logistische Regression </li>
<li>Datensplit (Trainings- und Testdatensatz). Sklearn.model_selection -> train_test_split</li>
<li>Metriken definieren (Accuracy, Precision, Recall, F1 Score)</li>
<li>Training und erste Evaluierung des Modells.</li>
<p> <b>Ergebnis:  </b>
<li>Trainingssetgröße:4387</li>
<li>Testsetgröße:1097</li>
<li>Genauigkeit: 0.9881494986326345</li>
<li>Precision: 1.0</li>
<li>Recall: 0.13333333333333333</li>
<li>F1 Score: 0.23529411764705882 </li>
<li>Confusion Matrix: [[1082    0] <br>
 [  13    2]] </li>

<p><img src="img/LogRegModel_metriks_2.png" ></p>
<p><img src="img/confusion_matrix_2.png" ></p>

