// Nastavení cesty k složce se soubory PSD
var folder = Folder.selectDialog("Vyberte složku se soubory PSD");

// Načtení všech souborů PSD ze složky
var files = folder.getFiles("*.psd");

// Procházení všemi soubory
for (var i = 0; i < files.length; i++) {
  // Otevření souboru
  var doc = open(files[i]);
  var doc= app.activeDocument;

  // Skrytí vrstvy Background layer
  doc.layers.getByName("Background").visible = false;

  // Invertování barev
  doc.layers.getByName("Layer 1").invert();


// Cesta pro uložení nového souboru
var pngFile = new File(folder + "/" + doc.name + ".png");


// Nastavení parametrů pro export
var pngOptions = new ExportOptionsSaveForWeb();
pngOptions.format = SaveDocumentType.PNG;
pngOptions.PNG8 = false;
pngOptions.transparency = true;
pngOptions.interlaced = false;
pngOptions.quality = 100;

// Export aktivního dokumentu
activeDocument.exportDocument(pngFile, ExportType.SAVEFORWEB, pngOptions);

  // Zavření souboru
  doc.close(SaveOptions.DONOTSAVECHANGES);
}

// Potvrzení dokončení skriptu
alert("Skript byl úspěšně dokončen!");