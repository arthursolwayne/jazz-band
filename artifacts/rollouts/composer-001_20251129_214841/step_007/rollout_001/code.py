
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &
    (36, 1.5, 0.375),  # Kick on 3
    (38, 1.875, 0.375), # Snare on 4
]

for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=start,
        end=start + duration
    )
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (60, 1.5, 0.375), # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375), # D
    (60, 2.625, 0.375), # C
    # Bar 3
    (62, 3.0, 0.375), # D
    (63, 3.375, 0.375), # D#
    (64, 3.75, 0.375), # E
    (62, 4.125, 0.375), # D
    # Bar 4
    (64, 4.5, 0.375), # E
    (65, 4.875, 0.375), # F
    (67, 5.25, 0.375), # G
    (65, 5.625, 0.375), # F
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(
        velocity=90,
        pitch=note,
        start=start,
        end=start + duration
    )
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.375), # C
    (64, 1.875, 0.375), # E
    (67, 1.875, 0.375), # G
    (71, 1.875, 0.375), # Bb
    # Bar 3
    (60, 3.375, 0.375), # C
    (64, 3.375, 0.375), # E
    (67, 3.375, 0.375), # G
    (71, 3.375, 0.375), # Bb
    # Bar 4
    (60, 4.875, 0.375), # C
    (64, 4.875, 0.375), # E
    (67, 4.875, 0.375), # G
    (71, 4.875, 0.375), # Bb
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(
        velocity=95,
        pitch=note,
        start=start,
        end=start + duration
    )
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375), # D
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375), # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375), # D
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375), # D
    (60, 4.125, 0.375), # C
    (62, 4.5, 0.375), # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375), # D
    (60, 5.625, 0.375), # C
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(
        velocity=105,
        pitch=note,
        start=start,
        end=start + duration
    )
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
