
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
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.0, 1.0),     # Hihat on 1
    (38, 0.5, 1.0),     # Snare on 2
    (42, 0.5, 1.0),     # Hihat on 2
    (36, 1.0, 1.0),     # Kick on 3
    (42, 1.0, 1.0),     # Hihat on 3
    (38, 1.5, 1.0),     # Snare on 4
    (42, 1.5, 1.0)      # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (62, 1.5, 0.5),     # Dm7 root
    (64, 2.0, 0.5),     # chromatic up
    (63, 2.5, 0.5),     # chromatic down
    (61, 3.0, 0.5),     # chromatic down
    (62, 3.5, 0.5),     # Dm7 root
    (64, 4.0, 0.5),     # chromatic up
    (63, 4.5, 0.5),     # chromatic down
    (61, 5.0, 0.5),     # chromatic down
    (62, 5.5, 0.5)      # Dm7 root
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.5),     # Dm7
    (67, 1.5, 0.5),
    (69, 1.5, 0.5),
    (71, 1.5, 0.5),
    # Bar 3
    (62, 3.0, 0.5),     # Dm7
    (67, 3.0, 0.5),
    (69, 3.0, 0.5),
    (71, 3.0, 0.5),
    # Bar 4
    (62, 4.5, 0.5),     # Dm7
    (67, 4.5, 0.5),
    (69, 4.5, 0.5),
    (71, 4.5, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.5),     # Kick on 1
    (42, 1.5, 0.5),     # Hihat on 1
    (38, 2.0, 0.5),     # Snare on 2
    (42, 2.0, 0.5),     # Hihat on 2
    (36, 2.5, 0.5),     # Kick on 3
    (42, 2.5, 0.5),     # Hihat on 3
    (38, 3.0, 0.5),     # Snare on 4
    (42, 3.0, 0.5),     # Hihat on 4
    (36, 3.5, 0.5),     # Kick on 1
    (42, 3.5, 0.5),     # Hihat on 1
    (38, 4.0, 0.5),     # Snare on 2
    (42, 4.0, 0.5),     # Hihat on 2
    (36, 4.5, 0.5),     # Kick on 3
    (42, 4.5, 0.5),     # Hihat on 3
    (38, 5.0, 0.5),     # Snare on 4
    (42, 5.0, 0.5)      # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante) - Melody
sax_notes = [
    (62, 1.5, 0.5),     # D
    (66, 2.0, 0.5),     # F
    (69, 2.5, 0.5),     # A
    (65, 3.0, 0.5),     # Eb
    (62, 3.5, 0.5),     # D
    (66, 4.0, 0.5),     # F
    (69, 4.5, 0.5),     # A
    (62, 5.0, 0.5)      # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
