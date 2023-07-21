
def get_expected_componentids():
    expected_values_x64 = {
        'CMP_WinServer2012_balloon':['{96F961AC-18DC-4C70-A996-72B5BDD7D276}'],
        'CMP_balloon_WdfCoInstaller01011_2k12_amd64':['{F9C31B15-8B2B-40BE-98C7-21EC7C35D4B5}'],
        'CMP_blnsvr_2k12_amd64':['{17BD7E51-C4E5-4B4D-B316-1836BDFC6F94}'],
        'CMP_WinServer2012R2_balloon':['{49BC041E-20A7-4245-BBBC-0BADD40D38D7}'],
        'CMP_blnsvr_2k12R2_amd64':['{9E677EFA-B180-48D7-ACF8-28B99625FC84}'],
        'CMP_WinServer2016_balloon':['{D604612F-EFD0-44CE-956C-5AD25518A742}'],
        'CMP_blnsvr_2k16_amd64':['{AC3A4978-2B0A-4E5C-9DAA-327C503E98C6}'],
        'CMP_WinServer2019_balloon':['{0279689F-2B56-47BB-BE08-2D66A0B9F4FC}'],
        'CMP_blnsvr_2k19_amd64':['{367F3AA4-7747-4FDF-A3F9-3D2766D9D07E}'],
        'CMP_WinServer2022_balloon':['{824217E9-568A-403A-82E1-408171BDB05B}'],
        'CMP_blnsvr_2k22_amd64':['{D87C64B1-1769-4D6D-B912-C7389AA5F997}'],
        'CMP_Win8x64_balloon':['{08FCD606-81D7-4AA0-9768-B2927F997BB1}'],
        'CMP_balloon_WdfCoInstaller01011_w8_amd64':['{B8755C52-FD83-41F3-8150-1C9B4FAFEDB7}'],
        'CMP_blnsvr_w8_amd64':['{B2A7BDF8-CCF4-4EFD-8B87-D61381D6B9DD}'],
        'CMP_Win81x64_balloon':['{81FB4292-A246-4DD5-B0A6-CCB52306FC05}'],
        'CMP_blnsvr_w8.1_amd64':['{23E41A8A-9759-49BF-B459-80B421B29055}'],
        'CMP_Win10x64_balloon':['{75F1C56D-21E9-4A46-AF12-912C9ECD29D2}'],
        'CMP_blnsvr_w10_amd64':['{66B082AC-9CF4-44D1-9CE1-63F7235F6C1C}'],
        'CMP_Win11x64_balloon':['{7E770B97-A137-4350-837D-A562CEB878AC}'],
        'CMP_blnsvr_w11_amd64':['{1555D369-5A0F-4ED7-BF58-5B863398A00F}'],
        'CMP_WinServer2012_netkvm':['{45A3A444-B794-4DEF-B733-78C2FDABFA39}'],
        'CMP_netkvm_netkvmco_2k12_amd64':['{18B0E0E7-388F-4D6C-B562-9900FB8F2B38}'],
        'CMP_netkvm_readme_2k12_amd64':['{1D81BACF-85B7-463F-8C4F-3D9E3A541158}'],
        'CMP_WinServer2012R2_netkvm':['{D600A20F-0D4F-4E89-BCD4-A2D2D6E22BD7}'],
        'CMP_netkvm_netkvmco_2k12R2_amd64':['{E5F8F3CE-D271-4139-B0B8-CD7934373344}'],
        'CMP_netkvm_readme_2k12R2_amd64':['{63602C8B-CDCC-4980-A7CF-688F6047BA09}'],
        'CMP_WinServer2016_netkvm':['{F76DFEFF-FC33-45E8-876B-0013852A0BC4}'],
        'CMP_netkvm_netkvmco_2k16_amd64':['{6A71DDEB-0CF4-4A64-94F4-CE3F5F396CEF}'],
        'CMP_netkvm_readme_2k16_amd64':['{9310CAD4-1935-4C02-8AE4-F3C91BD9BFA1}'],
        'CMP_WinServer2019_netkvm':['{EDDE3DE9-AEBB-49D5-A232-F2B7310A60A8}'],
        'CMP_netkvm_netkvmco_2k19_amd64':['{27B38D8F-0B8B-4261-8E26-5ACDA7BC5B18}'],
        'CMP_netkvm_readme_2k19_amd64':['{3D8E57A6-4643-4D57-BCC9-658696DB7F56}'],
        'CMP_WinServer2022_netkvm':['{3FC5E6F9-544A-49A0-963A-8452CB20E949}'],
        'CMP_netkvm_netkvmco_2k22_amd64':['{F3A70552-1D26-4B75-A5FF-53921B0F0DBC}'],
        'CMP_netkvm_readme_2k22_amd64':['{3B7BE477-98FC-4E97-80EE-6EC875A49D5E}'],
        'CMP_Win8x64_netkvm':['{161E7681-9AE9-4F31-8D90-02F119DD7555}'],
        'CMP_netkvm_netkvmco_w8_amd64':['{EFC2103D-BED3-4FD6-AC43-93F9B53BFDFE}'],
        'CMP_netkvm_readme_w8_amd64':['{3DAED9C8-8F64-41F2-913D-26D19DD61CBE}'],
        'CMP_Win81x64_netkvm':['{631BC21C-27E3-4C36-9789-7D2B22C6E5F3}'],
        'CMP_netkvm_netkvmco_w8.1_amd64':['{F5D6C74A-7D16-4B5D-8208-8E97C4654CAD}'],
        'CMP_netkvm_readme_w8.1_amd64':['{D51D70D8-E2BE-43E1-8D0C-042E145C89F1}'],
        'CMP_Win10x64_netkvm':['{DC8B83A8-6501-4494-81A7-454F43EB07E0}'],
        'CMP_netkvm_netkvmco_w10_amd64':['{2EC241D0-DFB0-4F2D-9E1F-F98475940BA4}'],
        'CMP_netkvm_readme_w10_amd64':['{85EDD336-0051-4F6B-89C3-5AD153E7B554}'],
        'CMP_Win11x64_netkvm':['{B931E603-768A-4FCE-A505-3E1435EBA378}'],
        'CMP_netkvm_netkvmco_w11_amd64':['{21928595-F2F6-4669-94C3-2E33BABC247D}'],
        'CMP_netkvm_readme_w11_amd64':['{20298575-7E69-47A6-82C9-7A9DEB802DB5}'],
        'CMP_WinServer2012_viorng':['{93C2AE75-81D3-437C-A445-9FFF42D1F340}'],
        'CMP_viorng_viorngum_2k12_amd64':['{56C0396B-DDD1-46BB-AEEE-83DD436BE882}'],
        'CMP_viorng_WdfCoInstaller01011_2k12_amd64':['{4B6225BD-CC20-4B0D-B19F-0F551FA7EC7D}'],
        'CMP_WinServer2012R2_viorng':['{550C5C07-46E0-4CE8-BA0E-77F79E914773}'],
        'CMP_viorng_viorngum_2k12R2_amd64':['{7549E5E9-EDAB-4DDC-8BE5-2A25F00C305E}'],
        'CMP_WinServer2016_viorng':['{106DD383-EA41-4CED-A1DE-BAD4B1421B42}'],
        'CMP_viorng_viorngum_2k16_amd64':['{903768B1-286A-4B00-B3B7-B3704394D5D7}'],
        'CMP_WinServer2019_viorng':['{EB4404C4-34A2-4378-9D66-A4D8841BAE56}'],
        'CMP_viorng_viorngum_2k19_amd64':['{8D85AA97-4238-4A28-9A79-B009FBEA7961}'],
        'CMP_WinServer2022_viorng':['{8B71783C-4721-4203-BA5B-69664BEECCCD}'],
        'CMP_viorng_viorngum_2k22_amd64':['{6A477A10-5405-4EDE-B0BB-F5831DE6D644}'],
        'CMP_Win8x64_viorng':['{6C430409-AFFA-4239-991F-FE03EA84B11E}'],
        'CMP_viorng_viorngum_w8_amd64':['{A8B4F308-C944-4BC6-898A-0190F041F038}'],
        'CMP_viorng_WdfCoInstaller01011_w8_amd64':['{13A176EC-65CF-48FC-848D-C3EA903E253D}'],
        'CMP_Win81x64_viorng':['{38CFF550-A911-498E-A9CB-061C5D9C6E6E}'],
        'CMP_viorng_viorngum_w8.1_amd64':['{D10D01BA-28C8-46D8-A967-2C60AFC014FF}'],
        'CMP_Win10x64_viorng':['{8600A950-7C8B-4EAE-84A4-8FFEA8BE906F}'],
        'CMP_viorng_viorngum_w10_amd64':['{32659F53-B2EB-4D72-A3D9-CBA7C6401D08}'],
        'CMP_Win11x64_viorng':['{09A012A4-0DA0-426E-95B8-5E91CC1AA174}'],
        'CMP_viorng_viorngum_w11_amd64':['{04DFD7AE-0E1D-4FC5-8F79-EC991DAF03E2}'],
        'CMP_WinServer2012_vioscsi':['{DF58EBA6-EFA5-4997-AC9E-618EC9093800}'],
        'CMP_WinServer2012R2_vioscsi':['{A7F4C0E2-9BBA-46E9-991C-74AEC0BEE4E6}'],
        'CMP_WinServer2016_vioscsi':['{2581A672-FDCB-45E4-9C3E-2D143FAD9D88}'],
        'CMP_WinServer2019_vioscsi':['{9B505BFA-24F1-4AFA-8F20-1150AD7DC384}'],
        'CMP_WinServer2022_vioscsi':['{CD88A70E-5F84-4A11-BA3C-AD8D158F8D68}'],
        'CMP_Win8x64_vioscsi':['{59D86BA7-401C-4022-A009-771CEB370A6F}'],
        'CMP_Win81x64_vioscsi':['{212B141F-9939-4945-AACC-EE5D5CDC2717}'],
        'CMP_Win10x64_vioscsi':['{D78BF955-D5B6-4080-A702-E98754D9174A}'],
        'CMP_Win11x64_vioscsi':['{4F28D54F-7DA0-4027-A61B-50355010345C}'],
        'CMP_WinServer2012_vioser':['{23C405AD-2234-417C-AFA0-33680AA344E5}'],
        'CMP_vioser_WdfCoInstaller01011_2k12_amd64':['{E1897898-22EB-4880-8BDE-192FC8B20CC1}'],
        'CMP_WinServer2012R2_vioser':['{E2EBF6E5-C5B5-41E4-BBDC-B9CCB668D45C}'],
        'CMP_WinServer2016_vioser':['{3DCC592D-542C-49E1-90EA-45177C01BC26}'],
        'CMP_WinServer2019_vioser':['{AA85E501-4E99-42A1-A519-9769D8C6ACAC}'],
        'CMP_WinServer2022_vioser':['{6AEBEAD8-7BE9-4981-A72F-14DC6E076D18}'],
        'CMP_Win8x64_vioser':['{69DC0B9B-F2F8-40C1-9E3D-3CC711696BDF}'],
        'CMP_vioser_WdfCoInstaller01011_w8_amd64':['{178B36BC-BE6B-4853-B586-F6F07853BC3A}'],
        'CMP_Win81x64_vioser':['{73568A72-CFAF-4C60-B915-D45746DC54D9}'],
        'CMP_Win10x64_vioser':['{98A0368C-E2D6-49A8-9B8C-1E3DFBCFFD19}'],
        'CMP_Win11x64_vioser':['{91CBFAC6-D648-4330-A205-C44B571954CE}'],
        'CMP_WinServer2012_viostor':['{E706318F-9E7A-4421-A951-C2A3562C8EC4}'],
        'CMP_WinServer2012R2_viostor':['{4964D140-95BC-4DF5-B6E6-A9607920C6B6}'],
        'CMP_WinServer2016_viostor':['{6AB4DF0A-AEC8-4F66-B9FE-AB47ADDCB857}'],
        'CMP_WinServer2019_viostor':['{57F26A76-3048-43AD-8852-412BF36D017B}'],
        'CMP_WinServer2022_viostor':['{83B88AE8-CE82-423F-9ED2-5403381105FE}'],
        'CMP_Win8x64_viostor':['{616B7CA7-4D72-474E-8FA4-CF7DBF76B294}'],
        'CMP_Win81x64_viostor':['{99116486-F088-4E7E-9187-49D5BE1C3B1F}'],
        'CMP_Win10x64_viostor':['{884ADCD2-0334-45AB-9806-F21ED4D16D48}'],
        'CMP_Win11x64_viostor':['{70FFAB18-7DAA-47D7-86B4-CEA358DEFB0C}'],
        'CMP_WinServer2012_viofs':['{0B1F3B06-EB7C-422E-A347-58BE0D1C5E8B}'],
        'CMP_viofs_WdfCoInstaller01011_2k12_amd64':['{0CED08C2-7C43-40AA-8453-1D72F4455C19}'],
        'CMP_virtiofs_2k12_amd64':['{E27A24F9-EDDA-4F34-ADB6-0E9E8A40AE6A}'],
        'CMP_WinServer2012R2_viofs':['{E790AD8E-A7F8-4182-AC87-4FCA639D125E}'],
        'CMP_virtiofs_2k12R2_amd64':['{90139462-F500-4411-A1D2-CCC4093B6A8E}'],
        'CMP_WinServer2016_viofs':['{3D1814BB-CDF2-4918-BD34-EA697A14D63B}'],
        'CMP_virtiofs_2k16_amd64':['{7F51A186-28F4-4C7C-986B-279AC73F6C9C}'],
        'CMP_WinServer2019_viofs':['{794FE5BB-E999-4257-A4C1-2E4E9DC4A213}'],
        'CMP_virtiofs_2k19_amd64':['{1D146EAB-CC13-45E8-A0BC-FA70A2F913AF}'],
        'CMP_WinServer2022_viofs':['{0EE9BBA1-9168-4D30-83BC-9DCD408BEB19}'],
        'CMP_virtiofs_2k22_amd64':['{E355531E-4609-4CD3-8F9C-361795825A02}'],
        'CMP_Win8x64_viofs':['{5DA3AF56-C49F-47AC-83D7-70AB4AF45292}'],
        'CMP_viofs_WdfCoInstaller01011_w8_amd64':['{1E6ED880-FC13-4912-8F92-B572FF739330}'],
        'CMP_virtiofs_w8_amd64':['{4F231DC2-A646-4463-A55E-F81F19AE2701}'],
        'CMP_Win81x64_viofs':['{F2F51EE8-09F2-4E05-9720-D4F0120CBC16}'],
        'CMP_virtiofs_w8.1_amd64':['{275DDF53-AE23-40B4-9BA0-850BE7F8C528}'],
        'CMP_Win10x64_viofs':['{E4F42A9F-D576-4606-B2BF-96D24E53E365}'],
        'CMP_virtiofs_w10_amd64':['{3D0B70D1-C98E-4986-A0D1-6CF4B1E06CC9}'],
        'CMP_Win11x64_viofs':['{78836E98-4BD5-4D03-82CC-3AC21542545D}'],
        'CMP_virtiofs_w11_amd64':['{643AE04C-905E-478D-A955-387DB8F65425}'],
#        'CMP_WinServer2012_viogpudo':['{04300AD8-1B36-4BCC-B0B3-B63A2E503F77}'],
#        'CMP_WinServer2012R2_viogpudo':['{4F2BE310-5CC4-4BB0-B241-870724119DAC}'],
        'CMP_WinServer2016_viogpudo':['{2749BFA1-F330-408C-9FB3-872D173DA3AE}'],
        'CMP_WinServer2019_viogpudo':['{F76D4E1B-9FF2-4B82-A5E3-17F64E6253FC}'],
        'CMP_WinServer2022_viogpudo':['{B541D990-26F9-4141-AC56-A39A804C3F4D}'],
#        'CMP_Win8x64_viogpudo':['{72D2DEA4-31C6-4C05-B352-19E103278EC1}'],
#        'CMP_Win81x64_viogpudo':['{ED43C5C5-C68E-44A5-B798-BFB859933734}'],
        'CMP_Win10x64_viogpudo':['{0FEEC31F-F6E7-4865-AFD3-3E02451C46AD}'],
        'CMP_Win11x64_viogpudo':['{EAC432D2-C88F-49CA-90E7-7AC72974D325}'],
        'CMP_WinServer2022_pvpanic':['{6623B93F-8C4A-4FD3-8A02-767B04682A42}'],
        'CMP_Win11x64_pvpanic':['{B465A5A3-25A9-4924-9F6F-79BFE5066DC3}'],
        'CMP_WinServer2022_qemupciserial':['{9A944EAD-1E58-4AE0-A2FE-303FE4BCBA69}'],
        'CMP_Win11x64_qemupciserial':['{8D61E1C4-B9F4-4FDE-A171-5ECFB9AEADBA}'],
        'CMP_WinServer2022_vioinput':['{753A2041-BE3E-44F9-ABE3-394B7EBD2B46}'],
        'CMP_vioinput_viohidkmdf_2k22_amd64':['{D80F19F5-B422-4177-A9B9-6233C3A5EEDB}'],
        'CMP_Win11x64_vioinput':['{FDFC0048-91E6-4179-B235-0941C7EAEAA4}'],
        'CMP_vioinput_viohidkmdf_w11_amd64':['{283CA7B0-1797-410D-8B42-5255267C5DB0}'],
        'CMP_WinServer2012_fwcfg':['{11691408-18A5-43E1-AA4E-2E0217A76993}'],
        'CMP_fwcfg_WdfCoInstaller01011_2k12_amd64':['{0562B734-7F4A-431A-A4CC-CE3211345C46}'],
        'CMP_WinServer2012R2_fwcfg':['{935496ED-7356-47C7-895F-7656D9B31F94}'],
        'CMP_WinServer2016_fwcfg':['{7D32ABFB-E9A0-42D9-89F5-72E11B088989}'],
        'CMP_WinServer2019_fwcfg':['{B1C91741-7C0E-4041-A651-E6887B197A15}'],
        'CMP_WinServer2022_fwcfg':['{F20E93BC-E083-4E56-9AFD-4147369880AD}'],
        'CMP_Win8x64_fwcfg':['{04B0AB4E-2415-41CB-A025-074F1E4537CD}'],
        'CMP_fwcfg_WdfCoInstaller01011_w8_amd64':['{B50E490D-F987-439F-9035-54111ED73576}'],
        'CMP_Win81x64_fwcfg':['{979D702D-82B2-42C3-BF5D-4E1DA7404D2F}'],
        'CMP_Win10x64_fwcfg':['{73F380D6-BA74-44D3-82A3-40679FA73522}'],
        'CMP_Win11x64_fwcfg':['{7CD5A9FE-D145-4F82-BD09-EB4599C8558B}'],
    }

    expected_values_x86 = {
        'CMP_Win8x86_balloon':['{8A0794B3-D4C5-4D2A-A9D2-DD052656839C}'],
        'CMP_balloon_WdfCoInstaller01011_w8_x86':['{BD468265-3A74-4E40-9E41-B8B5E4F4F391}'],
        'CMP_blnsvr_w8_x86':['{95C93A87-8CC7-4577-B651-0B3886CD8022}'],
        'CMP_Win81x86_balloon':['{C5990116-89B9-4EE6-89BB-B41AD5F7A892}'],
        'CMP_blnsvr_w8.1_x86':['{3E282EDE-EB0E-4103-87A5-73A134E1BC6F}'],
        'CMP_Win10x86_balloon':['{DF5DA075-CFCF-425A-A555-548E60B2835E}'],
        'CMP_blnsvr_w10_x86':['{908D56E1-A780-46CB-BAFC-8775E7BC2B7F}'],
        'CMP_Win8x86_netkvm':['{9370CEF5-6103-4BDB-AD70-C90CCDC036F4}'],
        'CMP_netkvm_netkvmco_w8_x86':['{80056865-091E-4DCE-ADF5-DCCD5F29A6AC}'],
        'CMP_netkvm_readme_w8_x86':['{012C7189-BD1A-4A4B-BFBB-9F9D33C92734}'],
        'CMP_Win81x86_netkvm':['{F003BBF6-F97D-4E78-9301-ABD4AC13D528}'],
        'CMP_netkvm_netkvmco_w8.1_x86':['{10565F6E-4CEC-4781-BBA8-69090B6F48D6}'],
        'CMP_netkvm_readme_w8.1_x86':['{54B9CBFA-9589-4BF0-8C2F-6BC69621861B}'],
        'CMP_Win10x86_netkvm':['{51E576FD-C649-4D6C-B30D-8FD5807318C1}'],
        'CMP_netkvm_netkvmco_w10_x86':['{06224827-B12C-451D-A0E7-1023747302E9}'],
        'CMP_netkvm_readme_w10_x86':['{D9A889B2-6D9A-45FF-AC88-7E0FFA4C44FA}'],
        'CMP_Win8x86_viorng':['{99B5101C-9EDD-40FF-9528-9B2C630FCECA}'],
        'CMP_viorng_viorngum_w8_x86':['{D13FBFD8-D38C-467F-9939-BF5D2E75382D}'],
        'CMP_viorng_WdfCoInstaller01011_w8_x86':['{8019163B-C400-4801-A261-8017BA746F6C}'],
        'CMP_Win81x86_viorng':['{97AB60B7-B7DB-47D9-8A39-2BFE3CB63D9A}'],
        'CMP_viorng_viorngum_w8.1_x86':['{DBCA6A6E-5C09-41CB-97D9-7DFE5BDF9177}'],
        'CMP_Win10x86_viorng':['{8702F843-FC88-4810-9BB4-E28560187290}'],
        'CMP_viorng_viorngum_w10_x86':['{675D7446-E963-4AF3-A4DB-FF3D749FDAF9}'],
        'CMP_Win8x86_vioscsi':['{D4386CD9-8535-4926-90D0-A3E7C54FB0FC}'],
        'CMP_Win81x86_vioscsi':['{68C0498E-2CA1-4A97-819C-05C6BFA97886}'],
        'CMP_Win10x86_vioscsi':['{3A763786-27EA-4967-86DB-D6D982D7CACB}'],
        'CMP_Win8x86_vioser':['{349C230C-DF4C-44F5-8F29-5C743772E702}'],
        'CMP_vioser_WdfCoInstaller01011_w8_x86':['{AC95A59D-399F-4B2D-BBFA-6DF1B42DD0C7}'],
        'CMP_Win81x86_vioser':['{56DD4FB0-6075-4136-BCC5-B4E37B5483E1}'],
        'CMP_Win10x86_vioser':['{DF2A920C-E408-4479-8156-E86EC9DCA9D4}'],
        'CMP_Win8x86_viostor':['{071F14DE-1368-4117-8C82-3A388DF0BE81}'],
        'CMP_Win81x86_viostor':['{1AD92C03-9AB7-42A8-893B-77758F4F340C}'],
        'CMP_Win10x86_viostor':['{E514AF40-771B-4028-96B3-0E0268A4C176}'],
        'CMP_Win8x86_viofs':['{968E6D29-2F81-40EB-8318-4C7849228EFD}'],
        'CMP_viofs_WdfCoInstaller01011_w8_x86':['{3711996F-2AE9-4363-AB70-CD6A6B66140B}'],
        'CMP_virtiofs_w8_x86':['{B72B9865-9D86-41FB-936B-18FD4B9DC34A}'],
        'CMP_Win81x86_viofs':['{CD229D7D-9052-4F3A-8D30-11C92C42AE38}'],
        'CMP_virtiofs_w8.1_x86':['{25676CB3-D9A7-4E34-8DF7-5C33891EABEA}'],
        'CMP_Win10x86_viofs':['{19BCC8D3-F4E9-41C1-AF79-196C9F2B16B8}'],
        'CMP_virtiofs_w10_x86':['{CDC4821F-E00B-48BB-9A4A-5C1A420333F9}'],
 #       'CMP_Win8x86_viogpudo':['{B7583BDC-6079-45F5-8F75-D990547AC7C7}'],
 #       'CMP_Win81x86_viogpudo':['{1D3226C6-6446-4E81-8162-0B1E33823F99}'],
        'CMP_Win10x86_viogpudo':['{D5AB2386-95A5-4ECD-A0CF-8F0DF40ABDD3}'],
        'CMP_Win8x86_fwcfg':['{C2EC93F7-F85A-498B-AF47-83556C006D75}'],
        'CMP_fwcfg_WdfCoInstaller01011_w8_x86':['{53EB7169-2583-4F39-92FE-21E3CA57434A}'],
        'CMP_Win81x86_fwcfg':['{B66970A5-3AD3-4454-97DE-5E5D88D93FFF}'],
        'CMP_Win10x86_fwcfg':['{576398C6-231E-4FE0-8AF6-E62BF5015F70}'],
        }
    return (
        ("Component", "ComponentId"),
        {
            'x86': expected_values_x86,
            'x64': expected_values_x64
        }
    )


def get_expected_upgrade_code():
    expected_values_x64 = {'UpgradeCode':['{05294E2F-7778-4E46-B2A3-CF039D5767C8}']}
    expected_values_x86 = {'UpgradeCode':['{22C8F100-2ED1-4A99-A8FC-C391F0D1D7E7}']}
    return (
        ("Property", "Value"),
        {
            'x86': expected_values_x86,
            'x64': expected_values_x64
        }
    )

def get_expected_allusers_property():
    expected_values_x64 = {'ALLUSERS':['1']}
    expected_values_x86 = {'ALLUSERS':['1']}
    return (
        ("Property", "Value"),
        {
            'x86': expected_values_x86,
            'x64': expected_values_x64
        }
    )

def get_expected_RegLocator():
    expected_values_x64 = {
        'ProductNameSearch': [r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 'ProductName'],
        'CurrentBuildNumberSearch': [r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 'CurrentBuildNumber'],
        'wgt_uninstall_path': [r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{042CD13C-735D-4140-B146-D3F8263D7E4C}', 'UninstallString']
    }
    expected_values_x86 = {
        'ProductNameSearch':[r'SOFTWARE\Microsoft\Windows NT\CurrentVersion', 'ProductName'],
        'wgt_uninstall_path':[r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{042CD13C-735D-4140-B146-D3F8263D7E4C}', 'UninstallString'],
    }
    return (
        ("Signature", "Key", "Name"),
        {
            'x86': expected_values_x86,
            'x64': expected_values_x64
        }
    )

def get_expected_registry():
    expected_values_x64 = {'Registry_Tcp1323Opts': [r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'Tcp1323Opts']}
    expected_values_x86 = {'Registry_Tcp1323Opts': [r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters', 'Tcp1323Opts']}
    return (
        ("Registry", "Key", "Name"),
        {
            'x86': expected_values_x86,
            'x64': expected_values_x64
        }
    )
