# Dependency Status Report

Generated on 2026-07-02 00:03:14

## Summary

- **Total Checked**: 2
- **Up-to-date**: 0
- **Outdated**: 2 (Patch: 0, Minor: 2, Major: 0)
- **Security Vulnerabilities**: 2 found in 1 packages

## Dependency Details

| Package | Type | Declared | Installed | Latest | Status | Vuls | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `github.com/gin-gonic/gin` | Direct | `v1.9.0` | `v1.9.0` | `v1.12.0` | ⚠️ Minor Update | ⚠️ **2** |  |
| `github.com/google/uuid` | Transitive (via indirect) | `v1.3.0` | `v1.3.0` | `v1.6.0` | ⚠️ Minor Update | ✅ |  |

## Security Vulnerabilities Details

### `github.com/gin-gonic/gin@v1.9.0` (2 vulnerabilities)

- **GHSA-2c4m-59x9-fr2g** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N]: Gin Web Framework does not properly sanitize filename parameter of Context.FileAttachment function
  > The filename parameter of the Context.FileAttachment function is not properly sanitized. A maliciously crafted filename can cause the Content-Disposition header to be sent with an unexpected filename value or otherwise modify the Content-Disposition header. For example, a filename of "setup.bat&quot;;x=.txt" will be sent as a file named "setup.bat".
> 
> If the FileAttachment function is called with names provided by an untrusted source, this may permit an attacker to cause a file to be served with a name different than provided. Maliciously crafted attachment file name can modify the Content-Disposition header.

- **GO-2023-1737** [UNKNOWN]: Improper handling of filenames in Content-Disposition HTTP header in github.com/gin-gonic/gin
  > The filename parameter of the Context.FileAttachment function is not properly sanitized. A maliciously crafted filename can cause the Content-Disposition header to be sent with an unexpected filename value or otherwise modify the Content-Disposition header. For example, a filename of "setup.bat&quot;;x=.txt" will be sent as a file named "setup.bat".
> 
> If the FileAttachment function is called with names provided by an untrusted source, this may permit an attacker to cause a file to be served with a name different than provided. Maliciously crafted attachment file name can modify the Content-Disposition header.

