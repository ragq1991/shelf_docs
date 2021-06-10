import shelf_of_docs as sd

class TestThis:

    def test_check_document_existance(self):
        assert sd.check_document_existance("2207 876234") == True
        assert sd.check_document_existance("11-2") == True
        assert sd.check_document_existance("10006") == True
        assert sd.check_document_existance("123") == False

    def test_get_doc_owner_name(self):
        assert sd.get_doc_owner_name("2207 876234") == "Василий Гупкин"
        assert sd.get_doc_owner_name("11-2") == "Геннадий Покемонов"
        assert sd.get_doc_owner_name("10006") == "Аристарх Павлов"
        assert sd.get_doc_owner_name("123") == None

    def test_get_all_doc_owners_names(self):
        assert sd.get_all_doc_owners_names() == {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}

    def test_add_new_shelf(self):
        assert sd.add_new_shelf("1") == ("1", False)
        assert sd.add_new_shelf("2") == ("2", False)
        assert sd.add_new_shelf("3") == ("3", False)
        assert sd.add_new_shelf("4") == ("4", True)

    def test_get_doc_shelf(self):
        assert sd.get_doc_shelf("2207 876234") == "1"
        assert sd.get_doc_shelf("11-2") == "1"
        assert sd.get_doc_shelf("10006") == "2"
        assert sd.get_doc_shelf("123") == None

    def test_show_document_info(self):
        for current_document in sd.documents:
            assert sd.show_document_info(current_document) == (current_document["type"], current_document["number"],
                                                               current_document["name"])

    def test_remove_doc_from_shelf(self):
        assert sd.remove_doc_from_shelf("2207 876234") == True
        assert sd.remove_doc_from_shelf("11-2") == True
        assert sd.remove_doc_from_shelf("10006") == True
        assert sd.remove_doc_from_shelf("123") == False

    def test_delete_doc(self):
        assert sd.delete_doc("2207 876234") == ("2207 876234", True)
        assert sd.delete_doc("11-2") == ("11-2", True)
        assert sd.delete_doc("10006") == ("10006", True)
        assert sd.delete_doc("123") == None
