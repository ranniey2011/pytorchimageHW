const fs = require('fs');
const { argv } = require('process');

// Check if input file argument is provided
if (argv.length < 3) {
  console.error('Please provide input file name as argument.');
  process.exit(1);
}

// Get input file name from command line argument
const inputFileName = argv[2];

// Check if input file argument is in correct format
if (!inputFileName.startsWith('--input=')) {
  console.error('Invalid input file format. Please provide input file name in format --input=filename.json');
  process.exit(1);
}

// Extract file name from input argument
const fileName = inputFileName.slice(8);

// Set output file name
const outputFileName = `${fileName.slice(0, fileName.lastIndexOf('.'))}_nf.json`;

// Read input file
fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(`Error reading ${fileName}:`, err);
    return;
  }

  try {
    const imageUrlData = JSON.parse(data);
    
    // Filter out URLs that don't start with "https" and don't contain "facebook"
    const cleanedImageData = {};
    Object.keys(imageUrlData).forEach(key => {
      cleanedImageData[key] = imageUrlData[key].filter(url => url.startsWith('https') && !url.includes('facebook'));
    });

    // Write filtered data to output file
    fs.writeFile(outputFileName, JSON.stringify(cleanedImageData, null, 2), 'utf8', (err) => {
      if (err) {
        console.error(`Error writing ${outputFileName}:`, err);
        return;
      }
      console.log(`Filtered URLs saved to ${outputFileName}`);
    });

  } catch (parseError) {
    console.error(`Error parsing JSON from ${fileName}:`, parseError);
  }
});
