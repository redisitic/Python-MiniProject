import os
from argparse import ArgumentParser

from raytracer.project import Project


def main(project_path: str, export_path: str | None, quite: bool):
    project = Project.load(project_path, quite)

    if export_path is None:
        export_path = os.path.join("output", f"{project.name}.png")

    project.render(export_path)


def launch():
    argparser = ArgumentParser(
        prog="Python Raytracer",
        description="A simple python raytracer that runs on the CPU."
    )

    argparser.add_argument('project', action='store', type=str, help="Path to the project file.")
    argparser.add_argument('-s', '--save', action='store', type=str, help="Save path. (Defaults to: `output/{PROJECT NAME}.png`", default=None)
    argparser.add_argument('-q', '--quite', action='store_true', help="Be quite.")

    args = argparser.parse_args()
    main(args.project, args.save, args.quite)


if __name__ == '__main__':
    launch()
