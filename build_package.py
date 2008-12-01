import zipfile

PACKAGE_FILENAME = 'youtube.gg'

FILES = [
  'constants.js',
  'details.js',
  'details.xml',
  'gadget.gmanifest',
  'icon24_youtube.png',
  'icon32_youtube.png',
  'main.js',
  'main.xml',
  'options.js',
  'profile.js',
  'simple_http_request.js',
  'utils.js',
  'version_checker.js',
  'youtube.js',
  'en/strings.xml',
  'images/details/bottom.png',
  'images/details/bottom_left.png',
  'images/details/bottom_right.png',
  'images/details/center.png',
  'images/details/close_default.png',
  'images/details/close_down.png',
  'images/details/close_hover.png',
  'images/details/left.png',
  'images/details/right.png',
  'images/details/star_empty.png',
  'images/details/star_full.png',
  'images/details/star_half.png',
  'images/details/top.png',
  'images/details/top_left.png',
  'images/details/top_right.png',
  'images/main/bottom.png',
  'images/main/bottom_left.png',
  'images/main/bottom_right.png',
  'images/main/dropdown_bottom.png',
  'images/main/dropdown_right.png',
  'images/main/drop_arrow.png',
  'images/main/left.png',
  'images/main/logo.png',
  'images/main/right.png',
  'images/main/scrollbar.png',
  'images/main/scrollbar_track.png',
  'images/main/search_close.png',
  'images/main/search_close_hover.png',
  'images/main/search_left.png',
  'images/main/search_middle.png',
  'images/main/search_right.png',
  'images/main/top.png',
  'images/main/top_left.png',
  'images/main/top_right.png',
]

package = zipfile.ZipFile(PACKAGE_FILENAME, 'w',
    compression=zipfile.ZIP_DEFLATED)
for file in FILES:
  print file
  package.write(file)
package.close()

print
print PACKAGE_FILENAME
