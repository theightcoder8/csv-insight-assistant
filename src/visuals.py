<!DOCTYPE html>
<!-- saved from url=(0037)http://localhost:8888/edit/visuals.py -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style>body {transition: opacity ease-in 0.2s; } 
body[unresolved] {opacity: 0; display: block; overflow: hidden; position: relative; } 
</style>
    

    <title>visuals.py - Jupyter Text Editor</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon-file.ico?v=f9f0a782d7d67b3a57bf7dce251d771b405c7890604576ec8b9a621a39d7670f6b43ffabef1e566f1cd741ee302e15977d9e1cf60bbacebafe75787b9916415c">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./visuals.py - Jupyter Text Editor_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./visuals.py - Jupyter Text Editor_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="./visuals.py - Jupyter Text Editor_files/codemirror.css">
<link rel="stylesheet" href="./visuals.py - Jupyter Text Editor_files/dialog.css">

    <link rel="stylesheet" href="./visuals.py - Jupyter Text Editor_files/style.min.css" type="text/css">
    

    <link rel="stylesheet" href="./visuals.py - Jupyter Text Editor_files/custom.css" type="text/css">
    <script src="./visuals.py - Jupyter Text Editor_files/promise.min.js" type="text/javascript" charset="utf-8"></script>
    <script src="./visuals.py - Jupyter Text Editor_files/react.production.min.js" type="text/javascript"></script>
    <script src="./visuals.py - Jupyter Text Editor_files/react-dom.production.min.js" type="text/javascript"></script>
    <script src="./visuals.py - Jupyter Text Editor_files/index.js" type="text/javascript"></script>
    <script src="./visuals.py - Jupyter Text Editor_files/require.js" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20250609031451",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/dist/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

      // error-catching custom-preload.js shim.
      define("custom-preload", function (require, exports, module) {
          try {
              var custom = require('custom/custom-preload');
              console.debug('loaded custom-preload.js');
              return custom;
          } catch (e) {
              console.error("error loading custom-preload.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./visuals.py - Jupyter Text Editor_files/contents.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom-preload" src="./visuals.py - Jupyter Text Editor_files/custom-preload.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./visuals.py - Jupyter Text Editor_files/custom.js"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="codemirror/mode/python/python" src="./visuals.py - Jupyter Text Editor_files/python.js"></script></head>

<body class="edit_app " data-base-url="/" data-file-path="visuals.py" data-jupyter-api-token="f947e654c8095738ab69dc9a10df1d10d61d47f179844b15" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="newsId" style="display: none">
    
    <div class="alert alert-info" role="alert">
      <div style="display: flex">
        <div>
          <span class="label label-warning">UPDATE</span>
          Read <a href="https://jupyter-notebook.readthedocs.io/en/latest/migrate_to_notebook7.html" style="text-decoration: underline;" target="_blank">the migration plan</a> to Notebook 7 to learn about the new features and the actions to take if you are using extensions
          -
          Please note that updating to Notebook 7 might break some of your extensions.
        </div>
        <div style="margin-left: auto;">
          <a href="http://localhost:8888/edit/visuals.py" onclick="alert(&#39;This message will not be shown anymore.&#39;); return false;">
            <button type="button" class="btn btn-default btn-xs" id="dontShowId">
              Don't show anymore
            </button>
          </a>
        </div>
      </div>
    </div>
    
  </div>
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=f947e654c8095738ab69dc9a10df1d10d61d47f179844b15" title="dashboard">
      <img src="./visuals.py - Jupyter Text Editor_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename">visuals.py</span>
    <div class="dirty-indicator-clean" title="No changes to save"></div><span class="last_modified" title="Mon, Jun 9, 2025 3:36 AM">a minute ago</span>
</span>


  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p class="navbar-text indicator_area">
          <span id="current-mode" title="The current language is Python">Python</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"><div id="notification_save" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="http://localhost:8888/edit/visuals.py#" class="dropdown-toggle" data-toggle="dropdown">File</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="http://localhost:8888/edit/visuals.py#">New</a></li>
                <li id="save-file"><a href="http://localhost:8888/edit/visuals.py#">Save</a></li>
                <li id="rename-file"><a href="http://localhost:8888/edit/visuals.py#">Rename</a></li>
                <li id="download-file"><a href="http://localhost:8888/edit/visuals.py#">Download</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8888/edit/visuals.py#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="http://localhost:8888/edit/visuals.py#">Find</a></li>
                <li id="menu-replace"><a href="http://localhost:8888/edit/visuals.py#">Find &amp; Replace</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Key Map</li>
                <li id="menu-keymap-default"><a href="http://localhost:8888/edit/visuals.py#">Default<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="http://localhost:8888/edit/visuals.py#">Sublime Text<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="http://localhost:8888/edit/visuals.py#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs" class="selected-keymap"><a href="http://localhost:8888/edit/visuals.py#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8888/edit/visuals.py#" class="dropdown-toggle" data-toggle="dropdown">View</a>
              <ul id="view-menu" class="dropdown-menu">
              <li id="toggle_header" title="Show/Hide the logo and notebook title (above menu bar)">
              <a href="http://localhost:8888/edit/visuals.py#">Toggle Header</a></li>
              <li id="menu-line-numbers"><a href="http://localhost:8888/edit/visuals.py#">Toggle Line Numbers</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8888/edit/visuals.py#" class="dropdown-toggle" data-toggle="dropdown">Language</a>
              <ul id="mode-menu" class="dropdown-menu">
              <li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to APL">APL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to PGP">PGP</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to ASN.1">ASN.1</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Asterisk">Asterisk</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Brainfuck">Brainfuck</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to C">C</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to C++">C++</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Cobol">Cobol</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to C#">C#</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Clojure">Clojure</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to ClojureScript">ClojureScript</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Closure Stylesheets (GSS)">Closure Stylesheets (GSS)</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to CMake">CMake</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to CoffeeScript">CoffeeScript</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Common Lisp">Common Lisp</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Cypher">Cypher</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Cython">Cython</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Crystal">Crystal</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to CSS">CSS</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to CQL">CQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to D">D</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Dart">Dart</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to diff">diff</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Django">Django</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Dockerfile">Dockerfile</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to DTD">DTD</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Dylan">Dylan</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to EBNF">EBNF</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to ECL">ECL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to edn">edn</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Eiffel">Eiffel</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Elm">Elm</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Embedded Javascript">Embedded Javascript</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Embedded Ruby">Embedded Ruby</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Erlang">Erlang</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Esper">Esper</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Factor">Factor</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to FCL">FCL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Forth">Forth</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Fortran">Fortran</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to F#">F#</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Gas">Gas</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Gherkin">Gherkin</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to GitHub Flavored Markdown">GitHub Flavored Markdown</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Go">Go</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Groovy">Groovy</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to HAML">HAML</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Haskell">Haskell</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Haskell (Literate)">Haskell (Literate)</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Haxe">Haxe</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to HXML">HXML</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to ASP.NET">ASP.NET</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to HTML">HTML</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to HTTP">HTTP</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to IDL">IDL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Pug">Pug</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Java">Java</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Java Server Pages">Java Server Pages</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to JavaScript">JavaScript</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to JSON">JSON</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to JSON-LD">JSON-LD</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to JSX">JSX</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Jinja2">Jinja2</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Julia">Julia</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Kotlin">Kotlin</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to LESS">LESS</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to LiveScript">LiveScript</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Lua">Lua</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Markdown">Markdown</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to mIRC">mIRC</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to MariaDB SQL">MariaDB SQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Mathematica">Mathematica</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Modelica">Modelica</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to MUMPS">MUMPS</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to MS SQL">MS SQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to mbox">mbox</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to MySQL">MySQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Nginx">Nginx</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to NSIS">NSIS</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to NTriples">NTriples</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Objective-C">Objective-C</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Objective-C++">Objective-C++</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to OCaml">OCaml</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Octave">Octave</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Oz">Oz</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Pascal">Pascal</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to PEG.js">PEG.js</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Perl">Perl</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to PHP">PHP</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Pig">Pig</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Plain Text">Plain Text</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to PLSQL">PLSQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to PostgreSQL">PostgreSQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to PowerShell">PowerShell</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Properties files">Properties files</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to ProtoBuf">ProtoBuf</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Python">Python</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Puppet">Puppet</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Q">Q</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to R">R</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to reStructuredText">reStructuredText</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to RPM Changes">RPM Changes</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to RPM Spec">RPM Spec</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Ruby">Ruby</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Rust">Rust</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to SAS">SAS</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Sass">Sass</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Scala">Scala</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Scheme">Scheme</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to SCSS">SCSS</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Shell">Shell</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Sieve">Sieve</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Slim">Slim</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Smalltalk">Smalltalk</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Smarty">Smarty</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Solr">Solr</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to SML">SML</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Soy">Soy</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to SPARQL">SPARQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Spreadsheet">Spreadsheet</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to SQL">SQL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to SQLite">SQLite</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Squirrel">Squirrel</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Stylus">Stylus</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Swift">Swift</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to sTeX">sTeX</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to LaTeX">LaTeX</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to SystemVerilog">SystemVerilog</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Tcl">Tcl</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Textile">Textile</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to TiddlyWiki">TiddlyWiki</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Tiki wiki">Tiki wiki</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to TOML">TOML</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Tornado">Tornado</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to troff">troff</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to TTCN">TTCN</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to TTCN_CFG">TTCN_CFG</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Turtle">Turtle</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to TypeScript">TypeScript</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to TypeScript-JSX">TypeScript-JSX</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Twig">Twig</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Web IDL">Web IDL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to VB.NET">VB.NET</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to VBScript">VBScript</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Velocity">Velocity</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Verilog">Verilog</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to VHDL">VHDL</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Vue.js Component">Vue.js Component</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to XML">XML</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to XQuery">XQuery</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Yacas">Yacas</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to YAML">YAML</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to Z80">Z80</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to mscgen">mscgen</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to xu">xu</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to msgenny">msgenny</a></li><li><a href="http://localhost:8888/edit/visuals.py#" title="Set language to WebAssembly">WebAssembly</a></li></ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site" style="display: block; height: 906.43px;">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"><div class="CodeMirror cm-s-ipython CodeMirror-wrap" style="height: 866.43px;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59375px; left: 38px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="bottom: 0px;"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 34px; margin-bottom: -15px; border-right-width: 35px; min-height: 215px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre><div class="CodeMirror-linenumber CodeMirror-gutter-elt"><div>12</div></div></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 17px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">matplotlib</span>.<span class="cm-property">pyplot</span> <span class="cm-keyword">as</span> <span class="cm-variable">plt</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">plot_bar</span>(<span class="cm-variable">data</span>, <span class="cm-variable">title</span>, <span class="cm-variable">xlabel</span>, <span class="cm-variable">ylabel</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">figure</span>(<span class="cm-variable">figsize</span><span class="cm-operator">=</span>(<span class="cm-number">10</span>, <span class="cm-number">6</span>))</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">data</span>.<span class="cm-property">plot</span>(<span class="cm-variable">kind</span><span class="cm-operator">=</span><span class="cm-string">'bar'</span>, <span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">'skyblue'</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">6</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">title</span>(<span class="cm-variable">title</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">7</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">xlabel</span>(<span class="cm-variable">xlabel</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">8</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">ylabel</span>(<span class="cm-variable">ylabel</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">9</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">xticks</span>(<span class="cm-variable">rotation</span><span class="cm-operator">=</span><span class="cm-number">45</span>, <span class="cm-variable">ha</span><span class="cm-operator">=</span><span class="cm-string">'right'</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">10</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">tight_layout</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">11</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">grid</span>(<span class="cm-keyword">True</span>, <span class="cm-variable">linestyle</span><span class="cm-operator">=</span><span class="cm-string">'--'</span>, <span class="cm-variable">alpha</span><span class="cm-operator">=</span><span class="cm-number">0.6</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">12</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"> &nbsp; &nbsp;<span class="cm-variable">plt</span>.<span class="cm-property">show</span>()</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 35px; width: 1px; border-bottom: 0px solid transparent; top: 215px;"></div><div class="CodeMirror-gutters" style="height: 250px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 33px;"></div></div></div></div></div>
</div>


</div>






    


<script src="./visuals.py - Jupyter Text Editor_files/main.min.js" type="text/javascript" charset="utf-8"></script>


<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
  sys_info = {"notebook_version": "6.5.4", "notebook_path": "/Users/theightcoder/anaconda3/lib/python3.11/site-packages/notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]", "sys_executable": "/Users/theightcoder/anaconda3/bin/python", "sys_platform": "darwin", "platform": "macOS-15.4.1-arm64-arm-64bit", "os_name": "posix", "default_encoding": "utf-8"};
  document.addEventListener('DOMContentLoaded', function () {
    const newsId = document.querySelector('#newsId');
    const dontShowId = document.querySelector('#dontShowId');
    const showNotebookNews = localStorage.getItem('showNotebookNews');
    dontShowId.addEventListener('click', () => {
      localStorage.setItem('showNotebookNews', false);
      newsId.style.display = 'none';
    });
    if (!showNotebookNews) newsId.style.display = 'inline';
  });
</script>


<veepn-guard-alert><template shadowrootmode="open"><style>html{box-sizing:border-box;text-size-adjust:100%;word-break:normal;-moz-tab-size:4;tab-size:4}*,:before,:after{background-repeat:no-repeat;box-sizing:border-box}:before,:after{text-decoration:inherit;vertical-align:inherit}*{padding:0;margin:0}hr{overflow:visible;height:0;color:inherit;border:0;border-top:1px solid}details,main{display:block}summary{display:list-item}small{font-size:80%}[hidden]{display:none}abbr[title]{border-bottom:none;text-decoration:underline;text-decoration:underline dotted}a{background-color:transparent}a:active,a:hover{outline-width:0}code,kbd,pre,samp{font-family:monospace}pre{font-size:1em}b,strong{font-weight:bolder}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}table{border-color:inherit;text-indent:0}iframe{border-style:none}input{border-radius:0}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;-moz-appearance:textfield;appearance:textfield;outline-offset:-2px}[type=search]::-webkit-search-decoration{-webkit-appearance:none;-moz-appearance:none;appearance:none}textarea{overflow:auto;resize:vertical}button,input,optgroup,select,textarea{font:inherit;color:inherit}optgroup{font-weight:700}button{overflow:visible}button,select{text-transform:none}button,[type=button],[type=reset],[type=submit],[role=button]{cursor:pointer}button::-moz-focus-inner,[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner{border-style:none;padding:0}button,html [type=button],[type=reset],[type=submit]{-webkit-appearance:button;-moz-appearance:button;appearance:button}button,input,select,textarea{background-color:transparent;border-style:none}button:-moz-focusring,[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner{outline:1px dotted ButtonText}select{-webkit-appearance:none;-moz-appearance:none;appearance:none}a:focus,button:focus,input:focus,select:focus,textarea:focus{outline-width:0}select::-ms-expand{display:none}select::-ms-value{color:currentcolor}legend{border:0;color:inherit;display:table;white-space:normal;max-width:100%}::-webkit-file-upload-button{-webkit-appearance:button;-moz-appearance:button;appearance:button;color:inherit;font:inherit}[disabled]{cursor:default}img{border-style:none}progress{vertical-align:baseline}[aria-busy=true]{cursor:progress}[aria-controls]{cursor:pointer}[aria-disabled=true]{cursor:default}ul,ol{list-style-type:none}figure{margin:0}.guard-popup{font-family:FigtreeVF,sans-serif;position:fixed;z-index:2147483638;top:8px;left:24px;overflow:visible;color:#222e3a;background-color:#fff;max-width:416px;width:calc(100% - 48px);border-radius:16px;box-shadow:0 4px 20px #00000040;padding:24px}.guard-popup__header{display:flex;justify-content:space-between;align-items:center;column-gap:16px;margin-bottom:24px}.guard-popup__close{display:flex;align-items:center;justify-content:center;width:24px;height:24px;opacity:.7}.guard-popup__img{line-height:0;margin-bottom:24px}.guard-popup__img img{width:100%;aspect-ratio:368/142;object-fit:cover;border-radius:12px;overflow:hidden}.guard-popup__title{font-size:24px;line-height:32px;margin-bottom:8px}.guard-popup__description{font-size:20px;line-height:28px;font-weight:500;color:#4a5764;margin-bottom:28px}.guard-popup__actions{display:flex;justify-content:flex-end;column-gap:16px}.guard-popup__btn{display:flex;align-items:center;justify-content:center;padding:8px 16px;border-radius:5px;font-size:16px;line-height:24px;font-weight:700;cursor:pointer;color:#fff;background:linear-gradient(180deg,#5695fd,#1554ff)}</style></template><style>@font-face{font-family:FigtreeVF;src:url(chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/fonts/FigtreeVF.woff2) format("woff2 supports variations"),url(chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/fonts/FigtreeVF.woff2) format("woff2-variations");font-weight:100 1000;font-display:swap}</style></veepn-guard-alert><veepn-lock-screen><template shadowrootmode="open"><style>html{box-sizing:border-box;text-size-adjust:100%;word-break:normal;-moz-tab-size:4;tab-size:4}*,:before,:after{background-repeat:no-repeat;box-sizing:border-box}:before,:after{text-decoration:inherit;vertical-align:inherit}*{padding:0;margin:0}hr{overflow:visible;height:0;color:inherit;border:0;border-top:1px solid}details,main{display:block}summary{display:list-item}small{font-size:80%}[hidden]{display:none!important}abbr[title]{border-bottom:none;text-decoration:underline;text-decoration:underline dotted}a{background-color:transparent}a:active,a:hover{outline-width:0}code,kbd,pre,samp{font-family:monospace}pre{font-size:1em}b,strong{font-weight:bolder}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}table{border-color:inherit;text-indent:0}iframe{border-style:none}input{border-radius:0}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;-moz-appearance:textfield;appearance:textfield;outline-offset:-2px}[type=search]::-webkit-search-decoration{-webkit-appearance:none;-moz-appearance:none;appearance:none}textarea{overflow:auto;resize:vertical}button,input,optgroup,select,textarea{font:inherit;color:inherit}optgroup{font-weight:700}button{overflow:visible}button,select{text-transform:none}button,[type=button],[type=reset],[type=submit],[role=button]{cursor:pointer}button::-moz-focus-inner,[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner{border-style:none;padding:0}button,html [type=button],[type=reset],[type=submit]{-webkit-appearance:button;-moz-appearance:button;appearance:button}button,input,select,textarea{background-color:transparent;border-style:none}button:-moz-focusring,[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner{outline:1px dotted ButtonText}select{-webkit-appearance:none;-moz-appearance:none;appearance:none}a:focus,button:focus,input:focus,select:focus,textarea:focus{outline-width:0}select::-ms-expand{display:none}select::-ms-value{color:currentcolor}legend{border:0;color:inherit;display:table;white-space:normal;max-width:100%}::-webkit-file-upload-button{-webkit-appearance:button;-moz-appearance:button;appearance:button;color:inherit;font:inherit}[disabled]{cursor:default}img{border-style:none}progress{vertical-align:baseline}[aria-busy=true]{cursor:progress}[aria-controls]{cursor:pointer}[aria-disabled=true]{cursor:default}ul,ol{list-style-type:none}figure{margin:0}.lock-screen{font-family:FigtreeVF,sans-serif;letter-spacing:normal;position:fixed;z-index:2147483638;top:0;right:0;bottom:0;left:0;padding:32px 40px;color:#222e3a;background-color:#fdfdfd;display:flex;flex-direction:column;row-gap:12px;overflow:auto;background-image:radial-gradient(circle at 0% 0%,#e6fffdcc,#e6fffd00 50%),radial-gradient(circle at 100% 0%,#ebfffecc,#ebfffe00 50%),radial-gradient(circle at 100% 100%,#f0f5ffcc,#f0f5ff00 50%),radial-gradient(circle at 0% 100%,#f2f2ffcc,#f2f2ff00 50%),radial-gradient(circle at 50% 50%,#fff,#fffc,#f5f5ff66,#f0f0ff33,#f0f0ff00),linear-gradient(to bottom right,#e6fffd,#f2f2ff);background-size:100% 100%;background-repeat:no-repeat}.lock-screen__header{display:flex;align-items:center;justify-content:space-between}.lock-screen__logo{display:inline-flex;align-items:center;column-gap:12px;font-size:18px;font-weight:600}.lock-screen__close{display:flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background-color:#222e3a1a}.lock-screen__main{flex-grow:1;align-content:center}.lock-screen__container{max-width:1120px;margin-inline:auto;display:flex;align-items:center;gap:24px}@media (width < 972px){.lock-screen__container{flex-direction:column}}.lock-screen__timer{display:flex;align-items:center;justify-content:center;width:100%}.lock-screen__content{width:100%}.lock-screen__title{font-size:48px;font-weight:700;line-height:56px;margin-bottom:16px}.lock-screen__description{font-size:18px;line-height:32px;margin-bottom:24px}.lock-screen__actions{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}.lock-screen__action{height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;text-align:center;padding:8px 24px}.upgrade-btn{color:#fff;background:linear-gradient(180deg,#20df9e,#13cf8f)}.skip-btn{color:#3066ff;border-width:1px;border-style:solid;border-color:#3066ff;position:relative}.skip-btn__tooltip{font-size:14px;line-height:24px;font-weight:400;position:absolute;z-index:1;left:50%;top:calc(100% + 18px);padding:8px 12px;color:#fff;border:1px solid #4a5764;background-color:#222e3a;border-radius:8px;width:max-content;pointer-events:none;animation:slide-in .6s ease-in-out forwards}@keyframes slide-in{0%{opacity:0;transform:translate(-50%,-100%)}to{opacity:1;transform:translate(-50%)}}.skip-btn__tooltip:after{content:"";display:block;position:absolute;z-index:1;top:-8px;left:50%;width:0;height:0;border-style:solid;border-width:0 8px 8px;border-color:transparent transparent #222e3a;transform:translate(-6px)}.skip-btn__icon{display:none}.skip-btn:disabled{cursor:not-allowed}.skip-btn:disabled .skip-btn__tooltip,.skip-btn:disabled .skip-btn__text{display:none}.skip-btn:disabled .skip-btn__icon{display:initial;animation:tick-tock .8s steps(8,end) infinite}@keyframes tick-tock{to{transform:rotate(360deg)}}.timer{position:relative;max-width:422px;width:100%;aspect-ratio:1/1;border-radius:50%;background-color:#fff;box-shadow:0 0 40px #2b374114;display:flex;align-items:center;justify-content:center;pointer-events:none;-webkit-user-select:none;user-select:none}.timer__circle-backward{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:0;max-width:100%;height:auto;opacity:.4}.timer__circle-forward{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(45deg);z-index:1;max-width:100%;height:auto;animation:sector 5s linear forwards}.timer__fire-icon{position:absolute;top:22%;left:50%;transform:translate(-50%);z-index:2}.timer__text{font-size:clamp(18px,10vw,88px);letter-spacing:-1px;text-align:center;font-variant-numeric:tabular-nums;position:relative;z-index:3}.timer--finished .timer__text{color:#98a0a9}.timer--finished .timer__circle-forward{display:none}@keyframes sector{0%{clip-path:polygon(50% 50%,0% 2%,100% 0%,100% 100%,0% 100%,0% 2%)}25%{clip-path:polygon(50% 50%,0% 2%,100% 0%,100% 100%,0% 100%,0% 100%)}25.000001%{clip-path:polygon(50% 50%,0% 2%,100% 0%,100% 100%,0% 100%)}50%{clip-path:polygon(50% 50%,0% 2%,100% 0%,100% 100%,100% 100%)}50.000001%{clip-path:polygon(50% 50%,0% 2%,100% 0%,100% 100%)}75%{clip-path:polygon(50% 50%,0% 2%,100% 0%,100% 0%)}75.000001%{clip-path:polygon(50% 50%,0% 2%,100% 0%)}to{clip-path:polygon(50% 50%,0% 2%,0% 0%)}}@media (prefers-color-scheme: dark){.lock-screen{color:#fff;background-image:radial-gradient(circle at 0% 0%,#2f4f4fcc,#2f4f4f00 50%),radial-gradient(circle at 100% 0%,#193042cc,#19304200 50%),radial-gradient(circle at 100% 100%,#1c3041cc,#1c304100 50%),radial-gradient(circle at 0% 100%,#1b263bcc,#1b263b00 50%),radial-gradient(circle at 50% 50%,#141e28,#141e28cc,#1b263b66,#1c304133,#1c304100),linear-gradient(to bottom right,#2f4f4f,#1b263b)}.lock-screen__close{background-color:#ffffff1a}.skip-btn{color:#fff;border-color:#fff}.skip-btn__tooltip{color:#222e3a;border:1px solid #f5f6f7;background-color:#fff}.skip-btn__tooltip:after{border-color:transparent transparent #fff}.timer{background-color:#191b25}.timer__circle-backward{opacity:1}.timer--finished .timer__text{color:#5c6977}}</style></template><style>@font-face{font-family:FigtreeVF;src:url(chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/fonts/FigtreeVF.woff2) format("woff2 supports variations"),url(chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/fonts/FigtreeVF.woff2) format("woff2-variations");font-weight:100 1000;font-display:swap}</style></veepn-lock-screen></body></html>