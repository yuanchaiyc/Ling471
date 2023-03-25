library(MASS)
library(phonTools)
library(RColorBrewer)

data(h95)

cols = brewer.pal(2, "Dark2")

iy = h95[h95$type == "g" & h95$vowel == "i",c("f1", "f2", "vowel")]
ih = h95[h95$type == "g" & h95$vowel == "I",c("f1", "f2", "vowel")]
vowels = rbind(iy, ih)
vowels$vowel = droplevels(vowels$vowel)
plot(vowels$f1, vowels$f2, col=cols[vowels$vowel], pch=16, cex=1.5,
     xlab="F1 (Hz)", ylab="F2 (Hz)", main="Linear separation of [i] and [ɪ] vowels")

da = lda(vowel ~ f1 + f2, data=vowels)
mygrid = expand.grid(f1=seq(min(vowels$f1), max(vowels$f1), length.out=1000),
                     f2=seq(min(vowels$f2), max(vowels$f2), length.out=1000))
close_enough = mygrid[abs(predict(da, mygrid)$posterior - 0.5) <= 0.01,]
close_enough = close_enough[order(close_enough$f1, close_enough$f2),]
points(close_enough$f1, close_enough$f2, cex=0.5)
legend("topright", legend=c("[i]", "[ɪ]"), col=(cols[1:2]), pch=16)

uw = h95[h95$type == "g" & h95$vowel == "u",c("f1", "f2", "vowel")]
uh = h95[h95$type == "g" & h95$vowel == "U",c("f1", "f2", "vowel")]
vowels = rbind(uw, uh)
vowels$vowel = droplevels(vowels$vowel)
plot(vowels$f1, vowels$f2, col=cols[vowels$vowel], pch=16, cex=1.5,
     xlab="F1 (Hz)", ylab="F2 (Hz)", main="Nonlinear separation of [u] and [ʊ] vowels")

da = qda(vowel ~ f1 + f2, data=vowels)
mygrid = expand.grid(f1=seq(min(vowels$f1), max(vowels$f1), length.out=1000),
                     f2=seq(min(vowels$f2), max(vowels$f2), length.out=1000))
close_enough = mygrid[abs(predict(da, mygrid)$posterior - 0.5) <= 0.01,]
close_enough = close_enough[order(close_enough$f1, close_enough$f2),]
points(close_enough$f1, close_enough$f2, cex=0.5)
legend("topright", legend=c("[u]", "[ʊ]"), col=(cols[1:2]), pch=16)

par(mfrow=c(2,2))
plot(x, x, main="f(x) = x", type="l")
plot(x, x^2, main="f(x) = x^2", type="l")
plot(x, log(x), main="f(x) = ln(x)", type="l")
plot(x, 2^x, main="f(x) = 2^x", type="l")

par(mfrow=c(1,1))
plot(density(rnorm(10000000)), main="Probability density function",
     xlab="X data point value", ylab="Probability")

x = seq(-2, 2, length=500)
y = -(x-1)^2+4
plot(x, y, type="l", main="f(x) = -(x-1)^2 + 4")
abline(v=1, col="red", lw=3)

x = seq(0, 1, length=500)
y = x^3 * (1-x)^2
plot(x, y, type="l", xlab="θ", ylab="Probability",
     main="θ^3*(1-θ)^2")
abline(v=3/5, col="red", lw=3)

y = log(x^3 * (1-x)^2)
plot(x, y, type="l", xlab="θ", ylab="Log probability",
     main="ln(θ^3*(1-θ)^2)")
abline(v=3/5, col="red", lw=3)

plot(x[-1], diff(y), type="l")
abline(h=0, col="red", lw=3)
