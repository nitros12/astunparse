import ast
import sys

from tests.common import AstunparseCommonTestCase

import astunparse_noparen

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class UnparseTestCase(AstunparseCommonTestCase, unittest.TestCase):

    def assertASTEqual(self, ast1, ast2):
        self.assertEqual(ast.dump(ast1), ast.dump(ast2))

    def check_roundtrip(self, code1, filename="internal", mode="exec"):
        ast1 = compile(str(code1), filename, mode, ast.PyCF_ONLY_AST)
        code2 = astunparse_noparen.unparse(ast1)
        ast2 = compile(code2, filename, mode, ast.PyCF_ONLY_AST)
        self.assertASTEqual(ast1, ast2)
