(function (e) {
    function t(t) {
        for (var r, a, u = t[0], s = t[1], i = t[2], d = 0, h = []; d < u.length; d++) a = u[d], Object.prototype.hasOwnProperty.call(o, a) && o[a] && h.push(o[a][0]), o[a] = 0;
        for (r in s) Object.prototype.hasOwnProperty.call(s, r) && (e[r] = s[r]);
        f && f(t);
        while (h.length) h.shift()();
        return c.push.apply(c, i || []), n()
    }

    function n() {
        for (var e, t = 0; t < c.length; t++) {
            for (var n = c[t], r = !0, a = 1; a < n.length; a++) {
                var u = n[a];
                0 !== o[u] && (r = !1)
            }
            r && (c.splice(t--, 1), e = s(s.s = n[0]))
        }
        return e
    }

    var r = {}, a = {app: 0}, o = {app: 0}, c = [];

    function u(e) {
        return s.p + "js/" + ({}[e] || e) + "." + {
            "chunk-2d0e5e97": "095f52f7",
            "chunk-54f50b4e": "3b5fc0f6",
            "chunk-74781238": "983c41c6",
            "chunk-562b5199": "afc27bbf",
            "chunk-4fbd5345": "a6a10f8e",
            "chunk-5a33e234": "b3139c83",
            "chunk-2426a722": "43e2fc63",
            "chunk-2d0e5d25": "abb8e616",
            "chunk-6e19e8f7": "5919989b",
            "chunk-79ba1026": "682dbbf0",
            "chunk-a57e7254": "071758db"
        }[e] + ".js"
    }

    function s(t) {
        if (r[t]) return r[t].exports;
        var n = r[t] = {i: t, l: !1, exports: {}};
        return e[t].call(n.exports, n, n.exports, s), n.l = !0, n.exports
    }

    s.e = function (e) {
        var t = [], n = {
            "chunk-54f50b4e": 1,
            "chunk-74781238": 1,
            "chunk-562b5199": 1,
            "chunk-4fbd5345": 1,
            "chunk-5a33e234": 1,
            "chunk-2426a722": 1,
            "chunk-6e19e8f7": 1,
            "chunk-79ba1026": 1
        };
        a[e] ? t.push(a[e]) : 0 !== a[e] && n[e] && t.push(a[e] = new Promise((function (t, n) {
            for (var r = "css/" + ({}[e] || e) + "." + {
                "chunk-2d0e5e97": "31d6cfe0",
                "chunk-54f50b4e": "dcc009ac",
                "chunk-74781238": "2c9445f6",
                "chunk-562b5199": "e5a04aaf",
                "chunk-4fbd5345": "b62e84f4",
                "chunk-5a33e234": "8f03ff58",
                "chunk-2426a722": "e7188e40",
                "chunk-2d0e5d25": "31d6cfe0",
                "chunk-6e19e8f7": "e7188e40",
                "chunk-79ba1026": "db4c766e",
                "chunk-a57e7254": "31d6cfe0"
            }[e] + ".css", o = s.p + r, c = document.getElementsByTagName("link"), u = 0; u < c.length; u++) {
                var i = c[u], d = i.getAttribute("data-href") || i.getAttribute("href");
                if ("stylesheet" === i.rel && (d === r || d === o)) return t()
            }
            var h = document.getElementsByTagName("style");
            for (u = 0; u < h.length; u++) {
                i = h[u], d = i.getAttribute("data-href");
                if (d === r || d === o) return t()
            }
            var f = document.createElement("link");
            f.rel = "stylesheet", f.type = "text/css", f.onload = t, f.onerror = function (t) {
                var r = t && t.target && t.target.src || o,
                    c = new Error("Loading CSS chunk " + e + " failed.\n(" + r + ")");
                c.code = "CSS_CHUNK_LOAD_FAILED", c.request = r, delete a[e], f.parentNode.removeChild(f), n(c)
            }, f.href = o;
            var l = document.getElementsByTagName("head")[0];
            l.appendChild(f)
        })).then((function () {
            a[e] = 0
        })));
        var r = o[e];
        if (0 !== r) if (r) t.push(r[2]); else {
            var c = new Promise((function (t, n) {
                r = o[e] = [t, n]
            }));
            t.push(r[2] = c);
            var i, d = document.createElement("script");
            d.charset = "utf-8", d.timeout = 120, s.nc && d.setAttribute("nonce", s.nc), d.src = u(e);
            var h = new Error;
            i = function (t) {
                d.onerror = d.onload = null, clearTimeout(f);
                var n = o[e];
                if (0 !== n) {
                    if (n) {
                        var r = t && ("load" === t.type ? "missing" : t.type), a = t && t.target && t.target.src;
                        h.message = "Loading chunk " + e + " failed.\n(" + r + ": " + a + ")", h.name = "ChunkLoadError", h.type = r, h.request = a, n[1](h)
                    }
                    o[e] = void 0
                }
            };
            var f = setTimeout((function () {
                i({type: "timeout", target: d})
            }), 12e4);
            d.onerror = d.onload = i, document.head.appendChild(d)
        }
        return Promise.all(t)
    }, s.m = e, s.c = r, s.d = function (e, t, n) {
        s.o(e, t) || Object.defineProperty(e, t, {enumerable: !0, get: n})
    }, s.r = function (e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {value: "Module"}), Object.defineProperty(e, "__esModule", {value: !0})
    }, s.t = function (e, t) {
        if (1 & t && (e = s(e)), 8 & t) return e;
        if (4 & t && "object" === typeof e && e && e.__esModule) return e;
        var n = Object.create(null);
        if (s.r(n), Object.defineProperty(n, "default", {
            enumerable: !0,
            value: e
        }), 2 & t && "string" != typeof e) for (var r in e) s.d(n, r, function (t) {
            return e[t]
        }.bind(null, r));
        return n
    }, s.n = function (e) {
        var t = e && e.__esModule ? function () {
            return e["default"]
        } : function () {
            return e
        };
        return s.d(t, "a", t), t
    }, s.o = function (e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, s.p = "/", s.oe = function (e) {
        throw console.error(e), e
    };
    var i = window["webpackJsonp"] = window["webpackJsonp"] || [], d = i.push.bind(i);
    i.push = t, i = i.slice();
    for (var h = 0; h < i.length; h++) t(i[h]);
    var f = d;
    c.push([0, "chunk-vendors"]), n()
})({
    0: function (e, t, n) {
        e.exports = n("56d7")
    }, "56d7": function (e, t, n) {
        "use strict";
        n.r(t);
        var r = {};
        n.r(r), n.d(r, "namespaced", (function () {
            return re
        })), n.d(r, "state", (function () {
            return ae
        })), n.d(r, "mutations", (function () {
            return oe
        })), n.d(r, "actions", (function () {
            return ce
        })), n.d(r, "getters", (function () {
            return ue
        }));
        var a = {};
        n.r(a), n.d(a, "namespaced", (function () {
            return se
        })), n.d(a, "state", (function () {
            return ie
        })), n.d(a, "mutations", (function () {
            return de
        })), n.d(a, "actions", (function () {
            return he
        })), n.d(a, "getters", (function () {
            return fe
        }));
        var o = {};
        n.r(o), n.d(o, "namespaced", (function () {
            return le
        })), n.d(o, "state", (function () {
            return me
        })), n.d(o, "mutations", (function () {
            return pe
        })), n.d(o, "actions", (function () {
            return ve
        })), n.d(o, "getters", (function () {
            return be
        }));
        var c = {};
        n.r(c), n.d(c, "namespaced", (function () {
            return ke
        })), n.d(c, "state", (function () {
            return _e
        })), n.d(c, "mutations", (function () {
            return ge
        })), n.d(c, "actions", (function () {
            return we
        })), n.d(c, "getter", (function () {
            return Se
        }));
        var u = {};
        n.r(u), n.d(u, "namespaced", (function () {
            return Te
        })), n.d(u, "state", (function () {
            return Ee
        })), n.d(u, "mutations", (function () {
            return Re
        })), n.d(u, "actions", (function () {
            return ye
        })), n.d(u, "getters", (function () {
            return Oe
        }));
        n("e260"), n("e6cf"), n("cca6"), n("a79d");
        var s = n("2b0e"), i = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("v-app", [n("TheAppBar"), n("v-main", [n("TheNavBar"), n("router-view")], 1)], 1)
            }, d = [], h = function () {
                var e = this, t = e.$createElement, r = e._self._c || t;
                return r("v-app-bar", {
                    attrs: {
                        app: "",
                        color: "#f2dda8",
                        dark: "",
                        height: "80"
                    }
                }, [r("v-btn", {staticClass: "mr-6 ml-3", attrs: {to: "/", icon: ""}}, [r("v-avatar", {
                    attrs: {
                        tile: "",
                        size: "96"
                    }
                }, [r("v-img", {
                    attrs: {
                        contain: "",
                        src: n("87a7")
                    }
                })], 1)], 1), r("v-spacer"), e.userUniversity ? r("p", {
                    staticClass: "text-center mb-0 hidden-sm-and-down text-h6",
                    staticStyle: {color: "#4a4a4a"}
                }, [e._v(" " + e._s(e.userUniversity.name) + " ")]) : e._e(), r("v-spacer"), e.isAuth ? r("v-btn", {
                    attrs: {
                        text: "",
                        color: "#4a4a4a",
                        rounded: ""
                    }, on: {click: e.logout}
                }, [e._v(" Выйти")]) : r("v-btn", {
                    attrs: {
                        text: "",
                        color: "#4a4a4a",
                        rounded: "",
                        to: "/login"
                    }
                }, [e._v("Вход")])], 1)
            }, f = [], l = (n("7db0"), n("5530")), m = n("2f62"), p = {
                name: "TheAppBar", created: function () {
                    this.isAuth && (this.$store.dispatch("university/fetchUniversities"), this.$store.dispatch("university/fetchUserUniversity", this.$store.state.auth.userId))
                }, computed: Object(l["a"])(Object(l["a"])({}, Object(m["b"])(["university"])), {}, {
                    isAuth: function () {
                        return this.$store.state.auth.user
                    }, userUniversity: function () {
                        var e = this;
                        return this.university.universities.find((function (t) {
                            return t.id === e.university.userUniversity.university_id
                        }))
                    }
                }), methods: {
                    logout: function () {
                        var e = this;
                        this.$store.dispatch("auth/logout").then((function () {
                            e.$router.push({name: "login"})
                        }))
                    }
                }
            }, v = p, b = n("2877"), k = n("6544"), _ = n.n(k), g = n("40dc"), w = n("8212"), S = n("8336"), T = n("adda"),
            E = n("2fa4"), R = Object(b["a"])(v, h, f, !1, null, "cb831700", null), y = R.exports;
        _()(R, {VAppBar: g["a"], VAvatar: w["a"], VBtn: S["a"], VImg: T["a"], VSpacer: E["a"]});
        var O = function () {
                var e = this, t = e.$createElement, n = e._self._c || t;
                return n("v-container", {attrs: {fluid: ""}}, [e.isAuthUser ? n("v-row", [e._l(e.links, (function (t) {
                    return n("v-col", {key: t.id}, [n("v-card", {
                        attrs: {
                            color: "#f2dda8",
                            width: "100%"
                        }
                    }, [n("v-card-actions", [n("v-btn", {
                        staticClass: "mx-auto",
                        attrs: {text: "", color: "#4a4a4a", rounded: "", to: t.url}
                    }, [e._v(" " + e._s(t.name) + " ")])], 1)], 1)], 1)
                })), n("v-col", [n("v-card", {attrs: {color: "#f2dda8"}}, [n("v-card-actions", [n("v-btn", {
                    staticClass: "mx-auto",
                    attrs: {text: "", color: "#4a4a4a", rounded: "", href: "https://autolib.tdtu.uz/admin"}
                }, [e._v(" Управление книгами "), n("v-icon", {
                    staticClass: "ml-1",
                    attrs: {small: ""}
                }, [e._v("mdi-open-in-new")])], 1)], 1)], 1)], 1)], 2) : e._e()], 1)
            }, x = [], A = {
                name: "TheNavBar", computed: {
                    isAuthUser: function () {
                        return this.$store.state.auth.user
                    }
                }, data: function () {
                    return {
                        links: [{id: 1, url: "/library", name: "Активные заказы"}, {
                            id: 2,
                            url: "/library/books-in-use",
                            name: "Книги в эксплуатации"
                        }, {id: 3, url: "/library/orders-list", name: "Все заказы"}, {
                            id: 4,
                            url: "/library/statistics",
                            name: "Статистика"
                        }, {id: 5, url: "/library/book-list", name: "Каталог книг"}]
                    }
                }
            }, U = A, I = n("b0af"), P = n("99d9"), j = n("62ad"), B = n("a523"), q = n("132d"), C = n("0fd9"),
            V = Object(b["a"])(U, O, x, !1, null, "3a0f7392", null), D = V.exports;
        _()(V, {
            VBtn: S["a"],
            VCard: I["a"],
            VCardActions: P["a"],
            VCol: j["a"],
            VContainer: B["a"],
            VIcon: q["a"],
            VRow: C["a"]
        });
        var N = {name: "App", components: {TheAppBar: y, TheNavBar: D}}, L = N, $ = (n("5c0b"), n("7496")),
            H = n("f6c4"), M = Object(b["a"])(L, i, d, !1, null, null, null), K = M.exports;
        _()(M, {VApp: $["a"], VMain: H["a"]});
        n("45fc"), n("d3b7");
        var Y = n("8c4f"), z = {
            getToken: function (e) {
                return localStorage.getItem(e)
            }, saveToken: function (e, t) {
                localStorage.setItem(e, t)
            }, removeToken: function (e) {
                localStorage.removeItem(e)
            }
        }, W = z;
        s["a"].use(Y["a"]);
        var G = [{
            path: "/library", name: "active-orders", component: function () {
                return Promise.all([n.e("chunk-562b5199"), n.e("chunk-54f50b4e"), n.e("chunk-5a33e234"), n.e("chunk-2426a722")]).then(n.bind(null, "5e81"))
            }, meta: {requiresAuth: !0}
        }, {
            path: "/library/books-in-use", name: "books-in-use", component: function () {
                return Promise.all([n.e("chunk-562b5199"), n.e("chunk-54f50b4e"), n.e("chunk-5a33e234"), n.e("chunk-6e19e8f7")]).then(n.bind(null, "b0d4"))
            }, meta: {requiresAuth: !0}
        }, {
            path: "/library/book-list", name: "book-list", component: function () {
                return Promise.all([n.e("chunk-562b5199"), n.e("chunk-4fbd5345")]).then(n.bind(null, "0e6d"))
            }
        }, {
            path: "/library/book-show/:id", name: "book-show", component: function () {
                return n.e("chunk-a57e7254").then(n.bind(null, "65fe"))
            }, meta: {requiresAuth: !0}
        }, {
            path: "/library/statistics", name: "statistics", component: function () {
                return Promise.all([n.e("chunk-54f50b4e"), n.e("chunk-74781238")]).then(n.bind(null, "fcd1"))
            }, meta: {requiresAuth: !0}
        }, {
            path: "/library/orders-list", name: "orders-list", component: function () {
                return Promise.all([n.e("chunk-562b5199"), n.e("chunk-54f50b4e"), n.e("chunk-5a33e234"), n.e("chunk-2d0e5d25")]).then(n.bind(null, "95b5"))
            }
        }, {
            path: "/library/login", name: "login", component: function () {
                return Promise.all([n.e("chunk-562b5199"), n.e("chunk-79ba1026")]).then(n.bind(null, "a55b"))
            }
        }, {
            path: "/library/404", name: "not-found", component: function () {
                return n.e("chunk-2d0e5e97").then(n.bind(null, "9703"))
            }
        }, {path: "*", redirect: {name: "not-found"}}], J = new Y["a"]({mode: "history", base: "/", routes: G});
        J.beforeEach((function (e, t, n) {
            if (e.matched.some((function (e) {
                return e.meta.requiresAuth
            }))) {
                var r = W.getToken("access");
                if (r) return void n();
                n("/library/login")
            } else n()
        }));
        var F = J, Q = (n("96cf"), n("1da1")), X = n("bc3a"), Z = n.n(X), ee = {
                _interceptor: null, init: function (e) {
                    Z.a.defaults.baseURL = e, Z.a.defaults.withCredentials = !1, Z.a.defaults.headers.common["Accept"] = "application/json", Z.a.defaults.headers.common["Content-Type"] = "application/json"
                }, setHeader: function (e, t) {
                    Z.a.defaults.headers.common[e] = t
                }, removeHeader: function (e) {
                    delete Z.a.defaults.headers.common[e]
                }, customRequest: function (e) {
                    return Z()(e)
                }, mountInterceptor: function () {
                    this._interceptor = Z.a.interceptors.response.use((function (e) {
                        return e
                    }), (function (e) {
                        throw 401 === e.request.status && (W.getToken("refresh") ? xe.dispatch("auth/refreshToken", {refresh: W.getToken("refresh")}).then((function () {
                            location.reload()
                        })) : xe.dispatch("auth/logout")), e
                    }))
                }
            }, te = ee, ne = n("1232"), re = !0,
            ae = {user: null, accessToken: W.getToken("access"), refreshToken: W.getToken("refresh"), userId: null},
            oe = {
                SET_AUTH_USER: function (e, t) {
                    e.user = t
                }, SET_USER_ID: function (e, t) {
                    e.userId = t
                }, LOGOUT: function () {
                    localStorage.removeItem("access"), localStorage.removeItem("refresh"), location.reload()
                }
            }, ce = {
                login: function (e, t) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function n() {
                        var r, a, o, c;
                        return regeneratorRuntime.wrap((function (n) {
                            while (1) switch (n.prev = n.next) {
                                case 0:
                                    return r = e.commit, a = {
                                        method: "post",
                                        url: "/token/",
                                        data: t
                                    }, n.prev = 2, n.next = 5, te.customRequest(a);
                                case 5:
                                    o = n.sent, c = Object(ne["a"])(o.data.access).user_id, te.setHeader("Authorization", "Bearer ".concat(o.data.access)), W.saveToken("access", o.data.access), W.saveToken("refresh", o.data.refresh), r("SET_AUTH_USER", o.data), r("SET_USER_ID", c), n.next = 17;
                                    break;
                                case 14:
                                    throw n.prev = 14, n.t0 = n["catch"](2), new n.t0;
                                case 17:
                                case"end":
                                    return n.stop()
                            }
                        }), n, null, [[2, 14]])
                    })))()
                }, refreshToken: function (e, t) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function n() {
                        var r, a, o, c;
                        return regeneratorRuntime.wrap((function (n) {
                            while (1) switch (n.prev = n.next) {
                                case 0:
                                    return r = e.commit, a = {
                                        method: "post",
                                        url: "/token/refresh/",
                                        data: t
                                    }, n.prev = 2, n.next = 5, te.customRequest(a);
                                case 5:
                                    o = n.sent, c = Object(ne["a"])(o.data.access).user_id, te.setHeader("Authorization", "Bearer ".concat(o.data.access)), W.saveToken("access", o.data.access), r("SET_USER_ID", c), n.next = 15;
                                    break;
                                case 12:
                                    throw n.prev = 12, n.t0 = n["catch"](2), new n.t0;
                                case 15:
                                case"end":
                                    return n.stop()
                            }
                        }), n, null, [[2, 12]])
                    })))()
                }, logout: function (e) {
                    var t = e.commit;
                    t("LOGOUT")
                }
            }, ue = {}, se = !0, ie = {universities: [], userUniversity: {}}, de = {
                SET_UNIVERSITIES: function (e, t) {
                    e.universities = t
                }, SET_USER_UNIVERSITY: function (e, t) {
                    e.userUniversity = t
                }
            }, he = {
                fetchUniversities: function (e) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function t() {
                        var n, r, a;
                        return regeneratorRuntime.wrap((function (t) {
                            while (1) switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit, r = {
                                        method: "get",
                                        url: "/university/"
                                    }, t.prev = 2, t.next = 5, te.customRequest(r);
                                case 5:
                                    a = t.sent, n("SET_UNIVERSITIES", a.data), t.next = 12;
                                    break;
                                case 9:
                                    throw t.prev = 9, t.t0 = t["catch"](2), new t.t0;
                                case 12:
                                case"end":
                                    return t.stop()
                            }
                        }), t, null, [[2, 9]])
                    })))()
                }, fetchUserUniversity: function (e, t) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function n() {
                        var r, a, o;
                        return regeneratorRuntime.wrap((function (n) {
                            while (1) switch (n.prev = n.next) {
                                case 0:
                                    return r = e.commit, a = {
                                        method: "get",
                                        url: "/user/" + t,
                                        data: t
                                    }, n.prev = 2, n.next = 5, te.customRequest(a);
                                case 5:
                                    o = n.sent, r("SET_USER_UNIVERSITY", o.data), n.next = 12;
                                    break;
                                case 9:
                                    throw n.prev = 9, n.t0 = n["catch"](2), new n.t0;
                                case 12:
                                case"end":
                                    return n.stop()
                            }
                        }), n, null, [[2, 9]])
                    })))()
                }
            }, fe = {}, le = !0, me = {orders: [], activeOrders: [], order: {}}, pe = {
                SET_ORDERS: function (e, t) {
                    e.orders = t
                }, SET_ORDER: function (e, t) {
                    e.order = t
                }, SET_ACTIVE_ORDERS: function (e, t) {
                    e.activeOrders = t
                }
            }, ve = {
                fetchOrders: function (e) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function t() {
                        var n, r, a;
                        return regeneratorRuntime.wrap((function (t) {
                            while (1) switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit, r = {
                                        method: "get",
                                        url: "/orders/"
                                    }, t.prev = 2, t.next = 5, te.customRequest(r);
                                case 5:
                                    a = t.sent, n("SET_ORDERS", a.data), t.next = 12;
                                    break;
                                case 9:
                                    throw t.prev = 9, t.t0 = t["catch"](2), new t.t0;
                                case 12:
                                case"end":
                                    return t.stop()
                            }
                        }), t, null, [[2, 9]])
                    })))()
                }, fetchActiveOrders: function (e) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function t() {
                        var n, r, a;
                        return regeneratorRuntime.wrap((function (t) {
                            while (1) switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit, r = {
                                        method: "get",
                                        url: "/active_orders/"
                                    }, t.prev = 2, t.next = 5, te.customRequest(r);
                                case 5:
                                    a = t.sent, n("SET_ACTIVE_ORDERS", a.data), t.next = 12;
                                    break;
                                case 9:
                                    throw t.prev = 9, t.t0 = t["catch"](2), new t.t0;
                                case 12:
                                case"end":
                                    return t.stop()
                            }
                        }), t, null, [[2, 9]])
                    })))()
                }, updateActiveOrder: function (e, t) {
                    var n = this;
                    return Object(Q["a"])(regeneratorRuntime.mark((function r() {
                        var a, o, c, u;
                        return regeneratorRuntime.wrap((function (r) {
                            while (1) switch (r.prev = r.next) {
                                case 0:
                                    return a = e.dispatch, o = t.id, c = t.order, u = {
                                        method: "put",
                                        url: "/active_orders/" + o,
                                        data: c
                                    }, r.prev = 3, r.next = 6, te.customRequest(u);
                                case 6:
                                    return r.next = 8, a("fetchActiveOrders");
                                case 8:
                                    r.next = 15;
                                    break;
                                case 10:
                                    return r.prev = 10, r.t0 = r["catch"](3), r.next = 14, n.updateActiveOrder({dispatch: a}, {
                                        id: o,
                                        order: c
                                    });
                                case 14:
                                    throw new r.t0;
                                case 15:
                                case"end":
                                    return r.stop()
                            }
                        }), r, null, [[3, 10]])
                    })))()
                }
            }, be = {}, ke = !0, _e = {booksInUse: [], book: {}, books: []}, ge = {
                SET_BOOKS_IN_USE: function (e, t) {
                    e.booksInUse = t
                }, SET_BOOKS: function (e, t) {
                    e.books = t
                }, SET_BOOK: function (e, t) {
                    e.book = t
                }
            }, we = {
                fetchBooks: function (e) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function t() {
                        var n, r, a;
                        return regeneratorRuntime.wrap((function (t) {
                            while (1) switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit, r = {
                                        method: "get",
                                        url: "/books/"
                                    }, t.prev = 2, t.next = 5, te.customRequest(r);
                                case 5:
                                    a = t.sent, n("SET_BOOKS", a.data), t.next = 12;
                                    break;
                                case 9:
                                    throw t.prev = 9, t.t0 = t["catch"](2), new t.t0;
                                case 12:
                                case"end":
                                    return t.stop()
                            }
                        }), t, null, [[2, 9]])
                    })))()
                }, fetchBooksInUse: function (e) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function t() {
                        var n, r, a;
                        return regeneratorRuntime.wrap((function (t) {
                            while (1) switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit, r = {
                                        method: "get",
                                        url: "/book_in_use/"
                                    }, t.prev = 2, t.next = 5, te.customRequest(r);
                                case 5:
                                    a = t.sent, n("SET_BOOKS_IN_USE", a.data), t.next = 12;
                                    break;
                                case 9:
                                    throw t.prev = 9, t.t0 = t["catch"](2), new t.t0;
                                case 12:
                                case"end":
                                    return t.stop()
                            }
                        }), t, null, [[2, 9]])
                    })))()
                }, fetchBook: function (e, t) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function n() {
                        var r, a, o;
                        return regeneratorRuntime.wrap((function (n) {
                            while (1) switch (n.prev = n.next) {
                                case 0:
                                    return r = e.commit, a = {
                                        method: "get",
                                        url: "/books/" + t,
                                        data: t
                                    }, n.prev = 2, n.next = 5, te.customRequest(a);
                                case 5:
                                    o = n.sent, r("SET_BOOK", o.data), n.next = 12;
                                    break;
                                case 9:
                                    throw n.prev = 9, n.t0 = n["catch"](2), new n.t0;
                                case 12:
                                case"end":
                                    return n.stop()
                            }
                        }), n, null, [[2, 9]])
                    })))()
                }, updateBookInUse: function (e, t) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function n() {
                        var r, a, o, c;
                        return regeneratorRuntime.wrap((function (n) {
                            while (1) switch (n.prev = n.next) {
                                case 0:
                                    return r = e.dispatch, a = t.id, o = t.book, c = {
                                        method: "put",
                                        url: "/book_in_use/" + a,
                                        data: o
                                    }, n.prev = 3, n.next = 6, te.customRequest(c);
                                case 6:
                                    return n.next = 8, r("fetchBooksInUse");
                                case 8:
                                    n.next = 13;
                                    break;
                                case 10:
                                    throw n.prev = 10, n.t0 = n["catch"](3), new n.t0;
                                case 13:
                                case"end":
                                    return n.stop()
                            }
                        }), n, null, [[3, 10]])
                    })))()
                }
            }, Se = {}, Te = !0,
            Ee = {statsPerDay: {}, statsPerMonth: {}, statsPerWeek: {}, statsPerYear: {}, isLoaded: !1}, Re = {
                SET_STATS_PER_DAY: function (e, t) {
                    e.statsPerDay = t
                }, SET_STATS_PER_WEEK: function (e, t) {
                    e.statsPerWeek = t
                }, SET_STATS_PER_MONTH: function (e, t) {
                    e.statsPerMonth = t
                }, SET_STATS_PER_YEAR: function (e, t) {
                    e.statsPerYear = t
                }
            }, ye = {
                fetchStatsPerDay: function (e) {
                    return Object(Q["a"])(regeneratorRuntime.mark((function t() {
                        var n, r, a;
                        return regeneratorRuntime.wrap((function (t) {
                            while (1) switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit, r = {
                                        method: "get",
                                        url: "/stats_per_day/"
                                    }, t.prev = 2, t.next = 5, te.customRequest(r);
                                case 5:
                                    a = t.sent, n("SET_STATS_PER_DAY", a.data), t.next = 12;
                                    break;
                                case 9:
                                    throw t.prev = 9, t.t0 = t["catch"](2), new t.t0;
                                case 12:
                                case"end":
                                    return t.stop()
                            }
                        }), t, null, [[2, 9]])
                    })))()
                }, fetchStatsPerWeek: function (e) {
                    var t = e.commit, n = {method: "get", url: "/stats_per_week/"};
                    return te.customRequest(n).then((function (e) {
                        t("SET_STATS_PER_WEEK", e.data)
                    })).finally((function () {
                        Ee.isLoaded = !0
                    })).catch((function (e) {
                        throw e
                    }))
                }, fetchStatsPerMonth: function (e) {
                    var t = e.commit, n = {method: "get", url: "/stats_per_month/"};
                    return te.customRequest(n).then((function (e) {
                        t("SET_STATS_PER_MONTH", e.data)
                    })).finally((function () {
                        Ee.isLoaded = !0
                    })).catch((function (e) {
                        throw e
                    }))
                }, fetchStatsPerYear: function (e) {
                    var t = e.commit, n = {method: "get", url: "/stats_per_year/"};
                    return te.customRequest(n).then((function (e) {
                        t("SET_STATS_PER_YEAR", e.data)
                    })).finally((function () {
                        Ee.isLoaded = !0
                    })).catch((function (e) {
                        throw e
                    }))
                }
            }, Oe = {};
        s["a"].use(m["a"]);
        var xe = new m["a"].Store({modules: {auth: r, university: a, order: o, book: c, stats: u}}), Ae = n("f309"),
            Ue = n("2992"), Ie = n.n(Ue);
        s["a"].use(Ae["a"]);
        var Pe = new Ae["a"]({lang: {locales: {ru: Ie.a}, current: "ru"}});
        n("a5d8");
        s["a"].config.productionTip = !1, te.init("https://autolib.tdtu.uz/api/v1/admin");
        var je = W.getToken("access");
        if (je) {
            xe.commit("auth/SET_AUTH_USER", je);
            var Be = Object(ne["a"])(je).user_id;
            xe.commit("auth/SET_USER_ID", Be), te.setHeader("Authorization", "Bearer ".concat(je))
        }
        te.mountInterceptor(), new s["a"]({
            router: F, store: xe, vuetify: Pe, created: function () {
                var e = this;
                this.timeout = setInterval((function () {
                    return e.$store.dispatch("auth/refreshToken", {refresh: W.getToken("refresh")})
                }), 27e4)
            }, render: function (e) {
                return e(K)
            }
        }).$mount("#app")
    }, "5c0b": function (e, t, n) {
        "use strict";
        n("9c0c")
    }, "87a7": function (e, t, n) {
        e.exports = n.p + "img/white_logo.7f1d4b5b.png"
    }, "9c0c": function (e, t, n) {
    }
});
//# sourceMappingURL=app.51bafd2c.js.map