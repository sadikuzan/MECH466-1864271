classdef Mech466SadikUzan1864271v1 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        MECH466BrakingDynamicsSADIKUZANUIFigure  matlab.ui.Figure
        TabGroup                        matlab.ui.container.TabGroup
        HomeTab                         matlab.ui.container.Tab
        VehicleSpecificationsTab        matlab.ui.container.Tab
        LoadedPanel                     matlab.ui.container.Panel
        r                               matlab.ui.control.NumericEditField
        distancefromlateralaxisEditFieldLabel  matlab.ui.control.Label
        a                               matlab.ui.control.NumericEditField
        HeightEditFieldLabel            matlab.ui.control.Label
        h                               matlab.ui.control.NumericEditField
        WheelbaseEditFieldLabel         matlab.ui.control.Label
        L                               matlab.ui.control.NumericEditField
        LoadDistributionfrLabel         matlab.ui.control.Label
        f                               matlab.ui.control.NumericEditField
        VehicleMassEditFieldLabel       matlab.ui.control.Label
        Wv                              matlab.ui.control.NumericEditField
        UnloadedPanel                   matlab.ui.container.Panel
        TireRollingRadiusmmEditFieldLabel  matlab.ui.control.Label
        Rw                              matlab.ui.control.NumericEditField
        BrakeWheelCylinderDiameterfrmmEditFieldLabel  matlab.ui.control.Label
        BWCf                            matlab.ui.control.NumericEditField
        EditFieldLabel                  matlab.ui.control.Label
        BWCr                            matlab.ui.control.NumericEditField
        BrakefactorfrontdiskrearleadingEditFieldLabel  matlab.ui.control.Label
        BFf                             matlab.ui.control.NumericEditField
        BFr                             matlab.ui.control.NumericEditField
        Rr                              matlab.ui.control.NumericEditField
        EffectiveRadiusfrontdiskreardrummmEditFieldLabel  matlab.ui.control.Label
        Rf                              matlab.ui.control.NumericEditField
        IdealBFDFTab                    matlab.ui.container.Tab
        DecelerationtoFrontLockedFirstLabel  matlab.ui.control.Label
        d1                              matlab.ui.control.NumericEditField
        i_idealEditFieldLabel           matlab.ui.control.Label
        ifora                           matlab.ui.control.NumericEditField
        btnCalca                        matlab.ui.control.Button
        MaxdecelerationwithoutlockingforrearandfirstPanel  matlab.ui.container.Panel
        ForthefronwheelEditFieldLabel   matlab.ui.control.Label
        dforfront                       matlab.ui.control.NumericEditField
        FortheRearWheelEditFieldLabel   matlab.ui.control.Label
        dforrear                        matlab.ui.control.NumericEditField
        AdhesionCoeeficientEditFieldLabel  matlab.ui.control.Label
        MuFor3                          matlab.ui.control.NumericEditField
        MaxTotalBrakingForcewithoutLockbothWheelPanel  matlab.ui.container.Panel
        BrakingForceNEditFieldLabel     matlab.ui.control.Label
        MaxFb3                          matlab.ui.control.NumericEditField
        calcMaxFb3                      matlab.ui.control.Button
        Warn                            matlab.ui.control.Label
        CheckBFDFavailibityPanel        matlab.ui.container.Panel
        Decelerationms2Label            matlab.ui.control.Label
        dforcheck                       matlab.ui.control.NumericEditField
        CheckButton                     matlab.ui.control.Button
        FortheFrontWheelEditFieldLabel  matlab.ui.control.Label
        iforfront                       matlab.ui.control.NumericEditField
        FortheRearWheelEditFieldLabel_2  matlab.ui.control.Label
        iforrear                        matlab.ui.control.NumericEditField
        porNot                          matlab.ui.control.Label
        ActualBDFDTab                   matlab.ui.container.Tab
        DynamicfrontandrearloadsPanel   matlab.ui.container.Panel
        decelerationEditFieldLabel      matlab.ui.control.Label
        dfor4                           matlab.ui.control.NumericEditField
        W_fNEditFieldLabel              matlab.ui.control.Label
        Wf                              matlab.ui.control.NumericEditField
        W_rNEditFieldLabel              matlab.ui.control.Label
        Wr                              matlab.ui.control.NumericEditField
        I_idealEditFieldLabel           matlab.ui.control.Label
        BFDFidealfor4                   matlab.ui.control.NumericEditField
        CalculateButton                 matlab.ui.control.Button
        ActualBrakeForceDistributionFactorPanel  matlab.ui.container.Panel
        CalculateBFDFactualandCheckforStandartButton  matlab.ui.control.Button
        i_actualEditFieldLabel          matlab.ui.control.Label
        BFDFactual4                     matlab.ui.control.NumericEditField
        ActualandIdealBFDFEqualEditFieldLabel  matlab.ui.control.Label
        dequalat                        matlab.ui.control.NumericEditField
        Warn1                           matlab.ui.control.Label
        d_maxvsiTab                     matlab.ui.container.Tab
        PlotLabel                       matlab.ui.control.Label
        Label                           matlab.ui.control.Label
        wheretheroadadhesioncoefficientisEditFieldLabel  matlab.ui.control.Label
        mu                              matlab.ui.control.NumericEditField
        DvsIFigure                      matlab.ui.control.UIAxes
        PlotButton                      matlab.ui.control.Button
    end


    properties (Access = private)
        BFDFideal % Description
        BFDFactual % Description
        d % Description
    end


    methods (Access = private)

        % Callback function
        function ButtonPushed(app, event)
            app.d = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9];
            IdealDist = (1-app.a.Value/app.L.Value)+(app.h.Value/app.L.Value)*app.d;
            plot(app.DvsIFigure,IdealDist,1-IdealDist);
        end

        % Button pushed function: PlotButton
        function PlotButtonPushed(app, event)
            i = 0.2:0.01:1;
            l = app.L.Value; % wheelbase [m]
            a_yuksuz = app.a_u.Value;
            a_yuklu = app.a.Value;
            b_yuksuz = l-a_yuksuz;
            b_yuklu = l-a_yuklu;
            mus = app.mu.Value;
            h_yuksuz = app.h_u.Value;
            h_yuklu=app.h.Value;
            df_yuksuz = mus*b_yuksuz/l./(i-mus*h_yuksuz/l);
            df_yuklu = mus*b_yuklu/l./(i-mus*h_yuklu/l);
            dr_yuksuz = mus*a_yuksuz/l./(1-i+mus*h_yuksuz/l);
            dr_yuklu = mus*a_yuklu/l./(1-i+mus*h_yuklu/l);
            plot(app.DvsIFigure,i*100,[df_yuksuz;df_yuklu;dr_yuksuz;dr_yuklu],'LineWidth',2);
            legend(app.DvsIFigure,'d_f unloaded','d_f loaded','d_r unloaded','d_r loaded');
           % if(app.mu.Value > 0.4)              
             %   ylim(app.DvsIFigure,[0.5 1])
               % xlim(app.DvsIFigure,[30 100])
            %else
            %ylim(app.DvsIFigure,[0.12 0.22])
           % xlim(app.DvsIFigure,[15 95])
           % end
            xlabel(app.DvsIFigure,'brake force distribution factor')
            ylabel(app.DvsIFigure,'max decel before front - rear wheel lock [g]')
   
        end

        % Button pushed function: btnCalca
        function btnCalcaButtonPushed(app, event)
            app.ifora.Value = (1-app.a.Value/app.L.Value) + app.h.Value/app.L.Value*app.d1.Value;
            muhdivL = app.MuFor3.Value*(app.h.Value/app.L.Value);
            app.dforfront.Value = ((app.MuFor3.Value)*(1-app.a.Value/app.L.Value))/(app.ifora.Value-muhdivL);
            app.dforrear.Value = ((app.MuFor3.Value)*(app.a.Value/app.L.Value))/((1-app.ifora.Value) + muhdivL);
        end

        % Button pushed function: calcMaxFb3
        function calcMaxFb3ButtonPushed(app, event)
            if app.dforfront.Value < app.dforrear.Value
                maxd = app.dforfront.Value;
                app.MaxFb3.Value = app.Wv.Value*9.81*maxd;
                app.Warn.Text = "Front Wheel Lock First";
            else
                maxd = app.dforrear.Value;
                app.MaxFb3.Value = app.Wv.Value*9.81*maxd;
                app.Warn.Text = "Rear Wheel Lock First";
            end
            
        end

        % Button pushed function: CheckButton
        function CheckButtonPushed(app, event)
            dec = app.dforcheck.Value/9.81;
            Muu = app.MuFor3.Value; 
            app.iforfront.Value = Muu*(1-app.a.Value/app.L.Value + dec*app.h.Value/app.L.Value)/dec;
            app.iforrear.Value = 1-Muu*(app.a.Value/app.L.Value - dec*app.h.Value/app.L.Value)/dec;
            if app.iforfront.Value <= app.iforrear.Value
                app.porNot.Text =  "NOT POSSIBLE";
            else
                app.porNot.Text = "POSSIBLE";
            end
        end

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            app.Wf.Value = app.Wv.Value*9.81*(app.f.Value/100 + app.dfor4.Value*app.h.Value/app.L.Value);
            app.Wr.Value = app.Wv.Value*9.81*(app.r.Value/100 -app.dfor4.Value*app.h.Value/app.L.Value);
            app.BFDFidealfor4.Value = app.Wf.Value/(app.Wv.Value*9.81);
        end

        % Button pushed function: 
        % CalculateBFDFactualandCheckforStandartButton
        function CalculateBFDFactualandCheckforStandartButtonPushed(app, event)
            numf = pi*(app.BWCf.Value^2/4)*app.BFf.Value*app.Rf.Value;
            denr= numf + pi*(app.BWCr.Value^2/4)*app.BFr.Value*app.Rr.Value;
            app.BFDFactual4.Value = numf/denr;
            
            decEqual = (app.BFDFactual4.Value-app.f.Value/100)*app.L.Value/app.h.Value;
            app.dequalat.Value = round(decEqual,2);
            if app.dequalat.Value == 0.8
                app.Warn1.Text = "Suitable";
            else
                app.Warn1.Text = "Not Suitable";
            end
            
        end
    end

    % App initialization and construction
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create MECH466BrakingDynamicsSADIKUZANUIFigure
            app.MECH466BrakingDynamicsSADIKUZANUIFigure = uifigure;
            app.MECH466BrakingDynamicsSADIKUZANUIFigure.Colormap = [0.2431 0.149 0.6588;0.251 0.1647 0.7059;0.2588 0.1804 0.7529;0.2627 0.1961 0.7961;0.2706 0.2157 0.8353;0.2745 0.2353 0.8706;0.2784 0.2549 0.898;0.2784 0.2784 0.9216;0.2824 0.302 0.9412;0.2824 0.3216 0.9569;0.2784 0.3451 0.9725;0.2745 0.3686 0.9843;0.2706 0.3882 0.9922;0.2588 0.4118 0.9961;0.2431 0.4353 1;0.2196 0.4588 0.9961;0.1961 0.4863 0.9882;0.1843 0.5059 0.9804;0.1804 0.5294 0.9686;0.1765 0.549 0.9529;0.1686 0.5686 0.9373;0.1529 0.5922 0.9216;0.1451 0.6078 0.9098;0.1373 0.6275 0.898;0.1255 0.6471 0.8902;0.1098 0.6627 0.8745;0.0941 0.6784 0.8588;0.0706 0.6941 0.8392;0.0314 0.7098 0.8157;0.0039 0.7216 0.7922;0.0078 0.7294 0.7647;0.0431 0.7412 0.7412;0.098 0.749 0.7137;0.1412 0.7569 0.6824;0.1725 0.7686 0.6549;0.1922 0.7765 0.6235;0.2157 0.7843 0.5922;0.2471 0.7922 0.5569;0.2902 0.7961 0.5176;0.3412 0.8 0.4784;0.3922 0.8039 0.4353;0.4471 0.8039 0.3922;0.5059 0.8 0.349;0.5608 0.7961 0.3059;0.6157 0.7882 0.2627;0.6706 0.7804 0.2235;0.7255 0.7686 0.1922;0.7725 0.7608 0.1647;0.8196 0.749 0.1529;0.8627 0.7412 0.1608;0.902 0.7333 0.1765;0.9412 0.7294 0.2118;0.9725 0.7294 0.2392;0.9961 0.7451 0.2353;0.9961 0.7647 0.2196;0.9961 0.7882 0.2039;0.9882 0.8118 0.1882;0.9804 0.8392 0.1765;0.9686 0.8627 0.1647;0.9608 0.8902 0.1529;0.9608 0.9137 0.1412;0.9647 0.9373 0.1255;0.9686 0.9608 0.1059;0.9765 0.9843 0.0824;1 1 1];
            app.MECH466BrakingDynamicsSADIKUZANUIFigure.Position = [200 200 793 517];
            app.MECH466BrakingDynamicsSADIKUZANUIFigure.Name = 'MECH 466 | Braking Dynamics | SADIK UZAN';

            % Create TabGroup
            app.TabGroup = uitabgroup(app.MECH466BrakingDynamicsSADIKUZANUIFigure);
            app.TabGroup.Position = [1 1 793 517];

            % Create HomeTab
            app.HomeTab = uitab(app.TabGroup);
            app.HomeTab.Title = 'Home';

            % Create VehicleSpecificationsTab
            app.VehicleSpecificationsTab = uitab(app.TabGroup);
            app.VehicleSpecificationsTab.Title = 'Vehicle Specifications';

            % Create LoadedPanel
            app.LoadedPanel = uipanel(app.VehicleSpecificationsTab);
            app.LoadedPanel.TitlePosition = 'centertop';
            app.LoadedPanel.Title = 'Loaded';
            app.LoadedPanel.Position = [78 313 300 180];

            % Create r
            app.r = uieditfield(app.LoadedPanel, 'numeric');
            app.r.ValueDisplayFormat = '%5.2f';
            app.r.Position = [244 98 40 22];
            app.r.Value = 47;

            % Create distancefromlateralaxisEditFieldLabel
            app.distancefromlateralaxisEditFieldLabel = uilabel(app.LoadedPanel);
            app.distancefromlateralaxisEditFieldLabel.HorizontalAlignment = 'right';
            app.distancefromlateralaxisEditFieldLabel.Position = [34 12 140 15];
            app.distancefromlateralaxisEditFieldLabel.Text = 'distance from lateral axis';

            % Create a
            app.a = uieditfield(app.LoadedPanel, 'numeric');
            app.a.ValueDisplayFormat = '%.2f';
            app.a.Position = [184 8 100 22];
            app.a.Value = 745.89;

            % Create HeightEditFieldLabel
            app.HeightEditFieldLabel = uilabel(app.LoadedPanel);
            app.HeightEditFieldLabel.HorizontalAlignment = 'right';
            app.HeightEditFieldLabel.Position = [114 42 41 15];
            app.HeightEditFieldLabel.Text = 'Height';

            % Create h
            app.h = uieditfield(app.LoadedPanel, 'numeric');
            app.h.Position = [184 38 102 22];
            app.h.Value = 576;

            % Create WheelbaseEditFieldLabel
            app.WheelbaseEditFieldLabel = uilabel(app.LoadedPanel);
            app.WheelbaseEditFieldLabel.HorizontalAlignment = 'right';
            app.WheelbaseEditFieldLabel.Position = [82 72 67 15];
            app.WheelbaseEditFieldLabel.Text = 'Wheelbase';

            % Create L
            app.L = uieditfield(app.LoadedPanel, 'numeric');
            app.L.Position = [182 68 102 22];
            app.L.Value = 2632;

            % Create LoadDistributionfrLabel
            app.LoadDistributionfrLabel = uilabel(app.LoadedPanel);
            app.LoadDistributionfrLabel.HorizontalAlignment = 'right';
            app.LoadDistributionfrLabel.Position = [10 102 133 15];
            app.LoadDistributionfrLabel.Text = 'Load Distribution (f/r) %';

            % Create f
            app.f = uieditfield(app.LoadedPanel, 'numeric');
            app.f.ValueDisplayFormat = '%5.2f';
            app.f.Position = [190 98 34 22];
            app.f.Value = 53;

            % Create VehicleMassEditFieldLabel
            app.VehicleMassEditFieldLabel = uilabel(app.LoadedPanel);
            app.VehicleMassEditFieldLabel.HorizontalAlignment = 'right';
            app.VehicleMassEditFieldLabel.Position = [74 132 78 15];
            app.VehicleMassEditFieldLabel.Text = 'Vehicle Mass';

            % Create Wv
            app.Wv = uieditfield(app.LoadedPanel, 'numeric');
            app.Wv.Position = [184 128 100 22];
            app.Wv.Value = 1587;

            % Create UnloadedPanel
            app.UnloadedPanel = uipanel(app.VehicleSpecificationsTab);
            app.UnloadedPanel.TitlePosition = 'centertop';
            app.UnloadedPanel.Title = 'Unloaded';
            app.UnloadedPanel.Position = [31 122 428 180];

            % Create TireRollingRadiusmmEditFieldLabel
            app.TireRollingRadiusmmEditFieldLabel = uilabel(app.UnloadedPanel);
            app.TireRollingRadiusmmEditFieldLabel.HorizontalAlignment = 'right';
            app.TireRollingRadiusmmEditFieldLabel.Position = [86 129 141 15];
            app.TireRollingRadiusmmEditFieldLabel.Text = 'Tire Rolling Radius (mm)';

            % Create Rw
            app.Rw = uieditfield(app.UnloadedPanel, 'numeric');
            app.Rw.Position = [242 125 100 22];
            app.Rw.Value = 302;

            % Create BrakeWheelCylinderDiameterfrmmEditFieldLabel
            app.BrakeWheelCylinderDiameterfrmmEditFieldLabel = uilabel(app.UnloadedPanel);
            app.BrakeWheelCylinderDiameterfrmmEditFieldLabel.HorizontalAlignment = 'right';
            app.BrakeWheelCylinderDiameterfrmmEditFieldLabel.Position = [1 94 222 15];
            app.BrakeWheelCylinderDiameterfrmmEditFieldLabel.Text = 'Brake Wheel Cylinder Diameter (f/r) mm';

            % Create BWCf
            app.BWCf = uieditfield(app.UnloadedPanel, 'numeric');
            app.BWCf.Position = [238 90 47 22];
            app.BWCf.Value = 63.2;

            % Create EditFieldLabel
            app.EditFieldLabel = uilabel(app.UnloadedPanel);
            app.EditFieldLabel.HorizontalAlignment = 'right';
            app.EditFieldLabel.Position = [260 94 25 15];
            app.EditFieldLabel.Text = '';

            % Create BWCr
            app.BWCr = uieditfield(app.UnloadedPanel, 'numeric');
            app.BWCr.Position = [300 90 44 22];
            app.BWCr.Value = 21.07;

            % Create BrakefactorfrontdiskrearleadingEditFieldLabel
            app.BrakefactorfrontdiskrearleadingEditFieldLabel = uilabel(app.UnloadedPanel);
            app.BrakefactorfrontdiskrearleadingEditFieldLabel.HorizontalAlignment = 'right';
            app.BrakefactorfrontdiskrearleadingEditFieldLabel.Position = [17 62 209 15];
            app.BrakefactorfrontdiskrearleadingEditFieldLabel.Text = 'Brake factor (front disk / rear leading )';

            % Create BFf
            app.BFf = uieditfield(app.UnloadedPanel, 'numeric');
            app.BFf.Position = [241 58 44 22];
            app.BFf.Value = 0.88;

            % Create BFr
            app.BFr = uieditfield(app.UnloadedPanel, 'numeric');
            app.BFr.Position = [301 58 43 22];
            app.BFr.Value = 2.8;

            % Create Rr
            app.Rr = uieditfield(app.UnloadedPanel, 'numeric');
            app.Rr.Position = [300 24 42 22];
            app.Rr.Value = 102.4;

            % Create EffectiveRadiusfrontdiskreardrummmEditFieldLabel
            app.EffectiveRadiusfrontdiskreardrummmEditFieldLabel = uilabel(app.VehicleSpecificationsTab);
            app.EffectiveRadiusfrontdiskreardrummmEditFieldLabel.HorizontalAlignment = 'right';
            app.EffectiveRadiusfrontdiskreardrummmEditFieldLabel.Position = [31 150 240 15];
            app.EffectiveRadiusfrontdiskreardrummmEditFieldLabel.Text = 'Effective Radius (front disk / rear drum) mm';

            % Create Rf
            app.Rf = uieditfield(app.VehicleSpecificationsTab, 'numeric');
            app.Rf.Position = [273 146 50 22];
            app.Rf.Value = 83;

            % Create IdealBFDFTab
            app.IdealBFDFTab = uitab(app.TabGroup);
            app.IdealBFDFTab.Title = 'Ideal BFDF';

            % Create DecelerationtoFrontLockedFirstLabel
            app.DecelerationtoFrontLockedFirstLabel = uilabel(app.IdealBFDFTab);
            app.DecelerationtoFrontLockedFirstLabel.HorizontalAlignment = 'right';
            app.DecelerationtoFrontLockedFirstLabel.Position = [24 456 188 15];
            app.DecelerationtoFrontLockedFirstLabel.Text = 'Deceleration to Front Locked First';

            % Create d1
            app.d1 = uieditfield(app.IdealBFDFTab, 'numeric');
            app.d1.ValueDisplayFormat = '%.3f';
            app.d1.Position = [227 452 100 22];

            % Create i_idealEditFieldLabel
            app.i_idealEditFieldLabel = uilabel(app.IdealBFDFTab);
            app.i_idealEditFieldLabel.HorizontalAlignment = 'right';
            app.i_idealEditFieldLabel.Position = [168 418 42 15];
            app.i_idealEditFieldLabel.Text = 'i_ideal';

            % Create ifora
            app.ifora = uieditfield(app.IdealBFDFTab, 'numeric');
            app.ifora.ValueDisplayFormat = '%.3f';
            app.ifora.Position = [225 414 102 22];

            % Create btnCalca
            app.btnCalca = uibutton(app.IdealBFDFTab, 'push');
            app.btnCalca.ButtonPushedFcn = createCallbackFcn(app, @btnCalcaButtonPushed, true);
            app.btnCalca.Position = [55 418 100 22];
            app.btnCalca.Text = 'Calculate';

            % Create MaxdecelerationwithoutlockingforrearandfirstPanel
            app.MaxdecelerationwithoutlockingforrearandfirstPanel = uipanel(app.IdealBFDFTab);
            app.MaxdecelerationwithoutlockingforrearandfirstPanel.Title = 'Max deceleration without locking for rear and first';
            app.MaxdecelerationwithoutlockingforrearandfirstPanel.Position = [24 285 341 102];

            % Create ForthefronwheelEditFieldLabel
            app.ForthefronwheelEditFieldLabel = uilabel(app.MaxdecelerationwithoutlockingforrearandfirstPanel);
            app.ForthefronwheelEditFieldLabel.HorizontalAlignment = 'right';
            app.ForthefronwheelEditFieldLabel.Position = [19 49 103 15];
            app.ForthefronwheelEditFieldLabel.Text = 'For the fron wheel';

            % Create dforfront
            app.dforfront = uieditfield(app.MaxdecelerationwithoutlockingforrearandfirstPanel, 'numeric');
            app.dforfront.ValueDisplayFormat = '%.3f';
            app.dforfront.Position = [137 45 100 22];

            % Create FortheRearWheelEditFieldLabel
            app.FortheRearWheelEditFieldLabel = uilabel(app.MaxdecelerationwithoutlockingforrearandfirstPanel);
            app.FortheRearWheelEditFieldLabel.HorizontalAlignment = 'right';
            app.FortheRearWheelEditFieldLabel.Position = [11 13 111 15];
            app.FortheRearWheelEditFieldLabel.Text = 'For the Rear Wheel';

            % Create dforrear
            app.dforrear = uieditfield(app.MaxdecelerationwithoutlockingforrearandfirstPanel, 'numeric');
            app.dforrear.ValueDisplayFormat = '%.3f';
            app.dforrear.Position = [137 9 100 22];

            % Create AdhesionCoeeficientEditFieldLabel
            app.AdhesionCoeeficientEditFieldLabel = uilabel(app.IdealBFDFTab);
            app.AdhesionCoeeficientEditFieldLabel.HorizontalAlignment = 'right';
            app.AdhesionCoeeficientEditFieldLabel.Position = [351 456 122 15];
            app.AdhesionCoeeficientEditFieldLabel.Text = 'Adhesion Coeeficient';

            % Create MuFor3
            app.MuFor3 = uieditfield(app.IdealBFDFTab, 'numeric');
            app.MuFor3.ValueDisplayFormat = '%.3f';
            app.MuFor3.Position = [488 452 100 22];

            % Create MaxTotalBrakingForcewithoutLockbothWheelPanel
            app.MaxTotalBrakingForcewithoutLockbothWheelPanel = uipanel(app.IdealBFDFTab);
            app.MaxTotalBrakingForcewithoutLockbothWheelPanel.Title = 'Max Total Braking Force without Lock both Wheel';
            app.MaxTotalBrakingForcewithoutLockbothWheelPanel.Position = [380 285 389 102];

            % Create BrakingForceNEditFieldLabel
            app.BrakingForceNEditFieldLabel = uilabel(app.MaxTotalBrakingForcewithoutLockbothWheelPanel);
            app.BrakingForceNEditFieldLabel.HorizontalAlignment = 'right';
            app.BrakingForceNEditFieldLabel.Position = [22 53 101 15];
            app.BrakingForceNEditFieldLabel.Text = 'Braking Force (N)';

            % Create MaxFb3
            app.MaxFb3 = uieditfield(app.MaxTotalBrakingForcewithoutLockbothWheelPanel, 'numeric');
            app.MaxFb3.Position = [138 49 100 22];

            % Create calcMaxFb3
            app.calcMaxFb3 = uibutton(app.MaxTotalBrakingForcewithoutLockbothWheelPanel, 'push');
            app.calcMaxFb3.ButtonPushedFcn = createCallbackFcn(app, @calcMaxFb3ButtonPushed, true);
            app.calcMaxFb3.Position = [258 46 100 22];
            app.calcMaxFb3.Text = 'Find Force';

            % Create Warn
            app.Warn = uilabel(app.MaxTotalBrakingForcewithoutLockbothWheelPanel);
            app.Warn.FontSize = 20;
            app.Warn.FontWeight = 'bold';
            app.Warn.FontColor = [1 0 0];
            app.Warn.Position = [30 13 328 27];
            app.Warn.Text = '';

            % Create CheckBFDFavailibityPanel
            app.CheckBFDFavailibityPanel = uipanel(app.IdealBFDFTab);
            app.CheckBFDFavailibityPanel.Title = 'Check BFDF availibity';
            app.CheckBFDFavailibityPanel.Position = [24 78 343 194];

            % Create Decelerationms2Label
            app.Decelerationms2Label = uilabel(app.CheckBFDFavailibityPanel);
            app.Decelerationms2Label.HorizontalAlignment = 'right';
            app.Decelerationms2Label.Position = [8 144 118 15];
            app.Decelerationms2Label.Text = 'Deceleration (m/s^2)';

            % Create dforcheck
            app.dforcheck = uieditfield(app.CheckBFDFavailibityPanel, 'numeric');
            app.dforcheck.ValueDisplayFormat = '%.3f';
            app.dforcheck.Position = [141 140 100 22];

            % Create CheckButton
            app.CheckButton = uibutton(app.CheckBFDFavailibityPanel, 'push');
            app.CheckButton.ButtonPushedFcn = createCallbackFcn(app, @CheckButtonPushed, true);
            app.CheckButton.Position = [268 140 62 22];
            app.CheckButton.Text = 'Check';

            % Create FortheFrontWheelEditFieldLabel
            app.FortheFrontWheelEditFieldLabel = uilabel(app.CheckBFDFavailibityPanel);
            app.FortheFrontWheelEditFieldLabel.HorizontalAlignment = 'right';
            app.FortheFrontWheelEditFieldLabel.Position = [12 114 112 15];
            app.FortheFrontWheelEditFieldLabel.Text = 'For the Front Wheel';

            % Create iforfront
            app.iforfront = uieditfield(app.CheckBFDFavailibityPanel, 'numeric');
            app.iforfront.ValueDisplayFormat = '%.3f';
            app.iforfront.Position = [139 110 100 22];

            % Create FortheRearWheelEditFieldLabel_2
            app.FortheRearWheelEditFieldLabel_2 = uilabel(app.CheckBFDFavailibityPanel);
            app.FortheRearWheelEditFieldLabel_2.HorizontalAlignment = 'right';
            app.FortheRearWheelEditFieldLabel_2.Position = [13 81 111 15];
            app.FortheRearWheelEditFieldLabel_2.Text = 'For the Rear Wheel';

            % Create iforrear
            app.iforrear = uieditfield(app.CheckBFDFavailibityPanel, 'numeric');
            app.iforrear.ValueDisplayFormat = '%.3f';
            app.iforrear.Position = [139 77 100 22];

            % Create porNot
            app.porNot = uilabel(app.CheckBFDFavailibityPanel);
            app.porNot.FontSize = 20;
            app.porNot.FontWeight = 'bold';
            app.porNot.FontColor = [1 0 0];
            app.porNot.Position = [31 39 297 26];
            app.porNot.Text = '';

            % Create ActualBDFDTab
            app.ActualBDFDTab = uitab(app.TabGroup);
            app.ActualBDFDTab.Title = 'Actual BDFD';

            % Create DynamicfrontandrearloadsPanel
            app.DynamicfrontandrearloadsPanel = uipanel(app.ActualBDFDTab);
            app.DynamicfrontandrearloadsPanel.Title = 'Dynamic front and rear loads';
            app.DynamicfrontandrearloadsPanel.FontSize = 14;
            app.DynamicfrontandrearloadsPanel.Position = [15 325 303 158];

            % Create decelerationEditFieldLabel
            app.decelerationEditFieldLabel = uilabel(app.DynamicfrontandrearloadsPanel);
            app.decelerationEditFieldLabel.HorizontalAlignment = 'right';
            app.decelerationEditFieldLabel.FontSize = 14;
            app.decelerationEditFieldLabel.Position = [-5 107 105 18];
            app.decelerationEditFieldLabel.Text = '@ deceleration ';

            % Create dfor4
            app.dfor4 = uieditfield(app.DynamicfrontandrearloadsPanel, 'numeric');
            app.dfor4.FontSize = 14;
            app.dfor4.Position = [114 106 88 22];

            % Create W_fNEditFieldLabel
            app.W_fNEditFieldLabel = uilabel(app.DynamicfrontandrearloadsPanel);
            app.W_fNEditFieldLabel.HorizontalAlignment = 'right';
            app.W_fNEditFieldLabel.FontSize = 14;
            app.W_fNEditFieldLabel.Position = [35 76 52 18];
            app.W_fNEditFieldLabel.Text = 'W_f [N]';

            % Create Wf
            app.Wf = uieditfield(app.DynamicfrontandrearloadsPanel, 'numeric');
            app.Wf.FontSize = 14;
            app.Wf.Position = [102 75 100 22];

            % Create W_rNEditFieldLabel
            app.W_rNEditFieldLabel = uilabel(app.DynamicfrontandrearloadsPanel);
            app.W_rNEditFieldLabel.HorizontalAlignment = 'right';
            app.W_rNEditFieldLabel.FontSize = 14;
            app.W_rNEditFieldLabel.Position = [35 44 53 18];
            app.W_rNEditFieldLabel.Text = 'W_r [N]';

            % Create Wr
            app.Wr = uieditfield(app.DynamicfrontandrearloadsPanel, 'numeric');
            app.Wr.FontSize = 14;
            app.Wr.Position = [103 43 100 22];

            % Create I_idealEditFieldLabel
            app.I_idealEditFieldLabel = uilabel(app.DynamicfrontandrearloadsPanel);
            app.I_idealEditFieldLabel.HorizontalAlignment = 'right';
            app.I_idealEditFieldLabel.FontSize = 14;
            app.I_idealEditFieldLabel.Position = [39 12 47 18];
            app.I_idealEditFieldLabel.Text = 'I_ideal';

            % Create BFDFidealfor4
            app.BFDFidealfor4 = uieditfield(app.DynamicfrontandrearloadsPanel, 'numeric');
            app.BFDFidealfor4.FontSize = 14;
            app.BFDFidealfor4.Position = [101 11 100 22];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.DynamicfrontandrearloadsPanel, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.Position = [213 106 79 22];
            app.CalculateButton.Text = 'Calculate';

            % Create ActualBrakeForceDistributionFactorPanel
            app.ActualBrakeForceDistributionFactorPanel = uipanel(app.ActualBDFDTab);
            app.ActualBrakeForceDistributionFactorPanel.Title = 'Actual Brake Force Distribution Factor';
            app.ActualBrakeForceDistributionFactorPanel.FontSize = 14;
            app.ActualBrakeForceDistributionFactorPanel.Position = [356 325 375 158];

            % Create CalculateBFDFactualandCheckforStandartButton
            app.CalculateBFDFactualandCheckforStandartButton = uibutton(app.ActualBrakeForceDistributionFactorPanel, 'push');
            app.CalculateBFDFactualandCheckforStandartButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateBFDFactualandCheckforStandartButtonPushed, true);
            app.CalculateBFDFactualandCheckforStandartButton.FontSize = 14;
            app.CalculateBFDFactualandCheckforStandartButton.Position = [38 100 322 25];
            app.CalculateBFDFactualandCheckforStandartButton.Text = 'Calculate BFDF (actual) and Check for Standart';

            % Create i_actualEditFieldLabel
            app.i_actualEditFieldLabel = uilabel(app.ActualBrakeForceDistributionFactorPanel);
            app.i_actualEditFieldLabel.HorizontalAlignment = 'right';
            app.i_actualEditFieldLabel.FontSize = 14;
            app.i_actualEditFieldLabel.Position = [166 73 54 18];
            app.i_actualEditFieldLabel.Text = 'i_actual';

            % Create BFDFactual4
            app.BFDFactual4 = uieditfield(app.ActualBrakeForceDistributionFactorPanel, 'numeric');
            app.BFDFactual4.FontSize = 14;
            app.BFDFactual4.Position = [234 72 100 22];

            % Create ActualandIdealBFDFEqualEditFieldLabel
            app.ActualandIdealBFDFEqualEditFieldLabel = uilabel(app.ActualBrakeForceDistributionFactorPanel);
            app.ActualandIdealBFDFEqualEditFieldLabel.HorizontalAlignment = 'right';
            app.ActualandIdealBFDFEqualEditFieldLabel.FontSize = 14;
            app.ActualandIdealBFDFEqualEditFieldLabel.Position = [12 41 207 18];
            app.ActualandIdealBFDFEqualEditFieldLabel.Text = 'Actual and Ideal BFDF Equal @';

            % Create dequalat
            app.dequalat = uieditfield(app.ActualBrakeForceDistributionFactorPanel, 'numeric');
            app.dequalat.FontSize = 14;
            app.dequalat.Position = [234 40 100 22];

            % Create Warn1
            app.Warn1 = uilabel(app.ActualBrakeForceDistributionFactorPanel);
            app.Warn1.FontSize = 14;
            app.Warn1.FontWeight = 'bold';
            app.Warn1.FontColor = [1 0 0];
            app.Warn1.Position = [239 12 108 18];
            app.Warn1.Text = 'NOT SUITABLE';

            % Create d_maxvsiTab
            app.d_maxvsiTab = uitab(app.TabGroup);
            app.d_maxvsiTab.Title = 'd_max vs i';

            % Create PlotLabel
            app.PlotLabel = uilabel(app.d_maxvsiTab);
            app.PlotLabel.FontSize = 14;
            app.PlotLabel.Position = [22 459 785 20];
            app.PlotLabel.Text = 'Plot the limiting values of deceleration before the front and rear wheels lock versus brake force distribution factor (BFDF)';

            % Create Label
            app.Label = uilabel(app.d_maxvsiTab);
            app.Label.FontSize = 14;
            app.Label.Position = [22 443 274 18];
            app.Label.Text = ' for both driver only and loaded conditions';

            % Create wheretheroadadhesioncoefficientisEditFieldLabel
            app.wheretheroadadhesioncoefficientisEditFieldLabel = uilabel(app.d_maxvsiTab);
            app.wheretheroadadhesioncoefficientisEditFieldLabel.HorizontalAlignment = 'right';
            app.wheretheroadadhesioncoefficientisEditFieldLabel.FontSize = 14;
            app.wheretheroadadhesioncoefficientisEditFieldLabel.Position = [295 442 255 18];
            app.wheretheroadadhesioncoefficientisEditFieldLabel.Text = ', where the road adhesion coefficient is';

            % Create mu
            app.mu = uieditfield(app.d_maxvsiTab, 'numeric');
            app.mu.FontSize = 14;
            app.mu.Position = [565 441 46 22];

            % Create DvsIFigure
            app.DvsIFigure = uiaxes(app.d_maxvsiTab);
            xlabel(app.DvsIFigure, 'X')
            ylabel(app.DvsIFigure, 'Y')
            app.DvsIFigure.DataAspectRatio = [1 1 1];
            app.DvsIFigure.PlotBoxAspectRatio = [1 1 1];
            app.DvsIFigure.XLim = [0 1];
            app.DvsIFigure.YLim = [0 1];
            app.DvsIFigure.ZLim = [0 1];
            app.DvsIFigure.CLim = [0 1];
            app.DvsIFigure.GridColor = [0.15 0.15 0.15];
            app.DvsIFigure.MinorGridColor = [0.1 0.1 0.1];
            app.DvsIFigure.XColor = [0.15 0.15 0.15];
            app.DvsIFigure.XTick = [0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1];
            app.DvsIFigure.YColor = [0.15 0.15 0.15];
            app.DvsIFigure.YTick = [0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1];
            app.DvsIFigure.ZColor = [0.15 0.15 0.15];
            app.DvsIFigure.ZTick = [0 0.5 1];
            app.DvsIFigure.CameraPosition = [0.5 0.5 9.16025403784439];
            app.DvsIFigure.CameraTarget = [0.5 0.5 0.5];
            app.DvsIFigure.CameraUpVector = [0 1 0];
            app.DvsIFigure.Position = [32 43 703 349];

            % Create PlotButton
            app.PlotButton = uibutton(app.d_maxvsiTab, 'push');
            app.PlotButton.ButtonPushedFcn = createCallbackFcn(app, @PlotButtonPushed, true);
            app.PlotButton.Position = [295 409 100 22];
            app.PlotButton.Text = 'Plot';
        end
    end

    methods (Access = public)

        % Construct app
        function app = Mech466SadikUzan1864271v1

            % Create and configure components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.MECH466BrakingDynamicsSADIKUZANUIFigure)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.MECH466BrakingDynamicsSADIKUZANUIFigure)
        end
    end
end