# Understanding the Bug Characteristics and Fix Strategies of Federated Learning Systems

This repository consists of three main folders: Dataset_Collection, Manual_Labelling and Quantitative_study.

1. **Dataset_Collection** folder: The list of Issues and Pull Rquests for each framework from GitHub mined in the **first two steps** are presented in the file `GitHub/{frameworkname}/issues_init.csv`, `GitHub/{frameworkname}/issues_step2.csv`, `GitHub/{frameworkname}/PRs_init.csv` and `GitHub/{frameworkname}/PRs_step2.csv`.

    Total data and data collection process of 6 federated learning frameworks (Issues and PRs that were posted before July 20, 2022 are collected.):
    <table>
        <tr>
            <th rowspan="2">Framework</th>
            <th colspan="5"><div align="center">Total</div></th>
            <th colspan="2"><div align="center">Step1</div></th>
            <th colspan="2"><div align="center">Step2</div></th>
            <th colspan="2"><div align="center">Step3</div></th>
        </tr>
        <tr>
            <td><div align="right">LOC</div></td>
            <td><div align="right">Forks</div></td>
            <td><div align="right">Stars</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
        </tr>
        <tr>
            <td>
                <div align="center">PySyft</div>
                <div align="center">FATE</div>
                <div align="center">TFF</div>
                <div align="center">Flower</div>
                <div align="center">Fedlearner</div>
                <div align="center">PaddleFL</div>
            </td>
            <td>
                <div align="right">3.8m</div>
                <div align="right">497.3k</div>
                <div align="right">206.5k</div>
                <div align="right">49.1k</div>
                <div align="right">209.8k</div>
                <div align="right">87.0k</div>
            </td>
            <td>
                <div align="right">1,833</div>
                <div align="right">1,310</div>
                <div align="right">473</div>
                <div align="right">293</div>
                <div align="right">166</div>
                <div align="right">102</div>
            </td>
            <td>
                <div align="right">8,218</div>
                <div align="right">4,371</div>
                <div align="right">1,901</div>
                <div align="right">1,136</div>
                <div align="right">783</div>
                <div align="right">393</div>
            </td>
            <td>
                <div align="right">3,062</div>
                <div align="right">834</div>
                <div align="right">242</div>
                <div align="right">118</div>
                <div align="right">20</div>
                <div align="right">65</div>
            </td>
            <td>
                <div align="right">3,491</div>
                <div align="right">2,800</div>
                <div align="right">2,630</div>
                <div align="right">894</div>
                <div align="right">944</div>
                <div align="right">153</div>
            </td>
            <td>
                <div align="right">439</div>
                <div align="right">271</div>
                <div align="right">163</div>
                <div align="right">35</div>
                <div align="right">6</div>
                <div align="right">24</div>
            </td>
            <td>
                <div align="right">649</div>
                <div align="right">163</div>
                <div align="right">173</div>
                <div align="right">36</div>
                <div align="right">35</div>
                <div align="right">14</div>
            </td>
            <td>
                <div align="right">270</div>
                <div align="right">224</div>
                <div align="right">68</div>
                <div align="right">22</div>
                <div align="right">4</div>
                <div align="right">11</div>
            </td>
            <td>
                <div align="right">386</div>
                <div align="right">129</div>
                <div align="right">96</div>
                <div align="right">13</div>
                <div align="right">29</div>
                <div align="right">11</div>
            </td>
            <td>
                <div align="right">80</div>
                <div align="right">79</div>
                <div align="right">21</div>
                <div align="right">8</div>
                <div align="right">2</div>
                <div align="right">2</div>
            </td>
            <td>
                <div align="right">49</div>
                <div align="right">46</div>
                <div align="right">26</div>
                <div align="right">5</div>
                <div align="right">11</div>
                <div align="right">6</div>
            </td>
        </tr>
        <tr>
            <td><div align="center">Sum</div></td>
            <td><div align="right">4.8m</div></td>
            <td><div align="right">4,177</div></td>
            <td><div align="right">16,802</div></td>
            <td><div align="right">4,341</div></td>
            <td><div align="right">10,912</div></td>
            <td><div align="right">938</div></td>
            <td><div align="right">1,070</div></td>
            <td><div align="right">599</div></td>
            <td><div align="right">664</div></td>
            <td><div align="right">192</div></td>
            <td><div align="right">143</div></td>
    </table>

    The list of StackOverflow bugs based on tag and keywords is presented in the file [Dataset_Collection/StackOverflow/so_init.csv](Dataset_Collection/SO_init/so_init.csv).
    
    The source codes used to collect initial data are `GitHub_data_collection.py` and `StackOverflow_data_collection.py`, respectively.
2. **Manual_Labelling** folder: In this folder, we have placed all the files associated with our manual labelled result (after **Step 3**). For the bugs, we further annotate `Symptom`, `Bug Type` and `Root cause`.

3. **Quantitative_Study** folder: In this folder, we have placed the source data from Quantitative Study in Section 7. In the lifecycle file from Github, we annotate the creation time, closing time and lifecycle.
   In the lifecycle file from StackOverflow, we annotate the creation time, last active time and lifecycle.

    In files of patch size, we annotate the number of added lines, deleted lines, the total number of lines, and changed files.



