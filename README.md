<div align="center">

  <img src="./stats.svg" width="100%" alt="Contributions in the last year"/>

  <p align="center">
    <a href="https://iqumnov.com" title="Website"><img src="./icons/website.svg" width="36" height="36" alt="Website"/></a>&nbsp;<a href="https://orcid.org/0009-0001-7924-1522" title="ORCID"><img src="./icons/orcid.svg" width="36" height="36" alt="ORCID"/></a>&nbsp;<a href="https://t.me/iqumnov" title="Telegram"><img src="./icons/telegram.svg" width="36" height="36" alt="Telegram"/></a>&nbsp;<a href="https://discord.com/users/iqumnov" title="Discord"><img src="./icons/discord.svg" width="36" height="36" alt="Discord"/></a>&nbsp;<a href="https://www.linkedin.com/in/iqumnov" title="LinkedIn"><img src="./icons/linkedin.svg" width="36" height="36" alt="LinkedIn"/></a>&nbsp;<a href="https://www.youtube.com/@Iqumnov" title="YouTube"><img src="./icons/youtube.svg" width="36" height="36" alt="YouTube"/></a>&nbsp;<a href="https://www.instagram.com/iqumnov" title="Instagram"><img src="./icons/instagram.svg" width="36" height="36" alt="Instagram"/></a>
  </p>

  <a href="mailto:matvei@iqumnov.com">matvei@iqumnov.com</a>

</div>

<br/>

<p align="center">
⌍ Overview ⌎
</p>

**Quantum Security, Cryptographic Engineering, and Low-Level Systems Defense.** Developing static verification tooling, kernel-level telemetry, and post-quantum cryptographic (PQC) architectures.

*   **Education:** B.S. in Information Security, Moscow Polytechnic University (Expected 2027).
*   Co-founder & curator at [Our Dynasty Art](https://ourdynasty.art) — gallery & collection spanning five generations of family artists.

---

<p align="center">
⌍ Core Initiatives ⌎
</p>

*   **[PQCanary](https://github.com/Iqumnov/PQCanary)** &nbsp;·&nbsp; [Visit ↗](https://pqcanary.pages.dev)
    *   **Enterprise Post-Quantum Cryptographic (PQC) Discovery, Verification & Automated Remediation Platform.**
    *   Identifies classical cryptographic algorithms vulnerable to quantum cryptanalysis (RSA, ECC, Diffie-Hellman) and generates compliance-ready Cryptographic Bills of Materials (CBOM) aligned with NIST standards (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA).
    *   Leverages the **Z3 SMT Solver** to formally prove inductive range bounds and constant-time execution across lattice polynomial reduction loops, statically eliminating secret-dependent timing side-channel leaks (KyberSlash).
    *   Features an automated AST-level code modernization engine alongside a zero-install, client-side WebAssembly analyzer running pure Rust, registered with persistent Zenodo DOI [10.5281/zenodo.24527917](https://doi.org/10.5281/zenodo.24527917).
    *   *Stack:* Rust, Solid.js, WebAssembly, Z3 SMT Solver, liboqs, Qiskit.

*   **[QIR Reversing](https://github.com/Iqumnov/Qir-Reversing)** &nbsp;·&nbsp; [Visit ↗](https://qir-reversing.iqumnov.com)
    *   **LLVM Quantum Intermediate Representation (QIR) Reverse Engineering, Topological Deobfuscation & Formal Verification Suite.**
    *   High-performance zero-copy disassembler parsing textual LLVM IR (`.ll`) and raw binary bitcode (`.bc`) with `#![forbid(unsafe_code)]` in the mathematical core.
    *   Applies quantum commutation algebra to eliminate self-inverse involutory gate pairs ($H^2 = I, X^2 = I, CX^2 = I$), consolidate continuous Lie group rotations ($R_z(\alpha) \cdot R_z(\beta)$), and prune dead unmeasured qubit telemetry.
    *   Mathematically verifies circuit equivalence via full dense matrix simulation in $2^N$-dimensional Hilbert space with exact Quantum Process Fidelity ($F = 1.00000000$), backed by machine-checked **Lean 4** unitary invariance proofs.
    *   Distributes standalone CLI binaries (`qir-rev`), an AI Agent Model Context Protocol server (`qir-rev-mcp`), a native C-ABI Rizin plugin (`librz_qir.so`), and a Cutter Qt/PySide GUI dock, registered with persistent Zenodo DOI [10.5281/zenodo.24528097](https://doi.org/10.5281/zenodo.24528097).
    *   *Stack:* Rust, LLVM QIR, Lean 4, WebAssembly, Rizin C-ABI, Cutter (PySide), OpenQASM 3.0, MCP JSON-RPC 2.0.

*   **[TurtleShell](https://github.com/Iqumnov/TurtleShell)** &nbsp;·&nbsp; [Visit ↗](https://turtleshell.iqumnov.com)
    *   **Multi-Tenant Process Isolation, Side-Channel Defense & Hardware Benchmarking Platform for Quantum Clouds.**
    *   Protects co-located multi-tenant workloads across Superconducting (IBM Heron/Eagle), Trapped-Ion, and Neutral-Atom lattices via a 4-contour defense architecture: graph-spectral QPU partitioning (Contour 1), static SHA-256 bytecode & anomaly auditing (Contour 2), temporal laser-cooling buffers with QuTiP Lindblad master equation verification (Contour 3), and telemetric differential SPC anomaly monitoring (Contour 4).
    *   Ships with the **QIB (Quantum Isolation Benchmark)** suite evaluating cross-tenant crosstalk, Rowhammer-style coherent gate hammering, and motional state residual excitation across cloud providers.
    *   Features an offline, zero-backend browser simulation engine on Cloudflare Pages alongside a high-throughput Python FastAPI/QuTiP backend, registered with persistent Zenodo DOI [10.5281/zenodo.24528037](https://doi.org/10.5281/zenodo.24528037).
    *   *Stack:* Python, FastAPI, QuTiP, Qiskit, TypeScript, React, Vite, NetworkX, Scikit-learn.

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
*   **[IBM Qiskit Quantum Excellence Awards](./Certifications/IBM_Quantum_Excellence_2026.pdf)** | 2026, 2021, 2020 (Qiskit Global Summer School)
*   **[Lomonosov MSU Case-Championship Winner](./Certifications/MSU_Winner_Matvei_Igumnov_Team_1.pdf)** | Medical Analytical Platform (Healthy Technologies)
*   **[Womanium Global Quantum Computing Program](./Certifications/Womanium_Quantum_2022_Matvei_Igumnov.pdf)** | Hardware Certificate (MIT, IBM, Princeton Partnership)
*   **[QHack Coding Challenges Certificate](./Certifications/QHack_Coding_Challenge_Matvei_Igumnov.pdf)** | PennyLane / Xanadu
*   **[QWorld QSilver Diploma](./Certifications/QSilver2021_Matvei_Igumnov.pdf)** | Complex Numbers & Shor’s Algorithm | No: QSilver2-50

---

<div align="center">
  <h2>Русская версия / Russian Version</h2>
</div>

<p align="center">
⌍ Описание ⌎
</p>

**Квантовая безопасность, криптографическая инженерия и низкоуровневая защита систем.** Разработка инструментов статической верификации, телеметрии уровня ядра и архитектур постквантовой криптографии (PQC).

*   **Образование:** Бакалавр по направлению «Информационная безопасность», Московский политехнический университет (выпуск 2027).
*   Сооснователь и куратор [Our Dynasty Art](https://ourdynasty.art) — художественная галерея и фамильное собрание пяти поколений художников династии.

---

<p align="center">
⌍ Ключевые проекты ⌎
</p>

*   **[PQCanary](https://github.com/Iqumnov/PQCanary)** &nbsp;·&nbsp; [Сайт ↗](https://pqcanary.pages.dev)
    *   **Корпоративная платформа аудита, формальной верификации и автоматизированной миграции на постквантовую криптографию (PQC).**
    *   Выявляет классические криптографические алгоритмы, уязвимые для квантового криптоанализа (RSA, ECC, Diffie-Hellman), и генерирует спецификации Cryptographic Bill of Materials (CBOM) в соответствии со стандартами NIST (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA).
    *   Использует **Z3 SMT Solver** для формального доказательства индуктивных границ диапазонов и постоянного времени выполнения циклов полиномиальной редукции в решетках, статически устраняя утечки по побочным каналам времени (атаки KyberSlash).
    *   Оснащен движком семантической модернизации кода на уровне AST и полностью клиентским WebAssembly-анализатором на чистом Rust без передачи данных по сети (Zenodo DOI [10.5281/zenodo.24527917](https://doi.org/10.5281/zenodo.24527917)).
    *   *Стек:* Rust, Solid.js, WebAssembly, Z3 SMT Solver, liboqs, Qiskit.

*   **[QIR Reversing](https://github.com/Iqumnov/Qir-Reversing)** &nbsp;·&nbsp; [Сайт ↗](https://qir-reversing.iqumnov.com)
    *   **Комплекс обратной разработки, деобфускации и формальной верификации квантового промежуточного представления LLVM QIR.**
    *   Высокопроизводительный дисассемблер без копирования памяти для текстового LLVM IR (`.ll`) и бинарного биткода (`.bc`) с гарантией безопасности `#![forbid(unsafe_code)]` в математическом ядре.
    *   Применяет коммутационную алгебру квантовых вентилей для устранения самообратных инволютивных пар ($H^2 = I, X^2 = I, CX^2 = I$), объединения непрерывных вращений групп Ли ($R_z(\alpha) \cdot R_z(\beta)$) и отсечения неиспользуемых измерительных цепей.
    *   Математически доказывает унитарную эквивалентность схем через плотное матричное моделирование в $2^N$-мерном гильбертовом пространстве с точным расчетом точности квантового процесса ($F = 1.00000000$), подтвержденным формальными доказательствами в **Lean 4**.
    *   Включает автономный CLI (`qir-rev`), MCP-сервер протокола контекста моделей для ИИ-агентов (`qir-rev-mcp`), плагин C-ABI для фреймворка Rizin (`librz_qir.so`) и панель для Cutter Qt/PySide GUI (Zenodo DOI [10.5281/zenodo.24528097](https://doi.org/10.5281/zenodo.24528097)).
    *   *Стек:* Rust, LLVM QIR, Lean 4, WebAssembly, Rizin C-ABI, Cutter (PySide), OpenQASM 3.0, MCP JSON-RPC 2.0.

*   **[TurtleShell](https://github.com/Iqumnov/TurtleShell)** &nbsp;·&nbsp; [Сайт ↗](https://turtleshell.iqumnov.com)
    *   **Платформа многоарендной изоляции процессов, защиты от атак по побочным каналам и аппаратного бенчмаркинга для квантовых облаков.**
    *   Обеспечивает взаимную изоляцию параллельных пользовательских задач на сверхпроводниковых процессорах (IBM Heron/Eagle), ионных ловушках и массивах нейтральных атомов через 4-контурную систему защиты: спектральное разбиение графа связности QPU (Контур 1), статический аудит SHA-256 и аномалий байткода компилятора (Контур 2), временные буферы лазерного охлаждения с верификацией уравнения Линдблада в QuTiP (Контур 3) и дифференциальный контроль телеметрии SPC (Контур 4).
    *   Содержит пакет бенчмарков **QIB (Quantum Isolation Benchmark)** для аудита межпользовательских наводок (ZZ-crosstalk), циклического импульсного нагрева (Rowhammer) и паразитного заселения колебательных фононных мод.
    *   Поддерживает работу как автономного браузерного симулятора на Cloudflare Pages с нулевым бэкендом, так и локального сервиса на FastAPI и QuTiP (Zenodo DOI [10.5281/zenodo.24528037](https://doi.org/10.5281/zenodo.24528037)).
    *   *Стек:* Python, FastAPI, QuTiP, Qiskit, TypeScript, React, Vite, NetworkX, Scikit-learn.

---

<p align="center">
⌍ Технические навыки ⌎
</p>

```text
┌── Языки программирования ──► Rust • Python • C/C++ • Java • C# • SQL (Postgres) • OpenQASM
├── Безопасность и бэкенд ──► Spring Boot • Spring Security • Quarkus • Bouncy Castle (JCA/PQC) • Keycloak • gRPC
├── Квантовые вычисления ───► Qiskit • PennyLane • ETSI GS QKD 014 • Z3 SMT
├── Криптография и аудит ───► liboqs • NIST PQC (FIPS 203/204/205) • PKI / X.509 • PKCS#11 • eBPF • OpenTelemetry • DORA / NIS2
├── Инфраструктура и облака ─► Linux (RHEL/Debian) • Git • Docker • Kubernetes • AWS
└── Языки общения ──────────► Русский (родной) • Английский (продвинутый) • Французский (изучаю)
```

---

<p align="center">
⌍ Сертификаты и достижения ⌎
</p>

*   **[eLearnSecurity Certified Web Penetration Tester (eWPT v1.0)](./Certifications/eWPT_v1.0_Matvei_Igumnov.pdf)** | ID: 8017284
*   **[IBM Qiskit Quantum Excellence Awards](./Certifications/IBM_Quantum_Excellence_2026.pdf)** | 2026, 2021, 2020 (Qiskit Global Summer School)
*   **[Победитель кейс-чемпионата МГУ им. М.В. Ломоносова](./Certifications/MSU_Winner_Matvei_Igumnov_Team_1.pdf)** | Медицинская аналитическая платформа (Здоровые технологии)
*   **[Womanium Global Quantum Computing Program](./Certifications/Womanium_Quantum_2022_Matvei_Igumnov.pdf)** | Сертификат по квантовому оборудованию (партнерство MIT, IBM, Princeton)
*   **[QHack Coding Challenges Certificate](./Certifications/QHack_Coding_Challenge_Matvei_Igumnov.pdf)** | PennyLane / Xanadu
*   **[QWorld QSilver Diploma](./Certifications/QSilver2021_Matvei_Igumnov.pdf)** | Комплексные числа и алгоритм Шора | №: QSilver2-50
