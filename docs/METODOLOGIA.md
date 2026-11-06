# Metodología econométrica

## 1. Pregunta de investigación

El proyecto estima cómo se relaciona el **riesgo sistemático** de empresas españolas con sus rentabilidades históricas y evalúa el CAPM mediante el análisis dentro de muestra y el contraste móvil fuera de muestra. No reconstruye los constituyentes históricos del índice ni propone un modelo de precio objetivo.

## 2. Series y tratamiento

**Mercado:** cierres diarios del índice **IBEX 35 Total Return** desde CSV de Investing. Se convierten a fin de mes (`resample("ME").last()`) y se calculan retornos mensuales simples `P_t / P_(t-1) − 1`, sin relleno automático de meses ausentes.

**Empresas:** precios diarios de Yahoo Finance con `auto_adjust=True`, agregados a fin de mes, obteniendo retornos mensuales simples. En la demo se usan Santander, Telefónica, Inditex, Repsol, Iberdrola y BBVA. El universo ampliado se obtiene en la fecha de ejecución mediante MarketScreener.

**Rf:** rendimiento anual (%) de deuda soberana española a 10 años según el BCE (serie `IRS/M.ES.L.L40.CI.0000.EUR.N.Z`). Para el retorno del mes `t`, se utiliza la observación de la serie del mes `t−1`; la tasa anual en decimal se transforma a mensual efectiva mediante `(1 + yield_anual) ** (1/12) − 1`. Se eliminan periodos sin dato.

La transformación de una **yield** a una tasa mensual efectiva es una *convención aproximada*: no equivale a la rentabilidad observada de un activo sin riesgo para un mes, ni resuelve el riesgo de precio/duración del bono. Para una especificación estricta de excesos mensuales correspondería considerar tasas monetarias cortas conocidas ex-ante y, para coste de capital actual, una rf adecuada al horizonte de valoración.

## 3. CAPM y anualización

El modelo estimado es:

`r_i,t − r_f,t = alpha_i + beta_i * (r_m,t − r_f,t) + epsilon_i,t`

Se estima mediante **OLS con errores estándar HAC** (tres rezagos). HAC ajusta las inferencias sobre coeficientes, pero no cambia las estimaciones puntuales OLS de beta y alfa.

- `Rf_anual`: `12 * mean(rf_m)` en la muestra válida de la empresa.
- `Prima_hist`: `12 * mean(r_m − rf_m)` en la muestra válida de la empresa.
- `Ke_hist`: `Rf_anual + beta * Prima_hist`.
- `Retorno_anual`: `12 * mean(r_i)` (aritmético anualizado).
- `CAGR_real`: `(product(1+r_i))**(12/n)-1` (geométrico anualizado).
- `Gap_pp`: `100 * (Retorno_anual − Ke_hist)`.

Si todos los términos usan la misma muestra, `Retorno_anual − Ke_hist = 12 * alpha` por la propiedad de las regresiones OLS con intercepto. Por tanto el `Gap_pp` es una representación del alfa dentro de muestra y no una validación fuera de muestra independiente.

## 4. Sensibilidad a la tasa actual

`Ke_rf_actual = rf_BCE_ultima + beta_hist * Prima_hist`.

`Delta_Ke_pp = 100 * (Ke_rf_actual − Ke_hist)`.

Se mantiene fija la beta y la prima de la muestra individual. Por construcción, `Delta_Ke_pp = 100 * (rf_BCE_ultima − Rf_anual)`. La comparación aísla el **efecto mecánico de reemplazar la rf**. No estima una prima prospectiva y no debe etiquetarse como CAPM ex-ante plenamente independiente.

## 5. SCL y SML

La **SCL** representa los excesos de retorno mensuales de cada acción frente a los del mercado y la recta OLS estimada. La **SML** pone en el eje horizontal la beta, y en el vertical el Ke histórico y el retorno anual aritmético observado. Hay una SML de referencia con la rf y prima de la muestra común, pero el Ke individual puede usar muestras de distinta longitud: las divergencias de muestras deben explicarse expresamente.

## 6. Rolling y separación temporal

Para cada objetivo mensual `t`, se estima beta y la media de prima usando **solo 36 meses inmediatamente anteriores**. El retorno objetivo se compara con la predicción `rf_t + beta_(t−1) * mean(market_excess)_(t−36:t−1)`. No se aceptan ventanas incompletas; no se usa el retorno objetivo para estimar la prima o la beta. La rf del objetivo es la última observación disponible conforme al desfase establecido.

Los diagnósticos incluyen diferencia media, p-valor robusto, proporción de meses que superan el CAPM y R² fuera de muestra comparado con la predicción basada en la rf.

## 7. Comparabilidad, sesgos y límites

El universo de MarketScreener corresponde a empresas detectadas en la ejecución, **no** a la composición histórica exacta de cada mes. Por tanto, los alfas y betas del conjunto no deben interpretarse como resultados de una cartera IBEX 35 históricamente investible. La selección dinámica evita una lista codificada a mano, pero no elimina el sesgo de supervivencia.

El benchmark es **TR bruto**; las series ajustadas de acciones pueden seguir convenciones de dividendos/impuestos distintas. Los resultados son sensibles a fechas, cantidad de datos, tratamiento corporativo y tasa escogida. La muestra histórica disponible no permite inferir la prima esperada futura sin hipótesis adicionales.
