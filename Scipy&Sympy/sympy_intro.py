#symbolik:herhangi bir denklemi çözsün sonucunu x ler vs şeklinde sembolik bir şekilde işlem yapsın istersem Sympy kullanıyorum
#belirsiz sembolik matematiksel işlemleri yapmak için kullanıyorum
#yani özet olarak manuel yaptığımız x lerden y lerden oluşam matematik işlemlerimizi bu kütüphaneyle yapabiliriz
#denklem(dif denklemde dahil) çözdürüp grafik oluşturmak için Sympy kullanmak hoş olur.Sympy=SEMBOL
import sympy as sp

#sembol tanımlaması
x = sp.Symbol('xxx') #burada x bir symbol sınıfı türünden
print(x)
y = sp.Symbol('y')
z = sp.Symbol('z')
print(y)
print(z)

#3 sembolü aynı anda da yaratabilirim =>>>>>   x, y, z = sp.symbols('x, y, z')

#sembollerimi reel ve pozitif yapmak istersem
x = sp.Symbol('x', real=True, positive=True) #burada x sembolümü oluşturdum
print(x)

#integer ve float nesneler tanımlama
x = sp.Symbol('x', real=True, positive=True)
a = sp.Integer(3)
b = sp.Float('4.3476587364587364876345876867345')
print(x)
print(a)
print(b)

#x sembolüyle denklem tanımı yapma
x = sp.Symbol('x', real=True, positive=True)
y = x ** 2 - 2*x - 4
print(y)

# ifadeyi  sembolük sadeleştirmek istersem
x = sp.Symbol('x')
e = (x ** 2 - 1) / (x + 1)
result = sp.simplify(e)
print(result)

#sin2x sembolik olarak açılımını verip sonucu aldım
x = sp.Symbol('x')
e = 2 * sp.sin(x) * sp.cos(x)
result = sp.simplify(e)
print(result)

#iki değişkenden oluşan bir denklemi sadeleştirmek istersem
x = sp.Symbol('x')
y = sp.Symbol('y')
e = ((x ** 2 + x - 6) / (x ** 2 + 3 * x - 10)) * ((x ** 2 - x * y + 5 * x  - 5 * y) / (x **2 + x * y + 3 * x + 3 * y))
result = sp.simplify(e)
print(result)

#expand methoduyla denklem çarpması işlemi yaptım küp açılımı oldu
x = sp.Symbol('x')
y = sp.Symbol('y')
e = (x + y) ** 3
result = sp.expand(e)
print(result)

#çarpanlara ayırmak istersem factor methodunu kullanıyorum
x = sp.Symbol('x')
y = sp.Symbol('y')
e = x ** 2 - 2 * x + 1
result = sp.factor(e)
print(result)


