def fix_django_headers(meta):
	"""
	Fix this nonsensical API:
	https://docs.djangoproject.com/en/1.11/ref/request-response/
	https://code.djangoproject.com/ticket/20147
	"""
	ret = {}
	for k, v in meta.items():
		if k.startswith("HTTP_"):
			k = k[len("HTTP_"):]
		elif k not in ("CONTENT_LENGTH", "CONTENT_TYPE"):
			# Skip CGI garbage
			continue

		ret[k.lower().replace("_", "-")] = v

	return ret


CURRENCY_SIGILS = {
	"CAD": "$",
	"EUR": "€",
	"GBP": "£",
	"USD": "$",
}


def get_friendly_currency_amount(amount, currency):
	currency = currency.upper()
	sigil = CURRENCY_SIGILS.get(currency, "")
	return "{sigil}{amount} {currency}".format(sigil=sigil, amount=amount, currency=currency)
