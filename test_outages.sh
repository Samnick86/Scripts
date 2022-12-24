#!/bin/bash

# Nastavení proměnných
url=$1  # URL, kterou chcete zkontrolovat
interval=5  # Interval kontroly dostupnosti v sekundách

# Funkce pro kontrolu dostupnosti URL pomocí ping
check_ping() {
  if ping -c 1 "$url" &> /dev/null
  then
    # URL je dostupná pomocí ping
    return 0
  else
    # URL není dostupná pomocí ping
    return 1
  fi
}

# Funkce pro kontrolu dostupnosti URL pomocí telnet
check_telnet() {
  if telnet "$url" 80 &> /dev/null
  then
    # URL je dostupná pomocí telnet
    return 0
  else
    # URL není dostupná pomocí telnet
    return 1
  fi
}

# Hlavní smyčka skriptu
while true
do
  # Kontrola dostupnosti URL pomocí ping
  if check_ping "$url"
  then
    # URL je dostupná pomocí ping
    :
  else
    # URL není dostupná pomocí ping, zkontrolujeme dostupnost pomocí telnet
    if check_telnet "$url"
    then
      # URL je dostupná pomocí telnet, zapíšeme informaci do souboru info.log
      echo "$(date): URL $url je dostupná pomocí telnet, ale není dostupná pomocí ping" >> info.log
    else
      # URL není dostupná pomocí telnet, zapíšeme informaci do souboru out.log
      echo "$(date): URL $url není dostupná pomocí ping ani pomocí telnet" >> out.log
    fi
  fi

  # Přestávka po kontrole dostupnosti URL
  sleep "$interval"
done
