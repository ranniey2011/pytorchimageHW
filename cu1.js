const fs = require('fs');

// Get filename from command line arguments
const args = process.argv.slice(2);
if (args.length !== 1) {
  console.error('Usage: node script.js --input=filename.json');
  process.exit(1);
}
const inputFilename = args[0].split('=')[1];

// Set output filename
const outputFilename = `${inputFilename.split('.')[0]}_cu.json`;

// Read the specified input file
fs.readFile(inputFilename, 'utf8', (err, data) => {
  if (err) {
    console.error(`Error reading ${inputFilename}:`, err);
    return;
  }

  try {
    const imageUrlData = JSON.parse(data);

    // Filter out URLs that don't start with "https"
    const cleanedImageData = {};
    Object.keys(imageUrlData).forEach((key) => {
      cleanedImageData[key] = imageUrlData[key].filter((url) => url.startsWith('https'));
    });

    // Write filtered data to the output file
    fs.writeFile(outputFilename, JSON.stringify(cleanedImageData, null, 2), 'utf8', (err) => {
      if (err) {
        console.error(`Error writing ${outputFilename}:`, err);
        return;
      }
      console.log(`Filtered URLs saved to ${outputFilename}`);
    });
  } catch (parseError) {
    console.error(`Error parsing JSON from ${inputFilename}:`, parseError);
  }
});
