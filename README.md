<div align="center">

  <img src="./stats.svg" width="100%" alt="Contributions in the last year"/>

  [Instagram](https://www.instagram.com/iqumnov) &nbsp;·&nbsp;
  [LinkedIn](https://www.linkedin.com/in/iqumnov) &nbsp;·&nbsp;
  [Telegram](https://t.me/iqumnov) &nbsp;·&nbsp;
  [Email](mailto:iqumnov@proton.me)

</div>

<br/>

<p align="center">
⌍ Overview ⌎
</p>

**Quantum Security, Cryptographic Engineering, and Low-Level Systems Defense.** Developing static verification tooling, kernel-level telemetry, and post-quantum cryptographic (PQC) architectures.

*   **Education:** B.S. in Information Security, Moscow Polytechnic University (Expected 2027).

---

<p align="center">
⌍ Core Initiatives ⌎
</p>

*   **[PQCanary](https://github.com/Iqumnov/PQCanary)** &nbsp;·&nbsp; [Live Platform ↗](https://pqcanary.pages.dev)
    *   **Enterprise Post-Quantum Cryptographic (PQC) Discovery, Verification & Automated Remediation Platform.**
    *   Identifies classical cryptographic algorithms vulnerable to quantum cryptanalysis (RSA, ECC, Diffie-Hellman) and generates compliance-ready Cryptographic Bills of Materials (CBOM) aligned with NIST standards (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA).
    *   Leverages the **Z3 SMT Solver** to formally prove inductive range bounds and constant-time execution across lattice polynomial reduction loops, statically eliminating secret-dependent timing side-channel leaks (KyberSlash).
    *   Features an automated AST-level code modernization engine alongside a zero-install, client-side WebAssembly analyzer running pure Rust.
    *   *Stack:* Rust, Solid.js, WebAssembly, Z3 SMT Solver, liboqs, Qiskit.

*   **[qir-reversing](https://github.com/Iqumnov/Qir-Reversing)** &nbsp;·&nbsp; [Live Web App ↗](https://qir-reversing.iqumnov.com) &nbsp;·&nbsp; [Release v0.1.0 ↗](https://github.com/Iqumnov/Qir-Reversing/releases/tag/v0.1.0)
    *   **LLVM Quantum Intermediate Representation (QIR) Reverse Engineering, Topological Deobfuscation & Formal Verification Suite.**
    *   High-performance zero-copy disassembler parsing textual LLVM IR (`.ll`) and raw binary bitcode (`.bc`) with `#![forbid(unsafe_code)]` in the mathematical core.
    *   Applies quantum commutation algebra to eliminate self-inverse involutory gate pairs ($H^2 = I, X^2 = I, CX^2 = I$), consolidate continuous Lie group rotations ($R_z(\alpha) \cdot R_z(\beta)$), and prune dead unmeasured qubit telemetry.
    *   Mathematically verifies circuit equivalence via full dense matrix simulation in $2^N$-dimensional Hilbert space with exact Quantum Process Fidelity ($F = 1.00000000$), backed by machine-checked **Lean 4** unitary invariance proofs.
    *   Distributes standalone CLI binaries (`qir-rev`, `qrev`), an AI Agent Model Context Protocol server (`qir-rev-mcp`), a native C-ABI Rizin plugin (`librz_qir.so`), and a Cutter Qt/PySide GUI dock.
    *   *Stack:* Rust, LLVM QIR, Lean 4, WebAssembly, Rizin C-ABI, Cutter (PySide), OpenQASM 3.0, MCP JSON-RPC 2.0.

*   **[TurtleShell](https://github.com/Iqumnov/TurtleShell)** &nbsp;·&nbsp; [Quickstart ↗](https://github.com/Iqumnov/TurtleShell#quickstart)
    *   **High-Assurance Linux Process Isolation & Multi-Tenant Security Sandbox.**
    *   Enforces multi-layer defense-in-depth isolation for untrusted workloads using strict **Seccomp-BPF** dynamic syscall filter graphs, unprivileged user namespaces (`CLONE_NEWUSER`, `CLONE_NEWPID`, `CLONE_NEWNET`, `CLONE_NEWNS`), and POSIX capability bounding set stripping (`cap_drop_bound`).
    *   Integrates kernel-level **Landlock LSM** to enforce unbypassable, fine-grained filesystem hierarchy access controls at the kernel VFS layer.
    *   Includes open-source numerical and formal boundary verification benchmarks for multi-tenant containment integrity.
    *   *Stack:* Rust, C, Linux Seccomp-BPF, Landlock LSM, Namespaces, Capabilities.

---

<p align="center">
⌍ Technical Skills ⌎
</p>

```text
┌── Languages ───────────► Rust • Python • C/C++ • Java • C# • SQL (Postgres) • OpenQASM
├── Security & Backend ──► Spring Boot • Spring Security • Quarkus • Bouncy Castle (JCA/PQC) • Keycloak • gRPC
├── Quantum & Formal ────► Qiskit • PennyLane • ETSI GS QKD 014 • Z3 SMT
├── Crypto & Compliance ─► liboqs • NIST PQC (FIPS 203/204/205) • PKI / X.509 • PKCS#11 • eBPF • OpenTelemetry • DORA / NIS2
├── Infra & Cloud ───────► Linux (RHEL/Debian) • Git • Docker • Kubernetes • AWS
└── Spoken Languages ────► English (Advanced) • French (Learning) • Russian (Native)
```

---

<p align="center">
⌍ Validation & Milestones ⌎
</p>

*   **[eLearnSecurity Certified Web Penetration Tester (eWPT v1.0)](./Certifications/eWPT_v1.0_Matvei_Igumnov.pdf)** | ID: 8017284
*   **[IBM Qiskit Quantum Excellence Awards](./Certifications/IBM_Quantum_Excellence_2026.pdf)** | 2026, 2021, 2020 ([Qiskit Global Summer School](./Certifications/IBM_Qiskit_Global_Summer_School_Excellence_Matvei_Igumnov.pdf))
*   **[Lomonosov MSU Case-Championship Winner](./Certifications/MSU_Winner_Matvei_Igumnov_Team_1.pdf)** | Medical Analytical Platform (Healthy Technologies)
*   **[Womanium Global Quantum Computing Program](./Certifications/Womanium_Quantum_2022_Matvei_Igumnov.pdf)** | Hardware Certificate (MIT, IBM, Princeton Partnership)
*   **[QHack Coding Challenges Certificate](./Certifications/QHack_Coding_Challenge_Matvei_Igumnov.pdf)** | PennyLane / Xanadu
*   **[QWorld QSilver Diploma](./Certifications/QSilver2021_Matvei_Igumnov.pdf)** | Complex Numbers & Shor’s Algorithm | No: QSilver2-50
