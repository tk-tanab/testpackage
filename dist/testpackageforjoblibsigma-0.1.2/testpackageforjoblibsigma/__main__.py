import argparse

import for_sigma
import joblib_sigma


# メインの処理
def main(args):
    """引数に応じて計算したシグマの値を返す

    Args:
        args : parseされた引数オブジェクト
    """
    if args.both or args.for_sigma:
        sigma_result = for_sigma.for_sigma(args.x0, args.x1, args.x2)
        print("for_result", sigma_result * args.coefficient)

    if args.both or args.joblib_sigma:
        sigma_result = joblib_sigma.joblib_sigma(args.x0, args.x1, args.x2)
        print("joblib_result", sigma_result * args.coefficient)


# 引数の処理 （エントリーポイント）
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="add one float and two integers")
    parser.add_argument("x0", type=float, help="exponent number (float)")
    parser.add_argument("x1", type=int, nargs="?", default=1, help="start k number (int)")
    parser.add_argument("x2", type=int, nargs="?", default=100, help="start k number (int)")

    parser.add_argument("-c", "--coefficient", nargs="?", type=float, default=1, help="coefficient number (float)")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--both", action="store_true", help="exert both for_sigma and joblib_sigma")
    group.add_argument("--for", action="store_true", help="exert for_sigma")
    group.add_argument("--joblib", action="store_true", help="exert joblib_sigma")

    args = parser.parse_args()
    main(args)
