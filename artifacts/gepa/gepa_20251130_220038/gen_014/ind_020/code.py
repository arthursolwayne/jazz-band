
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start+duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (53, 1.5, 0.375),  # F
    (55, 1.875, 0.375), # Ab
    (57, 2.25, 0.375),  # Bb
    (59, 2.625, 0.375), # C
    (53, 2.625, 0.375), # F
    (55, 3.0, 0.375),   # Ab
    (57, 3.375, 0.375), # Bb
    (59, 3.75, 0.375),  # C
    (53, 3.75, 0.375),  # F
    (55, 4.125, 0.375), # Ab
    (57, 4.5, 0.375),   # Bb
    (60, 4.875, 0.375), # D
    (53, 4.875, 0.375), # F
    (55, 5.25, 0.375),  # Ab
    (57, 5.625, 0.375), # Bb
    (60, 5.625, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start+duration))

# Piano (Diane)
piano_notes = [
    (62, 1.5, 0.375),   # F7
    (60, 1.875, 0.375), # D7
    (62, 2.25, 0.375),  # F7
    (60, 2.625, 0.375), # D7
    (64, 3.0, 0.375),   # A7
    (62, 3.375, 0.375), # F7
    (64, 3.75, 0.375),  # A7
    (62, 4.125, 0.375), # F7
    (66, 4.5, 0.375),   # C8
    (64, 4.875, 0.375), # A7
    (66, 5.25, 0.375),  # C8
    (64, 5.625, 0.375)  # A7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start+duration))

# Sax (Dante)
sax_notes = [
    (66, 1.5, 0.375),   # D7
    (67, 1.875, 0.375), # Eb7
    (69, 2.25, 0.375),  # F7
    (66, 2.625, 0.375), # D7
    (67, 3.0, 0.375),   # Eb7
    (69, 3.375, 0.375), # F7
    (66, 3.75, 0.375),  # D7
    (67, 4.125, 0.375), # Eb7
    (69, 4.5, 0.375),   # F7
    (66, 4.875, 0.375), # D7
    (67, 5.25, 0.375),  # Eb7
    (69, 5.625, 0.375)  # F7
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start+duration))

# Drums (Bars 2-4)
drum_notes = [
    (36, 1.5, 0.375),   # Kick 1
    (42, 1.5, 0.1875),  # Hihat 1
    (38, 1.875, 0.375), # Snare 2
    (42, 1.875, 0.1875),# Hihat 2
    (36, 2.25, 0.375),  # Kick 3
    (42, 2.25, 0.1875), # Hihat 3
    (38, 2.625, 0.375), # Snare 4
    (42, 2.625, 0.1875),# Hihat 4
    (36, 3.0, 0.375),   # Kick 1
    (42, 3.0, 0.1875),  # Hihat 1
    (38, 3.375, 0.375), # Snare 2
    (42, 3.375, 0.1875),# Hihat 2
    (36, 3.75, 0.375),  # Kick 3
    (42, 3.75, 0.1875), # Hihat 3
    (38, 4.125, 0.375), # Snare 4
    (42, 4.125, 0.1875),# Hihat 4
    (36, 4.5, 0.375),   # Kick 1
    (42, 4.5, 0.1875),  # Hihat 1
    (38, 4.875, 0.375), # Snare 2
    (42, 4.875, 0.1875),# Hihat 2
    (36, 5.25, 0.375),  # Kick 3
    (42, 5.25, 0.1875), # Hihat 3
    (38, 5.625, 0.375), # Snare 4
    (42, 5.625, 0.1875) # Hihat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start+duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
