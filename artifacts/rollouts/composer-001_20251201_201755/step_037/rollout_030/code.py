
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar1_start + i * 0.375
    end = start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass line (Marcus) - walking line in Fm (F, Ab, D, Eb)
# Bar 2: F (D2), Ab (E2), D (G2), Eb (F2)
bass_notes = []
# Bar 2
bass_notes.append(pretty_midi.Note(velocity=80, pitch=38, start=bar2_start, end=bar2_start + 0.375))  # F (D2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=bar2_start + 0.375, end=bar2_start + 0.75))  # Ab (E2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=bar2_start + 0.75, end=bar2_start + 1.125))  # D (G2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=44, start=bar2_start + 1.125, end=bar2_start + 1.5))  # Eb (F2)

# Bar 3: Ab (E2), D (G2), Eb (F2), F (D2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=bar3_start, end=bar3_start + 0.375))  # Ab (E2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=bar3_start + 0.375, end=bar3_start + 0.75))  # D (G2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=44, start=bar3_start + 0.75, end=bar3_start + 1.125))  # Eb (F2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=38, start=bar3_start + 1.125, end=bar3_start + 1.5))  # F (D2)

# Bar 4: D (G2), Eb (F2), F (D2), Ab (E2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=43, start=bar4_start, end=bar4_start + 0.375))  # D (G2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=44, start=bar4_start + 0.375, end=bar4_start + 0.75))  # Eb (F2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=38, start=bar4_start + 0.75, end=bar4_start + 1.125))  # F (D2)
bass_notes.append(pretty_midi.Note(velocity=80, pitch=41, start=bar4_start + 1.125, end=bar4_start + 1.5))  # Ab (E2)

bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, resolve on last bar
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = []
# Bar 2
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar2_start, end=bar2_start + 1.5))  # F (F4)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=68, start=bar2_start, end=bar2_start + 1.5))  # Ab (Ab4)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_start + 1.5))  # D (D5)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar2_start, end=bar2_start + 1.5))  # C (C5)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar3_start, end=bar3_start + 1.5))  # Bb (Bb4)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar3_start, end=bar3_start + 1.5))  # D (D5)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar3_start, end=bar3_start + 1.5))  # F (F5)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=68, start=bar3_start, end=bar3_start + 1.5))  # Ab (Ab5)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar4_start, end=bar4_start + 1.5))  # C (C4)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar4_start, end=bar4_start + 1.5))  # Eb (Eb4)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar4_start, end=bar4_start + 1.5))  # G (G4)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar4_start, end=bar4_start + 1.5))  # Bb (Bb4)

piano.notes.extend(piano_notes)

# Drums for Bars 2-4
# Bar 2
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
snare3 = pretty_midi.Note(velocity=110, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.875)
hihat_notes2 = []
for i in range(0, 4):
    start = bar2_start + i * 0.375
    end = start + 0.125
    hihat_notes2.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend([kick3, snare3] + hihat_notes2)

# Bar 3
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
snare4 = pretty_midi.Note(velocity=110, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
hihat_notes3 = []
for i in range(0, 4):
    start = bar3_start + i * 0.375
    end = start + 0.125
    hihat_notes3.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend([kick4, snare4] + hihat_notes3)

# Bar 4
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
snare5 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
hihat_notes4 = []
for i in range(0, 4):
    start = bar4_start + i * 0.375
    end = start + 0.125
    hihat_notes4.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend([kick5, snare5] + hihat_notes4)

# Saxophone (Dante) - short motif, make it sing
# Bar 2: Start the motif
sax_notes = []
# Bar 2: F (F4), Ab (Ab4), D (D5), Eb (Eb5)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=bar2_start, end=bar2_start + 0.375))  # F (F4)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=68, start=bar2_start + 0.375, end=bar2_start + 0.75))  # Ab (Ab4)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125))  # D (D5)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=bar2_start + 1.125, end=bar2_start + 1.5))  # Eb (Eb5)

# Bar 3: Leave it hanging
# Bar 3: F (F4), Ab (Ab4), D (D5), Eb (Eb5)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=bar3_start, end=bar3_start + 0.375))  # F (F4)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=68, start=bar3_start + 0.375, end=bar3_start + 0.75))  # Ab (Ab4)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.125))  # D (D5)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=bar3_start + 1.125, end=bar3_start + 1.5))  # Eb (Eb5)

# Bar 4: Come back and finish it
# Bar 4: F (F4), Ab (Ab4), D (D5), Eb (Eb5)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=bar4_start, end=bar4_start + 0.375))  # F (F4)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=68, start=bar4_start + 0.375, end=bar4_start + 0.75))  # Ab (Ab4)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=bar4_start + 0.75, end=bar4_start + 1.125))  # D (D5)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=bar4_start + 1.125, end=bar4_start + 1.5))  # Eb (Eb5)

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
