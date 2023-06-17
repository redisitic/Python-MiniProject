import os
from argparse import ArgumentParser

from raytracer.project import Project


def main(project_path: str, export_path: str | None):
    project = Project.load(project_path)

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

    args = argparser.parse_args()
    main(args.project, args.save)


if __name__ == '__main__':
    launch()
