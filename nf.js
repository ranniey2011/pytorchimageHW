const fs = require('fs');

// Read image_urls.json
fs.readFile('image_urls_clean.json', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading image_urls.json:', err);
    return;
  }

  try {
    const imageUrlData = JSON.parse(data);
    
    // Filter out URLs that don't start with "https" and don't contain "facebook"
    const cleanedImageData = {};
    Object.keys(imageUrlData).forEach(key => {
      cleanedImageData[key] = imageUrlData[key].filter(url => url.startsWith('https') && !url.includes('facebook'));
    });

    // Write filtered data to image_urls_clean.json
    fs.writeFile('image_urls_clean2.json', JSON.stringify(cleanedImageData, null, 2), 'utf8', (err) => {
      if (err) {
        console.error('Error writing image_urls_clean.json:', err);
        return;
      }
      console.log('Filtered URLs saved to image_urls_clean.json');
    });

  } catch (parseError) {
    console.error('Error parsing JSON from image_urls.json:', parseError);
  }
});
