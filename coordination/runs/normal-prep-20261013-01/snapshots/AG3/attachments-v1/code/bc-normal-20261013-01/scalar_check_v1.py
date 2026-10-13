"""AG2 AI-authored teacher check, revision 1, generated_material.

Model: x_next = x + u, u = -K*x + b; dimensionless, no delay/noise/saturation.
Source: disciplinary/mechanism-notes-v1.md and fixed AG1 design v1.
This is a finite numerical check, not robot simulation or learner performance.
All inputs and outputs are explicit files; output is created exclusively.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform


def rollout(k, b, e0, steps):
    values = [e0]
    for _ in range(steps):
        values.append((1.0 - k) * values[-1] + b)
    return values


def closed_form(k, b, e0, t):
    rho = 1.0 - k
    if rho == 1.0:
        return e0 + t * b
    return rho**t * e0 + b * (1.0 - rho**t) / (1.0 - rho)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    input_path, output_path = Path(args.input), Path(args.output)
    input_bytes = input_path.read_bytes()
    spec = json.loads(input_bytes.decode("utf-8-sig"))
    cases = []
    for case in spec["cases"]:
        values = rollout(case["K"], case["b"], case["e0"], case["steps"])
        for t, value in enumerate(values):
            if not math.isclose(value, closed_form(case["K"], case["b"], case["e0"], t), rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError("recurrence/closed form mismatch")
        cases.append({**case, "rho": 1.0 - case["K"], "nominal_mse": case["b"]**2,
                      "errors_t0_to_T": values, "terminal_within_tolerance": None if "tolerance" not in case else abs(values[-1]) <= case["tolerance"]})
    # Boundary conditions check the formula branch and an alternating contraction.
    for k, b, e0 in [(0.0, 0.02, 0.1), (1.5, 0.02, 0.1), (0.5, 0.0, 0.1)]:
        for t, value in enumerate(rollout(k, b, e0, 6)):
            assert math.isclose(value, closed_form(k, b, e0, t), rel_tol=1e-12, abs_tol=1e-12)
    result = {"origin": "generated_material", "executor": "AG2_teacher", "revision": 1,
              "python": platform.python_version(), "model_scope": spec["model_scope"],
              "input_path": input_path.as_posix(), "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
              "code_path": Path(__file__).as_posix(), "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "cases": cases, "verification": "recurrence equals closed form on requested finite cases and stated formula boundaries",
              "limitations": "no empirical data, no robot execution, no general proof, no learner run"}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps({"saved": output_path.as_posix(), "cases": len(cases)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
