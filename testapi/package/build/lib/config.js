"use strict";function _interopRequireDefault(e){return e&&e.__esModule?e:{"default":e}}Object.defineProperty(exports,"__esModule",{value:!0});var _classCallCheck2=require("babel-runtime/helpers/classCallCheck"),_classCallCheck3=_interopRequireDefault(_classCallCheck2),_path=require("path"),_path2=_interopRequireDefault(_path),Config=function e(t){(0,_classCallCheck3["default"])(this,e);var s="win32"===t.platform,l=t.env[s?"USERPROFILE":"HOME"];this.registry=t.env.ACE_REGISTRY||"https://registry.npmjs.org/",this.cacheDir=t.env.ACE_CACHE_DIR||_path2["default"].join(l,".ace_cache"),this.globalNodeModules=t.env.ACE_GLOBAL_NODE_MODULES||_path2["default"].join(l,".node_modules"),this.globalBin=t.env.ACE_GLOBAL_BIN||_path2["default"].resolve(t.execPath,".."),this.httpProxy=t.env.ACE_HTTP_PROXY||t.env.HTTP_PROXY||null,this.httpsProxy=t.env.ACE_HTTPS_PROXY||t.env.HTTPS_PROXY||null,this.requestRetries=parseInt(t.env.ACE_REQUEST_RETRIES,10)||5,this.sh=t.env.ACE_SH||(s?t.env.comspec||"cmd":"sh"),this.shFlag=t.env.ACE_SH_FLAG||(s?"/d /s /c":"-c"),this.symlinkType=s?"junction":"file"};exports["default"]=new Config(process);