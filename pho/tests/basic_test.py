import re
import unittest

from pho.models import Pho

html = """
<!DOCTYPE html>
<html>
  <meta charset='utf-8'>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="apple-mobile-web-app-capable" content="yes">

<meta property="fb:page_id" content="494540977223862" />

<meta name="description" content="Stylr is a location based fashion application.">
<meta name="keywords" content="stylr,local,shop,fashion,application">

<title>Stylr</title>
<meta property="og:title" content="Stylr" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Stylr" />
<meta property="og:description" content="Stylr is a location based fashion application." />
<meta property="og:url" content="stylr.com" />
<meta property="og:image" content="" />

  <head>
  </head>
  <body>
    <!-- Begin LaunchRock Widget -->
    <div id="lr-widget" rel="MZRDFXDB"></div>
    <script type="text/javascript" src="//ignition.launchrock.com/ignition-current.min.js"></script>
    <!-- End LaunchRock Widget -->
    <select name="ddlSize" onchange="javascript:setTimeout('__doPostBack(\'ddlSize\',\'\')', 0)" id="ddlSize" style="width:93px;height:18px;border:1px solid #989898;font:10px Verdana;border-color:#989898;">
			<option value="Choose Size">Choose Size</option>
			<option value="2">XS</option>
			<option selected="selected" value="3">S</option>
			<option value="4">M</option>
			<option value="5">L</option>
		</select>
    <div class='foo'>
      <div class='bar'> 
        <div class='bar'> 
        </div>
        <div class='bar'> 
        </div>
      </div>
    </div>
    <td width="165" valign="top" style="padding:8px 0 7px 7px;border-right:1px solid #ebe7e4">
      <strong>Address</strong><br>
      429 Broadway (at Howard, 1blk N of Canal)<br>
        New York, NY 10013<br>
      Tel. (212) 925-0560
    </td>
    <li class="swatch button selected lastRow last selected" id="swatchList_18578-400" title="BLUE" data-color-id="18578" data-photo-group-id="7565648"><div class="swatch">
      <a href="javascript:void(0);" tabindex="0"><img alt="Color List having 1 item BLUEBLUE" title="BLUE" src="http://g-lvl3.nordstromimage.com/imagegallery/store/product/SwatchSmall/1/_7565501.jpg" /></a>
      </div><label>BLUE</label>
    </li>
  </body>
</html>
"""

clean_html = """
<select>
  <option>Choose Size</option>
  <option>XS</option>
  <option>S</option>
  <option>M</option>
  <option>L</option>
</select>
""".strip()

class TestPho(unittest.TestCase):
    def test_basic(self):
        self.assertEquals('Stylr', Pho(html).find('title').get_text())

    def test_non_recursive(self):
        parent = Pho(html).find('div', {'class': 'foo'})
        self.assertEquals(3, len(parent.find_all('div', {'class': 'bar'})))
        self.assertEquals(1, len(parent.find_all('div',
            attrs={'class': 'bar'},
            recursive=False,
            )))

    def test_attribute(self):
        self.assertEquals('MZRDFXDB', Pho(html).find('div', {'id': 'lr-widget'})['rel'])

    def test_regex(self):
        self.assertEquals('MZRDFXDB',
                Pho(html).find('div', {'id': re.compile('lr')})['rel'])

    def test_regex_complex(self):
        self.assertEquals('BLUE', Pho(html).find('li', {'id': re.compile(r'swatchList_.+')}).get('title'))
        self.assertEquals(None, Pho(html).find('li', {'id': re.compile(r'swatsdfsdchList_.+')}))

    def test_multi_select(self):
        select = Pho(html).find('select', {'name': 'ddlSize'})
        self.assertEquals(5, len(select.find_all('option')))

    def test_clean_node(self):
        node = Pho(html).find('select', {'name': 'ddlSize'})
        self.assertEquals(clean_html, str(node.clean_node()).strip())

if __name__ == "__main__":
    unittest.main()
