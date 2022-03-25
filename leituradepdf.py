{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "57896440",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "import tabula\n",
    "\n",
    "lista_tabelas = tabula.read_pdf(\"ResultadoVale.pdf\", pages=\"11\")\n",
    "print(len(lista_tabelas))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "056079f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "for tabela in lista_tabelas:\n",
    "    display(tabela)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
