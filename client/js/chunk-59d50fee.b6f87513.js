(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-59d50fee"],{"99d9":function(t,a,n){"use strict";n.d(a,"a",(function(){return c})),n.d(a,"b",(function(){return s})),n.d(a,"c",(function(){return u}));var e=n("b0af"),r=n("80d2"),c=Object(r["i"])("v-card__actions"),i=Object(r["i"])("v-card__subtitle"),s=Object(r["i"])("v-card__text"),u=Object(r["i"])("v-card__title");e["a"]},f28a:function(t,a,n){"use strict";n.r(a);var e=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("v-container",[n("v-row",[n("v-col",{attrs:{cols:"12",xs:"8",md:"8"}},[t.success?n("v-card",{staticClass:"mx-auto",attrs:{width:"600"}},[n("v-card-text",[t._v(" Ваша почта успешно активирована ")])],1):t._e()],1)],1)],1)},r=[],c={name:"EmailConfirm",data:function(){return{success:!1}},mounted:function(){var t=this;this.$store.dispatch("auth/emailConfirm",{uid:this.$route.params.uid,token:this.$route.params.token}).then((function(){t.success=!0,t.$router.push("/login")}))}},i=c,s=n("2877"),u=n("6544"),o=n.n(u),d=n("b0af"),f=n("99d9"),l=n("62ad"),v=n("a523"),b=n("0fd9"),h=Object(s["a"])(i,e,r,!1,null,"639f641a",null);a["default"]=h.exports;o()(h,{VCard:d["a"],VCardText:f["b"],VCol:l["a"],VContainer:v["a"],VRow:b["a"]})}}]);
//# sourceMappingURL=chunk-59d50fee.b6f87513.js.map