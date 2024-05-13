"""Groq AI example."""

import json
from bdb import BdbQuit
from os import environ
from random import choice
from sys import argv, exit

import inflect
from groq import BadRequestError, Groq
from pydantic import (BaseModel, Field, ValidationError, computed_field,
                      create_model)
from rich import print as rprint
from rich.table import Table

bp = breakpoint
Plural = inflect.engine()


Things = [
    "flowers"
    "meals",
    "jobs",
    "holidays",
    "books",
    "movies",
    "songs",
    "bands",
    "actors",
    "garments",
    "hobbies",
    "authors",
    "quotes",
    "languages",
    "countries",
]


class Thing(BaseModel):
    """Schema for an individual item."""

    number: int
    name: str


class List(BaseModel):
    """Schema for a list of arbitrary Thing objects."""

    items: list[Thing]

    @computed_field
    def plural(self) -> str:
        """Pluralized category name."""
        return Plural.plural(self.category, 2)


def make_model(category):
    """Return a model class."""
    category = Plural.singular_noun(category.lower())
    model_name = category.title().replace(" ", "")
    model = create_model(
        f"{model_name}List",
        category=(str, Field(default=category, init=False, frozen=True)),
        __base__=List,
    )

    return model


def main(category=None, count=5, model="llama3-8b-8192"):
    """Run an example Groq request."""
    category = category or choice(Things)
    key = environ.get("GROQ_API_KEY")
    client = Groq(api_key=key)

    Model = make_model(category)
    schema = json.dumps(Model.model_json_schema())

    messages = [
        {
            "role": "system",
            "content": (
                f"You will provide a list of {category}, "
                "excluding content with apostrophes,"
                "formatted in valid JSON;\n"
                f"The JSON object should use this schema: {schema}"
            )
        },
        {
            "role": "user",
            "content": f"Give me a list of {count} random {category}."
        }
    ]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
            stream=False
        )
    except BadRequestError as e:
        # Failure reasons:
        # - responses that contain apostraphies
        # - a response that was formatted as '{ item, item, item'

        rsp = e.response
        j = rsp.json()["error"]
        reason = f"{rsp.status_code} {rsp.reason_phrase}"
        desc = f"{j['code']} {j['message']}"
        failure = j.get("failed_generation")
        rprint(f"[Error {reason}] Request failed: {desc}")
        if failure:
            rprint(failure, highlight=False)
        exit(1)

    except ValidationError as e:
        message = e.body['error']['message']
        bp()
        rprint(f"[Error {e.status_code}] Request failed: {message}")
        exit(1)

    except BaseException as e:
        bp()
        exit(1)
        e

    content = response.choices[0].message.content
    items = Model.model_validate_json(content)

    table = Table("#", items.plural.title())

    for item in items.items:
        table.add_row(str(item.number), item.name)

    rprint(table)


if __name__ == "__main__":
    try:
        main(*argv[1:])
    except (SystemExit, BdbQuit):
        ...
