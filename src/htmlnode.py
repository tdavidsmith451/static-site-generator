class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        html_string = ""
        for k, v in self.props.items():
            html_string += f' {k}="{v}"'
        return html_string
    
    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")

    def __eq__(self, other_node):
        if self.tag == other_node.tag and self.value == other_node.value and self.children == other_node.children and self.props == other_node.props:
            return True

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
  
    def to_html(self):
        if self.value == None:
            raise ValueError("value must not be None")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag must not be None")
        if self.children == None:
            raise ValueError("children must not be None")
        children_string = ""
        for c in self.children:
            children_string += c.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>'