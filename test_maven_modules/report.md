# Dependency Status Report

Generated on 2026-07-01 23:55:49

## Summary

- **Total Checked**: 2
- **Up-to-date**: 0
- **Outdated**: 2 (Patch: 0, Minor: 1, Major: 1)
- **Security Vulnerabilities**: 9 found in 1 packages

## Dependency Details

| Package | Type | Declared | Installed | Latest | Status | Vuls | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `com.fasterxml.jackson.core:jackson-databind` | Direct | `2.12.3` | `2.12.3` | `2.22.0` | ⚠️ Minor Update | ⚠️ **9** |  |
| `org.json:json` | Direct | `20231013` | `20231013` | `20260522` | ❌ Major Update | ✅ |  |

## Security Vulnerabilities Details

### `com.fasterxml.jackson.core:jackson-databind@2.12.3` (9 vulnerabilities)

- **GHSA-3wrr-7qpf-2prh** [MODERATE]: jackson-databind: Deeply nested JsonNode throws StackOverflowError for toString()
  > ### Impact
> 
> Potential Denial-of-Service when attacker sends deeply nested JSON if (and only if) service:
> 
> 1. Reads deeply nested (1000s of levels) JSON as `JsonNode` (ObjectMapper.readTree())
> 2. Writes out same (or modifided) node using `JsonNode.toString()`
> 
> which can consume significant amount of resources with concurrent relatively small requests (1000 nested arrays is 2kB).
> 
> ### Patches
> 
> Fixed in 2.14.0 via https://github.com/FasterXML/jackson-databind/issues/3447.
> 
> ### Workarounds
> 
> Avoid serializing `JsonNode` using `toString()`: use ObjectMapper.writeValueAsString(node)

- **GHSA-3x8x-79m2-3w2w** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: jackson-databind possible Denial of Service if using JDK serialization to serialize JsonNode
  > jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNode JDK serialization.

- **GHSA-57j2-w4cx-62h2** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Deeply nested json in jackson-databind
  > jackson-databind is a data-binding package for the Jackson Data Processor. jackson-databind allows a Java stack overflow exception and denial of service via a large depth of nested objects.

- **GHSA-5jmj-h7xm-6q6v** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N]: jackson-databind has case-insensitive deserialization bypasses per-property @JsonIgnoreProperties
  > ## Summary
> In `BeanDeserializerBase.createContextual()`, per-property `@JsonIgnoreProperties` exclusions are applied by `_handleByNameInclusion()`, producing a `contextual` deserializer whose `BeanPropertyMap` has the ignored properties removed. The subsequent per-property case-insensitivity block (triggered by `@JsonFormat(ACCEPT_CASE_INSENSITIVE_PROPERTIES)`) rebuilds from `this._beanProperties` (the original, unfiltered map) instead of `contextual._beanProperties`, then overwrites the filtered map — restoring every property `_handleByNameInclusion` had just removed. The ignored property becomes writable again.
> 
> ## Impact
> An application that both enables case-insensitive matching and relies on per-property `@JsonIgnoreProperties` to keep a field unwritable can have that field set from untrusted JSON (mass-assignment-style write).
> 
> ## Affected / Patched
> Will be fixed in 2.18.9, 2.21.5, 2.22.1 and 3.1.4.
> 
> ## Severity / CWE
> Maintainer: minor. Reporter: Moderate. CWE-915.
> 
> ## Upstream fix
> FasterXML/jackson-databind#5962 (PR #5964, `0e1b0b2`), milestone 3.1.4. Released 2026-06-04.

- **GHSA-hgj6-7826-r7m5** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N]: jackson-databind: InetSocketAddress deserialization triggers eager DNS resolution (SSRF)
  > ## Summary
> `JDKFromStringDeserializer` constructed `InetSocketAddress` with `new InetSocketAddress(host, port)`, which performs eager DNS name resolution for hostname inputs at deserialization time. An application that binds untrusted JSON into a type containing an `InetSocketAddress` field issues an attacker-chosen DNS query during `readValue`, before any application-level validation or connect logic. The fix uses `InetSocketAddress.createUnresolved(host, port)`, deferring DNS to an explicit connect.
> 
> ## Impact
> An attacker controlling JSON deserialized into an `InetSocketAddress`-bearing type can force outbound DNS lookups for attacker-chosen hostnames at deserialization time (SSRF / DNS-based out-of-band interaction / internal-resolver probing), purely from binding.
> 
> ## Affected / Patched (verified via `git tag --contains` on `1f5a103`)
> - 2.18 line: `>= 2.18.0, < 2.18.8` -> fixed in **2.18.8**
> - 2.19-2.21 line: `>= 2.19.0, < 2.21.4` -> fixed in **2.21.4**
> - 3.x line: `>= 3.0.0, < 3.1.4` -> fixed in **3.1.4**
> 
> ## Severity / CWE
> Maintainer: minor. Reporter: LOW. CWE-918 (SSRF).
> 
> ## Upstream fix
> FasterXML/jackson-databind#5951 ("Improve InetSocketAddress deserialization"). Released 2026-06-04 in 2.18.8 / 2.21.4 / 3.1.4.
> 
> ## Credits
> Omkhar Arasaratnam (@omkhar) - finder.

- **GHSA-j3rv-43j4-c7qm** [CVSS CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H]: jackson-databind has a PolymorphicTypeValidator bypass via generic type parameters that allows arbitrary class instantiation
  > `jackson-databind`'s `PolymorphicTypeValidator` (PTV) is the primary safety mechanism guarding polymorphic deserialization. When polymorphic typing is enabled and a type identifier contains generic parameters (i.e. the type ID string contains `<`), `DatabindContext._resolveAndValidateGeneric()` validates **only the raw container class name** (the substring before `<`) against the configured PTV.
> 
> If the container type is approved, the method parses the full canonical type string via `TypeFactory.constructFromCanonical()` and returns the fully parameterized type **without ever validating the nested type arguments** against the PTV. The nested type arguments are then resolved, instantiated, and populated as beans during deserialization.
> 
> An attacker who controls the type ID can therefore place a denied class as a generic type parameter of an allowed container — for example `java.util.ArrayList<com.evil.Gadget>` when only `java.util.ArrayList` is allow-listed. The container passes the PTV check; `com.evil.Gadget` is loaded via `Class.forName(name, true, loader)`, instantiated, and its properties are set from attacker-controlled JSON. This completely bypasses an explicitly configured PTV allow-list.
> 
> This is the same vulnerability class responsible for the historical sequence of jackson-databind deserialization CVEs; here it manifests as a validator bypass rather than a missing deny-list entry.
> 
> 
> ## Impact
> 
> - **Bypass of the PTV allow-list**, including the recommended `BasicPolymorphicTypeValidator` configured with name-prefix allow rules.
> - **Arbitrary class instantiation** of any type assignable to the container's element/parameter position, with attacker-controlled property values (setter/field injection).
> - **Potential unauthenticated remote code execution** when a class with exploitable side effects (JNDI lookup, JDBC/connection-pool gadgets,`TemplatesImpl`-style loaders, etc.) is present on the classpath.
> 
> Applications that accept untrusted JSON and rely on a configured PTV — the documented, security-conscious configuration — are affected.
> 
> 
> ## Proof of Concept
> 
> Configuration restricting polymorphic deserialization to a single safe container:
> 
> ```java
> BasicPolymorphicTypeValidator ptv = BasicPolymorphicTypeValidator.builder()
>         .allowIfSubType("java.util.ArrayList")
>         .build();
> 
> ObjectMapper mapper = JsonMapper.builder()
>         .polymorphicTypeValidator(ptv)
>         .build();
> ```
> 
> Malicious payload (`Wrapper.value` is `Object` with `@JsonTypeInfo(use = Id.CLASS, include = As.WRAPPER_ARRAY)`):
> 
> ```json
> {"value":["java.util.ArrayList<com.evil.EvilGadget>",[{"cmd":"calc.exe"}]]}
> ```
> 
> On vulnerable versions, `com.evil.EvilGadget` is instantiated and its `cmd` property is set, despite only `java.util.ArrayList` being allow-listed. On `2.18.8` / `2.21.4` / `3.1.4` the deserialization throws `InvalidTypeIdException` before instantiation.
> 
> **Variant payloads** (all bypass an `ArrayList`/`HashMap` allow-list):
> 
> | Type ID | Smuggled type position |
> |---|---|
> | `java.util.ArrayList<Evil>` | list element |
> | `java.util.HashMap<Evil,String>` | map key |
> | `java.util.HashMap<String,Evil>` | map value |
> | `java.util.ArrayList<java.util.ArrayList<Evil>>` | nested element |
> | `java.util.ArrayList<Evil[]>` | array element |
> 
> ---
> 
> ## Patches
> 
> Fixed in **2.18.8**, **2.21.4** and **3.1.4** via the changes for [FasterXML/jackson-databind#5988](https://github.com/FasterXML/jackson-databind/issues/5988), commit `434d6c511`. The fix adds recursive validation of each non-trivial type parameter (and array element types appearing as parameters) through the full PTV chain, with documented exemptions for `Object` (wildcard resolution) and `Enum` types.
> 
> `PolymorphicTypeValidator` was added in 2.10.0 so vulnerability N/A for versions prior to that.

- **GHSA-jjjh-jjxp-wpff** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Uncontrolled Resource Consumption in Jackson-databind
  > In FasterXML jackson-databind 2.4.0-rc1 until 2.12.7.1 and in 2.13.x before 2.13.4.2 resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, when the UNWRAP_SINGLE_VALUE_ARRAYS feature is enabled. This was patched in 2.12.7.1, 2.13.4.2, and 2.14.0.
> 
> Commits that introduced vulnerable code are 
> https://github.com/FasterXML/jackson-databind/commit/d499f2e7bbc5ebd63af11e1f5cf1989fa323aa45, https://github.com/FasterXML/jackson-databind/commit/0e37a39502439ecbaa1a5b5188387c01bf7f7fa1, and https://github.com/FasterXML/jackson-databind/commit/7ba9ac5b87a9d6ac0d2815158ecbeb315ad4dcdc.
> 
> Fix commits are https://github.com/FasterXML/jackson-databind/commit/cd090979b7ea78c75e4de8a4aed04f7e9fa8deea and https://github.com/FasterXML/jackson-databind/commit/d78d00ee7b5245b93103fef3187f70543d67ca33.
> 
> The `2.13.4.1` release does fix this issue, however it also references a non-existent jackson-bom which causes build failures for gradle users. See https://github.com/FasterXML/jackson-databind/issues/3627#issuecomment-1277957548 for details. This is fixed in `2.13.4.2` which is listed in the advisory metadata so that users are not subjected to unnecessary build failures

- **GHSA-rgv9-q543-rqg4** [CVSS CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H]: Uncontrolled Resource Consumption in FasterXML jackson-databind
  > In FasterXML jackson-databind before 2.12.7.1 and in 2.13.x before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. This issue can only happen when the `UNWRAP_SINGLE_VALUE_ARRAYS` feature is explicitly enabled.

- **GHSA-rmj7-2vxq-3g9f** [CVSS CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H]: jackson-databind has an array subtype allowlist bypass in BasicPolymorphicTypeValidator (allowIfSubTypeIsArray)
  > ## Summary
> `BasicPolymorphicTypeValidator.Builder.allowIfSubTypeIsArray()` allowlists any array type based only on `clazz.isArray()`, without validating the array's component (element) type against the configured allowlist. A PTV built with `allowIfSubTypeIsArray()` plus an explicit concrete-type allowlist therefore still permits `EvilType[]` even though `EvilType` is not allowlisted. When Jackson deserializes the elements and no per-element type IDs are present, it instantiates the component type directly with no further PTV check, bypassing the allowlist.
> 
> ## Impact
> Applications using `BasicPolymorphicTypeValidator` with `allowIfSubTypeIsArray()` as a safeguard get no protection for concrete array component types; an attacker controlling JSON can instantiate non-allowlisted types via an array wrapper, re-opening the gadget-instantiation risk PTV is meant to prevent.
> 
> ## Affected / Patched (verified via `git tag --contains`)
> - 2.18 line: `>= 2.10.0, < 2.18.8` -> fixed in **2.18.8**
> - 2.19-2.21 line: `>= 2.19.0, < 2.21.4` -> fixed in **2.21.4**
> - 3.x line: `>= 3.0.0, < 3.1.4` -> fixed in **3.1.4**
> 
> `PolymorphicTypeValidator` was added in 2.10.0 so vulnerability N/A for versions prior to that.
> 
> ## Severity / CWE
> Maintainer: significant. Reporter: HIGH. CWE-184 (Incomplete List of Disallowed Inputs); related CWE-502.
> 
> ## Upstream fix
> FasterXML/jackson-databind#5981; fix PR #5983 (`24529da`), 2.18 backport PR #5984 (`01d1692`). Released 2026-06-04 in 2.18.8 / 2.21.4 / 3.1.4.
> 
> ## Credits
> Omkhar Arasaratnam (@omkhar) - finder.

