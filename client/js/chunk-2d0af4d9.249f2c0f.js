(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0af4d9"],{"0e6d":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",{attrs:{fluid:""}},[0===t.paginatedItems.length?a("div",{staticClass:"d-flex align-center justify-center"},[a("p",{staticClass:"text-center text-h6 font-weight-light mt-10"},[t._v(" Поиск не дал результатов. Попробуйте вводить что нибудь другое ")])]):t._e(),t.paginatedItems.length>0?a("v-row",t._l(t.paginatedItems,(function(t){return a("v-col",{key:t.id,attrs:{cols:"12",sm:"4",md:"3"}},[a("BookMedia",{attrs:{book:t}})],1)})),1):t._e(),t.paginatedItems.length>0?a("div",{staticClass:"text-center"},[a("v-pagination",{attrs:{length:Math.ceil(this.book.books.length/this.perPage),"total-visible":7},model:{value:t.page,callback:function(e){t.page=e},expression:"page"}})],1):t._e()],1)},i=[],o=(a("fb6a"),a("5530")),s=a("66ec"),c=a("2f62"),l={name:"BookList",data:function(){return{page:1,perPage:20}},components:{BookMedia:s["a"]},computed:Object(o["a"])(Object(o["a"])({},Object(c["b"])(["book"])),{},{paginatedItems:function(){return this.book.books.slice((this.page-1)*this.perPage,this.page*this.perPage)}})},r=l,p=a("2877"),d=a("6544"),g=a.n(d),u=a("62ad"),h=a("a523"),b=a("891e"),f=a("0fd9"),k=Object(p["a"])(r,n,i,!1,null,"5ed169a7",null);e["default"]=k.exports;g()(k,{VCol:u["a"],VContainer:h["a"],VPagination:b["a"],VRow:f["a"]})}}]);
//# sourceMappingURL=chunk-2d0af4d9.249f2c0f.js.map