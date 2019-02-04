from sympy import (Symbol, zeta, nan, Rational, Float, pi, dirichlet_eta, log,
                   zoo, expand_func, polylog, lerchphi, S, exp, sqrt, I,
                   exp_polar, polar_lift, O)
from sympy.utilities.randtest import (test_derivative_numerically as td,
                      random_complex_number as randcplx, test_numerically as tn)
from sympy.utilities.pytest import XFAIL

x = Symbol('x')
a = Symbol('a')
z = Symbol('z')
s = Symbol('s')


def test_zeta_eval():

    assert zeta(nan) == nan
    assert zeta(x, nan) == nan

    assert zeta(0) == Rational(-1, 2)
    assert zeta(0, x) == Rational(1, 2) - x

    assert zeta(1) == zoo
    assert zeta(1, 2) == zoo
    assert zeta(1, -7) == zoo
    assert zeta(1, x) == zoo

    assert zeta(2, 1) == pi**2/6

    assert zeta(2) == pi**2/6
    assert zeta(4) == pi**4/90
    assert zeta(6) == pi**6/945

    assert zeta(2, 2) == pi**2/6 - 1
    assert zeta(4, 3) == pi**4/90 - Rational(17, 16)
    assert zeta(6, 4) == pi**6/945 - Rational(47449, 46656)

    assert zeta(2, -2) == pi**2/6 + Rational(5, 4)
    assert zeta(4, -3) == pi**4/90 + Rational(1393, 1296)
    assert zeta(6, -4) == pi**6/945 + Rational(3037465, 2985984)

    assert zeta(-1) == -Rational(1, 12)
    assert zeta(-2) == 0
    assert zeta(-3) == Rational(1, 120)
    assert zeta(-4) == 0
    assert zeta(-5) == -Rational(1, 252)

    assert zeta(-1, 3) == -Rational(37, 12)
    assert zeta(-1, 7) == -Rational(253, 12)
    assert zeta(-1, -4) == Rational(119, 12)
    assert zeta(-1, -9) == Rational(539, 12)

    assert zeta(-4, 3) == -17
    assert zeta(-4, -8) == 8772

    assert zeta(0, 1) == -Rational(1, 2)
    assert zeta(0, -1) == Rational(1, 2)

    assert zeta(0, 2) == -Rational(3, 2)
    assert zeta(0, -2) == Rational(3, 2)

    assert zeta(
        3).evalf(20).epsilon_eq(Float("1.2020569031595942854", 20), 1e-19)


def test_zeta_series():
    assert zeta(x, a).series(a, 0, 2) == \
        zeta(x, 0) - x*a*zeta(x + 1, 0) + O(a**2)


def test_dirichlet_eta_eval():

    assert dirichlet_eta(0) == Rational(1, 2)
    assert dirichlet_eta(-1) == Rational(1, 4)
    assert dirichlet_eta(1) == log(2)
    assert dirichlet_eta(2) == pi**2/12
    assert dirichlet_eta(4) == pi**4*Rational(7, 720)


def test_rewriting():
    assert dirichlet_eta(x).rewrite(zeta) == (1 - 2**(1 - x))*zeta(x)
    assert zeta(x).rewrite(dirichlet_eta) == dirichlet_eta(x)/(1 - 2**(1 - x))
    assert tn(dirichlet_eta(x), dirichlet_eta(x).rewrite(zeta), x)
    assert tn(zeta(x), zeta(x).rewrite(dirichlet_eta), x)

    assert zeta(x, a).rewrite(lerchphi) == lerchphi(1, x, a)
    assert polylog(s, z).rewrite(lerchphi) == lerchphi(z, s, 1)*z

    assert lerchphi(1, x, a).rewrite(zeta) == zeta(x, a)
    assert z*lerchphi(z, s, 1).rewrite(polylog) == polylog(s, z)


def test_derivatives():
    from sympy import Derivative
    assert zeta(x, a).diff(x) == Derivative(zeta(x, a), x)
    assert zeta(x, a).diff(a) == -x*zeta(x + 1, a)
    assert lerchphi(
        z, s, a).diff(z) == (lerchphi(z, s - 1, a) - a*lerchphi(z, s, a))/z
    assert lerchphi(z, s, a).diff(a) == -s*lerchphi(z, s + 1, a)
    assert polylog(s, z).diff(z) == polylog(s - 1, z)/z

    b = randcplx()
    c = randcplx()
    assert td(zeta(b, x), x)
    assert td(polylog(b, z), z)
    assert td(lerchphi(c, b, x), x)
    assert td(lerchphi(x, b, c), x)


def myexpand(func, target):
    expanded = expand_func(func)
    if target is not None:
        return expanded == target
    if expanded == func:  # it didn't expand
        return False

    # check to see that the expanded and original evaluate to the same value
    subs = {}
    for a in func.free_symbols:
        subs[a] = randcplx()
    return abs(func.subs(subs).n()
               - expanded.replace(exp_polar, exp).subs(subs).n()) < 1e-10


def test_polylog_expansion():
    from sympy import factor, log
    assert polylog(s, 0) == 0
    assert polylog(s, 1) == zeta(s)
    assert polylog(s, -1) == dirichlet_eta(s)

    assert myexpand(polylog(1, z), -log(1 + exp_polar(-I*pi)*z))
    assert myexpand(polylog(0, z), z/(1 - z))
    assert myexpand(polylog(-1, z), z**2/(1 - z)**2 + z/(1 - z))
    assert myexpand(polylog(-5, z), None)


def test_lerchphi_expansion():
    assert myexpand(lerchphi(1, s, a), zeta(s, a))
    assert myexpand(lerchphi(z, s, 1), polylog(s, z)/z)

    # direct summation
    assert myexpand(lerchphi(z, -1, a), a/(1 - z) + z/(1 - z)**2)
    assert myexpand(lerchphi(z, -3, a), None)

    # polylog reduction
    assert myexpand(lerchphi(z, s, S(1)/2),
                    2**(s - 1)*(polylog(s, sqrt(z))/sqrt(z)
                              - polylog(s, polar_lift(-1)*sqrt(z))/sqrt(z)))
    assert myexpand(lerchphi(z, s, 2), -1/z + polylog(s, z)/z**2)
    assert myexpand(lerchphi(z, s, S(3)/2), None)
    assert myexpand(lerchphi(z, s, S(7)/3), None)
    assert myexpand(lerchphi(z, s, -S(1)/3), None)
    assert myexpand(lerchphi(z, s, -S(5)/2), None)

    # hurwitz zeta reduction
    assert myexpand(lerchphi(-1, s, a),
                    2**(-s)*zeta(s, a/2) - 2**(-s)*zeta(s, (a + 1)/2))
    assert myexpand(lerchphi(I, s, a), None)
    assert myexpand(lerchphi(-I, s, a), None)
    assert myexpand(lerchphi(exp(2*I*pi/5), s, a), None)
