
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
drum_notes = [
    (36, 0.0, 0.75),     # Kick on 1
    (38, 0.75, 0.75),    # Snare on 2
    (42, 0.0, 0.375),    # Hihat on 1
    (42, 0.375, 0.375),  # Hihat on 2
    (42, 0.75, 0.375),   # Hihat on 3
    (42, 1.125, 0.375),  # Hihat on 4
    (36, 1.5, 0.75),     # Kick on 3
    (38, 1.5, 0.75),     # Snare on 4
    (42, 1.5, 0.375),    # Hihat on 3
    (42, 1.875, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (D2-G2, MIDI 38-43), walking line with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),     # D2 on 1
    (40, 1.875, 0.375),   # Eb2 on 2
    (43, 2.25, 0.375),    # G2 on 3
    (38, 2.625, 0.375),   # D2 on 4
    (40, 3.0, 0.375),     # Eb2 on 1
    (43, 3.375, 0.375),   # G2 on 2
    (41, 3.75, 0.375),    # F2 on 3
    (38, 4.125, 0.375),   # D2 on 4
    (40, 4.5, 0.375),     # Eb2 on 1
    (43, 4.875, 0.375),   # G2 on 2
    (41, 5.25, 0.375),    # F2 on 3
    (38, 5.625, 0.375),   # D2 on 4
]
for note, start, duration in bass_notes:
    no = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(no)

# Piano - Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: F7 (F, A, C, E) -> C minor 7 (C, Eb, G, Bb)
piano_notes_bar2 = [
    (65, 1.5, 0.375),     # F4
    (68, 1.5, 0.375),     # A4
    (60, 1.5, 0.375),     # C4
    (64, 1.5, 0.375),     # E4
    (60, 1.875, 0.375),   # C4
    (63, 1.875, 0.375),   # Eb4
    (67, 1.875, 0.375),   # G4
    (62, 1.875, 0.375),   # Bb4
]
for note, start, duration in piano_notes_bar2:
    no = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(no)

# Bar 3: Dm7 (D, F, A, C)
piano_notes_bar3 = [
    (62, 2.25, 0.375),    # D4
    (64, 2.25, 0.375),    # F4
    (67, 2.25, 0.375),    # A4
    (60, 2.25, 0.375),    # C4
    (60, 2.625, 0.375),   # C4
    (63, 2.625, 0.375),   # Eb4
    (67, 2.625, 0.375),   # G4
    (62, 2.625, 0.375),   # Bb4
]
for note, start, duration in piano_notes_bar3:
    no = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(no)

# Bar 4: G7 (G, B, D, F)
piano_notes_bar4 = [
    (67, 3.0, 0.375),     # G4
    (71, 3.0, 0.375),     # B4
    (69, 3.0, 0.375),     # D4
    (64, 3.0, 0.375),     # F4
    (67, 3.375, 0.375),   # G4
    (71, 3.375, 0.375),   # B4
    (69, 3.375, 0.375),   # D4
    (64, 3.375, 0.375),   # F4
]
for note, start, duration in piano_notes_bar4:
    no = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(no)

# Sax - Dante (one short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Melody: F (65), Ab (67), Bb (62), G (67), F (65), rest, F (65), Ab (67), rest
sax_notes = [
    (65, 1.5, 0.375),     # F4 on 1
    (67, 1.875, 0.375),   # Ab4 on 2
    (62, 2.25, 0.375),    # Bb4 on 3
    (67, 2.625, 0.375),   # G4 on 4
    (65, 3.0, 0.375),     # F4 on 1
    (67, 3.375, 0.375),   # Ab4 on 2
    (65, 3.75, 0.375),    # F4 on 3
    (67, 4.125, 0.375),   # Ab4 on 4
]
for note, start, duration in sax_notes:
    no = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(no)

# Drums continue (Bar 2-4)
# Bar 2
drum_notes_bar2 = [
    (36, 1.5, 0.75),      # Kick on 1
    (38, 1.875, 0.75),    # Snare on 2
    (42, 1.5, 0.375),     # Hihat on 1
    (42, 1.875, 0.375),   # Hihat on 2
    (42, 2.25, 0.375),    # Hihat on 3
    (42, 2.625, 0.375),   # Hihat on 4
    (36, 3.0, 0.75),      # Kick on 1
    (38, 3.375, 0.75),    # Snare on 2
    (42, 3.0, 0.375),     # Hihat on 1
    (42, 3.375, 0.375),   # Hihat on 2
    (42, 3.75, 0.375),    # Hihat on 3
    (42, 4.125, 0.375),   # Hihat on 4
]
for note, start, duration in drum_notes_bar2:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 3
drum_notes_bar3 = [
    (36, 3.75, 0.75),     # Kick on 1
    (38, 4.125, 0.75),    # Snare on 2
    (42, 3.75, 0.375),    # Hihat on 1
    (42, 4.125, 0.375),   # Hihat on 2
    (42, 4.5, 0.375),     # Hihat on 3
    (42, 4.875, 0.375),   # Hihat on 4
    (36, 5.25, 0.75),     # Kick on 1
    (38, 5.625, 0.75),    # Snare on 2
    (42, 5.25, 0.375),    # Hihat on 1
    (42, 5.625, 0.375),   # Hihat on 2
    (42, 6.0, 0.375),     # Hihat on 3
    (42, 6.375, 0.375),   # Hihat on 4
]
for note, start, duration in drum_notes_bar3:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
