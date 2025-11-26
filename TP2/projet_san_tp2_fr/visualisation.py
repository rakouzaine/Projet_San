{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00976711",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa55f55f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38aeba93",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'outils_signal'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[16]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mnumpy\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mnp\u001b[39;00m \n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mplotly\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m express \u001b[38;5;28;01mas\u001b[39;00m px\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01moutils_signal\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m (\n\u001b[32m      5\u001b[39m     charger_signal,\n\u001b[32m      6\u001b[39m     centrer_signal,\n\u001b[32m      7\u001b[39m     calculer_spectre_amplitude,\n\u001b[32m      8\u001b[39m     normaliser_spectre_amplitude,\n\u001b[32m      9\u001b[39m )\n\u001b[32m     11\u001b[39m DOSSIER_DONNEES = \u001b[33m\"\u001b[39m\u001b[33mdata/\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m     13\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mafficher_signal_et_spectre\u001b[39m(nom_fichier: \u001b[38;5;28mstr\u001b[39m, titre_prefixe: \u001b[38;5;28mstr\u001b[39m = \u001b[33m\"\u001b[39m\u001b[33mSignal\u001b[39m\u001b[33m\"\u001b[39m):\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'outils_signal'"
     ]
    }
   ],
   "source": [
    "\n",
    "import numpy as np \n",
    "from plotly import express as px\n",
    "from outils_signal import (\n",
    "    charger_signal,\n",
    "    centrer_signal,\n",
    "    calculer_spectre_amplitude,\n",
    "    normaliser_spectre_amplitude,\n",
    ")\n",
    "\n",
    "DOSSIER_DONNEES = \"data/\"\n",
    "\n",
    "def afficher_signal_et_spectre(nom_fichier: str, titre_prefixe: str = \"Signal\"):\n",
    "    \"\"\"\n",
    "    Affiche le signal temporel centré et son spectre normalisé\n",
    "    à l'aide de plotly.express (graphique interactif).\n",
    "    \"\"\"\n",
    "    chemin = DOSSIER_DONNEES + nom_fichier\n",
    "    temps, signal_temporel, fe = charger_signal(chemin)\n",
    "    signal_centre = centrer_signal(signal_temporel)\n",
    "\n",
    "    frequences, amplitude_spectre = calculer_spectre_amplitude(signal_centre, fe)\n",
    "    amplitude_norm = normaliser_spectre_amplitude(amplitude_spectre)\n",
    "\n",
    "    # Graphique temporel\n",
    "    fig_signal = px.line(\n",
    "        x=temps,\n",
    "        y=signal_centre,\n",
    "        labels={\"x\": \"Temps (s)\", \"y\": \"Amplitude\"},\n",
    "        title=f\"{titre_prefixe} - domaine temporel (signal centré)\",\n",
    "    )\n",
    "    fig_signal.show()\n",
    "\n",
    "    # Graphique fréquentiel\n",
    "    fig_spectre = px.line(\n",
    "        x=frequences,\n",
    "        y=amplitude_norm,\n",
    "        labels={\"x\": \"Fréquence (Hz)\", \"y\": \"Amplitude normalisée\"},\n",
    "        title=f\"{titre_prefixe} - spectre d'amplitude normalisé (max = 1)\",\n",
    "    )\n",
    "    fig_spectre.show()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    # Exemple : visualiser le signal 4\n",
    "    afficher_signal_et_spectre(\"signal_4.npz\", titre_prefixe=\"Signal 4\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env_msi",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
