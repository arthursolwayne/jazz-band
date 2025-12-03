
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2
    (40, 1.875, 0.375), # Eb2 (chromatic approach)
    (43, 2.25, 0.375),  # G2
    (40, 2.625, 0.375), # Eb2 (chromatic approach)
    (38, 2.625, 0.375),  # D2 (repetition)
    (40, 3.0, 0.375),   # Eb2
    (43, 3.375, 0.375), # G2
    (40, 3.75, 0.375),  # Eb2
    (38, 3.75, 0.375),  # D2
    (40, 4.125, 0.375), # Eb2
    (43, 4.5, 0.375),   # G2
    (40, 4.875, 0.375), # Eb2
    (38, 4.875, 0.375),  # D2
    (40, 5.25, 0.375),  # Eb2
    (43, 5.625, 0.375), # G2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D4
    (65, 1.5, 0.375),  # F4
    (67, 1.5, 0.375),  # A4
    (69, 1.5, 0.375),  # C5
    # Bar 3: Gm7 (G, Bb, D, F)
    (67, 2.25, 0.375), # G4
    (71, 2.25, 0.375), # Bb4
    (69, 2.25, 0.375), # D4
    (71, 2.25, 0.375), # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 3.0, 0.375),  # C4
    (64, 3.0, 0.375),  # Eb4
    (67, 3.0, 0.375),  # G4
    (71, 3.0, 0.375),  # Bb4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F4 (65), G4 (67), D4 (62) but only the first three notes in bar 2
# Then rest in bar 3, repeat motif in bar 4
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D4
    (65, 1.875, 0.375), # F4
    (67, 2.25, 0.375),  # G4
    # Bar 3: Rest
    # Bar 4: Repeat motif
    (62, 4.5, 0.375),  # D4
    (65, 4.875, 0.375), # F4
    (67, 5.25, 0.375),  # G4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
