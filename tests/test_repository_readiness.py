from __future__ import annotations
import hashlib, importlib.util, json, subprocess, tarfile, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("inputs", ROOT / "scripts/validate_deployment_inputs.py"); assert SPEC and SPEC.loader
INPUTS = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(INPUTS)
class ReadinessTests(unittest.TestCase):
    def test_validator(self) -> None: subprocess.run(["python3", "scripts/validate_repository_readiness.py"], cwd=ROOT, check=True)
    def test_image_override_is_rejected(self) -> None: self.assertEqual(INPUTS.validate({"BLACKBOX_EXPORTER_IMAGE": "example.invalid/x@sha256:" + "0" * 64}), 1)
    def test_fixed_inputs_pass(self) -> None: self.assertEqual(INPUTS.validate({}), 0)
    def test_bundle_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            paths = [Path(directory) / name for name in ("one.tar.gz", "two.tar.gz")]
            for path in paths: subprocess.run(["python3", "scripts/build_config_bundle.py", "--output", str(path)], cwd=ROOT, check=True)
            self.assertEqual(hashlib.sha256(paths[0].read_bytes()).digest(), hashlib.sha256(paths[1].read_bytes()).digest())
            manifest = json.loads((ROOT / "codestra/release/config-bundle.manifest.json").read_text())
            with tarfile.open(paths[0], "r:gz") as archive: names = set(archive.getnames())
            self.assertEqual(names, set(manifest["files"]) | {"codestra/release/config-bundle.manifest.json"})
if __name__ == "__main__": unittest.main()
