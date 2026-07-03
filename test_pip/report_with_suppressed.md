# Dependency Status Report

Generated on 2026-07-02 20:37:56

## Summary

- **Total Checked**: 6
- **Up-to-date**: 0
- **Outdated**: 6 (Patch: 0, Minor: 2, Major: 4)
- **Security Vulnerabilities**: 51 found in 4 packages
- **Suppressed Alerts**: 6

## Dependency Details

| Package | Type | Declared | Installed | Latest | Status | Vuls | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `certifi` | Transitive (via requests) | `==2022.12.7` | `2022.12.7` | `2026.6.17` | ❌ Major Update | ✅ |  |
| `charset-normalizer` | Transitive (via requests) | `==2.1.1` | `2.1.1` | `3.4.7` | ❌ Major Update | ✅ |  |
| `django` | Direct | `==4.0.0` | `4.0.0` | `6.0.6` | ❌ Major Update | ⚠️ **32** |  |
| `idna` | Transitive (via requests) | `==3.4` | `3.4` | `3.18` | ⚠️ Minor Update | ⚠️ **4** |  |
| `requests` | Direct | `==2.28.1` | `2.28.1` | `2.34.2` | ⚠️ Minor Update | ⚠️ **5** |  |
| `urllib3` | Transitive (via requests) | `==1.26.15` | `1.26.15` | `2.7.0` | ❌ Major Update | ⚠️ **10** |  |

## Security Vulnerabilities Details

### `django@4.0.0` (32 vulnerabilities)

- **GHSA-2hrw-hx67-34x6** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Resource exhaustion in Django
  > An issue was discovered in the Multipart Request Parser in Django 3.2 before 3.2.18, 4.0 before 4.0.10, and 4.1 before 4.1.7. Passing certain inputs (e.g., an excessive number of parts) to multipart forms could result in too many open files or memory exhaustion, and provided a potential vector for a denial-of-service attack.

- **GHSA-53qw-q765-4fww** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Denial-of-service in Django
  > An issue was discovered in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1. `UserAttributeSimilarityValidator` incurred significant overhead in evaluating a submitted password that was artificially large in relation to the comparison values. In a situation where access to user registration was unrestricted, this provided a potential vector for a denial-of-service attack.

- **GHSA-6cw3-g6wv-c2xv** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Infinite Loop in Django
  > An issue was discovered in MultiPartParser in Django 2.2 before 2.2.27, 3.2 before 3.2.12, and 4.0 before 4.0.2. Passing certain inputs to multipart forms could result in an infinite loop when parsing files.

- **GHSA-6w2r-r2m5-xq5w** [CVSS CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:N]: Django is subject to SQL injection through its column aliases
  > An issue was discovered in Django 4.2 before 4.2.24, 5.1 before 5.1.12, and 5.2 before 5.2.6. FilteredRelation is subject to SQL injection in column aliases, using a suitably crafted dictionary, with dictionary expansion, as the **kwargs passed QuerySet.annotate() or QuerySet.alias().

- **GHSA-7xr5-9hcq-chf9** [CVSS CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:L/A:N]: Django Improper Output Neutralization for Logs vulnerability
  > An issue was discovered in Django 5.2 before 5.2.2, 5.1 before 5.1.10, and 4.2 before 4.2.22. Internal HTTP response logging does not escape request.path, which allows remote attackers to potentially manipulate log output via crafted URLs. This may lead to log injection or forgery when logs are viewed in terminals or processed by external systems.

- **GHSA-8c5j-9r9f-c6w8** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N]: Information disclosure in Django
  > An issue was discovered in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1. Due to leveraging the Django Template Language's variable resolution logic, the dictsort template filter was potentially vulnerable to information disclosure, or an unintended method call, if passed a suitably crafted key.

- **GHSA-8x94-hmjh-97hq** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H]: Django vulnerable to Reflected File Download attack
  > An issue was discovered in the HTTP FileResponse class in Django 3.2 before 3.2.15 and 4.0 before 4.0.7. An application is vulnerable to a reflected file download (RFD) attack that sets the Content-Disposition header of a FileResponse when the filename is derived from user-supplied input.

- **GHSA-95rw-fx8r-36v6** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N]: Cross-site Scripting in Django
  > The `{% debug %}` template tag in Django 2.2 before 2.2.27, 3.2 before 3.2.12, and 4.0 before 4.0.2 does not properly encode the current context. This may lead to XSS.

- **GHSA-frmv-pr5f-9mcr** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N]: Django vulnerable to SQL injection via _connector keyword argument in QuerySet and Q objects.
  > An issue was discovered in 5.1 before 5.1.14, 4.2 before 4.2.26, and 5.2 before 5.2.8.
> The methods `QuerySet.filter()`, `QuerySet.exclude()`, and `QuerySet.get()`, and the class `Q()`, are subject to SQL injection when using a suitably crafted dictionary, with dictionary expansion, as the `_connector` argument.
> Earlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.
> Django would like to thank cyberstan for reporting this issue.

- **GHSA-jh3w-4vvf-mjgr** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Django has regular expression denial of service vulnerability in EmailValidator/URLValidator
  > In Django 3.2 before 3.2.20, 4 before 4.1.10, and 4.2 before 4.2.3, `EmailValidator` and `URLValidator` are subject to a potential ReDoS (regular expression denial of service) attack via a very large number of domain name labels of emails and URLs.

- **GHSA-jrh2-hc4r-7jwx** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N]: Directory-traversal in Django
  > Storage.save in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1 allows directory traversal if crafted filenames are directly passed to it.

- **GHSA-p64x-8rxx-wf6q** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H]: Django `Trunc()` and `Extract()` database functions vulnerable to SQL Injection
  > An issue was discovered in Django 3.2 before 3.2.14 and 4.0 before 4.0.6. The `Trunc()` and `Extract()` database functions are subject to SQL injection if untrusted data is used as a kind/lookup_name value. Applications that constrain the lookup name and kind choice to a known safe list are unaffected.

- **GHSA-q2jf-h9jm-m7p4** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Django contains Uncontrolled Resource Consumption via cached header
  > In Django 3.2 before 3.2.17, 4.0 before 4.0.9, and 4.1 before 4.1.6, the parsed values of Accept-Language headers are cached in order to avoid repetitive parsing. This leads to a potential denial-of-service vector via excessive memory usage if the raw value of Accept-Language headers is very large.

- **GHSA-qrw5-5h28-6cmg** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Django denial-of-service vulnerability in internationalized URLs
  > In Django 3.2 before 3.2.16, 4.0 before 4.0.8, and 4.1 before 4.1.2, internationalized URLs were subject to a potential denial of service attack via the locale parameter, which is treated as a regular expression. 

- **GHSA-qw25-v68c-qjf3** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Django has a denial-of-service vulnerability in HttpResponseRedirect and HttpResponsePermanentRedirect on Windows
  > An issue was discovered in 5.1 before 5.1.14, 4.2 before 4.2.26, and 5.2 before 5.2.8.
> NFKC normalization in Python is slow on Windows. As a consequence, `django.http.HttpResponseRedirect`, `django.http.HttpResponsePermanentRedirect`, and the shortcut `django.shortcuts.redirect`  were subject to a potential  denial-of-service attack via certain inputs with a very large number of Unicode characters.
> Earlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.
> Django would like to thank Seokchan Yoon for reporting this issue.

- **GHSA-r3xc-prgr-mg9p** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H]: Django bypasses validation when using one form field to upload multiple files
  > In Django 3.2 before 3.2.19, 4.x before 4.1.9, and 4.2 before 4.2.1, it was possible to bypass validation when using one form field to upload multiple files. This multiple upload has never been supported by forms.FileField or forms.ImageField (only the last uploaded file was validated). However, Django's "Uploading multiple files" documentation suggested otherwise.

- **GHSA-rrqc-c2jx-6jgv** [CVSS CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N]: Django allows enumeration of user e-mail addresses
  > An issue was discovered in Django v5.1.1, v5.0.9, and v4.2.16. The django.contrib.auth.forms.PasswordResetForm class, when used in a view implementing password reset flows, allows remote attackers to enumerate user e-mail addresses by sending password reset requests and observing the outcome (only when e-mail sending is consistently failing).

- **GHSA-w24h-v9qh-8gxj** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H]: SQL Injection in Django
  > A SQL injection issue was discovered in `QuerySet.explain()` in Django 2.2 before 2.2.28, 3.2 before 3.2.13, and 4.0 before 4.0.4. This occurs by passing a crafted dictionary (with dictionary expansion) as the `**options` argument, and placing the injection payload in an option name.

- **PYSEC-2022-1** [UNKNOWN]: No summary provided
  > An issue was discovered in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1. UserAttributeSimilarityValidator incurred significant overhead in evaluating a submitted password that was artificially large in relation to the comparison values. In a situation where access to user registration was unrestricted, this provided a potential vector for a denial-of-service attack.

- **PYSEC-2022-19** [UNKNOWN]: No summary provided
  > The {% debug %} template tag in Django 2.2 before 2.2.27, 3.2 before 3.2.12, and 4.0 before 4.0.2 does not properly encode the current context. This may lead to XSS.

- **PYSEC-2022-190** [UNKNOWN]: No summary provided
  > An issue was discovered in Django 2.2 before 2.2.28, 3.2 before 3.2.13, and 4.0 before 4.0.4. QuerySet.annotate(), aggregate(), and extra() methods are subject to SQL injection in column aliases via a crafted dictionary (with dictionary expansion) as the passed **kwargs.

- **PYSEC-2022-191** [UNKNOWN]: No summary provided
  > A SQL injection issue was discovered in QuerySet.explain() in Django 2.2 before 2.2.28, 3.2 before 3.2.13, and 4.0 before 4.0.4. This occurs by passing a crafted dictionary (with dictionary expansion) as the **options argument, and placing the injection payload in an option name.

- **PYSEC-2022-2** [UNKNOWN]: No summary provided
  > An issue was discovered in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1. Due to leveraging the Django Template Language's variable resolution logic, the dictsort template filter was potentially vulnerable to information disclosure, or an unintended method call, if passed a suitably crafted key.

- **PYSEC-2022-20** [UNKNOWN]: No summary provided
  > An issue was discovered in MultiPartParser in Django 2.2 before 2.2.27, 3.2 before 3.2.12, and 4.0 before 4.0.2. Passing certain inputs to multipart forms could result in an infinite loop when parsing files.

- **PYSEC-2022-213** [UNKNOWN]: No summary provided
  > An issue was discovered in Django 3.2 before 3.2.14 and 4.0 before 4.0.6. The Trunc() and Extract() database functions are subject to SQL injection if untrusted data is used as a kind/lookup_name value. Applications that constrain the lookup name and kind choice to a known safe list are unaffected.

- **PYSEC-2022-245** [UNKNOWN]: No summary provided
  > An issue was discovered in the HTTP FileResponse class in Django 3.2 before 3.2.15 and 4.0 before 4.0.7. An application is vulnerable to a reflected file download (RFD) attack that sets the Content-Disposition header of a FileResponse when the filename is derived from user-supplied input.

- **PYSEC-2022-3** [UNKNOWN]: No summary provided
  > Storage.save in Django 2.2 before 2.2.26, 3.2 before 3.2.11, and 4.0 before 4.0.1 allows directory traversal if crafted filenames are directly passed to it.

- **PYSEC-2022-304** [UNKNOWN]: No summary provided
  > In Django 3.2 before 3.2.16, 4.0 before 4.0.8, and 4.1 before 4.1.2, internationalized URLs were subject to a potential denial of service attack via the locale parameter, which is treated as a regular expression.

- **PYSEC-2023-100** [UNKNOWN]: No summary provided
  > In Django 3.2 before 3.2.20, 4 before 4.1.10, and 4.2 before 4.2.3, EmailValidator and URLValidator are subject to a potential ReDoS (regular expression denial of service) attack via a very large number of domain name labels of emails and URLs.

- **PYSEC-2023-12** [UNKNOWN]: No summary provided
  > In Django 3.2 before 3.2.17, 4.0 before 4.0.9, and 4.1 before 4.1.6, the parsed values of Accept-Language headers are cached in order to avoid repetitive parsing. This leads to a potential denial-of-service vector via excessive memory usage if the raw value of Accept-Language headers is very large.

- **PYSEC-2023-13** [UNKNOWN]: No summary provided
  > An issue was discovered in the Multipart Request Parser in Django 3.2 before 3.2.18, 4.0 before 4.0.10, and 4.1 before 4.1.7. Passing certain inputs (e.g., an excessive number of parts) to multipart forms could result in too many open files or memory exhaustion, and provided a potential vector for a denial-of-service attack.

- **PYSEC-2023-61** [UNKNOWN]: No summary provided
  > In Django 3.2 before 3.2.19, 4.x before 4.1.9, and 4.2 before 4.2.1, it was possible to bypass validation when using one form field to upload multiple files. This multiple upload has never been supported by forms.FileField or forms.ImageField (only the last uploaded file was validated). However, Django's "Uploading multiple files" documentation suggested otherwise.

### `idna@3.4` (via requests) (4 vulnerabilities)

- **GHSA-65pc-fj4g-8rjx** [MODERATE]: Internationalized Domain Names in Applications (IDNA): Specially crafted inputs to idna.encode() can bypass CVE-2024-3651 fix
  > This is the same issue as CVE-2024-3651, however the original remediation in 2024 was not a complete fix. Payloads such as `"\u0660" * N` or `"\u30fb" * N + "\u6f22"` utilize the `valid_contexto` function prior to length rejection, and for high values of `N` will take a long time to process.
> 
> ### Impact
> A specially crafted argument to the `idna.encode()` function could consume significant resources. This may lead to a denial-of-service.
> 
> ### Patches
> Starting in version 3.14, the function rejects long inputs as soon as practicable prior to any further processing to minimize resource consumption. In version 3.15, this approach was extended to lesser used alternate functions (i.e. per-label conversions and codec support).
> 
> ### Workarounds
> Domain names cannot exceed 253 characters in length, if this length limit is enforced prior to passing the domain to the `idna.encode()` function it should no longer consume significant resources. This is triggered by arbitrarily large inputs that would not occur in normal usage, but may be passed to the library assuming there is no preliminary input validation by the higher-level application.

- **GHSA-jjg7-2v4v-x38h** [CVSS CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Internationalized Domain Names in Applications (IDNA) vulnerable to denial of service from specially crafted inputs to idna.encode
  > ### Impact
> A specially crafted argument to the `idna.encode()` function could consume significant resources. This may lead to a denial-of-service.
> 
> ### Patches
> The function has been refined to reject such strings without the associated resource consumption in version 3.7.
> 
> ### Workarounds
> Domain names cannot exceed 253 characters in length, if this length limit is enforced prior to passing the domain to the `idna.encode()` function it should no longer consume significant resources. This is triggered by arbitrarily large inputs that would not occur in normal usage, but may be passed to the library assuming there is no preliminary input validation by the higher-level application.
> 
> ### References
> * https://huntr.com/bounties/93d78d07-d791-4b39-a845-cbfabc44aadb

- **PYSEC-2024-60** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: No summary provided
  > A vulnerability was identified in the kjd/idna library, specifically within the `idna.encode()` function, affecting version 3.6. The issue arises from the function's handling of crafted input strings, which can lead to quadratic complexity and consequently, a denial of service condition. This vulnerability is triggered by a crafted input that causes the `idna.encode()` function to process the input with considerable computational load, significantly increasing the processing time in a quadratic manner relative to the input size.

- **PYSEC-2026-215** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L]: No summary provided
  > Internationalized Domain Names in Applications (IDNA) for Python provides support for Internationalized Domain Names in Applications (IDNA) and Unicode IDNA Compatibility Processing. In versions prior to 3.15, payloads such as `"\u0660" * N` or `"\u30fb" * N + "\u6f22"` utilize the `valid_contexto` function prior to length rejection, and for high values of `N` will take a long time to process. This is the same issue as CVE-2024-3651, however the original remediation in 2024 was not a complete fix. A specially crafted argument to the `idna.encode()` function could consume significant resources. This may lead to a denial-of-service. Starting in version 3.14, the function rejects long inputs as soon as practicable prior to any further processing to minimize resource consumption. In version 3.15, this approach was extended to lesser used alternate functions (i.e. per-label conversions and codec support). A workaround is available. Domain names cannot exceed 253 characters in length. If this length limit is enforced prior to passing the domain to the `idna.encode()` function, it should no longer consume significant resources. This is triggered by arbitrarily large inputs that would not occur in normal usage, but may be passed to the library assuming there is no preliminary input validation by the higher-level application.

### `requests@2.28.1` (5 vulnerabilities)

- **GHSA-9hjg-9r4m-mvj7** [CVSS CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:N]: Requests vulnerable to .netrc credentials leak via malicious URLs
  > ### Impact
> 
> Due to a URL parsing issue, Requests releases prior to 2.32.4 may leak .netrc credentials to third parties for specific maliciously-crafted URLs.
> 
> ### Workarounds
> For older versions of Requests, use of the .netrc file can be disabled with `trust_env=False` on your Requests Session ([docs](https://requests.readthedocs.io/en/latest/api/#requests.Session.trust_env)).
> 
> ### References
> https://github.com/psf/requests/pull/6965
> https://seclists.org/fulldisclosure/2025/Jun/2

- **GHSA-9wx4-h78v-vm56** [CVSS CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:N]: Requests `Session` object does not verify requests after making first request with verify=False
  > When using a `requests.Session`, if the first request to a given origin is made with `verify=False`, TLS certificate verification may remain disabled for all subsequent requests to that origin, even if `verify=True` is explicitly specified later.
> 
> This occurs because the underlying connection is reused from the session's connection pool, causing the initial TLS verification setting to persist for the lifetime of the pooled connection. As a result, applications may unintentionally send requests without certificate verification, leading to potential man-in-the-middle attacks and compromised confidentiality or integrity.
> 
> This behavior affects versions of `requests` prior to 2.32.0.

- **GHSA-gc5v-m9x4-r6x2** [CVSS CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:N/I:H/A:N]: Requests has Insecure Temp File Reuse in its extract_zipped_paths() utility function
  > ### Impact
> The `requests.utils.extract_zipped_paths()` utility function uses a predictable filename when extracting files from zip archives into the system temporary directory. If the target file already exists, it is reused without validation. A local attacker with write access to the temp directory could pre-create a malicious file that would be loaded in place of the legitimate one.
> 
> ### Affected usages
> **Standard usage of the Requests library is not affected by this vulnerability.** Only applications that call `extract_zipped_paths()` directly are impacted.
> 
> ### Remediation
> Upgrade to at least Requests 2.33.0, where the library now extracts files to a non-deterministic location.
> 
> If developers are unable to upgrade, they can set `TMPDIR` in their environment to a directory with restricted write access.

- **GHSA-j8r2-6x86-q33q** [CVSS CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:N/A:N]: Unintended leak of Proxy-Authorization header in requests
  > ### Impact
> 
> Since Requests v2.3.0, Requests has been vulnerable to potentially leaking `Proxy-Authorization` headers to destination servers, specifically during redirects to an HTTPS origin. This is a product of how `rebuild_proxies` is used to recompute and [reattach the `Proxy-Authorization` header](https://github.com/psf/requests/blob/f2629e9e3c7ce3c3c8c025bcd8db551101cbc773/requests/sessions.py#L319-L328) to requests when redirected. Note this behavior has _only_ been observed to affect proxied requests when credentials are supplied in the URL user information component (e.g. `https://username:password@proxy:8080`).
> 
> **Current vulnerable behavior(s):**
> 
> 1. HTTP → HTTPS: **leak**
> 2. HTTPS → HTTP: **no leak**
> 3. HTTPS → HTTPS: **leak**
> 4. HTTP → HTTP: **no leak**
> 
> For HTTP connections sent through the proxy, the proxy will identify the header in the request itself and remove it prior to forwarding to the destination server. However when sent over HTTPS, the `Proxy-Authorization` header must be sent in the CONNECT request as the proxy has no visibility into further tunneled requests. This results in Requests forwarding the header to the destination server unintentionally, allowing a malicious actor to potentially exfiltrate those credentials.
> 
> The reason this currently works for HTTPS connections in Requests is the `Proxy-Authorization` header is also handled by urllib3 with our usage of the ProxyManager in adapters.py with [`proxy_manager_for`](https://github.com/psf/requests/blob/f2629e9e3c7ce3c3c8c025bcd8db551101cbc773/requests/adapters.py#L199-L235). This will compute the required proxy headers in `proxy_headers` and pass them to the Proxy Manager, avoiding attaching them directly to the Request object. This will be our preferred option going forward for default usage.
> 
> ### Patches
> Starting in Requests v2.31.0, Requests will no longer attach this header to redirects with an HTTPS destination. This should have no negative impacts on the default behavior of the library as the proxy credentials are already properly being handled by urllib3's ProxyManager.
> 
> For users with custom adapters, this _may_ be potentially breaking if you were already working around this behavior. The previous functionality of `rebuild_proxies` doesn't make sense in any case, so we would encourage any users impacted to migrate any handling of Proxy-Authorization directly into their custom adapter.
> 
> ### Workarounds
> For users who are not able to update Requests immediately, there is one potential workaround.
> 
> You may disable redirects by setting `allow_redirects` to `False` on all calls through Requests top-level APIs. Note that if you're currently relying on redirect behaviors, you will need to capture the 3xx response codes and ensure a new request is made to the redirect destination.
> ```
> import requests
> r = requests.get('http://github.com/', allow_redirects=False)
> ```
> 
> ### Credits
> 
> This vulnerability was discovered and disclosed by the following individuals.
> 
> Dennis Brinkrolf, Haxolot (https://haxolot.com/)
> Tobias Funke, (tobiasfunke93@gmail.com)

- **PYSEC-2023-74** [UNKNOWN]: No summary provided
  > Requests is a HTTP library. Since Requests 2.3.0, Requests has been leaking Proxy-Authorization headers to destination servers when redirected to an HTTPS endpoint. This is a product of how we use `rebuild_proxies` to reattach the `Proxy-Authorization` header to requests. For HTTP connections sent through the tunnel, the proxy will identify the header in the request itself and remove it prior to forwarding to the destination server. However when sent over HTTPS, the `Proxy-Authorization` header must be sent in the CONNECT request as the proxy has no visibility into the tunneled request. This results in Requests forwarding proxy credentials to the destination server unintentionally, allowing a malicious actor to potentially exfiltrate sensitive information. This issue has been patched in version 2.31.0.
> 
> 

### `urllib3@1.26.15` (via requests) (10 vulnerabilities)

- **GHSA-2xpw-w6gg-jr37** [HIGH]: urllib3 streaming API improperly handles highly compressed data
  > ### Impact
> 
> urllib3's [streaming API](https://urllib3.readthedocs.io/en/2.5.0/advanced-usage.html#streaming-and-i-o) is designed for the efficient handling of large HTTP responses by reading the content in chunks, rather than loading the entire response body into memory at once.
> 
> When streaming a compressed response, urllib3 can perform decoding or decompression based on the HTTP `Content-Encoding` header (e.g., `gzip`, `deflate`, `br`, or `zstd`). The library must read compressed data from the network and decompress it until the requested chunk size is met. Any resulting decompressed data that exceeds the requested amount is held in an internal buffer for the next read operation.
> 
> The decompression logic could cause urllib3 to fully decode a small amount of highly compressed data in a single operation. This can result in excessive resource consumption (high CPU usage and massive memory allocation for the decompressed data; CWE-409) on the client side, even if the application only requested a small chunk of data.
> 
> 
> ### Affected usages
> 
> Applications and libraries using urllib3 version 2.5.0 and earlier to stream large compressed responses or content from untrusted sources.
> 
> `stream()`, `read(amt=256)`, `read1(amt=256)`, `read_chunked(amt=256)`, `readinto(b)` are examples of `urllib3.HTTPResponse` method calls using the affected logic unless decoding is disabled explicitly.
> 
> 
> ### Remediation
> 
> Upgrade to at least urllib3 v2.6.0 in which the library avoids decompressing data that exceeds the requested amount.
> 
> If your environment contains a package facilitating the Brotli encoding, upgrade to at least Brotli 1.2.0 or brotlicffi 1.2.0.0 too. These versions are enforced by the `urllib3[brotli]` extra in the patched versions of urllib3.
> 
> 
> ### Credits
> 
> The issue was reported by @Cycloctane.
> Supplemental information was provided by @stamparm during a security audit performed by [7ASecurity](https://7asecurity.com/) and facilitated by [OSTIF](https://ostif.org/).

- **GHSA-34jh-p97f-mpxf** [CVSS CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:N/A:N]: urllib3's Proxy-Authorization request header isn't stripped during cross-origin redirects
  > When using urllib3's proxy support with `ProxyManager`, the `Proxy-Authorization` header is only sent to the configured proxy, as expected.
> 
> However, when sending HTTP requests *without* using urllib3's proxy support, it's possible to accidentally configure the `Proxy-Authorization` header even though it won't have any effect as the request is not using a forwarding proxy or a tunneling proxy. In those cases, urllib3 doesn't treat the `Proxy-Authorization` HTTP header as one carrying authentication material and thus doesn't strip the header on cross-origin redirects.
> 
> Because this is a highly unlikely scenario, we believe the severity of this vulnerability is low for almost all users. Out of an abundance of caution urllib3 will automatically strip the `Proxy-Authorization` header during cross-origin redirects to avoid the small chance that users are doing this on accident.
> 
> Users should use urllib3's proxy support or disable automatic redirects to achieve safe processing of the `Proxy-Authorization` header, but we still decided to strip the header by default in order to further protect users who aren't using the correct approach.
> 
> ## Affected usages
> 
> We believe the number of usages affected by this advisory is low. It requires all of the following to be true to be exploited:
> 
> * Setting the `Proxy-Authorization` header without using urllib3's built-in proxy support.
> * Not disabling HTTP redirects.
> * Either not using an HTTPS origin server or for the proxy or target origin to redirect to a malicious origin.
> 
> ## Remediation
> 
> * Using the `Proxy-Authorization` header with urllib3's `ProxyManager`.
> * Disabling HTTP redirects using `redirects=False` when sending requests.
> * Not using the `Proxy-Authorization` header.

- **GHSA-38jv-5279-wg99** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Decompression-bomb safeguards bypassed when following HTTP redirects (streaming API)
  > ### Impact
> 
> urllib3's [streaming API](https://urllib3.readthedocs.io/en/2.6.2/advanced-usage.html#streaming-and-i-o) is designed for the efficient handling of large HTTP responses by reading the content in chunks, rather than loading the entire response body into memory at once.
> 
> urllib3 can perform decoding or decompression based on the HTTP `Content-Encoding` header (e.g., `gzip`, `deflate`, `br`, or `zstd`). When using the streaming API, the library decompresses only the necessary bytes, enabling partial content consumption.
> 
> However, for HTTP redirect responses, the library would read the entire response body to drain the connection and decompress the content unnecessarily. This decompression occurred even before any read methods were called, and configured read limits did not restrict the amount of decompressed data. As a result, there was no safeguard against decompression bombs. A malicious server could exploit this to trigger excessive resource consumption on the client (high CPU usage and large memory allocations for decompressed data; CWE-409).
> 
> ### Affected usages
> 
> Applications and libraries using urllib3 version 2.6.2 and earlier to stream content from untrusted sources by setting `preload_content=False` when they do not disable redirects.
> 
> 
> ### Remediation
> 
> Upgrade to at least urllib3 v2.6.3 in which the library does not decode content of redirect responses when `preload_content=False`.
> 
> If upgrading is not immediately possible, disable [redirects](https://urllib3.readthedocs.io/en/2.6.2/user-guide.html#retrying-requests) by setting `redirect=False` for requests to untrusted source.

- **GHSA-g4mx-q9vg-27p4** [CVSS CVSS:3.1/AV:A/AC:H/PR:H/UI:N/S:U/C:H/I:N/A:N]: urllib3's request body not stripped after redirect from 303 status changes request method to GET
  > urllib3 previously wouldn't remove the HTTP request body when an HTTP redirect response using status 303 "See Other" after the request had its method changed from one that could accept a request body (like `POST`) to `GET` as is required by HTTP RFCs. Although the behavior of removing the request body is not specified in the section for redirects, it can be inferred by piecing together information from different sections and we have observed the behavior in other major HTTP client implementations like curl and web browsers.
> 
> From [RFC 9110 Section 9.3.1](https://www.rfc-editor.org/rfc/rfc9110.html#name-get):
> 
> > A client SHOULD NOT generate content in a GET request unless it is made directly to an origin server that has previously indicated, in or out of band, that such a request has a purpose and will be adequately supported.
> 
> ## Affected usages
> 
> Because the vulnerability requires a previously trusted service to become compromised in order to have an impact on confidentiality we believe the exploitability of this vulnerability is low. Additionally, many users aren't putting sensitive data in HTTP request bodies, if this is the case then this vulnerability isn't exploitable.
> 
> Both of the following conditions must be true to be affected by this vulnerability:
> 
> * If you're using urllib3 and submitting sensitive information in the HTTP request body (such as form data or JSON)
> * The origin service is compromised and starts redirecting using 303 to a malicious peer or the redirected-to service becomes compromised.
> 
> ## Remediation
> 
> You can remediate this vulnerability with any of the following steps:
> 
> * Upgrade to a patched version of urllib3 (v1.26.18 or v2.0.7)
> * Disable redirects for services that you aren't expecting to respond with redirects with `redirects=False`.
> * Disable automatic redirects with `redirects=False` and handle 303 redirects manually by stripping the HTTP request body.

- **GHSA-gm62-xv2j-4w53** [HIGH]: urllib3 allows an unbounded number of links in the decompression chain
  > ## Impact
> 
> urllib3 supports chained HTTP encoding algorithms for response content according to RFC 9110 (e.g., `Content-Encoding: gzip, zstd`).
> 
> However, the number of links in the decompression chain was unbounded allowing a malicious server to insert a virtually unlimited number of compression steps leading to high CPU usage and massive memory allocation for the decompressed data.
> 
> 
> ## Affected usages
> 
> Applications and libraries using urllib3 version 2.5.0 and earlier for HTTP requests to untrusted sources unless they disable content decoding explicitly.
> 
> 
> ## Remediation
> 
> Upgrade to at least urllib3 v2.6.0 in which the library limits the number of links to 5.
> 
> If upgrading is not immediately possible, use [`preload_content=False`](https://urllib3.readthedocs.io/en/2.5.0/advanced-usage.html#streaming-and-i-o) and ensure that `resp.headers["content-encoding"]` contains a safe number of encodings before reading the response content.

- **GHSA-qccp-gfcp-xxvc** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N]: urllib3: Sensitive headers forwarded across origins in proxied low-level redirects
  > ### Impact
> 
> When following cross-origin redirects for requests made using urllib3’s high-level APIs, such as `urllib3.request()`, `PoolManager.request()`, and `ProxyManager.request()`, sensitive headers — `Authorization`, `Cookie`, and `Proxy-Authorization` (defined in `Retry.DEFAULT_REMOVE_HEADERS_ON_REDIRECT`) — are stripped by default, as expected.
> 
> However, cross-origin redirects followed from the low-level API via `ProxyManager.connection_from_url().urlopen(..., assert_same_host=False)` still forward these sensitive headers.
> 
> ### Affected usage
> 
> Applications and libraries using urllib3 versions earlier than 2.7.0 may be affected if they allow cross-origin redirects while making requests through `HTTPConnection.urlopen()` instances created via `ProxyManager.connection_from_url()`.
> 
> ### Remediation
> 
> Upgrade to urllib3 version 2.7.0 or later, in which sensitive headers are stripped from redirects followed by `HTTPConnection`.
> 
> If upgrading is not immediately possible, avoid using this low-level redirect flow for cross-origin redirects. If appropriate for your use case, switch to `ProxyManager.request()`.

- **GHSA-v845-jxx5-vc9f** [CVSS CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:N]: `Cookie` HTTP header isn't stripped on cross-origin redirects
  > urllib3 doesn't treat the `Cookie` HTTP header special or provide any helpers for managing cookies over HTTP, that is the responsibility of the user. However, it is possible for a user to specify a `Cookie` header and unknowingly leak information via HTTP redirects to a different origin if that user doesn't disable redirects explicitly.
> 
> Users **must** handle redirects themselves instead of relying on urllib3's automatic redirects to achieve safe processing of the `Cookie` header, thus we decided to strip the header by default in order to further protect users who aren't using the correct approach.
> 
> ## Affected usages
> 
> We believe the number of usages affected by this advisory is low. It requires all of the following to be true to be exploited:
> 
> * Using an affected version of urllib3 (patched in v1.26.17 and v2.0.6)
> * Using the `Cookie` header on requests, which is mostly typical for impersonating a browser.
> * Not disabling HTTP redirects
> * Either not using HTTPS or for the origin server to redirect to a malicious origin.
> 
> ## Remediation
> 
> * Upgrading to at least urllib3 v1.26.17 or v2.0.6
> * Disabling HTTP redirects using `redirects=False` when sending requests.
> * Not using the `Cookie` header.

- **PYSEC-2023-192** [CVSS CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N]: No summary provided
  > urllib3 is a user-friendly HTTP client library for Python. urllib3 doesn't treat the `Cookie` HTTP header special or provide any helpers for managing cookies over HTTP, that is the responsibility of the user. However, it is possible for a user to specify a `Cookie` header and unknowingly leak information via HTTP redirects to a different origin if that user doesn't disable redirects explicitly. This issue has been patched in urllib3 version 1.26.17 or 2.0.5.

- **PYSEC-2023-212** [CVSS CVSS:3.1/AV:A/AC:H/PR:H/UI:N/S:U/C:H/I:N/A:N]: No summary provided
  > urllib3 is a user-friendly HTTP client library for Python. urllib3 previously wouldn't remove the HTTP request body when an HTTP redirect response using status 301, 302, or 303 after the request had its method changed from one that could accept a request body (like `POST`) to `GET` as is required by HTTP RFCs. Although this behavior is not specified in the section for redirects, it can be inferred by piecing together information from different sections and we have observed the behavior in other major HTTP client implementations like curl and web browsers. Because the vulnerability requires a previously trusted service to become compromised in order to have an impact on confidentiality we believe the exploitability of this vulnerability is low. Additionally, many users aren't putting sensitive data in HTTP request bodies, if this is the case then this vulnerability isn't exploitable. Both of the following conditions must be true to be affected by this vulnerability: 1. Using urllib3 and submitting sensitive information in the HTTP request body (such as form data or JSON) and 2. The origin service is compromised and starts redirecting using 301, 302, or 303 to a malicious peer or the redirected-to service becomes compromised. This issue has been addressed in versions 1.26.18 and 2.0.7 and users are advised to update to resolve this issue. Users unable to update should disable redirects for services that aren't expecting to respond with redirects with `redirects=False` and disable automatic redirects with `redirects=False` and handle 301, 302, and 303 redirects manually by stripping the HTTP request body.
> 

- **PYSEC-2026-141** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N]: No summary provided
  > urllib3 is an HTTP client library for Python. From 1.23 to before 2.7.0, cross-origin redirects followed from the low-level API via ProxyManager.connection_from_url().urlopen(..., assert_same_host=False) still forward these sensitive headers. This vulnerability is fixed in 2.7.0.


## Suppressed Vulnerabilities (Ignored)

### `certifi@2022.12.7` (via requests) (4 suppressed)

- **GHSA-248v-346w-9cwc**: Certifi removes GLOBALTRUST root certificate
  *Reason: Librería de certifi utilizada únicamente en entorno local/testeo.*

- **GHSA-xqr8-7jwr-rhp7**: Removal of e-Tugra root certificate
  *Reason: Librería de certifi utilizada únicamente en entorno local/testeo.*

- **PYSEC-2023-135**: No summary provided
  *Reason: Librería de certifi utilizada únicamente en entorno local/testeo.*

- **PYSEC-2024-230**: No summary provided
  *Reason: Librería de certifi utilizada únicamente en entorno local/testeo.*

### `django@4.0.0` (1 suppressed)

- **GHSA-2gwj-7jmv-h26r**: SQL Injection in Django
  *Reason: Inyección SQL mitigada por nuestro uso del ORM nativo seguro.*

### `urllib3@1.26.15` (via requests) (1 suppressed)

- **GHSA-pq67-6m6q-mj2v**: urllib3 redirects are not disabled when retries are disabled on PoolManager instantiation
  *Reason: Redirecciones no deshabilitadas en PoolManager mitigadas en nuestro código.*

