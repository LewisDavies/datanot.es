Title: Toggle Code in Jupyter Notebooks
Slug: tips-and-tricks/toggle-code-in-jupyter-notebooks
Category: Tips & Tricks
Tags: display_html, print 
Date: 2017-09-25
Modified: 2018-10-13

#### Import libraries and Add Toggle 


```python
import IPython.core.display as di
di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)
di.display_html('''<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Toggle code</button>''', raw=True)
```


<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>



<button onclick="jQuery('.input_area').toggle(); jQuery('.prompt').toggle();">Toggle code</button>


Although the button doesn't work in this window, add it to an Jupyter notebook and you can show or hide your code.

This is great when you export your notebook as an HTML file with the results front and centre, but still want to give people the option to peek under the hood!
