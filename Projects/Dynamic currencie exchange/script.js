var rates = {};
var amountInput = document.getElementById('amount');
var resultInput = document.getElementById('result');
var rateText = document.getElementById('rate');
var fromSelect = document.getElementById('from');
var toSelect = document.getElementById('to');
var swapBtn = document.getElementById('swap');

function fillCurrencies(currencyList) {
  fromSelect.innerHTML = '';
  toSelect.innerHTML = '';
  for (var i = 0; i < currencyList.length; i++) {
    var code = currencyList[i];
    fromSelect.appendChild(new Option(code, code));
    toSelect.appendChild(new Option(code, code));
  }
  fromSelect.value = 'USD';
  toSelect.value = 'KZT';
}

async function loadRate() {
  var fromCurrency = fromSelect.value || 'USD';
  var response = await fetch('https://api.exchangerate-api.com/v4/latest/' + fromCurrency);
  var data = await response.json();
  rates = data.rates;
  if (fromSelect.options.length === 0) {
    fillCurrencies(Object.keys(rates));
  }
  updateRateText();
  calculate();
  console.log('Rate loaded.');
}

function updateRateText() {
  var fromCurrency = fromSelect.value;
  var toCurrency = toSelect.value;
  var rate = rates[toCurrency];
  if (rate == null) {
    rateText.textContent = '1 ' + fromCurrency + ' = — ' + toCurrency;
    return;
  }
  rateText.textContent = '1 ' + fromCurrency + ' = ' + rate.toFixed(2) + ' ' + toCurrency;
}

function calculate() {
  var amount = parseFloat(amountInput.value);
  var toCurrency = toSelect.value;
  var rate = rates[toCurrency];
  if (isNaN(amount) || amount < 0 || rate == null) {
    resultInput.value = '—';
    return;
  }
  var result = amount * rate;
  resultInput.value = result.toFixed(2);
}

function swapCurrencies() {
  var fromVal = fromSelect.value;
  var toVal = toSelect.value;
  fromSelect.value = toVal;
  toSelect.value = fromVal;
  loadRate();
}

loadRate();

amountInput.addEventListener('input', calculate);
fromSelect.addEventListener('change', loadRate);
toSelect.addEventListener('change', function() {
  updateRateText();
  calculate();
});
swapBtn.addEventListener('click', swapCurrencies);
