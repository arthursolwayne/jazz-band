
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Double Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Time per bar: 1.5 seconds (160 BPM, 4/4 time)
bar_length = 1.5
note_length = 0.375  # 1/4 note at 160 BPM

# ==============================
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time stamps: 0.0, 0.375, 0.75, 1.125, 1.5
# Bar 1: 0.0 - 1.5s
# 1st beat: 0.0
# 2nd beat: 0.375
# 3rd beat: 0.75
# 4th beat: 1.125

drum_notes = [
    (drum_kick, 0.0, note_length),     # Kick on 1
    (drum_snare, 0.375, note_length),   # Snare on 2
    (drum_kick, 0.75, note_length),     # Kick on 3
    (drum_snare, 1.125, note_length),   # Snare on 4
    (drum_hihat, 0.0, note_length),     # Hihat on 1
    (drum_hihat, 0.375, note_length),   # Hihat on 2
    (drum_hihat, 0.75, note_length),    # Hihat on 3
    (drum_hihat, 1.125, note_length),   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# ==============================
# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43)
# D2 = 38, F2 = 41, G2 = 43, C3 = 48, D3 = 50, E3 = 52
# Roots and fifths with chromatic approaches

# Dm: D - F - A - C
# Walking pattern: D - F - G - C - D - F - D - C

bass_notes = [
    (38, 1.5, note_length),     # D2
    (41, 1.875, note_length),   # F2
    (43, 2.25, note_length),    # G2
    (48, 2.625, note_length),   # C3
    (38, 2.875, note_length),   # D2
    (41, 3.25, note_length),    # F2
    (38, 3.625, note_length),   # D2
    (48, 4.0, note_length),     # C3
    (38, 4.375, note_length),   # D2
    (41, 4.75, note_length),    # F2
    (43, 5.125, note_length),   # G2
    (48, 5.5, note_length),     # C3
    (38, 5.875, note_length),   # D2
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Dm7: D - F - A - C
# G7: G - B - D - F
# Cm7: C - Eb - G - Bb
# F7: F - A - C - Eb

# Bar 2 (1.5 - 3.0s): Dm7 -> G7
# Bar 3 (3.0 - 4.5s): Cm7 -> F7
# Bar 4 (4.5 - 6.0s): Dm7 -> G7

# Each chord is played in the 2nd and 4th beats

piano_notes = [
    (62, 1.875, note_length),   # D4 (Dm7: D)
    (64, 1.875, note_length),   # F4
    (67, 1.875, note_length),   # A4
    (60, 1.875, note_length),   # C4
    (67, 2.25, note_length),    # G4 (G7: G)
    (71, 2.25, note_length),    # B4
    (62, 2.25, note_length),    # D4
    (64, 2.25, note_length),    # F4

    (60, 3.25, note_length),    # C4 (Cm7: C)
    (63, 3.25, note_length),    # Eb4
    (67, 3.25, note_length),    # G4
    (65, 3.25, note_length),    # Bb4
    (65, 3.625, note_length),   # F4 (F7: F)
    (68, 3.625, note_length),   # A4
    (60, 3.625, note_length),   # C4
    (63, 3.625, note_length),   # Eb4

    (62, 4.75, note_length),    # D4 (Dm7: D)
    (64, 4.75, note_length),    # F4
    (67, 4.75, note_length),    # A4
    (60, 4.75, note_length),    # C4
    (67, 5.125, note_length),   # G4 (G7: G)
    (71, 5.125, note_length),   # B4
    (62, 5.125, note_length),   # D4
    (64, 5.125, note_length),   # F4
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Dm7: D, F, A, C
# Motif: D - F - G - C (D, F, G, C)

# Start it, leave it hanging, return and finish it

# Bar 2: D - F - G - [C]
# Bar 3: [C] - D - F - G
# Bar 4: C - D - F - G - C

sax_notes = [
    (62, 1.5, note_length),     # D4
    (64, 1.875, note_length),   # F4
    (67, 2.25, note_length),    # G4
    (60, 2.625, note_length),   # C4
    (60, 3.125, note_length),   # C4 (return)
    (62, 3.5, note_length),     # D4
    (64, 3.875, note_length),   # F4
    (67, 4.25, note_length),    # G4
    (60, 4.625, note_length),   # C4
    (62, 5.0, note_length),     # D4
    (64, 5.375, note_length),   # F4
    (67, 5.75, note_length),    # G4
    (60, 6.125, note_length),   # C4 (end)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_cellar_intro.mid")
