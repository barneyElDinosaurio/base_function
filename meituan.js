!
function () {
    "use strict";

    function n(n) {
        var t = n;
        return n && n.code && (t = n.code),
        t === He ? "E_TIME_OUT" : t === We ? "E_NO_JSBRIDGE" : t === Ze ? "E_KNB_FAIL" : t === Ge ? "E_KNB_CB_FAIL" : t === Ye ? "E_KNB_NOT_EXIST" : t === tr ? "ERR_PARAMS" : t === nr ? "E_KNB_METHOD_NOT_SUPPORT" : "unknown error: " + t
    }
    function t() {
        return location
    }
    function e() {
        return window
    }
    function r() {
        return document
    }
    function i() {
        return navigator
    }
    function u() {
        var n = e();
        return n.XMLHttpRequest
    }
    function o() {
        var n = Iu.get(Ei);
        if (n) {
            var t = n.split("|");
            return {
                mis: t[0],
                env: t[1] || ""
            }
        }
        return n || {}
    }
    function a(n) {
        var t = "v2/api/" + Di + "/validate",
            e = "validate-ocean" + Ci,
            r = 0 === J().indexOf("http:"),
            i = r ? "http:" : "https:",
            u = i + "//" + n + "/",
            a = X(),
            c = a.match(Ui) || [],
            s = o(),
            f = void 0,
            d = void 0;
        if (d = c && c[1] || s.mis || "") {
                Iu.set(Ei, d + "|" + (f || ""), Qi);
                var v = e;
                u = i + "//" + v + "/" + t + "?mis=" + d
            }
        return u
    }
    function c() {
        var n = zi.nativeSDKVer;
        wu.isStr(n) && (Hi.MVL = H(n, "4.14.0") > -1, Hi.QC = H(n, "4.14.0") > -1, Hi.getReqId = H(n, "4.12.0") > -1)
    }
    function s(n) {
        return !!Hi[n]
    }
    function f(n) {
        if (wu.isStr(n)) return n && Xi[n] || Xi
    }
    function d(n, t) {
        wu.isStr(n) && (Xi[n] = t)
    }
    function v(n) {
        Ki = n
    }
    function l() {
        return Ki === _e
    }
    function p(n) {
        return $i && !n || ($i = a(Ni)),
        $i
    }
    function h(n) {
        if (!Ji || n) {
            var t = "wreport.meituan.net";
            Ji = a(t)
        }
        return Ji
    }
    function g() {
        if (lu !== Zi) return Zi;
        var n = su.getElementsByTagName("meta");
        return Zi = "off" === M(n, "lx:native-report")
    }
    function m() {
        return Gi
    }
    function _(n) {
        g() || (Gi = n)
    }
    function y() {
        return Yi
    }
    function b(n) {
        Yi = !! n
    }
    function w(n) {
        iu = n
    }
    function x() {
        clearTimeout(ru);
        try {
            A()
        } catch (n) {} finally {
            m() === Wr ? ru = Xe(x, nu) : clearTimeout(ru)
        }
    }
    function S(n, t, e, r) {
        r = r || {};
        var i = t.category,
            u = e.req_id,
            o = e.val_cid,
            a = e.val_bid,
            c = r.tag;
        if (eu[n] && wu.isStr(n) && wu.isStr(i) && wu.isStr(u) && wu.isStr(o) && wu.isStr(a)) {
                var s = i + "_" + u + "_" + o + "_" + a,
                    f = eu[n];
                wu.isObj(f[s]) || (f[s] = {
                        env: wu.extend(!0, {}, t),
                        evs: e,
                        lab: []
                    }),
                wu.isObj(c) && (f[s].evs.tag = c);
                var d = wu.extend(!0, e.val_lab, {
                        _seq: e.seq,
                        _tm: e.tm
                    });
                f[s].lab.push(d),
                k()
            }
    }
    function k() {
        var n = 0;
        for (var t in eu) {
            var e = eu[t];
            for (var r in e) {
                var i = e[r].lab;
                n += i.length || 0
            }
        }
        n > tu && A()
    }
    function q(n, t) {
        var e = t || {},
            r = e.withUnload,
            i = eu[n];
        if (wu.isObj(i)) {
                var u = [];
                for (var o in i) {
                    var a = i[o],
                        c = !1;
                    if (a.lab && a.lab.length) {
                            var s = a.env,
                                f = a.evs,
                                d = {
                                    mv_list: a.lab,
                                    custom: {
                                        _withUnload: !! r
                                    }
                                };
                            f.val_lab = d;
                            for (var v = 0, l = u.length; v < l; v++) {
                                    var p = u[v];
                                    if (!O(p, s)) {
                                        p.evs.push(f),
                                        c = !0;
                                        break
                                    }
                                }
                            c || (s.evs = [f], u.push(s))
                        }
                }
                u.length && iu.send(u),
                eu[n] = {}
            }
    }
    function O(n, t) {
        var e = "evs|",
            r = 0,
            i = 0;
        for (var u in n) n.hasOwnProperty(u) && r++;
        for (var o in t) t.hasOwnProperty(o) && i++;
        var a = r > i ? n : t,
            c = r <= i ? n : t;
        for (var s in a) if (!(e.indexOf(s + "|") > -1)) if (wu.isObj(a[s]) && wu.isObj(c[s])) {
                var f = O(a[s], c[s]);
                if (f) return !0
            } else if (a[s] !== c[s]) return !0;
        return !1
    }
    function A(n) {
        var t = n || {},
            e = t.withUnload;
        for (var r in eu) q(r, {
                withUnload: e
            })
    }
    function I() {}
    function j(n) {
        return "undefined" == typeof n ? "undefined" : uu(n)
    }
    function D(n, t) {
        return j(n) === t
    }
    function E() {
        return +new Date
    }
    function C() {
        return Math.random()
    }
    function N(n) {
        return D(n, "number")
    }
    function F(n) {
        return !n && D(n, "object")
    }
    function T(n, t, e) {
        var r = void 0,
            i = !0 === n;
        return i || (e = t, t = n),
        t && wu.isObj(t) || (t = {}),
        e && wu.isObj(e) || (e = {}),
        ku.each(e, function (n, u) {
                i && wu.isObj(e[u]) ? (r = t[u], t[u] = wu.isObj(r) ? r : {}, T(i, t[u], e[u])) : t[u] = e[u]
            }),
        t
    }
    function L(n) {
        var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
            e = void 0,
            r = void 0,
            i = void 0,
            u = void 0,
            o = void 0,
            a = void 0,
            c = void 0,
            s = void 0,
            f = 0,
            d = 0,
            v = "",
            l = [];
        if (!n) return n;
        n = V(n);
        do e = n.charCodeAt(f++),
        r = n.charCodeAt(f++),
        i = n.charCodeAt(f++),
        s = e << 16 | r << 8 | i,
        u = s >> 18 & 63,
        o = s >> 12 & 63,
        a = s >> 6 & 63,
        c = 63 & s,
        l[d++] = t.charAt(u) + t.charAt(o) + t.charAt(a) + t.charAt(c);
        while (f < n.length);
        switch (v = l.join(""), n.length % 3) {
            case 1:
                v = v.slice(0, -2) + "==";
                break;
            case 2:
                v = v.slice(0, -1) + "="
            }
        return v
    }
    function V(n) {
        n = (n + "").replace(/\r\n/g, "\n").replace(/\r/g, "\n");
        var t = "",
            e = void 0,
            r = void 0,
            i = 0,
            u = void 0;
        for (e = r = 0, i = n.length, u = 0; u < i; u++) {
                var o = n.charCodeAt(u),
                    a = null;
                o < 128 ? r++ : a = o > 127 && o < 2048 ? String.fromCharCode(o >> 6 | 192, 63 & o | 128) : String.fromCharCode(o >> 12 | 224, o >> 6 & 63 | 128, 63 & o | 128),
                null !== a && (r > e && (t += n.substring(e, r)), t += a, e = r = u + 1)
            }
        return r > e && (t += n.substring(e, n.length)),
        t
    }
    function M(n, t) {
        var e = void 0,
            r = ku.find(n, function (n) {
                return wu.attr(n, "name") === t
            });
        return r && (e = wu.attr(r, "content")),
        e
    }
    function R() {
        var n = au[me];
        return au[n]
    }
    function P(n) {
        var t = n || E(),
            e = R();
        ju.update(t),
        _u = t,
        e && (e.l = t)
    }
    function B(n) {
        var t = void 0,
            e = ju.get(),
            r = E();
        if (n && e) t = e,
        ju.update(r);
        else {
                var i = R(),
                    u = au.performance && au.performance.timing;
                t = u && u.requestStart,
                t || (t = i ? i.l : _u),
                ju.update(r)
            }
        return r - t
    }
    function U(n) {
        var t = {
            duration: B(!0 === n)
        },
            e = void 0,
            r = zi.quit,
            i = wu.isFunc(r);
        return i && (e = r() || {}),
        t = wu.extend(t, e || {})
    }
    function Q(n, t) {
        !t[Xr]
    }
    function K(n) {
        return n < 2036
    }
    function $(n) {
        for (var t = n.length, e = t, r = 0; r < t; r++) {
            var i = n.charCodeAt(r);
            i > 127 && e++
        }
        return K(1.5 * e)
    }
    function J() {
        return cu.protocol
    }
    function X() {
        return cu.search
    }
    function z(n, t) {
        var e = void 0,
            r = Ai + Du++;
        if (t = t || 0, !(t > 2)) return au[r] = e = new Image,
        e.onload = function () {
                au[r] = null
            },
        e.onabort = e.onerror = function () {
                au[r] = null,
                z(n, ++t)
            },
        e.src = n,
        e
    }
    function H(n, t) {
        var e = /^((\d+\.)+\d+).*$/;
        if ("string" !== j(n) || "string" !== j(t)) return NaN;
        if (!e.test(n) || !e.test(t)) return NaN;
        for (var r = n.replace(e, "$1").split("."), i = t.replace(e, "$1").split("."), u = Math.max(r.length, i.length), o = 0, a = u; o < a; o++) {
            if (!r[o] || !i[o]) {
                var c = !r[o] && r || !i[o] && i;
                c.push("0")
            }
            var s = r[o].toString().length,
                f = i[o].toString().length;
            if (s !== f) {
                    var d = s > f ? i : r;
                    d[o] = Array(Math.abs(s - f) + 1).join("0") + d[o].toString()
                }
        }
        var v = parseInt(r.join("")),
            l = parseInt(i.join(""));
        return v == l ? 0 : v > l ? 1 : -1
    }
    function W(n, t, e, r, i, u, o) {
        return function (a) {
            if (!n) {
                n = !0;
                try {
                    if (t && new Date - e < 50) return;
                    if (r) return;
                    if (r = !1, !o()) {
                        var c = U();
                        i("pageDisappear", c, {
                            shouldStore: !0
                        })
                    }
                    A({
                        withUnload: !0
                    })
                } catch (s) {}
                u && u(a)
            }
        }
    }
    function Z(n) {
        if (!n) return lu;
        var t = lu,
            e = /^utm_(source|medium|term|content|campaign)$/;
        return ku.each(n, function (n, r) {
                e.test(r) && (!t && (t = {}), t[r] = n)
            }),
        t
    }
    function G() {
        return "daum:q eniro:search_word naver:query pchome:q images.google:q google:q yahoo:p msn:q bing:q aol:query aol:q lycos:q lycos:query ask:q cnn:query virgilio:qs baidu:wd baidu:word alice:qs yandex:text najdi:q seznam:q rakuten:qt biglobe:q goo.ne:MT search.smt.docomo:MT onet:qt onet:q kvasir:q terra:query rambler:query conduit:q babylon:q search-results:q avg:q comcast:q incredimail:q startsiden:q go.mail.ru:q centrum.cz:q 360.cn:q sogou:query tut.by:query globo:q ukr:q so.com:q haosou.com:q auone:q m.baidu:word wap.baidu:word baidu:word Baidu:bs www.soso:w wap.soso:key www.sogou:query wap.sogou:keyword m.so:q m.sogou:keyword so.com:pq youdao:q sm.cn:q sm.cn:keyword haosou:q".split(" ")
    }
    function Y(n) {
        var t = wu.parseQuery(n);
        return Z(t)
    }
    function nn(n) {
        var t = lu,
            e = n.match(/^[\w-]+:\/\/([^\/]+)(?:\/([^?]+)?)?/),
            r = e && e[1];
        if (r) {
                var i = wu.parseQuery(n),
                    u = G(),
                    o = "",
                    a = "";
                ku.each(u, function (n) {
                        var t = n.split(":"),
                            e = t[0],
                            u = t[1],
                            c = i[u],
                            s = -1 < e.indexOf(".") ? e : "." + e + ".";
                        if (-1 < r.indexOf(s.toLowerCase()) && (a = e, o = c)) return !1
                    }),
                a && (t = {}, t[no] = a, t[to] = "organic", o && (t[eo] = o))
            }
        return t
    }
    function tn(n) {
        if (n) {
            uo = n;
            var t = wu.stringifyQuery(n);
            return Iu.del(ri, fu),
            Iu.top(ri, t, ni, fu),
            !0
        }
        return !1
    }
    function en() {
        var n = Iu.get(ri);
        if (!Je.test(n)) return uo;
        var t = wu.isStr(n) ? wu.parseQuery(n) : null;
        return Z(t)
    }
    function rn() {
        var n = void 0,
            t = /(utmc(tr|sr|cn|md|ct))=([^|()]+)/g,
            e = Iu.get("__utmz"),
            r = e && e.match(t);
        return r && ku.each(r, function (t) {
                var e = t.split("="),
                    r = e[0],
                    i = void 0,
                    u = e[1] || "";
                "utmcsr" === r ? i = no : "utmccn" === r ? i = ro : "utmcmd" === r ? i = to : "utmcct" === r ? i = io : "utmctr" === r && (i = eo),
                i && (n = n || {}, n[i] = u)
            }),
        n
    }
    function un(n, t) {
        return (!uo && !oo || n) && (n = n || cu.href, t = t || su.referrer, uo = Y(n) || nn(t), uo ? tn(uo) : uo = en(), uo || (uo = rn(), tn(uo)), oo = he),
        uo
    }
    function on(n) {
        return so + n
    }
    function an() {
        return {
            length: 0,
            _data: {},
            setItem: function (n, t) {
                return this.length++,
                this._data[n] = String(t)
            },
            getItem: function (n) {
                return this._data.hasOwnProperty(n) ? this._data[n] : lu
            },
            removeItem: function (n) {
                return this.length--,
                delete this._data[n]
            },
            clear: function () {
                return this.length = 0,
                this._data = {}
            },
            key: function (n) {
                var t = [],
                    e = this._data;
                return ku.each(e, function (n) {
                        wu.hasOwn(e, n) && t.push(n)
                    }),
                t[n]
            }
        }
    }
    function cn(n, t, e, r, i, u) {
        var o = {};
        o.c = n,
        o.k = t,
        o.v = e,
        o.t = r || +new Date,
        o.u = i || "",
        o.r = u || "",
        this.toJSON = function () {
            return wu.extend(!0, {}, o)
        }
    }
    function sn(n) {
        var t = wu.now();
        return mo < t - n.t
    }
    function fn(n) {
        return n
    }
    function dn(n) {
        try {
            n(vn(this, bo), vn(this, yo))
        } catch (t) {
            if (this._state === wo) return hn(new dn(fn), yo, t)
        }
    }
    function vn(n, t) {
        return function (e) {
            return hn(n, t, e)
        }
    }
    function ln(n, t, e, r) {
        return j(e) === xo && (t._onFulfilled = e),
        j(r) === xo && (t._onRejected = r),
        n._state === wo ? n[n._pCount++] = t : pn(n, t),
        t
    }
    function pn(n, t) {
        return setTimeout(function () {
            var e = void 0,
                r = n._state ? t._onFulfilled : t._onRejected;
            if (void 0 === r) return void hn(t, n._state, n._value);
            try {
                    e = r(n._value)
                } catch (i) {
                    return void hn(t, yo, i)
                }
            gn(t, e)
        })
    }
    function hn(n, t, e) {
        if (n._state === wo) {
            n._state = t,
            n._value = e;
            for (var r = 0, i = n._pCount; r < i;) pn(n, n[r++]);
            return n
        }
    }
    function gn(n, t) {
        if (t === n && t) return void hn(n, yo, new Error("promise_circular_chain"));
        var e = void 0,
            r = j(t);
        if (null === t || r !== xo && r !== So) hn(n, bo, t);
        else {
                try {
                    e = t.then
                } catch (i) {
                    return void hn(n, yo, i)
                }
                j(e) === xo ? mn(n, t, e) : hn(n, bo, t)
            }
        return n
    }
    function mn(n, t, e) {
        try {
            e.call(t, function (e) {
                t && (t = null, gn(n, e))
            }, function (e) {
                t && (t = null, hn(n, yo, e))
            })
        } catch (r) {
            t && (hn(n, yo, r), t = null)
        }
    }
    function _n(n, t) {
        ku.each(Oo, function (e) {
            e(n, t)
        }),
        Oo = []
    }
    function yn(n) {
        var t = au.KNB;
        if (Gu()) {
            if (qe === Pu) n(lu, t);
            else if (ko || Io) n(Io, t);
            else if (Oo.push(n), !Ao) {
                Ao = !0;
                var e = Xe(function () {
                    Io = He,
                    _n(He, t)
                }, qo);
                E();
                /meituan \d+/i.test(vu) || /meituangroup\/7\.([0-7])\./i.test(vu) ? (Io = nr, _n(nr, t)) : (t.ready(function () {}), t.ready(function () {
                    t.isApiSupported({
                        apiName: "lxlog",
                        success: function (n) {
                            !0 === n ? (ko = !0, ze(e), _n(lu, t)) : (Io = nr, _n(nr, t))
                        },
                        fail: function () {
                            ze(e),
                            Io = Ge,
                            _n(Ge)
                        }
                    })
                }))
            }
        } else n(Ye, t)
    }
    function bn(n) {
        var t = {},
            e = n[Fe],
            r = e && "0" !== e;
        return r || "dp" !== n.type ? n[Fe] && (t[Fe] = n[Fe]) : t[Fe] = n[Ie],
        "dp" !== n.type && n[Ie] && (t[Ie] = n[Ie]),
        n.unionId && (t.unionId = n.unionId),
        n.userId && (t.userId = n.userId),
        t
    }
    function wn() {
        return Eo ? dn.resolve(Eo) : new dn(function (n, t) {
            yn(function (e, r) {
                var i = au.DPApp,
                    u = Xe(function () {
                        n({})
                    }, jo);
                r ? r.ready(function () {
                        r.use(Do, {
                            success: function (t) {
                                ze(u),
                                n(bn(t))
                            },
                            fail: function (n) {
                                ze(u),
                                t({
                                    code: Ze
                                })
                            }
                        })
                    }) : i && i[Do] ? i.ready(function () {
                        i[Do]({
                            success: function (t) {
                                ze(u);
                                var e = {};
                                (t.dpid || t.userId) && (e.dpid = t.dpid, e.userId = t.userId, e.unionId = t.unionId),
                                n(e)
                            },
                            fail: function (n) {
                                ze(u),
                                t({
                                    code: We,
                                    res: n
                                })
                            }
                        })
                    }) : t({
                        code: We
                    })
            })
        })
    }
    function xn() {
        return Iu.get(oi)
    }
    function Sn(n) {
        n && Iu.top(oi, n, ti)
    }
    function kn() {
        var n = xn() || Co();
        return Sn(n),
        n
    }
    function qn() {
        var n = Math.floor(1 + 65535 * wu.rnd());
        return n.toString(16).substring(1)
    }
    function On() {
        var n = [],
            t = +new Date;
        return n.push(t.toString(16)),
        n.push(qn()),
        n.push(qn()),
        n.push(qn()),
        n.join("-")
    }
    function An(n, t, e) {
        return Pu === qe && window.JavaScriptBridge ? void window.JavaScriptBridge.log(t, function (n) {
            var t = n.data;
            try {
                wu.isStr(t) && (t = co.parse(t)),
                e(lu, t.data ? t.data : t)
            } catch (r) {
                e(r)
            }
        }) : yn(function (r, i) {
            if (r) return e(r);
            var u = (new Date, !1),
                o = Xe(function () {
                    u = !0,
                    e(He)
                }, No);
            i.use(n, {
                    data: t,
                    success: function (n) {
                        if (ze(o), !u) if ("success" === n.status) {
                            var t = n.data || {};
                            try {
                                wu.isStr(t) && (t = co.parse(t)),
                                e(lu, t.data ? t.data : n)
                            } catch (r) {
                                e(r)
                            }
                        } else e(Ge)
                    },
                    fail: function () {
                        ze(o),
                        u || e(Ge)
                    }
                })
        })
    }
    function In(n) {
        var t = n.match(/(\d+)(?:\.(\d+)(?:\.(\d+))?)?/),
            e = [];
        if (t) for (var r = 1; r < t.length; r++) e.push(parseInt(t[r] || 0));
        return e
    }
    function jn(n, t) {
        var e = In(n),
            r = In(t);
        return !(e[0] < r[0]) && (!(e[0] === r[0] && e[1] < r[1]) && !(e[0] === r[0] && e[1] === r[1] && e[2] < r[2]))
    }
    function Dn() {
        return 100 * wu.now() + Bo++
    }
    function En(n) {
        var t = n._opts || {},
            e = t.nativeOptions || {},
            r = {
                cb: "_lx" + Dn(),
                mn: n._mn,
                cn: n._cn,
                data: n._d || {},
                options: e,
                ver: 4
            };
        return r
    }
    function Cn(n, t, e, r, i) {
        i = i || {};
        var u = this;
        u._cn = n,
        u._mn = t,
        u._d = e,
        u._cb = r,
        u._opts = i
    }
    function Nn(n, t, e, r, i) {
        if (gr === To || mr === To) return r(To);
        var u = new Cn(n, t, e, Pi, i);
        if (pr === To) u.send(function (n, t) {
            r(n, t)
        });
        else if (hr === To) {
            if (Po.push([u, r]), !Lo) {
                Lo = !0;
                var o = (new Date, new Cn(n, Fo, {}));
                o.send(function (n, t) {
                    if (n) To = gr;
                    else {
                        if (To = pr, _(Hr), wu.isStr(t)) try {
                            t = co.parse(t)
                        } catch (e) {}
                        Uo = t;
                        var r = t.sdk_ver || "";
                        Vo = jn(r, "4.0.0"),
                        Mo = jn(r, "4.3.0"),
                        Ro = !jn(r, "4.8.0")
                    }
                    ku.each(Po, function (t) {
                        var e = t[0],
                            r = t[1];
                        n ? r(n) : e.send(function (n, t) {
                                r(n, t)
                            })
                    })
                })
            }
        } else r(_r)
    }
    function Fn() {
        return !Ro
    }
    function Tn() {
        return Vo
    }
    function Ln() {
        return Mo
    }
    function Vn(n, t, e, r, i) {
        var u = [{
            project: "web-lx-sdk",
            pageUrl: cu.href,
            resourceUrl: n,
            category: i ? "jsError" : "ajaxError",
            sec_category: t,
            level: "error",
            unionId: e,
            timestamp: wu.now(),
            content: "" + r || ""
        }],
            o = $n("//catfront.dianping.com/api/log?v=1", "application/x-www-form-urlencoded");
        o && (o.onerror = o.onreadystatechange = function () {}, o.send("c=" + encodeURIComponent(co.stringify(u))))
    }
    function Mn(n, t) {
        if (Yo >= $o) return !1;
        t = wu.extend({
            cb: I
        }, t || {});
        var e = p(),
            r = !zi.use_post;
        try {
                r && Rn(n) ? t.cb(pr) : Un(e, n, t) || $u && Bn(e, n, t) || Pn(e, n) && t.cb(pr)
            } catch (i) {
                return Vn(cu.path, "report-ajax", 0, i.message, !0),
                !1
            }
        return !0
    }
    function Rn(n) {
        var t = E().toString(16) + Go++,
            e = void 0,
            r = "d",
            i = "t",
            u = "r",
            o = Xn(n);
        if (ku.each(o, function (n) {
                delete n.ua
            }), e = co.stringify(o), !$(e)) return ku.each(n, function (n) {
                ku.each(n.evs, function (n) {
                    var t = wu.extend(!0, {
                        custom: {
                            _s: 1
                        }
                    }, n.val_lab || {});
                    n.val_lab = t
                })
            }),
        !1;
        var a = L(e),
            c = mu(a),
            s = h();
        return s += -1 < s.indexOf("?") ? "&" + r + "=" + c : "?" + r + "=" + c,
        s = s + "&" + i + "=1&" + u + "=" + t,
        z(s),
        !0
    }
    function Pn(n, t) {
        var e = du.sendBeacon;
        return !!e && (n = Kn(n), e && e.call(du, n, co.stringify(t)))
    }
    function Bn(n, t, e, r) {
        if (!au.XDomainRequest) return !1;
        try {
            var i = new XDomainRequest;
            return i.open(ji, Kn(n), !0),
            i.onload = function () {
                Yo = 0,
                e && e.cb(pr),
                Wo = []
            },
            i.onerror = function () {
                Yo++
            },
            i.ontimeout = function () {
                Yo++,
                r || (Qn(n, t, Bn, e), Ho = !0)
            },
            i.timeout = Xo,
            i.send(co.stringify(t)),
            !0
        } catch (u) {
            return !1
        }
    }
    function Un(n, t, e, r, i) {
        if (!Bi()) return !1;
        try {
            var u = $n(n, "text/plain");
            return u.onreadystatechange = function () {
                if (4 === u.readyState) {
                    var o = u.status;
                    o >= 200 ? (Yo = 0, e && e.cb(pr, u.responseText), Wo = []) : (Yo++, r || !1 !== i || (Qn(n, t, Un, e), Ho = !0)),
                    e.nm === yr && (400 <= o || 0 === o) && Vn(n, "web-report-fail", t[0].union_id, o),
                    u.onreadystatechange = null
                }
            },
            u.onerror = function () {
                u.abort(),
                Yo++
            },
            u.send(co.stringify(t)),
            !0
        } catch (o) {
            return !1
        }
    }
    function Qn(n, t, e, r) {
        Wo = Wo.concat(t);
        var i = void 0,
            u = ku.reduce(Wo, function (n, t) {
                return t.evs = n.evs.concat(t.evs),
                i = t.evs.length,
                i > Jo && ku.slice(t.evs, i - Jo, i),
                t
            });
        if (Wo = [u], Zo.push(r), !Ho) var o = setInterval(function () {
                return Yo >= $o ? (clearInterval(o), !1) : void e(n, Wo, function (n) {
                    clearInterval(o),
                    Ho = !1,
                    ku.each(Zo, function (t) {
                        t && t(n)
                    })
                }, !0)
            }, zo)
    }
    function Kn(n) {
        var t = E().toString(16) + Go,
            e = "_lxsdk_rnd=" + t;
        return -1 === n.indexOf("?") ? n + "?" + e : n + "&" + e
    }
    function $n(n, t) {
        var e = u(),
            r = new e;
        return r.open(ji, Kn(n), !0),
        r.timeout = Xo,
        r.setRequestHeader("Content-Type", t),
        r
    }
    function Jn(n, t, e) {
        return bu.call(n, t) && n[t] && (n[e] = n[t], delete n[t]),
        n
    }
    function Xn(n) {
        var t = [],
            e = [{
                l: _i,
                s: yi
            },
            {
                l: fi,
                s: di
            },
            {
                l: vi,
                s: li
            },
            {
                l: pi,
                s: hi
            },
            {
                l: bi,
                s: wi
            },
            {
                l: gi,
                s: mi
            }];
        return ku.each(n, function (n) {
                var r = wu.extend(!0, {}, n);
                ku.each(e, function (n) {
                    Jn(r, n.l, n.s)
                });
                var i = [];
                ku.each(n.evs, function (n) {
                    n = wu.extend(!0, {}, n),
                    ku.each(n, function (t, e) {
                        if (-1 < e.indexOf("val_") && (n[e.replace("val_", "")] = n[e], delete n[e]), Jn(n, "refer_url", "urlr"), n[e] && "url" === e) {
                            var r = cu.hash;
                            r && (n.urlh = r),
                            delete n[e]
                        }
                    }),
                    i.push(n)
                }),
                r.evs = i,
                r[wi] === r.uuid && delete r.uuid;
                var u = r[li];
                u && (r[li] = u.replace("data_sdk_", "")),
                delete r.ua,
                t.push(r)
            }),
        t
    }
    function zn(n) {
        var t = /(^\w+\.\d+\.\d+\.\d+\.\d+)/,
            e = /(^\w+-\w+-\w+-\w+-\w+)/;
        if (e.test(n)) {
                var r = n.match(e);
                Iu.top(ii, r[1], ti)
            } else n && !t.test(n) && n.length < 100 ? Iu.top(ii, n, ti) : Iu.top(ii, "", -1)
    }
    function Hn(n, t, e) {
        var r = [];
        return r.push(n ? n : Gn()),
        r.push(t ? t : Yn()),
        r.push(e ? e : nt()),
        r.join(aa)
    }
    function Wn(n) {
        var t = Iu.get(ci);
        return t ? t.split(aa)[n] : ""
    }
    function Zn(n, t, e) {
        Iu.top(ci, Hn(n, t, e), ei)
    }
    function Gn() {
        return Wn(ia)
    }
    function Yn() {
        return Wn(ua)
    }
    function nt() {
        var n = 0,
            t = Wn(oa);
        return isNaN(t) || (n = parseInt(t)),
        n < 0 ? 0 : n
    }
    function tt(n) {
        var t = nt();
        return !0 === n && (t++, et(t)),
        (!t || -1 > t) && (t = 0, et(t)),
        t
    }
    function et(n) {
        Zn(lu, lu, n)
    }
    function rt(n) {
        var t = {};
        if (Je.test(n)) {
            var e = wu.parseQuery(n);
            return e[Ie] && (t[Ie] = e[Ie]),
            e[De] && (t[De] = e[De]),
            e[Ne] && (t[Ce] = e[Ne]),
            t
        }
        return t
    }
    function it(n) {
        var t = {
            none: !0
        };
        return new dn(function (e) {
            try {
                var r = H(ra, "4.12.0");
                !ra || !N(r) || r < 0 ? e(t) : n && Pu || Gu() ? Nn(n, "getReqId", {}, function (n, r) {
                    e(n ? t : r)
                }) : e(t)
            } catch (i) {
                e(t),
                Vn("sdk", "api-error", "", i.stack, !0)
            }
        })
    }
    function ut(n, t) {
        return new dn(function (e, r) {
            Xe(function () {
                r({
                    code: He
                })
            }, 3e3),
            Nn(n, "getEnv", {}, function (n, i) {
                if (n) r(n);
                else {
                    ra = zi.nativeSDKVer = i.sdk_ver,
                    c();
                    var u = {
                        uuid: Ie,
                        msid: je,
                        uid: Ce,
                        dpid: Fe,
                        appnm: Te,
                        union_id: Ve
                    };
                    t = t || {};
                    for (var o in u) {
                        var a = u[o];
                        i[o] && (t[a] = i[o])
                    }
                    e(t)
                }
            })
        })
    }
    function ot() {
        var n = Iu.get(si);
        if (n) {
            var t = n.split(","),
                e = /^\d+\.\d{5,}$/;
            return 3 !== t.length ? null : e.test(t[0]) && e.test(t[1]) ? {
                    lat: t[0],
                    lng: t[1],
                    tm: t[2]
                } : null
        }
        return null
    }
    function at() {
        var n = Iu.get(ii),
            t = Iu.get("iuuid") || Iu.get("uuid") || n,
            e = Gn(),
            r = Yn(),
            i = Iu.get(ai) || Iu.get(Fe),
            u = {};
        return t && (u[Ie] = t),
        e && (u[je] = e),
        n && (u[Ae] = n),
        r && (u[Ce] = r),
        i && (u[Fe] = i),
        u
    }
    function ct(n) {
        ea.push(n)
    }
    function st(n) {
        return wu.extend(!0, {}, n)
    }
    function ft(n) {
        var t = su.getElementsByTagName("meta"),
            e = M(t, "lx:appnm"),
            r = M(t, "lx:defaultAppnm"),
            i = Pu,
            u = su.domain,
            o = m();
        return d("appnm", e),
        d("defaultAppnm", r),
        Bu && Tu(Pu || e || r || u),
        Uu ? e ? 2 === o ? e : e : 2 === o ? n : i ? i : r ? r : u : e ? e : i ? i : r ? r : u
    }
    function dt() {
        var n = vu,
            t = n.replace(/^.*([A-Za-z-]+)\/com\.(sankuai(?!\.meituan\.)|meituan(?!\.sankuai\.)|dianping|sankuai\.meituan|meituan\.sankuai)\.([.A-Za-z0-9-]+)\/(\d+[.\d]+).*$/, "$4");
        return /^\d+(\.\d+)+$/.test(t) ? t : null
    }
    function vt() {
        var n = Pu === ke || Pu === we,
            t = at(),
            e = void 0,
            r = {};
        n && (r = rt(cu.href)),
        e = wu.extend(t, r),
        e.ct = Ku;
        var i = un();
        i && (e[Ee] = i);
        var u = kn();
        e[Ae] = u,
        e[Ie] || (e[Ie] = u),
        e[je] || (e[je] = On(), Zn(e[je], e.uid || "")),
        e[Ie] && zn(e[Ie]);
        var o = ft();
        wu.isStr(o) && (e[Te] = o);
        var a = dt();
        return a && (e[Le] = a),
        e
    }
    function lt(n) {
        return function (t) {
            var e = t;
            return n !== t && (e = wu.extend(n, t)),
            e.dpid && e.uid ? e : wn().then(function (n) {
                var t = {};
                return n.dpid && (t.dpid = n.dpid, n.userId && (t.uid = "" + n.userId), n.unionId && (t.union_id = n.unionId)),
                e = wu.extend(e, t)
            }, function (n) {
                return e
            })
        }
    }
    function pt(n) {
        return Yr === ta ? dn.resolve(st(na)) : Gr === ta ? new dn(function (n) {
            ct(function (t) {
                n(t)
            })
        }) : (ta = Gr, ca(n).then(function (n) {
            return na = wu.extend(!0, {}, n || {}),
            ta = Yr,
            ku.each(ea, function (t, e) {
                wu.isFunc(t) && ea[e](n)
            }),
            n
        }))
    }
    function ht() {
        function n() {
            return Math.floor(65536 * (1 + Math.random())).toString(16).substring(1)
        }
        return n() + n() + "-" + n() + "-" + n() + "-" + n() + "-" + n() + n() + n()
    }
    function gt() {
        return ht() + "." + Math.round(+new Date / 1e3)
    }
    function mt() {
        var n = Iu.get(fa);
        if (n || (n = gt(), Iu.top(fa, n, da)), n) {
            var t = n.match(sa);
            return t ? t[1] : ""
        }
        return ""
    }
    function _t() {
        return !va && la && (va = mt()),
        va
    }
    function yt(n) {
        var t = this;
        t.s = n;
        var e = void 0,
            r = vo.get(Oi) || {
                s: n,
                d: t.d
            };
        r.s !== n ? (vo.del(Oi), e = t.d = []) : e = t.d = r.d || [],
        t.l = e && e.length || 0
    }
    function bt(n) {
        return ha || (ha = new yt(n)),
        ha
    }
    function wt() {
        return ha
    }
    function xt(n, t) {
        var e = this;
        e.env = t || {},
        e.opts = wu.extend(!0, {}, n),
        Ia.push(e),
        w(e)
    }
    function St(n) {
        return n._ptpvs === rr
    }
    function kt() {
        return !Fa
    }
    function qt(n) {
        return n = n || {},
        n && !wu.isObj(n) && (n = {
            cid: "" + n
        }),
        n
    }
    function Ot(n, t, e, r, i) {
        i = i || {};
        var u = this,
            o = i,
            a = o.isLeave,
            c = o.currentPageInfo,
            s = o.mvDelay,
            f = o.sf;
        if (m() === Wr) {
                var d = Rt(u),
                    v = zt(_o.getAll()),
                    l = Kt(n, t, e, r),
                    p = l.body,
                    h = l.ev,
                    g = Ht(d, p, v);
                if (n === Sr) {
                        if (s) return wu.run(p, function (n) {
                            Da.push(n)
                        }),
                        void Xe(function () {
                            if (Da.length) {
                                var n = Ht(d, Da, v);
                                u.send(n),
                                Da = []
                            }
                        }, s * zr)
                    } else {
                        if (n === kr) return void S.call(u, kr, d, p[0], {
                            tag: v
                        });
                        if (n === wr) {
                            if (c && Ct(h, u._cpi), g = Ht(d, p, v), a) {
                                var y = U(),
                                    b = Qt(br, t, lu, y);
                                g.evs.push(b)
                            }
                            Bu && f && wt().set(t, e, f)
                        }
                    }
                u.send(g, {
                        nm: n
                    })
            } else {
                var w = u.env,
                    x = void 0,
                    k = Ut({
                        isQuickReport: !1
                    }),
                    q = [Xt.call(u, n, t, e, r)];
                if (n === wr && (x = {
                        sf: f
                    }, u._cpi && (x.cpi = u._cpi), q = [Xt.call(u, n, t, e, r, null, x)], a)) {
                        var O = U(),
                            A = Xt.call(u, br, t, null, O);
                        q.push(A)
                    }
                w[Ee] && (q = Zt(q, w));
                var I = Mt(w[ga]);
                new Date;
                Nn(I, _a, q, function (o, a) {
                        o && (_(Wr), Ot.call(u, n, t, e, r, i))
                    }, {
                        nativeOptions: k
                    })
            }
    }
    function At(n) {
        Ca = n
    }
    function It(n, t) {
        Na[n] = t
    }
    function jt() {
        return Ea || (Ea = Ft()),
        Ea
    }
    function Dt() {
        return Ea = Ft()
    }
    function Et() {
        var n = vo.get(Me);
        return n && vo.del(Me),
        n
    }
    function Ct(n, t) {
        wu.isObj(n[xi]) || (n[xi] = {}),
        n[xi][ka] = t
    }
    function Nt(n) {
        return !(!wu.isStr(n) && !n.length)
    }
    function Ft() {
        return wu.now().toString(16) + "-" + Math.floor(65535 * wu.rnd()) + "-" + Math.floor(65535 * wu.rnd())
    }
    function Tt(n) {
        var t = {};
        return t[Or] = "order",
        t[Ar] = "pay",
        t[wr] = "click",
        t[qr] = "return",
        t[Sr] = "view",
        t[xr] = "click",
        t[n]
    }
    function Lt(n) {
        var t = n.nm;
        yr === t ? (n.nm = "mpt", n.val_act = "pageview") : br === t ? (n.nm = "report", n.val_act = "quit") : (n.nm = "mge", n.event_type = Tt(t) || t),
        n.nt = 0,
        n.isauto = 8
    }
    function Vt(n) {
        var t = "data_sdk_";
        return 0 !== n.indexOf(t) && (n = t + n),
        n
    }
    function Mt(n) {
        var t = "data_sdk_";
        return 0 === n.indexOf(t) && (n = n.replace(ga, "")),
        n
    }
    function Rt(n) {
        var t = wu.extend(!0, {}, n.env);
        t[ga] = Vt(t[ga]);
        var e = t.utm,
            r = {
                ua: Vu,
                sdk_ver: Oe,
                ch: e && e.utm_source ? e.utm_source : "web",
                sc: Wu
            };
        return r[_i] = Oe,
        wu.extend(!0, r, t)
    }
    function Pt(n) {
        var t = wt(),
            e = t.toJSON();
        return e && (n[qa] = e),
        n
    }
    function Bt(n) {
        return n && n.custom && "v3" === n.custom._api
    }
    function Ut(n) {
        return n = n || {},
        {
            isQuickReport: s("QC") && !! n.isQuickReport
        }
    }
    function Qt(n, t, e, r, i) {
        i = i || er;
        var u = tt(!0),
            o = ot(),
            a = void 0,
            c = yr === n,
            s = Or === n,
            f = Ar === n,
            d = {
                nm: n,
                tm: wu.now(),
                nt: Wr,
                isauto: i,
                val_cid: t,
                req_id: jt(),
                seq: u
            };
        if (c) {
                var v = cu.href;
                d.url = v,
                a = ja,
                a && (d.refer_url = a),
                i === er && (ja = v)
            }
        return (s || c || f) && Bu && (d = Pt(d)),
        r = Ta(r, "_hguid", _t()),
        Bt(r) && !t && (d.val_cid = su.title || cu.pathname, r = Ta(r, "_cid", 1)),
        c && (r = Ta(r, "_hpid", pa())),
        e && (d[Sa] = e),
        r && (d[xi] = r),
        o && (d[Oa] = o.lat, d[Aa] = o.lng),
        d
    }
    function Kt(n, t, e, r, i) {
        var u = Qt(n, t, e, r, i);
        return {
            body: $t(u),
            ev: u
        }
    }
    function $t(n) {
        if (Da && 0 < Da.length) {
            var t = Da;
            return Da = [],
            t.push(n),
            t
        }
        return [n]
    }
    function Jt(n) {
        return Qu ? n : Ru && Fn() ? n : mu(n)
    }
    function Xt(n, t, e, r, i, u) {
        u = u || {},
        i = i || er;
        var o = this,
            a = o.env.appnm,
            c = ot(),
            s = y(),
            d = !s,
            v = void 0,
            l = {
                nm: n,
                tm: wu.now(),
                nt: Hr,
                isauto: i,
                val_cid: t,
                shouldCover: d
            };
        l = wu.extend(!0, l, Na),
        Ca && (l.req_id = Ca),
        u.sf && (l._sf = u.sf);
        var p = void 0,
            h = wu.extend(!0, {}, r || {}),
            g = yr === n;
        if (g) {
                var m = Jt(cu.href);
                p = {
                    ua: Vu,
                    url: m
                };
                var _ = un();
                _ && _.utm_source && (p.utm = _),
                v = ja,
                v && (p.refer_url = Jt(v)),
                i === er && (ja = m)
            } else p = {};
        return ku.each({
                web_req_id: jt(),
                web_sdk_ver: Oe,
                lxcuid: kn(),
                web_appnm: a,
                covered_by_native: d
            }, function (n, t) {
                wu.isStr(n) && (p[t] = n)
            }),
        wu.isObj(h.custom) && "v3" === h.custom._api && (p.web_appnm = f("appnm")),
        u.cpi && !h.page && (h.page = u.cpi),
        h.custom = wu.extend(!0, h.custom, p),
        h = Ta(h, "_hguid", _t()),
        g && (h = Ta(h, "_hpid", pa())),
        n !== xr || Ln() ? Tn() || Lt(l) : Tn() ? l.nm = wr : Lt(l),
        l[xi] = h,
        c && (l[Oa] = c.lat, l[Aa] = c.lng),
        e && (l[Sa] = e),
        g && !Tn() && (l.val_val = h, delete l[xi]),
        l
    }
    function zt(n) {
        return n
    }
    function Ht(n, t, e) {
        return ku.isArrayLike(t) || (t = [t]),
        wu.run(t, function (n) {
            n && e && (n.tag = e)
        }),
        n.evs = t,
        n
    }
    function Wt(n) {
        return Ii[n]
    }
    function Zt(n, t) {
        return ku.isArray(n) && n.length ? wu.isObj(n[0][xi]) ? wu.isObj(n[0][xi][ka]) ? (n[0][xi][ka] = wu.extend(!0, n[0][xi][ka], {
            utm: t[Ee]
        }), n) : (n[0][xi][ka] = {
            utm: t[Ee]
        }, n) : (n[0][xi] = {
            page: {
                utm: t[Ee]
            }
        }, n) : n
    }
    function Gt(n, t) {
        var e = {};
        return e[Xr] = t,
        wu.extend(e, n)
    }
    function Yt(n, t, e) {
        var r = null;
        return !wu.isStr(n) || t || e ? wu.isObj(n) && wu.isStr(t) && !e && (r = t, t = null) : (r = n, n = null),
        r && (e = wu.extend({
            cid: r
        }, e || {})),
        {
            lab: n,
            env: t,
            opts: e
        }
    }
    function ne(n, t, e, r) {
        var i = Yt(t, e, r),
            u = i.lab,
            o = i.env,
            a = i.opts;
        r = qt(a);
        var c = n.opts.cid = r.cid || n.opts.cid;
        r = wu.extend({
                cid: c
            }, r),
        o && wu.isObj(o) && ku.each(o, function (t, e) {
                n._dt.set(e, t)
            }),
        n._dt.pageView(u, r)
    }
    function te(n, t) {
        this.env = n || {},
        this.opts = t || {},
        this._t = []
    }
    function ee(n, t) {
        wu.isStr(n) && (t = wu.isFunc(t) && t ||
        function () {}, "on" + n in au || "KNB:" + n in au ? wu.on(window, n, function (n) {
            t(n)
        }) : (Qa = window.KNB, Qa && wu.isFunc(Qa.subscribe) && Qa.subscribe({
            action: n,
            handle: function () {
                t()
            },
            success: function () {},
            fail: function (n) {}
        })))
    }
    function re() {
        try {
            ee("appear", Ua.appear),
            ee("disappear", Ua.disappear),
            Ka && (ee("foreground", Ua.foreground), ee("background", Ua.background))
        } catch (n) {
            Vn("sdk", "api-error", "", n.stack, !0)
        }
        Ma = ue()
    }
    function ie(n, t) {
        return {
            cb: n,
            cmd: t
        }
    }
    function ue() {
        return za
    }
    function oe() {
        b(!1),
        it(Ha).then(function (n) {
            var t = n || {},
                e = t.val_ref,
                r = t.req_id,
                i = t.refer_req_id,
                u = !! (r || e || i);
            r && za._setRequestID(r),
            e && za._setNativeEvsData("val_ref", e),
            i && za._setNativeEvsData("refer_req_id", i),
            b(u)
        })
    }
    function ae(n, t) {
        if (Yr === Xa) n && n(za);
        else if (Gr === Xa) n && Ja.push(ie(n, t));
        else {
            wu.now();
            Ja = Ja.concat(ie(n, t));
            var e = su.getElementsByTagName("meta"),
                r = M(e, "lx:cid") || zi.cid;
            if (Ha = M(e, "lx:category"), !Ha) return void(Xa = Zr);
            Xa = Gr;
            var i = M(e, "lx:mvDelay");
            i = isNaN(i) ? 0 : parseInt(i, 10);
            var u = "off" !== M(e, "lx:autopv");
            zi.autoPV = u,
            Xe(oe, 1e3),
            dn.all([pt(Ha)]).then(function (n) {
                    var t = n[0],
                        e = t.appnm;
                    !wu.isStr(e) || e === su.domain,
                    za = new te(t, {
                            cid: r,
                            isDefault: !0,
                            mvDelay: i
                        }),
                    Ha && za.create(Ha, {
                            isDefault: !0
                        }),
                    t = wu.extend(!0, za._dt.env, t),
                    za._dt.env = t;
                    try {
                            var o = [];
                            ku.each(Ja, function (n) {
                                var e = n.cb,
                                    r = n.cmd;
                                "config" === r || "set" === r ? e(za, t) : o.push(n)
                            }),
                            Bu && bt(t.msid),
                            u && Ha && r && r && za._initPV(t, r),
                            $a.hook(function () {}),
                            ku.each(o, function (n) {
                                n && n.cb && n.cb(za, t)
                            })
                        } catch (a) {}
                }).then(function () {
                    Xa = Yr
                }, function (n) {
                    throw Xa = Yr,
                    n
                })
        }
    }
    function ce(n) {
        n = oc(n, n.val);
        var t = fc(n, !0);
        return [Rr, t, null, n[Lr]]
    }
    function se(n) {
        var t = tc(n);
        n = t[0];
        var e = void 0;
        return t[1] && (e = t[1]),
        [n, e]
    }
    function fe(n, t, e, r, i) {
        if (wu.isFunc(t)) t.call(n, n, r, i);
        else if (!i && wu.isStr(t) && wu.isFunc(n[t])) return n[t].apply(n, e)
    }
    function de() {
        if (!xc) {
            xc = !0;
            var n = void 0,
                t = void 0;
            $u && wu.on(su, "mouseup", function (t) {
                    var e = t.target || t.srcElement,
                        r = e.tagName + e.href;
                    r = r.toLocaleLowerCase(),
                    1 === e.nodeType && /^ajavascript:/i.test(r) && (n = new Date)
                });
            var e = !1,
                r = au.onbeforeunload;
            Bu && Qu ? au.addEventListener("pagehide", W(e, $u, n, t, le, lu, l)) : au.onbeforeunload = W(e, $u, n, t, le, r, l)
        }
    }
    function ve() {
        function n() {
            var n = R();
            n && (n.q.push = function l(n) {
                try {
                    var e = gc(n),
                        o = e ? e[0] : "";
                    if (ku.isArray(o)) return void Ou(e, function (n) {
                            l(n)
                        });
                    "start" === o ? (r = !0, i || t(u)) : !1 === r ? e && u.push(e) : le.apply(lu, e)
                } catch (a) {
                    try {
                        Vn("sdk", "api-error", "", a.stack, !0)
                    } catch (a) {}
                }
            });
            for (var e = void 0, o = void 0, a = [], c = [], s = [], f = n && ku.isArray(n.q) ? n.q : [], d = 0, v = f.length; d < v; d++) o = f[d][0],
            "config" === o ? c.push(f[d]) : e || "use" !== o ? s.push(f[d]) : (a.push(f[d]), e = !0);
            return f = c.concat(a.concat(s))
        }
        function t(n) {
            i || (n && ku.each(n, function (n) {
                var t = gc(n),
                    e = t ? t[0] : "";
                return ku.isArray(e) ? void Ou(t, function (n) {
                        le.apply(lu, n)
                    }) : void(e && le.apply(lu, t))
            }), le(function () {
                de()
            }), i = !0)
        }
        var e = Zu && !au.KNB && Sc;
        if (e) return qc && ze(qc),
        void(qc = Xe(function () {
            Sc--,
            ve()
        }, kc));
        var r = !0,
            i = !1,
            u = n();
        if (0 === u.length) ae(function (n) {
                wc = n,
                de()
            });
        else try {
                u = Au(u, function (n) {
                    var t = gc(n),
                        e = t ? t[0] : "";
                    if ("config" === e) {
                            var i = t[1],
                                u = t[2];
                            "autoStart" === i && !1 === u && (r = !1)
                        }
                    return t
                }),
                r && t(u)
            } catch (o) {}
    }
    function le(n) {
        var t = arguments;
        if (t.length) {
            var e = ku.slice(t, 1, t.length);
            try {
                wc ? fe(wc, n, e, wc._dt ? wc._dt.env : null) : ae(function (t, r, i) {
                    wc = t,
                    fe(t, n, e, r, i),
                    de()
                }, n)
            } catch (r) {
                try {
                    Vn("sdk", "api-error", "", r.message + "\n" + r.stack, !0)
                } catch (r) {}
            }
        }
    }
    function pe(n) {
        Ac && ze(Ac),
        Oc || (Oc = !0, ve())
    }
    var he = !0,
        ge = !1,
        me = "_MeiTuanALogObject",
        _e = 1,
        ye = 0,
        be = "dianping_nova",
        we = "waimai",
        xe = "moviepro",
        Se = "movie",
        ke = "group",
        qe = "demo",
        Oe = "4.8.2",
        Ae = "lxcuid",
        Ie = "uuid",
        je = "msid",
        De = "cityid",
        Ee = "utm",
        Ce = "uid",
        Ne = "userid",
        Fe = "dpid",
        Te = "appnm",
        Le = "app",
        Ve = "union_id",
        Me = "pd_data",
        Re = /dp\/com\.dianping\.[\w.]+\/([\d.]+)/i,
        Pe = /\bmeituanwaimai-c\/\d+\./i,
        Be = /\bmoviepro/i,
        Ue = /\bmaoyan\b/i,
        Qe = /\bmeituan \d+|meituangroup\/\d+\./i,
        Ke = /\bandroid|mobile\b|\bhtc\b/i,
        $e = /\btitans(no){0,1}x\b/i,
        Je = /^(([^? \r\n]*)\?)?([^?# \r\n]+)(#\S+)?$/,
        Xe = setTimeout,
        ze = clearTimeout,
        He = 1,
        We = 2,
        Ze = 3,
        Ge = 4,
        Ye = 5,
        nr = 6,
        tr = 20,
        er = 7,
        rr = 6,
        ir = /android/i,
        ur = /iphone/i,
        or = /ipad/i,
        ar = "android",
        cr = "iphone",
        sr = "ipad",
        fr = "www",
        dr = "i",
        vr = "statistics://_lx/?data=",
        lr = "lxlog",
        pr = 200,
        hr = 100,
        gr = 500,
        mr = 600,
        _r = -1,
        yr = "PV",
        br = "PD",
        wr = "MC",
        xr = "SC",
        Sr = "MV",
        kr = "MVL",
        qr = "ME",
        Or = "BO",
        Ar = "BP",
        Ir = "click",
        jr = "tap",
        Dr = "view",
        Er = "return",
        Cr = "order",
        Nr = "pay",
        Fr = "event_type",
        Tr = "val_act",
        Lr = "val_cid",
        Vr = "index",
        Mr = "element_id",
        Rr = "pageView",
        Pr = "pageDisappear",
        Br = "systemCheck",
        Ur = "moduleView",
        Qr = "moduleClick",
        Kr = "moduleEdit",
        $r = Cr,
        Jr = Nr,
        Xr = "order_id",
        zr = 1e3,
        Hr = 2,
        Wr = 0,
        Zr = -1,
        Gr = 0,
        Yr = 1,
        ni = 10080,
        ti = 1576800,
        ei = 30,
        ri = "_lx_utm",
        ii = "_lxsdk",
        ui = "_lxsdk_unoinid",
        oi = "_lxsdk_cuid",
        ai = "_lxsdk_dpid",
        ci = "_lxsdk_s",
        si = "latlng",
        fi = "msid",
        di = "ms",
        vi = "category",
        li = "c",
        pi = "login_type",
        hi = "lt",
        gi = "locate_city_id",
        mi = "lci",
        _i = "sdk_ver",
        yi = "sv",
        bi = "lxcuid",
        wi = "lxid",
        xi = "val_lab",
        Si = "val_bid",
        ki = "val_val",
        qi = "custom",
        Oi = "sf",
        Ai = "__$lx_beacon_",
        Ii = {
            category: he,
            union_id: he,
            lxcuid: he,
            app: he,
            sdk_ver: he,
            appnm: he,
            ch: he,
            lch: he,
            ct: he,
            did: he,
            dm: he,
            ua: he,
            msid: he,
            uuid: he,
            lat: he,
            log: he,
            net: he,
            os: he,
            idfa: he,
            pushid: he,
            subcid: he,
            mac: he,
            imsi: he,
            uid: he,
            logintype: he,
            cityid: he,
            apn: he,
            mno: he,
            pushSetting: he,
            wifi: he,
            bht: he,
            ip: he,
            vendorid: he,
            geohash: he,
            dtk: he,
            sns: he,
            android_id: he,
            version_code: he,
            brand: he,
            utm: he
        },
        ji = "post",
        Di = "validation",
        Ei = "__lx" + Di,
        Ci = ".sankuai.com",
        Ni = "report.meituan.com",
        Fi = "send",
        Ti = "use",
        Li = "event",
        Vi = "mge",
        Mi = "mpt",
        Ri = "report",
        Pi = function () {},
        Bi = function () {
            var n = u(),
                t = n && "withCredentials" in new n;
            return function () {
                    return t
                }
        }(),
        Ui = /__lxvalidation=([\w.]+)/i,
        Qi = 10,
        Ki = !1,
        $i = void 0,
        Ji = void 0,
        Xi = {},
        zi = {
            nativeSDKVer: null,
            pageValLab: null,
            pageEnv: null,
            use_post: !1,
            cid: null,
            appnm: null,
            quit: null,
            useQuickReport: !1,
            onWebviewAppearAutoPV: !0
        },
        Hi = {
            MVL: !1,
            QC: !1,
            getReqId: !1
        },
        Wi = [];
    zi.on = function (n, t) {
            Wi.push({
                name: n,
                fn: t
            })
        },
    zi.emit = function (n, t, e, r, i) {
            ku.each(Wi, function (u) {
                var o = u.name,
                    a = u.fn;
                o === n && a(t, e, r, i)
            })
        };
    var Zi = void 0,
        Gi = Wr,
        Yi = !1,
        nu = 5e3,
        tu = 50,
        eu = {
            MVL: {}
        },
        ru = void 0,
        iu = void 0;
    Xe(x, 100);
    var uu = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ?
    function (n) {
            return typeof n
        } : function (n) {
            return n && "function" == typeof Symbol && n.constructor === Symbol && n !== Symbol.prototype ? "symbol" : typeof n
        },
        ou = 1e3,
        au = e(),
        cu = t(),
        su = r(),
        fu = su.domain,
        du = i(),
        vu = du.userAgent.toString(),
        lu = void 0,
        pu = Array.prototype,
        hu = Object.prototype,
        gu = decodeURIComponent,
        mu = encodeURIComponent,
        _u = E(),
        yu = hu.toString,
        bu = hu.hasOwnProperty,
        wu = {};
    wu.trim = function (n) {
            return n.replace(/^[\s\uFEFF\xA0\u3000]+|[\s\uFEFF\xA0\u3000]+$/g, "")
        },
    wu.now = E,
    wu.rnd = C,
    wu.hasOwn = function (n, t) {
            return bu.call(n, t)
        },
    wu.extend = T;
    var xu = function (n) {
            return n && "[object Object]" === yu.call(n)
        };
    wu.isObj = xu;
    var Su = function (n) {
            return D(n, "string")
        };
    wu.isStr = Su,
    wu.isFunc = function (n) {
            return D(n, "function")
        },
    wu.attr = function (n, t) {
            return n.getAttribute(t)
        },
    wu.parseQuery = function (n) {
            var t = {};
            if (n) {
                var e = n.replace(Je, function (n, t, e, r) {
                    return r || ""
                }).split("&");
                return ku.each(e, function (n) {
                    var e = n.split("="),
                        r = e[0],
                        i = e[1] || "";
                    r && !bu.call(t, r) && (t[r] = gu(i))
                }),
                t
            }
        },
    wu.stringifyQuery = function (n) {
            var t = [];
            return wu.isObj(n) && ku.each(n, function (n, e) {
                wu.isFunc(n) || ((lu === n || F(n)) && (n = n || ""), t.push(mu(e) + "=" + mu(n)))
            }),
            t.join("&")
        },
    wu.genReqId = function () {
            return "" + E() * ou + parseInt(C() * ou)
        },
    wu.run = function (n, t) {
            qu(n) ? ku.each(n, t) : t(n)
        },
    wu.on = function (n, t, e) {
            n.addEventListener ? n.addEventListener(t, e, !1) : n.attachEvent && n.attachEvent("on" + t, e)
        },
    wu.off = function (n, t, e) {
            n.removeEventListener ? n.removeEventListener(t, e, !1) : n.detachEvent && n.detachEvent("on" + t, e)
        };
    var ku = {};
    ku.isArray = function (n) {
            return "[object Array]" === yu.call(n)
        };
    var qu = function (n) {
            if (!n) return !1;
            var t = n.length;
            return !!ku.isArray(n) || !! (n && N(t) && t >= 0) && (!wu.isObj(n) || (!(t > 1) || t - 1 in n))
        };
    ku.isArrayLike = qu,
    ku.find = function (n, t, e) {
            var r = void 0;
            return qu(n) && ku.each(n, function (i, u) {
                if (!0 === t.call(e, i, u, n)) return r = i,
                !1
            }),
            r
        },
    ku.filter = function (n, t, e) {
            var r = [];
            return qu(n) && ku.each(n, function (i, u) {
                t.call(e, i, u, n) && r.push(i)
            }),
            r
        },
    ku.toArray = function (n, t, e) {
            var r = [];
            return qu(n) && ku.each(n, function (n) {
                r.push(t ? t.call(e, n) : n)
            }, e),
            r
        };
    var Ou = function (n, t, e) {
            if (n) {
                var r = void 0,
                    i = void 0,
                    u = void 0,
                    o = void 0,
                    a = !1;
                if (qu(n)) for (i = 0, u = n.length; i < u && (o = t.call(e, n[i], i, n), a !== o); i++);
                else for (r in n) if (wu.hasOwn(n, r) && (o = t.call(e, n[r], r, n), a === o)) break
            }
        };
    ku.each = Ou;
    var Au = function (n, t, e) {
            if (n) {
                for (var r = [], i = 0, u = n.length; i < u; i++) {
                    var o = t.call(e, n[i], i, n);
                    r.push(o)
                }
                return r
            }
        };
    ku.slice = function (n, t, e) {
            return pu.slice.call(ku.toArray(n), t, e)
        },
    ku.reduce = function (n, t) {
            if (qu(n) && wu.isFunc(t)) {
                var e = n,
                    r = e.length >>> 0,
                    i = 0,
                    u = void 0,
                    o = arguments;
                if (3 === o.length) u = o[2];
                else {
                        for (; i < r && !(i in e);) i++;
                        if (i >= r) return;
                        u = e[i++]
                    }
                for (; i < r;) i in e && (u = t(u, e[i], i, e)),
                i++;
                return u
            }
        };
    var Iu = {};
    Iu.del = function (n, t) {
            var e = n + "=;path=/;domain=" + t,
                r = new Date;
            return r.setFullYear(1970),
            e += ";expires=" + r.toUTCString(),
            su.cookie = e,
            !0
        },
    Iu.get = function (n) {
            var t = su.cookie.match(new RegExp("(?:^|;)\\s*" + n + "=([^;]+)"));
            return gu(t ? t[1] : "")
        },
    Iu.set = function (n, t, e, r) {
            r = r || su.domain;
            var i = void 0,
                u = void 0,
                o = void 0,
                a = n + "=" + mu(t) + ";path=/;domain=" + r;
            lu === e || isNaN(e) || (i = new Date, u = 60 * parseInt(e, 10) * 1e3, o = i.getTime() + u, i.setTime(o), a += ";expires=" + i.toUTCString());
            try {
                    return su.cookie = a,
                    !0
                } catch (c) {
                    return !1
                }
        },
    Iu.top = function (n, t, e) {
            var r = su.domain,
                i = r.split("."),
                u = i.length,
                o = u - 1,
                a = void 0,
                c = !1;
            for (t = "" + t; !c && o >= 0 && (r = i.slice(o, u).join("."), Iu.set(n, t, e, r), a = Iu.get(n), lu !== a && (c = a === t), o--, !c););
        },
    Iu.del = function (n) {
            return Iu.top(n, "", -100)
        };
    var ju = function () {
            var n = void 0;
            return {
                update: function (t) {
                    n = t
                },
                get: function () {
                    return n
                }
            }
        }(),
        Du = 0,
        Eu = 4,
        Cu = "",
        Nu = function (n) {
            Eu = n
        },
        Fu = function () {
            return Cu && 3 === Eu
        },
        Tu = function (n) {
            Cu = n
        },
        Lu = function () {
            return Cu
        },
        Vu = vu,
        Mu = [{
            n: qe,
            r: /lingxi\/demo\/\d+/i,
            v: Vu
        },
        {
            n: be,
            r: Re,
            v: Vu
        },
        {
            n: we,
            r: Pe,
            v: Vu
        },
        {
            n: xe,
            r: Be,
            v: Vu
        },
        {
            n: Se,
            r: Ue,
            v: Vu
        },
        {
            n: ke,
            r: Qe,
            v: Vu
        }],
        Ru = /android/i.test(Vu),
        Pu = "",
        Bu = Ru,
        Uu = !1,
        Qu = !1,
        Ku = fr,
        $u = !1,
        Ju = -1;
    if (Ke.test(Vu)) {
            Ku = dr,
            Bu = !0,
            ku.each(Mu, function (n) {
                if (n.r.test(n.v)) return Pu = n.n,
                !1
            }),
            $e.test(Vu) && (Uu = !0);
            var Xu = ur.test(Vu),
                zu = or.test(Vu);
                (Xu || zu) && (Qu = !0),
            Pu && (Xu ? Ku = cr : ir.test(Vu) ? Ku = ar : zu && (Ku = sr))
        } else {
            var Hu = Vu.match(/(msie) (\d+)|Trident\/(d+)/i);
            Hu && ($u = !0, Hu && (Ju = parseInt(Hu[2], 10)))
        }
    var Wu = au.screen.width + "*" + au.screen.height,
        Zu = Uu || / knb\/\d+/i.test(vu),
        Gu = function () {
            var n = au.KNB;
            return Bu && Zu && n && n.isApiSupported
        },
        Yu = vu.replace(/^.*TitansX\/([\d.]+)\s.*$/i, "$1"),
        no = Ee + "_source",
        to = Ee + "_medium",
        eo = Ee + "_term",
        ro = Ee + "_campaign",
        io = Ee + "_content",
        uo = void 0,
        oo = ge,
        ao = au.JSON;
    ao || (ao = {
            parse: function (n) {
                return new Function("return (" + n + ")")()
            },
            stringify: function () {
                var n = ku.isArray,
                    t = {
                        '"': '\\"',
                        "\\": "\\\\",
                        "\b": "\\b",
                        "\f": "\\f",
                        "\n": "\\n",
                        "\r": "\\r",
                        "\t": "\\t"
                    },
                    e = function (n) {
                        return t[n] || "\\u" + (n.charCodeAt(0) + 65536).toString(16).substr(1)
                    },
                    r = /[\\"\u0000-\u001F\u2028\u2029]/g;
                return function i(t) {
                        if (null == t) return "null";
                        if (D(t, "number")) return isFinite(t) ? t.toString() : "null";
                        if (D(t, "boolean")) return t.toString();
                        if (D(t, "object")) {
                            if ("function" === j(t.toJSON)) return i(t.toJSON());
                            if (n(t)) {
                                for (var u = "[", o = 0; o < t.length; o++) u += (o ? ", " : "") + i(t[o]);
                                return u + "]"
                            }
                            if (wu.isObj(t)) {
                                var a = [];
                                for (var c in t) t.hasOwnProperty(c) && a.push(i(c) + ": " + i(t[c]));
                                return "{" + a.join(", ") + "}"
                            }
                        }
                        return '"' + t.toString().replace(r, e) + '"'
                    }
            }()
        });
    var co = ao,
        so = "__lxsdk_",
        fo = au.localStorage,
        vo = {
            get: function (n) {
                n = on(n);
                var t = fo.getItem(n);
                return t = lu !== t ? co.parse(t) : t
            },
            set: function (n, t) {
                return vo.del(n),
                fo.setItem(on(n), co.stringify(t))
            },
            keys: function Ic() {
                for (var Ic = [], n = void 0, t = 0; t < fo.length; t++) n = fo.key(t),
                0 === n.indexOf(so) && Ic.push(n.replace(so, ""));
                return Ic
            },
            del: function (n) {
                try {
                    return fo.removeItem(on(n))
                } catch (t) {}
            },
            clear: function () {
                for (var n = this.keys(), t = 0; t < n.length; t++) this.del(n[t])
            }
        };
    if (fo) {
            if (fo) {
                var lo = "___lxtest";
                vo.nt = !0;
                try {
                    vo.set(lo, 1);
                    var po = vo.get(lo);
                    1 !== po ? vo.clear() : vo.del(lo)
                } catch (ho) {
                    try {
                        vo.clear(),
                        fo.setItem(lo, 1),
                        fo.removeItem(lo)
                    } catch (ho) {
                        fo = an(),
                        vo.nt = !1
                    }
                }
            }
        } else fo = an(),
    vo.nt = !1;
    var go = "tag",
        mo = 18e5,
        _o = {
            set: function (n, t, e) {
                var r = void 0,
                    i = [],
                    u = vo.get(go) || [];
                if (!wu.isStr(t) || "" === t) return !1;
                for (var o = 0, a = u.length; o < a; o++) r = u[o],
                sn(r) || (n === r.c ? t !== r.k && i.push(r) : i.push(r));
                return r = new cn(n, t, e, (+new Date)),
                i.push(r.toJSON()),
                vo.set(go, i),
                !0
            },
            get: function (n, t) {
                var e = void 0,
                    r = vo.get(go);
                if (r && r.length) return e = {},
                ku.each(r, function (n) {
                        var t = {};
                        t[n.k] = n.v,
                        sn(n) || (e[n.c] = wu.extend(!0, e[n.c] || {}, t))
                    }),
                n && t ? e[n] && e[n][t] : n ? e[n] : e
            },
            getAll: function () {
                var n = vo.get(go),
                    t = {},
                    e = void 0;
                return ku.each(n, function (n) {
                        var r = void 0;
                        !sn(n) && n.v && (e = !0, r = {}, r[n.k] = n.v, t[n.c] = wu.extend(!0, t[n.c], r))
                    }),
                e && t
            },
            clear: function (n, t) {
                var e = arguments.length;
                if (!e) return vo.set(go, []);
                if (wu.isStr(n)) {
                    var r = vo.get(go),
                        i = [];
                    ku.each(r, function (e) {
                            (t !== lu && e.k !== t || n !== e.c) && i.push(e)
                        }),
                    vo.set(go, i)
                }
            }
        };
    dn.prototype.then = function (n, t) {
            return ln(this, new dn(fn), n, t)
        },
    dn.all = function (n) {
            return new dn(function (t, e) {
                for (var r = 0, i = n.length, u = [], o = 0, a = void 0, c = function (n) {
                    var t = [];
                    for (r = 0; r < i; r++) t.push(n[r] ? n[r].value : void 0);
                    return t
                }, s = function (n) {
                    return function (e) {
                        if (n.value = e, n.state = bo, o++, o === n.len && !a) {
                            var r = c(u);
                            t(r)
                        }
                    }
                }, f = function (n) {
                    return function (t) {
                        n.value = t,
                        n.state = yo,
                        o++,
                        a || (a = !0, e(t))
                    }
                }, d = function () {
                    var t = n[r],
                        e = {
                            value: null,
                            index: r,
                            state: null,
                            len: i
                        };
                    u.push(e),
                    !
                    function (n) {
                            t.then ? t.then(s(n), f(n)) : dn.resolve(t).then(s(n), f(n))
                        }(e)
                }; r < i; r++) d()
            })
        },
    dn.resolve = function (n) {
            if (n instanceof dn) return n;
            if (wu.isFunc(n.then)) {
                var t = n.then.bind(n);
                return new dn(function (n, e) {
                    t(n, e)
                })
            }
            return new dn(function (t) {
                t(n)
            })
        },
    dn.reject = function (n) {
            return new dn(function (t, e) {
                e(n)
            })
        };
    var yo = 0,
        bo = 1,
        wo = 2,
        xo = "function",
        So = "object";
    dn.prototype._state = wo,
    dn.prototype._pCount = 0;
    var ko = !1,
        qo = 2e3,
        Oo = [],
        Ao = !1,
        Io = void 0,
        jo = 500,
        Do = "getUserInfo",
        Eo = void 0,
        Co = function () {
            var n = function () {
                for (var n = 1 * new Date, t = 0; n === 1 * new Date && t < 200;) t++;
                return n.toString(16) + t.toString(16)
            },
                t = function () {
                    return Math.random().toString(16).replace(".", "")
                },
                e = function () {
                    function n(n, t) {
                        var e = void 0,
                            r = 0;
                        for (e = 0; e < t.length; e++) r |= i[e] << 8 * e;
                        return n ^ r
                    }
                    var t = Vu,
                        e = void 0,
                        r = void 0,
                        i = [],
                        u = 0;
                    for (e = 0; e < t.length; e++) r = t.charCodeAt(e),
                    i.unshift(255 & r),
                    i.length >= 4 && (u = n(u, i), i = []);
                    return i.length > 0 && (u = n(u, i)),
                    u.toString(16)
                };
            return function () {
                    var r = (screen.height * screen.width).toString(16);
                    return n() + "-" + t() + "-" + e() + "-" + r + "-" + n()
                }
        }(),
        No = 5e3,
        Fo = "getEnv",
        To = hr,
        Lo = !1,
        Vo = !1,
        Mo = !1,
        Ro = !1,
        Po = [],
        Bo = 0,
        Uo = void 0,
        Qo = wu.now(),
        Ko = Cn.prototype;
    Ko.send = function (n) {
            var t = this,
                e = En(t),
                r = vr + mu(co.stringify(e)),
                i = wu.now(),
                u = 5e3 < i - Qo;
            Uo && u && t._mn === Fo && To === pr ? n(0, Uo) : An(lr, r, function (t, e) {
                    n(t, e)
                })
        };
    var $o = 3,
        Jo = 150,
        Xo = 5e3,
        zo = 3500,
        Ho = !1,
        Wo = [],
        Zo = [],
        Go = 0,
        Yo = 0,
        na = {},
        ta = Zr,
        ea = [],
        ra = null,
        ia = 0,
        ua = 1,
        oa = 2,
        aa = "|",
        ca = function (n) {
            var t = vt();
            if (n && Pu || Gu()) {
                var e = ut(n, t),
                    r = be === Pu;
                return r && (e = e.then(lt(t), function (n) {
                        return lt(t)()
                    })),
                e.then(function (n) {
                        var e = ft(n[Te]),
                            r = n[Fe],
                            i = n[Ie],
                            u = n[Ve],
                            o = n;
                        return n !== t && (o = wu.extend(t, n)),
                        wu.isStr(e) && (o[Te] = e),
                        i && zn(i),
                        r && Iu.top(ai, r, ti),
                        u && Iu.top(ui, u, ti),
                        o
                    }, function (n) {
                        return t
                    })
            }
            var i = st(t);
            return dn.resolve(i)
        },
        sa = /([a-fA-F0-9-]+)(\.\d+)/,
        fa = "_hc.v",
        da = 525600,
        va = "",
        la = /(dper|dianping|51ping)\.com/.test(fu),
        pa = function () {
            var n = void 0;
            try {
                var t = document;
                if (t.querySelectorAll) {
                    var e = t.querySelectorAll("head script"),
                        r = t.querySelectorAll("body script"),
                        i = [];
                    ku.each(e, function (n) {
                            i.push(n)
                        }),
                    ku.each(r, function (n) {
                            i.push(n)
                        });
                    for (var u = 0; u < i.length; u++) {
                            var o = i[u].innerHTML,
                                a = o.match(/\[['"]\s*_setPageId\s*['"]\s*,\s*(\d+)\s*\]/);
                            if (a) {
                                    n = a[1];
                                    break
                                }
                        }
                }
            } catch (c) {}
            return function () {
                return n
            }
        }();
    yt.prototype = {
            constructor: yt,
            set: function (n, t, e) {
                var r = this,
                    i = r.l,
                    u = r.d,
                    o = r.indexOf(n),
                    a = i > 0 ? u[i - 1].scid + 1 : 0,
                    c = {
                        scid: a,
                        cid: n,
                        bid: t,
                        sf: e
                    }; - 1 < o ? u.splice(o, i - o, c) : u.push(c),
                r.l = u.length,
                vo.set(Oi, {
                        s: r.s,
                        d: u
                    })
            },
            indexOf: function (n) {
                for (var t = this, e = t.d || [], r = 0, i = e.length; r < i; r++) {
                    var u = e[r];
                    if (u.cid === n) return r
                }
                return -1
            },
            toJSON: function () {
                var n = this.d;
                return n && n.length ? n : null
            }
        };
    var ha = null,
        ga = "category",
        ma = "setEnv",
        _a = "setEvs",
        ya = "setTag",
        ba = "getTag",
        wa = "getSFrom",
        xa = -1,
        Sa = "val_bid",
        ka = "page",
        qa = "s_from",
        Oa = "lat",
        Aa = "lng",
        Ia = [],
        ja = su.referrer,
        Da = [],
        Ea = void 0,
        Ca = void 0,
        Na = {},
        Fa = 0,
        Ta = function (n, t, e) {
            if (e) {
                var r = {},
                    i = {
                        custom: r
                    };
                r[t] = e,
                n = wu.extend(!0, n || {}, i)
            }
            return n
        },
        La = xt.prototype;
    La.set = function (n, t, e) {
            var r = this,
                i = r.env;
            if (wu.isObj(n)) return void Ou(n, function (n, t) {
                    r.set(t, n)
                });
            if (i[n] = t, d(n, t), "utm" === n && wu.isObj(t) && tn(t), Hr !== m() || Wt(n)) wu.isFunc(e) && e(i, r);
            else {
                    var u = {},
                        o = Mt(i[ga]);
                    u[n] = t,
                    Nn(o, ma, u, function () {
                            wu.isFunc(e) && e(i, r)
                        })
                }
        },
    La.get = function (n, t) {
            var e = this;
            wu.isFunc(t) && t(e.env[n], e)
        },
    La.pageView = function (t, e) {
            e = qt(e) || {};
            var r = void 0,
                i = this,
                u = i.opts.cid,
                o = e.cid || u,
                a = e.isauto || er,
                c = e.isAutoInit,
                s = e.reportStatus,
                f = u && !(St(i) || c) && !kt(),
                d = s === Wr || Wr === m(),
                p = i.env;
            if (this._cpi = t, f && !l()) {
                    var h = U(!0);
                    r = d ? Qt(br, u, null, h) : Xt.call(i, br, u, null, h),
                    v(ye)
                }
            if (u && (St(i) || kt()) || Dt(), i.opts.cid = o, d) {
                    var g = Rt(i),
                        y = zt(_o.getAll()),
                        b = Kt(yr, o, null, t, a).body;
                    f && r && b.unshift(r);
                    var w = Ht(g, b, y);
                    this.send(w, {
                            nm: yr
                        }),
                    c || Fa++
                } else {
                    var x = [Xt.call(i, yr, o, null, t)];
                    f && r && x.push(r),
                    ku.each(x, function (n) {
                        n.appnm = p.appnm
                    }),
                    Nn(Mt(p[ga]), _a, x, function (r, u) {
                        r ? (_(Wr), i.pageView(t, e), Vn(cu.href, "native-report-error", i.env.union_id, n(r))) : c || Fa++
                    })
                }
            i._ptpvs = c ? rr : er
        },
    La.pageDisappear = function (n, t) {
            t = wu.extend({}, t);
            var e = this,
                r = t.cid || e.opts.cid,
                i = t.getDurationFromLastPV || !1,
                u = t.shouldStore;
            v(_e);
            var o = U(i);
            if (n = wu.extend(o, n), Wr === m() || u) {
                    var a = Rt(e),
                        c = Qt(br, r, null, n),
                        s = zt(_o.getAll()),
                        f = Ht(a, c, s);
                    u && vo.nt ? (Fu() && (f[Te] = Lu()), vo.set(Me, f)) : e.send(f)
                } else {
                    var d = this.env,
                        l = [Xt.call(e, br, r, null, n)],
                        p = Mt(d[ga]);
                    Nn(p, _a, l, function (r, i) {
                            r && (_(Wr), e.pageDisappear(n, t))
                        })
                }
            A()
        },
    La.systemCheck = function (n, t, e) {
            e = wu.extend({}, e);
            var r = this,
                i = e.cid || r.opts.cid,
                u = !! e.isLXLog;
            if (Wr === m()) {
                    var o = Rt(r),
                        a = Kt(xr, i, n, t).body,
                        c = zt(_o.getAll()),
                        s = Ht(o, a, c);
                    u && (o.category = "others"),
                    this.send(s)
                } else {
                    var f = r.env,
                        d = [Xt.call(r, xr, i, n, t)],
                        v = Mt(f[ga]);
                    u && (v = "others"),
                    Nn(v, _a, d, function (i, u) {
                            i && (_(Wr), r.systemCheck(n, t, e))
                        })
                }
        },
    La.moduleView = function (n, t, e) {
            e = wu.extend({}, e);
            var r = this,
                i = r.opts.mvDelay || e.delay,
                u = e.cid || r.opts.cid;
            Ot.call(r, Sr, u, n, t, {
                    mvDelay: i
                })
        },
    La.moduleViewList = function (n, t, e) {
            e = wu.extend({}, e);
            var r = this,
                i = r.opts.mvDelay || e.delay,
                u = e.cid || r.opts.cid,
                o = s("MVL");
            m() !== Hr || o ? Ot.call(r, kr, u, n, t) : Ot.call(r, Sr, u, n, t, {
                    mvDelay: i
                })
        },
    La.moduleClick = function (n, t, e) {
            e = wu.extend({}, e);
            var r = this,
                i = e.cid || r.opts.cid,
                u = e.sf;
            e && e.isLeave && v(_e);
            var o = e.withPageInfo && wu.isObj(r._cpi) ? r._cpi : lu;
            Ot.call(r, wr, i, n, t, {
                    currentPageInfo: o,
                    isLeave: e.isLeave,
                    sf: u
                })
        },
    La.moduleEdit = function (n, t, e) {
            e = wu.extend({}, e);
            var r = this,
                i = e.cid || r.opts.cid;
            Ot.call(r, qr, i, n, t, e)
        },
    La.order = function (n, t, e) {
            e = wu.extend({}, e);
            var r = this,
                i = e.cid || r.opts.cid;
            if (Q(n, t), Wr === m()) {
                    var u = Rt(this),
                        o = Kt(Or, i, n, t).body,
                        a = zt(_o.getAll()),
                        c = Ht(u, o, a);
                    this.send(c)
                } else {
                    var s = this.env,
                        f = [Xt.call(r, Or, i, n, t)],
                        d = Mt(s[ga]);
                    Nn(d, _a, f, function (i, u) {
                            i && (_(Wr), r.order(n, t, e))
                        })
                }
        },
    La.pay = function (n, t, e) {
            e = wu.extend({}, e);
            var r = this,
                i = e.cid || r.opts.cid;
            if (Q(n, t), Wr === m()) {
                    var u = Rt(r),
                        o = Kt(Ar, i, n, t).body,
                        a = zt(_o.getAll()),
                        c = Ht(u, o, a);
                    this.send(c, {
                            cb: function () {
                                _o.clear()
                            }
                        }),
                    r.clearTag()
                } else {
                    var s = this.env,
                        f = [Xt.call(r, Ar, i, n, t)],
                        d = Mt(s[ga]);
                    Nn(d, _a, f, function (i, u) {
                            i && (_(Wr), r.pay(n, t, e))
                        })
                }
        },
    La.tag = function (n, t, e, r) {
            var i = void 0,
                u = void 0,
                o = this.env,
                a = arguments,
                c = [],
                s = function (n) {
                    if (!wu.isObj(n)) return n;
                    for (var t = n, e = 0, r = c.length; e < r; e++) {
                        if (!t) return t;
                        t = t[c[e]]
                    }
                    return t
                },
                f = function () {
                    ku.each(a, function (n) {
                        return !!wu.isStr(n) && void c.push(n)
                    })
                },
                d = function (n, t, e) {
                    var i = {};
                    i[n] = t,
                    u = Mt(o[ga]),
                    Nn(u, ya, i, function (n, t) {
                        r && (e && f(), r(n, s(t), !0))
                    })
                },
                v = function (n) {
                    var t = _o.getAll();
                    n || f(),
                    r && r(0, s(t), !1)
                };
            if (ku.each(a, function (n) {
                    wu.isFunc(n) && (r = n)
                }), wu.isObj(n)) {
                    var l = this;
                    ku.each(n, function (n, t) {
                        l.tag(t, n)
                    })
                } else wu.isStr(n) && wu.isObj(t) ? Wr !== m() ? (i = t, d(n, i, !0)) : (Ou(t, function (t, e) {
                    _o.set(n, e, t)
                }), v(!0)) : (wu.isObj(e) || wu.isStr(e)) && Nt(n) && wu.isStr(t) ? Wr !== m() ? (i = {}, i[t] = e, d(n, i, !0)) : (_o.set(n, t, e), v(!0)) : wu.isFunc(n) || wu.isFunc(t) || wu.isStr(n) && wu.isStr(t) && wu.isFunc(e) ? Wr !== m() ? (f(a), u = Mt(o[ga]), Nn(u, ba, {}, function (n, t) {
                    r && r(n, s(t), !0)
                })) : v() : r && r(xa)
        },
    La.clearTag = function (n, t, e) {
            var r = 0;
            Wr === m() ? (wu.isFunc(n) && (e = n, n = lu), _o.clear(n, t), e && e(0)) : r = xa,
            e && e(r)
        },
    La.sfrom = function (n) {
            var t = void 0,
                e = void 0,
                r = this.env;
            Wr !== m() ? (e = Mt(r[ga]), Nn(e, wa, {}, function (e, r) {
                    if (r) {
                        var i = r.data ? r.data : r;
                        t = wu.isStr(i) ? JSON.parse(i) : i,
                        n(e, t)
                    }
                })) : n(1, [])
        },
    La.send = function (n, t) {
            var e = [];
            t = wu.extend({
                cb: function () {}
            }, t),
            wu.run(n, function (n) {
                Fu() && (n[Te] = Lu()),
                e.push(n)
            });
            var r = Et();
            r && e.unshift(r),
            Mn(e, t)
        },
    La.getAll = function () {
            return Ia
        };
    var Va = te.prototype;
    Va.create = function (n, t) {
            var e = this,
                r = wu.extend({}, e.env);
            r = wu.extend(r, {
                    category: n
                });
            var i = wu.extend({
                    isDefault: !1
                }, e.opts);
            i = wu.extend(i, t || {});
            var u = new xt(i, r);
            return e._t.push(u),
            t.isDefault && (e._dt = u),
            u
        },
    Va.config = function (n, t) {
            return lu !== n && (zi[n] = t),
            "cid" === n && Su(t) && (this.opts.cid = t),
            zi[n]
        },
    Va._initPV = function (n, t) {
            var e = this,
                r = e.config("pageValLab");
            n = wu.extend(n, e.config("pageEnv")),
            ne(e, r, n, {
                    isauto: rr,
                    reportStatus: Wr,
                    cid: t,
                    isAutoInit: !0
                })
        },
    Va.pageView = function (n, t, e) {
            ne(this, n, t, e)
        },
    Va.moduleView = function (n, t, e) {
            var r = this;
            r._dt.moduleView(n, t, e)
        },
    Va.moduleViewList = function (n, t, e) {
            var r = this;
            r._dt.moduleViewList(n, t, e)
        },
    Va.systemCheck = function (n, t, e) {
            var r = this;
            r._dt.systemCheck(n, t, e)
        },
    Va.moduleClick = function (n, t, e) {
            var r = this;
            r._dt.moduleClick(n, t, e)
        },
    Va.moduleEdit = function (n, t, e) {
            var r = this;
            r._dt.moduleEdit(n, t, e)
        },
    Va.order = function (n, t, e, r) {
            var i = this;
            i._dt.order(n, Gt(e, t), r)
        },
    Va.pay = function (n, t, e, r) {
            var i = this;
            i._dt.pay(n, Gt(e, t), r)
        },
    Va.pageDisappear = function (n, t) {
            var e = this;
            e._dt.pageDisappear(n, t)
        },
    Va.tag = function (n, t, e, r) {
            this._dt.tag(n, t, e, r)
        },
    Va.sfrom = function (n) {
            this._dt.sfrom(n)
        },
    Va.clearTag = function (n, t, e) {
            this._dt.clearTag(n, t, e)
        },
    Va.getAll = function (n) {
            n && n(this._t)
        },
    Va.getTracker = function (n, t) {
            var e = ku.find(this._t, function (t) {
                return t.env.category === n
            });
            t && t(e)
        },
    Va.get = function (n, t) {
            this._dt.get(n, t)
        },
    Va.set = function (n, t, e) {
            this._dt.set(n, t, e)
        },
    Va._setRequestID = function (n) {
            At(n)
        },
    Va._setNativeEvsData = function (n, t) {
            It(n, t)
        };
    var Ma = void 0,
        Ra = !0,
        Pa = function () {
            var n = !! zi.onWebviewAppearAutoPV;
            n && (P(), oe(), Ma.pageView(), v(ye))
        },
        Ba = function () {
            var n = !! zi.onWebviewAppearAutoPV;
            n && (l() || (v(_e), Ma.pageDisappear({}, {
                getDurationFromLastPV: !0
            })))
        },
        Ua = {
            appear: function () {
                Ra = !0,
                Pa()
            },
            disappear: function () {
                Ra = !1,
                Ba(),
                A()
            },
            foreground: function () {
                Ra && Pa()
            },
            background: function () {
                Ra && (Ba(), A())
            }
        },
        Qa = void 0,
        Ka = function () {
            return !!/\d\.\d\.\d/.test(Yu) && H(Yu, "11.3.0") >= 0
        }(),
        $a = {
            hook: re
        },
        Ja = [],
        Xa = Zr,
        za = void 0,
        Ha = void 0,
        Wa = [
            [Ir, Qr],
            [jr, Qr],
            [Dr, Ur],
            [Er, Kr],
            [Cr, $r],
            [Nr, Jr]
    ],
        Za = ku.reduce(Wa, function (n, t) {
            return n[t[0]] = t[1],
            n
        }, {}),
        Ga = [
            [Mi, Rr],
            [Ri, Pr]
    ],
        Ya = ku.reduce(Ga, function (n, t) {
            return n[t[0]] = t[1],
            n
        }, {}),
        nc = ku.reduce(["config", Li, Fi, Ti], function (n, t) {
            return n[t] = !0,
            n
        }, {}),
        tc = function (n) {
            var t = n.split("."),
                e = void 0;
            return 2 === t.length && (n = t[1], e = t[0]),
            [n, e]
        },
        ec = function (n) {
            var t = n.indexOf(".");
            return t > 0 && (n = n.substr(t + 1)),
            !! nc[n]
        },
        rc = function (n, t) {
            var e = su.getElementsByTagName("head")[0],
                r = su.createElement("meta");
            r.setAttribute("name", n),
            r.setAttribute("content", t),
            e.appendChild(r)
        },
        ic = function (n, t) {
            return n === Vi ? t ? Za[t] || Br : Qr : n === Mi || n === Ri ? Ya[n] : Br
        },
        uc = function (n) {
            var t = {
                act: 1,
                cid: 1,
                val: 1,
                lab: 1,
                bid: 1
            };
            return 1 === t[n]
        },
        oc = function (n, t) {
            return n = n || {},
            Ou(t, function (t, e) {
                uc(e) ? n["val_" + e] = t : n[e] = t
            }),
            n
        },
        ac = function (n) {
            var t = n.val;
            return t && (oc(n, t), delete n.val),
            n
        },
        cc = function (n, t, e) {
            if (n && !xu(n) && (n = {
                custom: {
                    _lab: n
                }
            }), !n && e && (n = {}), e) {
                var r = n[qi] = n[qi] || {};
                r[t] = e
            }
            return n
        },
        sc = function (n, t, e) {
            return n && !xu(n) && (n = {
                custom: {
                    _lab: n
                }
            }),
            n && (n[t] = e),
            n
        },
        fc = function (n, t) {
            var e = n[xi],
                r = n[ki];
            if (e && e === r && (r = T(!0, {}, r)), t && (r || e)) {
                    var i = e;
                    e = r || {},
                    i && (e = cc(e || {}, "_lab", i))
                } else if (!t && (r || e)) {
                    if (Su(r) && (r = {
                        analyse_val: r
                    }), Su(e)) {
                        var u = e;
                        e = {
                            val_lab: u
                        }
                    }
                    r && (e = sc(e || {}, "page", r))
                }
            return lu !== n[Tr] && (e = cc(e || {}, "_act", n[Tr])),
            lu !== n[Fr] && (e = cc(e || {}, "_et", n[Fr])),
            lu !== n[Vr] && (e = sc(e || {}, Vr, n[Vr])),
            lu !== n[Mr] && (e = cc(e || {}, "_el_id", n[Mr])),
            e
        },
        dc = function jc(n, t) {
            var e = se(n);
            n = e[0];
            var r = e[1],
                i = t[0],
                u = t[1];
            if (ku.isArray(i)) return Au(i, function (t) {
                    return jc(r ? r + "." + n : n, [t, u])
                });
            var o = (i.nm || Vi).toLowerCase();
            i.nm = o,
            i = ac(i);
            var a = Mi === o,
                c = Vi === o;
            if (a) return ce.apply(null, t);
            var s = $r === o,
                f = Jr === o,
                d = i[Fr],
                v = i[Tr],
                l = fc(i, !1);
            s || f || d || !c || !v ? f || s ? n = o : (n = ic(o, d), c || (l = cc(l || {}, "_nm", o))) : n = Qr;
            var p = i[Lr];
            return p && (u = u || {}, u.cid = p),
            r && cc(l, "_logchannel", r),
            l = l || {},
            cc(l, "_api", "v3"),
            n === $r || n === Jr ? [n, i[Si], l.order_id, l, u] : [n, i[Si], l, u]
        },
        vc = function (n, t) {
            var e = se(n),
                r = e[1];
            n = Rr;
            var i = t[1],
                u = t[2],
                o = r ? {
                    custom: {
                        _logchannel: r
                    }
                } : lu,
                a = {};
            if (Su(i)) xu(u) ? o = u : Su(u) && (o = cc({}, "analyse_val", u));
            else if (xu(i)) {
                    a = oc(a, i),
                    u = a[ki],
                    Su(u) && (u = cc({}, "analyse_val", u)),
                    o = u;
                    var c = a[xi];
                    c && cc(o, "_lab", c),
                    i = a[Lr]
                }
            var s = void 0;
            return i && (s = {}, s.cid = i),
            o = cc(o, "_api", "v3"),
            [n, o, lu, s]
        },
        lc = function (n, t) {
            var e = t[0],
                r = t[1];
            if (e && (e = e.replace(/^data_sdk_/i, ""), rc("lx:category", e)), xu(r)) return ["set", r]
        },
        pc = function (n, t, e) {
            return "appnm" === t && Su(e) ? void rc("lx:appnm", e) : "cid" === t && Su(e) ? (rc("lx:cid", e), [n, t, e]) : [n, t, e]
        },
        hc = function Dc() {
            var n = Dc.f;
            if (!n) {
                var t = "lx:autopv",
                    e = "off";
                rc(t, e),
                Dc.f = !0
            }
        },
        gc = function (n) {
            if (!n || !n.length) return n;
            try {
                var t = n[0];
                ec(t) && (n = ku.slice(n, 1), mc(t) ? (Nu(3), hc(), n = dc(t, n)) : _c(t) ? (Nu(3), hc(), n = vc(t, n)) : yc(t) ? (Nu(3), hc(), n = lc(t, n)) : bc(t, n[0], n[1]) ? (hc(), n = pc(t, n[0], n[1])) : n.unshift(t))
            } catch (e) {}
            return n
        },
        mc = function (n) {
            var t = n.indexOf(".");
            return t > 0 && (n = n.substr(t + 1)),
            n === Li
        },
        _c = function (n) {
            var t = n.indexOf(".");
            return t > 0 && (n = n.substr(t + 1)),
            n === Fi
        },
        yc = function (n) {
            return n === Ti
        },
        bc = function (n, t) {
            var e = !1;
            return "cid" !== t && "appnm" !== t || (Nu(3), e = !0),
            "config" === n && e
        },
        wc = void 0,
        xc = void 0,
        Sc = 1,
        kc = 100,
        qc = 0,
        Oc = !1,
        Ac = (E(), 0);
    Ac = Xe(function () {
            pe()
        }, 3e3),
    "complete" !== su.readyState ? (wu.on(su, "DOMContentLoaded", pe), wu.on(au, "load", pe)) : pe()
}();