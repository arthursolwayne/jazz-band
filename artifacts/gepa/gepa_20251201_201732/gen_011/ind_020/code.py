
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5, 0.375),   # D2 - root
    (41, 1.875, 0.375), # F2 - chromatic approach
    (43, 2.25, 0.375),  # G2 - fifth
    (38, 2.625, 0.375), # D2 - root
    (38, 3.0, 0.375),   # D2 - root
    (41, 3.375, 0.375), # F2 - chromatic approach
    (43, 3.75, 0.375),  # G2 - fifth
    (38, 4.125, 0.375), # D2 - root
    (38, 4.5, 0.375),   # D2 - root
    (41, 4.875, 0.375), # F2 - chromatic approach
    (43, 5.25, 0.375),  # G2 - fifth
    (38, 5.625, 0.375)  # D2 - root
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - Piano (Open voicings, comp on 2 and 4)
piano_notes = [
    # Bar 2 - Dm7 (D F A C)
    (62, 1.5, 0.375), # D4
    (65, 1.5, 0.375), # F4
    (67, 1.5, 0.375), # A4
    (69, 1.5, 0.375), # C5
    # Bar 3 - Gm7 (G Bb D F)
    (67, 2.625, 0.375), # G4
    (71, 2.625, 0.375), # Bb4
    (69, 2.625, 0.375), # D4
    (71, 2.625, 0.375), # F4
    # Bar 4 - Cm7 (C Eb G Bb)
    (60, 3.75, 0.375), # C4
    (63, 3.75, 0.375), # Eb4
    (67, 3.75, 0.375), # G4
    (71, 3.75, 0.375), # Bb4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on all eighths
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))

# Dante - Tenor Sax (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
sax_notes = [
    # Bar 2 - Melody (D4, F4, E4, D4)
    (62, 1.5, 0.375), # D4
    (65, 1.875, 0.375), # F4
    (64, 2.25, 0.375), # E4
    (62, 2.625, 0.375), # D4
    # Bar 3 - Silence (Leave it hanging)
    # Bar 4 - Return and finish (D4, Bb4, C4, D4)
    (62, 3.75, 0.375), # D4
    (71, 4.125, 0.375), # Bb4
    (60, 4.5, 0.375), # C4
    (62, 4.875, 0.375)  # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter.mid")
