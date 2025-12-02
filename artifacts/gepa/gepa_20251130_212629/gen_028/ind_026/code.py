
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.0, 0.5),     # Hihat on 1
    (38, 0.5, 1.0),     # Snare on 2
    (42, 0.5, 1.0),     # Hihat on 2
    (36, 1.0, 1.5),     # Kick on 3
    (42, 1.0, 1.5),     # Hihat on 3
    (38, 1.5, 2.0),     # Snare on 4
    (42, 1.5, 2.0),     # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repetition
bass_notes = [
    (64, 1.5, 1.625),  # D
    (63, 1.625, 1.75), # C
    (65, 1.75, 1.875), # Eb
    (64, 1.875, 2.0),  # D
    (64, 2.0, 2.125),  # D
    (63, 2.125, 2.25), # C
    (65, 2.25, 2.375), # Eb
    (67, 2.375, 2.5),  # F
    (67, 2.5, 2.625),  # F
    (65, 2.625, 2.75), # Eb
    (64, 2.75, 2.875), # D
    (63, 2.875, 3.0),  # C
    (64, 3.0, 3.125),  # D
    (63, 3.125, 3.25), # C
    (65, 3.25, 3.375), # Eb
    (64, 3.375, 3.5),  # D
    (64, 3.5, 3.625),  # D
    (63, 3.625, 3.75), # C
    (65, 3.75, 3.875), # Eb
    (67, 3.875, 4.0),  # F
    (67, 4.0, 4.125),  # F
    (65, 4.125, 4.25), # Eb
    (64, 4.25, 4.375), # D
    (63, 4.375, 4.5),  # C
    (64, 4.5, 4.625),  # D
    (63, 4.625, 4.75), # C
    (65, 4.75, 4.875), # Eb
    (64, 4.875, 5.0),  # D
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.0, 2.25),   # D7 on beat 2
    (60, 2.0, 2.25),   # F on beat 2
    (62, 2.0, 2.25),   # A on beat 2
    (65, 2.0, 2.25),   # C on beat 2
    (64, 4.0, 4.25),   # D7 on beat 4
    (60, 4.0, 4.25),   # F on beat 4
    (62, 4.0, 4.25),   # A on beat 4
    (65, 4.0, 4.25),   # C on beat 4
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 1.75),   # E
    (64, 1.75, 2.0),   # G
    (62, 2.0, 2.25),   # E
    (60, 2.25, 2.5),   # D
    (64, 2.5, 2.75),   # G
    (62, 2.75, 3.0),   # E
    (60, 3.0, 3.25),   # D
    (62, 3.25, 3.5),   # E
    (64, 3.5, 3.75),   # G
    (62, 3.75, 4.0),   # E
    (60, 4.0, 4.25),   # D
    (64, 4.25, 4.5),   # G
    (62, 4.5, 4.75),   # E
    (60, 4.75, 5.0),   # D
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
