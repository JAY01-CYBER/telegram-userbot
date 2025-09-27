from telethon import events
import ast, operator as op

# safe eval adapted from https://stackoverflow.com/a/9558001/404385
allowed_operators = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
    ast.USub: op.neg, ast.Mod: op.mod
}

def safe_eval(expr):
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return allowed_operators[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return allowed_operators[type(node.op)](_eval(node.operand))
        else:
            raise TypeError(node)
    return _eval(ast.parse(expr, mode='eval').body)

def register(client, owner_id):
    @client.on(events.NewMessage(pattern=r"^!calc\s+(.+)", incoming=True))
    async def calc_handler(event):
        expr = event.pattern_match.group(1).strip()
        try:
            result = safe_eval(expr)
            await event.reply(f"🧮 Result: {result}")
        except Exception as e:
            await event.reply(f"❌ Calc error: {e}")
