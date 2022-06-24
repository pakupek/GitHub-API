{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13171c29",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "ACCESS_KEY = \"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\"\n",
    "\n",
    "\n",
    "def get_api():\n",
    "    endpoint = \" https://api.github.com/users/KentBeck/repos\"\n",
    "    headers = {\n",
    "        \"Accept: application/vnd.github.v3+json\"\n",
    "        \"Authorization\": f'token {ACCESS_KEY}'\n",
    "    }\n",
    "    response = requests.get(endpoint, headers=headers)\n",
    "    response.raise_for_status()\n",
    "    return response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "dd381920",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name\t\t\t\t\tSize\t\tContributors Count\tBranch\t\tIs protected\n",
      "------------------------\t------------\t\t------------------\t-------------\t------------\n"
     ]
    }
   ],
   "source": [
    "print(\"Name\\t\\t\\t\\t\\tSize\\t\\tContributors Count\\tBranch\\t\\tIs protected\")\n",
    "print(\"------------------------\\t------------\\t\\t------------------\\t-------------\\t------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0eae25cc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
