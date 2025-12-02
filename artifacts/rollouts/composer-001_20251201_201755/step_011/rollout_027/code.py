
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 1.875 + 0.375)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(8):
    start = bar1_start + i * 0.375
    note = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# D2 (D), F (F), G (G), A (A), C (C), D (D)
bass_notes = [
    (1.5, 38, 0.125),  # D2
    (1.875, 43, 0.125),  # F (chromatic approach)
    (2.25, 43, 0.125),  # F
    (2.625, 46, 0.125),  # G
    (3.0, 49, 0.125),  # A
    (3.375, 52, 0.125),  # C
    (3.75, 38, 0.125),  # D2
    (4.125, 43, 0.125),  # F
    (4.5, 46, 0.125),  # G
    (4.875, 49, 0.125),  # A
    (5.25, 52, 0.125),  # C
    (5.625, 38, 0.125),  # D2
]
for start, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
# Comp on 2 and 4

# Bar 2 - Dm7
piano_notes = [
    (1.5, 62, 0.375),  # D4
    (1.5, 65, 0.375),  # F4
    (1.5, 69, 0.375),  # A4
    (1.5, 72, 0.375),  # C5
]
for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 3 - Gm7
piano_notes = [
    (3.0, 71, 0.375),  # G4
    (3.0, 76, 0.375),  # Bb4
    (3.0, 78, 0.375),  # D5
    (3.0, 81, 0.375),  # F5
]
for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 4 - Cm7
piano_notes = [
    (4.5, 60, 0.375),  # C4
    (4.5, 63, 0.375),  # Eb4
    (4.5, 71, 0.375),  # G4
    (4.5, 76, 0.375),  # Bb4
]
for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (E4), F (F4), D (E4), G (G4)
# Start at bar 2, leave it hanging on the third note, come back at bar 4 to finish.

# Bar 2: D, F, D
sax_notes = [
    (1.5, 62, 0.375),  # D4
    (1.875, 65, 0.375),  # F4
    (2.25, 62, 0.375),  # D4
]
for start, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bar 4: G
sax_notes = [
    (4.5, 67, 0.375),  # G4
]
for start, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_shorter_intro.mid")
