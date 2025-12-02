
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
    (42, 0.125, 0.25), # Hihat on &1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.5, 0.25),   # Hihat on &2
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.875, 0.25), # Hihat on &3
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.25, 0.25)   # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    # Bar 2 (1.5s)
    (38, 1.5, 0.375), # D2 on 1
    (40, 1.875, 0.375), # F2 on 3
    (43, 2.25, 0.375), # G2 on 4
    (41, 2.625, 0.375), # F#2 on &4

    # Bar 3 (2.5s)
    (43, 2.5, 0.375), # G2 on 1
    (38, 2.875, 0.375), # D2 on 3
    (40, 3.25, 0.375), # F2 on 4
    (39, 3.625, 0.375), # E2 on &4

    # Bar 4 (3.5s)
    (40, 3.5, 0.375), # F2 on 1
    (42, 3.875, 0.375), # G#2 on 3
    (43, 4.25, 0.375), # G2 on 4
    (41, 4.625, 0.375) # F#2 on &4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, resolve on the last chord. Comp on 2 and 4.
piano_notes = [
    # Bar 2 (1.5s) - Fmaj7 (F, A, C, E)
    (65, 1.5, 0.375), # F4
    (69, 1.5, 0.375), # A4
    (60, 1.5, 0.375), # C4
    (64, 1.5, 0.375), # E4

    # Bar 3 (2.5s) - G7 (G, B, D, F)
    (67, 2.5, 0.375), # G4
    (71, 2.5, 0.375), # B4
    (62, 2.5, 0.375), # D4
    (65, 2.5, 0.375), # F4

    # Bar 4 (3.5s) - Cmaj7 (C, E, G, B)
    (60, 3.5, 0.375), # C4
    (64, 3.5, 0.375), # E4
    (67, 3.5, 0.375), # G4
    (71, 3.5, 0.375)  # B4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif that sings, start it, leave it hanging, come back and finish it.
sax_notes = [
    # Bar 2 (1.5s) - Start motif
    (65, 1.5, 0.25), # F4
    (68, 1.75, 0.125), # A4
    (65, 1.875, 0.125), # F4
    (70, 2.0, 0.25), # Bb4

    # Bar 3 (2.5s) - No sax, leave it hanging
    # Bar 4 (3.5s) - Finish motif
    (65, 3.5, 0.25), # F4
    (68, 3.75, 0.125), # A4
    (65, 3.875, 0.125), # F4
    (70, 4.0, 0.25)  # Bb4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
