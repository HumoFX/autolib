(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-2d0e5d25"], {
    "95b5": function (e, t, a) {
        "use strict";
        a.r(t);
        var r = function () {
            var e = this, t = e.$createElement, a = e._self._c || t;
            return a("v-container", {attrs: {fluid: ""}}, [a("v-row", [a("v-col", [a("v-data-table", {
                staticClass: "elevation-2",
                attrs: {
                    headers: e.headers,
                    items: e.filledOrders,
                    "sort-by": ["id"],
                    "sort-desc": [!0, !1],
                    "items-per-page": 10,
                    search: e.search
                }
            })], 1)], 1)], 1)
        }, s = [], o = (a("d81d"), a("5530")), n = a("323e"), d = a.n(n), i = a("2f62"), l = a("c1df"), c = a.n(l);
        c.a.locale("ru");
        var u = {
                name: "OrdersList", data: function () {
                    return {
                        search: "",
                        headers: [{text: "№", align: "start", value: "id"}, {
                            sortable: !1,
                            text: "Имя пользователя",
                            value: "user.full_name"
                        }, {sortable: !1, text: "Название книги", value: "book.title"}, {
                            sortable: !1,
                            text: "Автор книги",
                            value: "book.author"
                        }, {sortable: !1, text: "ISBN", value: "book.isbn"}, {
                            sortable: !1,
                            text: "Сдал",
                            value: "retrieved"
                        }, {sortable: !1, text: "Время сдачи", value: "time_of_pass"}]
                    }
                }, computed: Object(o["a"])(Object(o["a"])({}, Object(i["b"])(["order"])), {}, {
                    filledOrders: function () {
                        return this.order.orders.map((function (e) {
                            return !1 === e.retrieved && (e.retrieved = "Не сдал", e.time_of_pass = ""), !0 === e.retrieved && (e.retrieved = "Сдал", e.time_of_pass = c()().format()), Object(o["a"])({}, e)
                        }))
                    }
                }), created: function () {
                    d.a.start(), this.$store.dispatch("order/fetchOrders")
                }, mounted: function () {
                    d.a.done()
                }
            }, f = u, b = a("2877"), v = a("6544"), h = a.n(v), p = a("62ad"), m = a("a523"), O = a("8fea"), _ = a("0fd9"),
            w = Object(b["a"])(f, r, s, !1, null, "2f755a93", null);
        t["default"] = w.exports;
        h()(w, {VCol: p["a"], VContainer: m["a"], VDataTable: O["a"], VRow: _["a"]})
    }
}]);
//# sourceMappingURL=chunk-2d0e5d25.abb8e616.js.map